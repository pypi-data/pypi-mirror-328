"""Test Template."""

import pytest

from python_template import app


@pytest.mark.unit
def test_app():
    """Validate package is importable."""
    assert app.app() == "Hello World!"
