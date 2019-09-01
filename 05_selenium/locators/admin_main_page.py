class AdminMainPage:
    """ Admin page locators
    """
    catalog = "#menu-catalog > a"
    products_menu = "#collapse1 > li:nth-child(2) > a"
    add_product = ".btn-primary"

    success_alert = "//*[@id='content']/div[2]/div[1]"

    search_by_product_name = "#input-name"
    search_filter_button = "#button-filter"
    found_product_edit_button = "//*[@id='form-product']/div/table/tbody/tr/td[8]/a"
    found_product_select_button = "//*[@id='form-product']/div/table/tbody/tr/td[1]/input"

    delete_button = ".btn-danger"

