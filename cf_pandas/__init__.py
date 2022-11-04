"""
cf-pandas: an accessor for pandas objects that interprets CF attributes
"""

from pkg_resources import DistributionNotFound, get_distribution

from .accessor import CFAccessor  # noqa
from .options import set_options  # noqa
from .reg import Reg
from .utils import always_iterable, astype, match_criteria_key
from .vocab import Vocab
from .widget import dropdown, Selector


try:
    __version__ = get_distribution("cf-pandas").version
except DistributionNotFound:
    # package is not installed
    __version__ = "unknown"
