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

    def navigate(self,url:str):
        self.page.goto(url)

    def login(self, school_code:str, username_or_email:str, password:str):
        self.school_code.fill(school_code)
        self.username_or_email.fill(username_or_email)
        self.password.fill(password)
        self.sign_in_button.click()
    
    def forgot_password(self):
        self.forgot_password1.click()

        


   
        
        
        
