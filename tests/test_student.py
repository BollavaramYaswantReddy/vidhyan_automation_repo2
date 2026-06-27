from playwright.sync_api import expect


def test_stu_001(logged_in_page):
    logged_in_page.click_students()
    expect(logged_in_page.student_desk).to_be_visible()


def test_stu_002(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_student_directory()
    expect(logged_in_page.student_directory_table).to_be_visible()


def test_stu_003(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_guardian_directory()
    expect(logged_in_page.student_guardian).to_be_visible()



def test_stu_004(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_add_students()
    expect(logged_in_page.Add_students).to_be_visible()


def test_stu_005(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_enroll_to_class()
    expect(logged_in_page.enroll_to_class).to_be_visible()
   


def test_stu_006(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_add_guardian()
    expect(logged_in_page.add_guardian).to_be_visible()



def test_stu_007(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_link_guardian()
    expect(logged_in_page.link_guardian).to_be_visible()


def test_stu_008(logged_in_page, stud_page):
    logged_in_page.click_students()
    stud_page.click_student_leadership()
    expect(logged_in_page.student_leadership).to_be_visible()


def test_stu_009(logged_in_page, stud_page):
    logged_in_page.click_students()
    expect(stud_page.total_students).to_be_visible()
    expect(stud_page.active_students).to_be_visible()
    expect(stud_page.pending_profiles).to_be_visible()
    expect(stud_page.guardian_directory).to_be_visible()


def test_stu_010(logged_in_page,stud_page):
    logged_in_page.click_students()
    expect(stud_page.breadcrumb).to_be_visible()