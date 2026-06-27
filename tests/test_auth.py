from playwright.sync_api import expect

def test_auth_001(config, auth_page):
    url=config["url"]
    auth_page.navigate(url)
    expect(auth_page.school_code).to_be_visible()
    expect(auth_page.username_or_email).to_be_visible()
    expect(auth_page.password).to_be_visible()
    expect(auth_page.sign_in_button).to_be_visible()


def test_auth_002(config, logged_in_page, auth_page):
    url=config["url"]
    expect(auth_page.page).to_have_url(f"{url}/app/dashboard")

def test_auth_003(config, auth_page):
    dash_url=config["dashboard_url"]
    auth_page_url=config["url"]
    auth_page.navigate(dash_url)
    expect(auth_page.page).to_have_url(f"{auth_page_url}/login")


def test_auth_004(config, auth_page):
    url=config["url"]
    auth_page.navigate(url)
    username_or_email=config["username_or_email"]
    password=config["password"]
    wrong_school_id=config["wrong_school_code"]
    auth_page.auth_login(wrong_school_id, username_or_email, password)
    expect(auth_page.error_message).to_be_visible()


def test_auth_005(config, auth_page):
    url=config["url"]
    auth_page.navigate(url)
    school_code=config["school_code"]
    username_or_email=config["username_or_email"]
    wrong_password=config["wrong_school_code"]
    auth_page.auth_login(school_code, username_or_email, wrong_password)
    expect(auth_page.invalid_password).to_be_visible()


def test_auth_006(config, auth_page):
    url=config["url"]
    auth_page.navigate(url)
    auth_page.forgot_password()
    expect(auth_page.page).to_have_url(f"{url}/forgot-password")
    expect(auth_page.school_code).to_be_visible()
    expect(auth_page.f_email_address).to_be_visible()
    expect(auth_page.sent_reset_link).to_be_visible()
    expect(auth_page.back_to_login).to_be_visible()



