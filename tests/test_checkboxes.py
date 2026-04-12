
def test_default_state(checkbox_page):
    checkbox_page.should_first_not_be_checked()
    checkbox_page.should_second_be_checked()

def test_check_and_uncheck(checkbox_page):
    checkbox_page.check_first()
    checkbox_page.should_first_be_checked()
    checkbox_page.uncheck_second()
    checkbox_page.should_second_not_be_checked()

def test_double_check(checkbox_page):
    checkbox_page.check_first()
    checkbox_page.check_first()
    checkbox_page.should_first_be_checked()
