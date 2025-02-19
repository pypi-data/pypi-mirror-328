import pytest

from zilla_package.zilla import Zilla


def test_zilla_initialization():
    z = Zilla("Godzilla")
    assert z.name == "Godzilla"


def test_zilla_create_valid_name():
    result = Zilla.create("Mega")
    assert result == "Mega-zilla "


def test_zilla_create_none_name():
    with pytest.raises(AssertionError, match="name of the zilla cannot be None"):
        Zilla.create(None)


def test_zilla_fixture_usage(zilla_instance):
    """Test that the fixture correctly initializes a Zilla instance."""
    assert zilla_instance.name == "test-zilla"


if __name__ == "__main__":
    pytest.main()
