class MainPage:
    logo = "#logo > h1 > a"
    search_input = "#search > input"
    cart_button = "#cart > button"
    promoblock = "#content"

    featured_product = "//*[@id='content']/div[2]/div[1]/div/div[1]/a"

    footer = "body > footer"

    @staticmethod
    def get_menu_button_by_id(button_id):
        return f"//*[@id='menu']/div[2]/ul/li[{button_id}]/a"
