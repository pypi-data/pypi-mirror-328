import warnings
from collections.abc import Callable, Generator, Sequence

import numpy as np
from scipy.stats import chi2, kstest, norm

__all__ = ["Histogram"]


def __dir__():
    return __all__


def sqrt_method(values, *args, **kwargs):
    return values - np.sqrt(values), values + np.sqrt(values)


def poisson_interval(
    sumw: np.ndarray,
    sumw2: np.ndarray,
    coverage: float = norm.cdf(1) - norm.cdf(-1),  # 0.6826894921370859 -> 1sigma
):
    """
    Frequentist coverage interval for Poisson-distributed observations

    Calculates the so-called 'Garwood' interval,
    c.f. https://www.ine.pt/revstat/pdf/rs120203.pdf or
    http://ms.mcmaster.ca/peter/s743/poissonalpha.html
    For weighted data, this approximates the observed count by ``sumw**2/sumw2``, which
    effectively scales the unweighted poisson interval by the average weight.
    This may not be the optimal solution: see https://arxiv.org/pdf/1309.1287.pdf for a
    proper treatment. When a bin is zero, the scale of the nearest nonzero bin is
    substituted to scale the nominal upper bound.
    If all bins zero, a warning is generated and interval is set to ``sumw``.
    Taken from Coffea

    Args:
        sumw (``np.ndarray``): Sum of weights vector
        sumw2 (``np.ndarray``): Sum weights squared vector
        coverage (``float``, default ``norm.cdf(1)-norm.cdf(-1)``):
            Central coverage interval, defaults to 68%
    """
    scale = np.empty_like(sumw)
    scale[sumw != 0] = sumw2[sumw != 0] / sumw[sumw != 0]
    if np.sum(sumw == 0) > 0:
        missing = np.where(sumw == 0)
        available = np.nonzero(sumw)
        if len(available[0]) == 0:
            warnings.warn(
                "All sumw are zero!  Cannot compute meaningful error bars",
                RuntimeWarning,
                stacklevel=2,
            )
            return np.vstack([sumw, sumw])
        nearest = np.sum(
            [np.subtract.outer(d, d0) ** 2 for d, d0 in zip(available, missing)]
        ).argmin(axis=0)
        argnearest = tuple(dim[nearest] for dim in available)
        scale[missing] = scale[argnearest]
    counts = sumw / scale
    lo = scale * chi2.ppf((1 - coverage) / 2, 2 * counts) / 2.0
    hi = scale * chi2.ppf((1 + coverage) / 2, 2 * (counts + 1)) / 2.0
    interval = np.array([lo, hi])
    interval[interval == np.nan] = 0.0  # chi2.ppf produces nan for counts=0
    return interval


def calculate_relative(method_fcn, values, variances):
    return np.abs(method_fcn(values, variances) - values)


class Histogram:
    r"""
    Create a histogram object for the underlying :math:`\chi^2` distribution.

    .. note::

        This class assumes that the base distribution of the flow is unit gaussian.

    Args:
        dim (``int``): number of features.
        bins (``Union[int, np.ndarray]``): If integer, indicates number of bins, if array, indicates
            bin edges.
        vals (``np.ndarray``): Sum of the feature values that deviate from the
            central Gaussian distriburion
        max_val (``float``, default ``None``): Maximum value that histogram can take.
            will only be used if ``bins`` input is ``int``.
        weights (``np.ndarray``, default ``None``): weight per value. If ``None`` taken as ``1``.
    """

    __slots__ = [
        "dim",
        "vals",
        "weights",
        "max_val",
        "bins",
        "sumw",
        "sumw2",
        "values",
        "variances",
        "bin_weights",
        "bin_width",
        "_kstest",
    ]

    def __init__(
        self,
        dim: int,
        bins: int,
        vals: np.ndarray,
        max_val: float = None,
        weights: np.ndarray = None,
    ) -> None:
        self.dim = dim
        self.vals = vals
        self.weights = weights or np.ones(len(self.vals))
        assert len(self.vals) == len(self.weights), "Invalid shape"

        if isinstance(bins, int):
            assert max_val is not None, "If bins are not defined, max_val is needed"
            self.max_val = max_val
            self.bins = np.linspace(0, max_val, bins + 1)
        else:
            self.bins = np.array(bins)
            self.max_val = max(bins)
        self.bin_width = self.bins[1:] - self.bins[:-1]

        self.sumw = np.sum(self.weights)
        self.sumw2 = np.sum(self.weights**2)

        val, var = [], []
        for mask in self.bin_mask:
            w = self.weights[mask]
            val.append(w.sum())
            var.append(np.sum(w**2))
        self.values = np.array(val)
        self.variances = np.array(var)
        self.bin_weights = self.values / self.sumw
        self._kstest = None

    @property
    def nbins(self) -> int:
        """Number of bins"""
        return len(self.bins) - 1

    @property
    def bin_mask(self) -> Generator[np.ndarray]:
        """Mask the values for each bin"""
        for left, right in self.bin_edges:
            yield (self.vals >= left) * (self.vals < right)

    @property
    def bin_edges(self) -> Generator[np.ndarray]:
        """Get bin edges"""
        for n in range(len(self.bins) - 1):
            yield self.bins[n : n + 2]

    @property
    def bin_centers(self) -> np.ndarray:
        """retreive bin centers"""
        return self.bins[:-1] + (self.bin_width / 2)

    @property
    def density(self) -> np.ndarray:
        """compute density"""
        total = self.values.sum() * self.bin_width
        return self.values / np.where(total > 0.0, total, 1.0)

    @property
    def pull(self) -> np.ndarray:
        """compute pull"""
        bin_prob = chi2.cdf(self.bins[1:], df=self.dim) - chi2.cdf(
            self.bins[:-1], df=self.dim
        )  # probability of getting events in each bin
        expected = bin_prob * self.values.sum()  # number of expected events in each bin
        # expected - observed / sqrt(var)
        with warnings.catch_warnings(record=True):
            return (expected - self.values) / np.sqrt(self.variances)

    @property
    def yerr(self) -> tuple[np.ndarray, np.ndarray]:
        """Compute y-error"""
        method = (
            poisson_interval
            if np.allclose(self.variances, np.around(self.variances))
            else sqrt_method
        )
        return calculate_relative(method, self.values, self.variances)

    @property
    def yerr_density(self) -> tuple[np.ndarray, np.ndarray]:
        """Compute y-error for density distribution"""
        with warnings.catch_warnings(record=True):
            return self.density * self.yerr / self.values

    @property
    def xerr(self) -> tuple[np.ndarray, np.ndarray]:
        """
        compute errors on the x-axis

        Returns:
            ``Tuple[np.ndarray, np.ndarray]``:
            low and high errors
        """
        xerr = np.array(
            [
                [center - left, right - center]
                for (left, right), center in zip(self.bin_edges, self.bin_centers)
            ]
        )
        return xerr[:, 0], xerr[:, 1]

    @property
    def kstest_pval(self) -> float:
        """Compute p-value for Kolmogorov-Smirnov test"""
        if self._kstest is None:
            self._kstest = kstest(self.vals, cdf=lambda x: chi2.cdf(x, df=self.dim))
        return self._kstest.pvalue

    @property
    def residuals_pvalue(self) -> float:
        """Compute the p-value for residuals"""
        pull = self.pull[:-1]  # K-1 independent variables
        return 1.0 - chi2.cdf(np.sum(pull**2), df=len(pull))

    def pull_mask(self, condition: Callable[[np.ndarray], Sequence[bool]]) -> np.ndarray:
        """Create a sample mask from the statistical pull"""

        sample_mask = []
        for pull_mask, bin_mask in zip(condition(self.pull), self.bin_mask):
            if pull_mask:
                sample_mask.append(bin_mask)

        return sum(sample_mask).astype(bool)
