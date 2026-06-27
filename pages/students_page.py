from playwright.sync_api import Page


class Students:
    def __init__(self, page: Page):
        self.page = page
        self.student_desk = page.get_by_role("heading", name="Student Desk")
        self.student_directory_find = page.get_by_role("button", name="Student Directory Find")
        self.student_directory_table= page.get_by_role("heading", name="Student Directory")
        self.student_guardian=  page.get_by_role("button", name="Guardian Directory Maintain")    
        self.Add_students=page.get_by_role("button", name="Add Student Create a new")
        self.enroll_to_class=page.get_by_role("button", name="Enroll to Class Assign class")
        self.add_guardian=page.get_by_role("button", name="Add Guardian Create parent or")
        self.link_guardian=page.get_by_role("button", name="Link Guardian Connect")
        self.student_leadership=page.get_by_role("button", name="Student Leadership Track")
        self.total_students = page.get_by_text("Total Students")
        self.active_students = page.get_by_text("Active Students")
        self.pending_profiles = page.get_by_text("Pending Profiles")
        self.guardian_directory = page.get_by_role("button",name="Guardian Directory Maintain")
        self.breadcrumb = page.get_by_role("navigation", name="breadcrumb")




    def click_student_directory(self):
        self.student_directory_find.click()


    def click_guardian_directory(self):
        self.student_guardian.click()


    def click_add_students(self):
        self.Add_students.click()


    def click_enroll_to_class(self):
        self.enroll_to_class.click()


    def click_add_guardian(self):
        self.add_guardian.click()


    def click_link_guardian(self):
        self.link_guardian.click()

    
    def click_student_leadership(self):
        self.student_leadership.click()

   

    
   
