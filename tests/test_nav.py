import time
from playwright.sync_api import expect

def test_nav_001(logged_in_page,login_page,config):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_home()
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")


def test_nav_002(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_students()
    expect(login_page.page).to_have_url(f"{url}/app/students")


def test_nav_003(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_teachers()
    expect(login_page.page).to_have_url(f"{url}/app/teachers")


def test_nav_004(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_staff()
    expect(login_page.page).to_have_url(f"{url}/app/staff")
    
def test_nav_005(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_academics()
    expect(login_page.page).to_have_url(f"{url}/app/academics")



def test_nav_006(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_attendance()
    expect(login_page.page).to_have_url(f"{url}/app/attendance")


def test_nav_007(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_fee()
    expect(login_page.page).to_have_url(f"{url}/app/fees")
    login_page.click_expenses()
    expect(login_page.page).to_have_url(f"{url}/app/revenue/expenses")
    login_page.click_payroll()
    expect(login_page.page).to_have_url(f"{url}/app/revenue/payroll")
    login_page.click_balance_sheet()
    expect(login_page.page).to_have_url(f"{url}/app/revenue/balance-sheet")
    login_page.click_set_up()
    expect(login_page.page).to_have_url(f"{url}/app/admin/academic")
    login_page.click_users()
    expect(login_page.page).to_have_url(f"{url}/app/admin")


def test_nav_008(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_settings()
    expect(login_page.page).to_have_url(f"{url}/app/settings")


def test_nav_009(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_user_account_menu()
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")


def test_nav_010(config, login_page,logged_in_page):
    url = config["url"]
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    login_page.click_notifications_icon()
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    