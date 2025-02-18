"""
OpenNEM Energy Market Data Access (DEPRECATED)

This package has been deprecated. Please use the new client:
https://github.com/OpenNEM/openelectricity-python

For more information, visit:
- OpenElectricity Platform: https://platform.openelectricity.org.au
- OpenElectricity Documentation: https://docs.openelectricity.org.au
"""

import warnings

__version__ = "10.0.0"

warnings.warn(
    "This package has been deprecated. Please use the new openelectricity-python client: "
    "https://github.com/OpenNEM/openelectricity-python",
    DeprecationWarning,
    stacklevel=2,
)
