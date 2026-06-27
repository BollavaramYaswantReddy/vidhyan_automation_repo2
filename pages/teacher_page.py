from playwright.sync_api import Page


class Teacher:
    def __init__(self, page: Page):
        self.page = page
        self.teacher_desk = page.get_by_role("heading", name="Teacher Desk")
        self.teacher_directory_find = page.get_by_role("button", name="Teacher Directory Find")
        self.add_teacher = page.get_by_role("button", name="Add Teacher Create a teacher")
        self.subject_master = page.get_by_role("button", name="Subject Master Review")
        self.subject_offerings = page.get_by_role("button", name="Subject Offerings Connect")
        self.portal_invitations = page.get_by_role("button", name="Portal Invitations Teacher")
        self.total_teachers = page.get_by_role("button", name="Total teachers 1 All teacher")
        self.active_teachers = page.get_by_role("button", name="Active teachers 1 Currently")
        self.pending_teacher_profiles = page.get_by_role("button", name="Pending profiles 0 Profiles")
        self.archived_teacher_records = page.get_by_role("button", name="Archived records 0 Inactive")
        self.academic_linkage = page.get_by_role("button", name="Academic Linkage Review")


        

    
    
    def click_add_teacher(self):
        self.add_teacher.click()


    def click_subject_offerings(self):
        self.subject_offerings.click()

    def click_portal_invitations(self):
        self.portal_invitations.click()

    def click_academic_linkage(self):
        self.academic_linkage.click()
