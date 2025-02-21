# mypy: disable-error-code="attr-defined"
"""PyMedX package."""

from importlib import metadata as importlib_metadata

from .api import PubMed, PubMedCentral


def get_version() -> str:
    """Return the program version."""
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "0.5.1"  # semantic-release


version = get_version()

__version__ = version


__all__ = ["PubMed", "PubMedCentral", "__version__"]
