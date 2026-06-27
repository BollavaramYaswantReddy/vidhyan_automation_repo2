from playwright.sync_api import expect


def test_tch_001(logged_in_page,teach_page):
    logged_in_page.click_teachers()
    expect(teach_page.teacher_desk).to_be_visible()



def test_tch_002(logged_in_page,teach_page):
    logged_in_page.click_teachers()
    expect(teach_page.teacher_directory_find ).to_be_visible()



def test_tch_003(logged_in_page,teach_page):
    logged_in_page.click_teachers()
    teach_page.click_add_teacher()
    expect(teach_page.add_teacher).to_be_visible()




def test_tch_004(logged_in_page, teach_page):
    logged_in_page.click_teachers()
    teach_page.click_add_teacher()
    expect(teach_page.subject_master).to_be_visible()


def test_tch_005(logged_in_page, teach_page):
    logged_in_page.click_teachers()
    teach_page.click_subject_offerings()
    expect(teach_page.subject_offerings).to_be_visible()



def test_tch_006(logged_in_page, teach_page):
    logged_in_page.click_teachers()
    teach_page.click_portal_invitations()
    expect(teach_page.portal_invitations).to_be_visible()


def test_tch_007(logged_in_page, teach_page):
    logged_in_page.click_teachers()
    expect(teach_page.total_teachers).to_be_visible()
    expect(teach_page.active_teachers).to_be_visible()
    expect(teach_page.pending_teacher_profiles).to_be_visible()
    expect(teach_page.archived_teacher_records).to_be_visible()


def test_tch_008(logged_in_page, teach_page):
    logged_in_page.click_teachers()
    teach_page.click_academic_linkage()
    expect(teach_page.academic_linkage).to_be_visible()

