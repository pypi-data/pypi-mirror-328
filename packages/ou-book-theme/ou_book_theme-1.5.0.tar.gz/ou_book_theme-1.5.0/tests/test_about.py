"""Tests for the about functionality."""

from ou_book_theme.__about__ import __version__


def test_version():
    """Test that the correct version is returned."""
    assert __version__ == "1.5.0"
