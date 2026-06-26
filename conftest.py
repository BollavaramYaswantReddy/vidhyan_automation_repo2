import pytest
import json
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage



@pytest.fixture
def config():
    with open('config/config.json') as configfile :

        data=json.load(configfile)
    
    return data


@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)


    

# login fixture

@pytest.fixture
def logged_in_page(config, login_page):

    url = config["url"]
    school_code = config["school_code"]
    username_or_email = config["username_or_email"]
    password = config["password"]

    login_page.navigate(url)
    login_page.login(school_code, username_or_email, password)

    expect(login_page.page).to_have_url(f"{url}/app/dashboard")

    return login_page
