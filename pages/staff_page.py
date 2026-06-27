from playwright.sync_api import Page


class Staff:
    def __init__(self, page: Page):
        self.page = page
        self.staff_directory = page.get_by_role("button", name="Staff Directory Find non-")
        self.add_staff = page.get_by_role("button", name="Add Staff Create a staff")
        self.drivers_staff = page.get_by_role("button", name="Drivers Review transport staff")
        self.facilities_staff = page.get_by_role("button", name="Facilities Review support")
        self.operations_roles_staff = page.get_by_role("button", name="Operations Roles Maintain")
        self.employment_status_staff = page.get_by_role("button", name="Employment Status Keep active")
        self.Total_staff = page.get_by_role("button", name="Total staff 2 All staff")
        self.active_staff = page.get_by_role("button", name="Active staff 2 Currently")
        self.drivers_desk_transport = page.get_by_role("button", name="Drivers 0 Transport-ready")
        self.janitors = page.get_by_role("button", name="Janitors 0 Facilities support") 



    def click_staff_directory(self):
        self.staff_directory.click()


    def click_add_staff(self):
        self.add_staff.click() 


    def click_drivers_staff(self):
        self.drivers_staff.click()


    def click_facilities_staff(self):
        self.facilities_staff.click()

    
    def click_operations_roles_staff(self):
        self.operations_roles_staff.click()

    
    def click_employment_status_staff(self):
        self.employment_status_staff.click()

