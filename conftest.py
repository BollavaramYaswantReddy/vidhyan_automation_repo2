import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
import json




@pytest.fixture
def config():
    with open('config/config.json') as configfile :

        data=json.load(configfile)
    
    return data


@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)


    


