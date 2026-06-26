from playwright.sync_api import expect


def test_dash_001(config, login_page):

    url = config["url"]
    school_code = config["school_code"]
    username_or_email = config["username_or_email"]
    password = config["password"]
    login_page.navigate(url)
    login_page.login(school_code, username_or_email, password)
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    expect(login_page.school_branding).to_be_visible()
    expect(login_page.welcome_message).to_be_visible()




def test_dash_002(config, login_page):

    url = config["url"]
    school_code = config["school_code"]
    username_or_email = config["username_or_email"]
    password = config["password"]


    login_page.navigate(url)
    login_page.login(school_code, username_or_email, password)
    expect(login_page.page).to_have_url(f"{url}/app/dashboard")
    expect(login_page.control_tower).to_be_visible()
    expect(login_page.attendance_health).to_be_visible()
    expect(login_page.fee_collection).to_be_visible()
    expect(login_page.academic_execution).to_be_visible()
    expect(login_page.teacher_coverage).to_be_visible()



def test_dash_003(logged_in_page):

    expect(logged_in_page.fee_followups).to_be_visible()
    expect(logged_in_page.rahul_verma).to_be_visible()
    expect(logged_in_page.sneha_iyer).to_be_visible()




def test_dash_004(logged_in_page):
    expect(logged_in_page.upcoming_calendar).to_be_visible()
    expect(logged_in_page.no_up_coming_events).to_be_visible()



def test_dash_005(logged_in_page):
    expect(logged_in_page.announcements).to_be_visible()
    expect(logged_in_page.announcement_card).to_be_visible()



def test_dash_006(logged_in_page):
    
    expect(logged_in_page.operational_journal).to_be_visible()
    
   

