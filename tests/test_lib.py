from first_package.lib import try_me


def test_try_me():

    res = try_me()

    assert "Mike" in res.split()