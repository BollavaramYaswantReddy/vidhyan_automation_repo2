from playwright.sync_api import expect


def test_stf_001(logged_in_page):
    logged_in_page.click_staff()
    expect(logged_in_page.staff_button).to_be_visible()


def test_stf_002(logged_in_page,staff_page):
    logged_in_page.click_staff()
    staff_page.click_staff_directory()
    expect(staff_page.staff_directory).to_be_visible()


def test_stf_003(logged_in_page,staff_page):
    logged_in_page.click_staff()
    staff_page.click_add_staff()
    expect(staff_page.add_staff).to_be_visible()


def test_stf_004(logged_in_page, staff_page):
    logged_in_page.click_staff()
    staff_page.click_drivers_staff()
    expect(staff_page.drivers_staff).to_be_visible()


def test_stf_005(logged_in_page, staff_page):
    logged_in_page.click_staff()
    staff_page.click_facilities_staff()
    expect(staff_page.facilities_staff).to_be_visible()


def test_stf_006(logged_in_page, staff_page):
    logged_in_page.click_staff()
    staff_page.click_operations_roles_staff()
    expect(staff_page.operations_roles_staff).to_be_visible()


def test_stf_007(logged_in_page, staff_page):
    logged_in_page.click_staff()
    staff_page.click_employment_status_staff()
    expect(staff_page.employment_status_staff).to_be_visible()
    

def test_stf_008(logged_in_page, staff_page):
    logged_in_page.click_staff()
    expect(staff_page.Total_staff).to_be_visible()
    expect(staff_page.active_staff).to_be_visible()
    expect(staff_page.drivers_desk_transport).to_be_visible()
    expect(staff_page.janitors).to_be_visible()