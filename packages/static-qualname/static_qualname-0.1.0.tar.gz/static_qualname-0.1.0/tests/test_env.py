import pytest

from static_qualname.core import Env


@pytest.mark.parametrize(
    "sample",
    (
        # Module
        "foo",
        "foo.floof",
        # Package
        "bar",
        "bar.baz",
        "bar.baz.floof",
        "bar.floof",
        # Entirely missing
        "floof",
        "floof.dog",
    ),
)
def test_direct_reference(sample, tmp_path):
    foo = tmp_path / "foo.py"
    foo.touch()
    (tmp_path / "bar").mkdir()
    bar = tmp_path / "bar" / "__init__.py"
    bar.touch()
    baz = tmp_path / "bar" / "baz.py"
    baz.touch()

    e = Env()
    e.add_site_packages(tmp_path)
    assert e.real_qualname(sample) == sample
