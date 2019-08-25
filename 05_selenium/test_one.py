

def test_home_page(app):
    """ check home page title
    """
    assert app.wd.title == "Your Store"


