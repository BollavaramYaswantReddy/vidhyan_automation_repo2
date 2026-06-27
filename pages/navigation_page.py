from playwright.sync_api import Page


class Navigation:
    def __init__(self, page: Page):
        self.page = page
        self.home_button=page.get_by_role("button", name="Home")
        self.teacher_button=page.get_by_role("button", name="Teachers")
        # self.staff_button=page.get_by_role("button", name="Staff")
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


    def click_home(self):
        self.home_button.click()


    # def click_teachers(self):
    #     self.teacher_button.click()


    # def click_staff(self):
    #     self.staff_button.click()


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

    
