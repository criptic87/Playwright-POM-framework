from pages.dropdown_page import DropdownPage

def test_select_option_1(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.navigate()
    dropdown_page.select_option_by_value("1")
    dropdown_page.should_have_value("1")