import pytest
import json
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.authentication_page import Authentication
from pages.students_page import Students
from pages.teacher_page import Teacher
from pages.staff_page import Staff


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


@pytest.fixture
def auth_page(page:Page):
    return Authentication(page) 


@pytest.fixture
def stud_page(page:Page):
    return Students(page)

@pytest.fixture
def teach_page(page:Page):
    return Teacher(page)

@pytest.fixture
def staff_page(page:Page):
    return Staff(page)
