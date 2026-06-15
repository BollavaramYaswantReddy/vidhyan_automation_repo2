import time
from playwright.sync_api import expect

def test_auth_001(config, login_page):
    url=config["url"]
    login_page.navigate(url)
    expect(login_page.school_code).to_be_visible()
    expect(login_page.username_or_email).to_be_visible()
    expect(login_page.password).to_be_visible()
    expect(login_page.sign_in_button).to_be_visible()

    time.sleep(5)

def test_auth_002(config, login_page):
    url=config["url"]
    school_code=config["school_code"]
    username_or_email=config["username_or_email"]
    password=config["password"]
    login_page.navigate(url)
    login_page.login(school_code, username_or_email, password)
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")

def test_auth_003(config, login_page):
    dash_url=config["dashboard_url"]
    login_page_url=config["url"]
    login_page.navigate(dash_url)
    expect(login_page.page).to_have_url(f"{login_page_url}/login")

    time.sleep(1)


def test_auth_004(config, login_page):
    url=config["url"]
    login_page.navigate(url)
    username_or_email=config["username_or_email"]
    password=config["password"]
    wrong_school_id=config["wrong_school_code"]
    login_page.login(wrong_school_id, username_or_email, password)
    expect(login_page.error_message).to_be_visible()


    time.sleep(3)


def test_auth_005(config, login_page):
    url=config["url"]
    login_page.navigate(url)
    school_code=config["school_code"]
    username_or_email=config["username_or_email"]
    wrong_password=config["wrong_school_code"]
    login_page.login(school_code, username_or_email, wrong_password)
    expect(login_page.invalid_password).to_be_visible()

    time.sleep(2)



def test_auth_006(config, login_page):
    url=config["url"]
    login_page.navigate(url)
    login_page.forgot_password()
    expect(login_page.page).to_have_url(f"{url}/forgot-password")
    expect(login_page.school_code).to_be_visible()
    expect(login_page.f_email_address).to_be_visible()
    expect(login_page.sent_reset_link).to_be_visible()
    expect(login_page.back_to_login).to_be_visible()

    time.sleep(2)

