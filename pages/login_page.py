from playwright.sync_api import Page 

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.school_code = page.get_by_role("textbox", name="School code")
        self.username_or_email = page.get_by_role("textbox", name="Username or email address")
        self.password = page.get_by_role("textbox", name="Password")
        self.sign_in_button = page.get_by_role("button", name="Sign in")
        self.error_message=page.get_by_text("Invalid school or credentials")
        self.invalid_password=page.get_by_text("Invalid input parameters")
        self.forgot_password1=page.get_by_role("link", name="Forgot password?")
        self.f_email_address=page.get_by_role("textbox", name="Email address")
        self.sent_reset_link=page.get_by_role("button", name="Send Reset Link")
        self.back_to_login=page.get_by_role("link", name="Back to Login")
        self.home_button=page.get_by_role("button", name="Home")
        self.student_button=page.get_by_role("button", name="Students")
        self.teacher_button=page.get_by_role("button", name="Teachers")
        self.staff_button=page.get_by_role("button", name="Staff")
        self.academics_button=page.get_by_role("button", name="Academics")
        self.attendance_button=page.get_by_role("button", name="Attendance")
        self.fee_button=page.get_by_role("button", name="Fee")
        self.expenses_button=page.get_by_role("button", name="Expenses")
        self.payroll_button=page.get_by_role("button", name="Payroll")
        self.balance_sheet_button=page.get_by_role("button", name="Balance Sheet")
        self.set_up_button=page.get_by_role("button", name="Setup")
        self.users_button=page.get_by_role("button", name="Users")
        self.settings_button=page.get_by_role("button", name="Settings", exact=True)
        self.user_account_menu=page.get_by_role("button", name="account of current user")
        self.notifications_icon=page.get_by_role("button", name="notifications")
        self.welcome_message = page.get_by_text("Welcome back")
        self.school_branding = page.get_by_text("Chaitanya Public School")
        self.control_tower = page.get_by_text("Today's Control Tower")
        self.attendance_health = page.get_by_text("Attendance Health")
        self.fee_collection = page.get_by_text("Fee Collection")
        self.academic_execution = page.get_by_role("heading",name="Academic Execution")
        self.teacher_coverage = page.get_by_role("heading",name="Teacher Coverage")
        self.fee_followups = page.get_by_text("Fee Follow-ups")
        self.rahul_verma = page.get_by_text("Rahul Verma")
        self.sneha_iyer = page.get_by_text("Sneha Iyer")
        self.upcoming_calendar = page.get_by_text("Upcoming Calendar")
        self.no_up_coming_events = page.get_by_text("No upcoming events")
        self.announcements = page.get_by_text("Announcements")
        self.announcement_card = page.get_by_role("button",name="Welcome to Academic Year 2026-27! 01 Jun")
        self.operational_journal=page.get_by_role("heading", name="Operational Journal")
        
       
       
        
        
       
        

    




    def navigate(self,url:str):
        self.page.goto(url)

    def login(self, school_code:str, username_or_email:str, password:str):
        self.school_code.fill(school_code)
        self.username_or_email.fill(username_or_email)
        self.password.fill(password)
        self.sign_in_button.click()
    
    def forgot_password(self):
        self.forgot_password1.click()

    def click_home(self):
        self.home_button.click() 

    def click_students(self):
        self.student_button.click() 

    def click_teachers(self):
        self.teacher_button.click() 

    def click_staff(self):
        self.staff_button.click() 

    def click_academics(self):
        self.academics_button.click() 

    def click_attendance(self):
        self.attendance_button.click() 
    
    def click_fee(self):
        self.fee_button.click()

    def click_expenses(self):
        self.expenses_button.click()

    def click_payroll(self):
        self.payroll_button.click()

    def click_balance_sheet(self):
        self.balance_sheet_button.click()
    
    def click_set_up(self):
        self.set_up_button.click()

    def click_users(self):
        self.users_button.click()

    def click_settings(self):
        self.settings_button.click()

    def click_user_account_menu(self):
        self.user_account_menu.click()

    def click_notifications_icon(self):
        self.notifications_icon.click()

   
    def click_subject_master(self):
        self.subject_master.click()





  
    