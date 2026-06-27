from playwright.sync_api import Page


class Dashboard:
    def __init__(self, page: Page):
        self.page = page
        self.school_branding = page.get_by_text("Chaitanya Public School")
        self.welcome_message = page.get_by_text("Welcome back")
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
