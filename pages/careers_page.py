from base.base_page import BasePage
from dataclasses import dataclass
from playwright.sync_api import TimeoutError

@dataclass
class JobInfo:
    position: str
    department: str
    location: str

class CareersPage(BasePage):
    URL = "https://insiderone.com/careers/"
    
    EXPLORE_OPEN_ROLES_BTN = "text='Explore open roles' >> nth=0"
    SEE_ALL_TEAMS_BTN = ".see-more"
    QA_TEAM_CARD = "a[href*='Quality%20Assurance']"
    
    JOB_LIST_ITEM = ".posting" 
    POSITION_TITLE = "[data-qa='posting-name']" 
    LOCATION_NAME = ".location" 
    APPLY_BTN = ".posting-btn-submit"

    def check(self):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector(self.EXPLORE_OPEN_ROLES_BTN, state="visible")

    def filter_qa_jobs(self):
        self.wait_and_click(self.EXPLORE_OPEN_ROLES_BTN)
        self.page.wait_for_selector(self.SEE_ALL_TEAMS_BTN, state="visible")
        self.wait_and_click(self.SEE_ALL_TEAMS_BTN)
        self.wait_and_click(self.QA_TEAM_CARD)

    def get_all_job_listings(self):
        self.page.locator(self.JOB_LIST_ITEM).first.wait_for(state="visible") 
        
        job_elements = self.page.locator(self.JOB_LIST_ITEM).all()
        jobs = []
        
        for job_el in job_elements:
            position = job_el.locator(self.POSITION_TITLE).inner_text()
            location = job_el.locator(self.LOCATION_NAME).inner_text()
            department = job_el.locator("xpath=ancestor::div[contains(@class, 'postings-group')]").locator(".posting-category-title").inner_text()
            
            jobs.append(JobInfo(position=position, department=department, location=location))
            
        return jobs

    def click_first_job_apply(self):
        # Smart Tab Management:
        try:
            # Wait up to 5 seconds for a new tab (popup) to open after clicking the button
            with self.page.context.expect_page(timeout=5000) as new_page_info:
                self.page.locator(self.APPLY_BTN).first.click()
            lever_page = new_page_info.value
        except TimeoutError:
            # If no new tab opens within 5 seconds, assume the flow continues in the same tab
            lever_page = self.page
            
        lever_page.wait_for_load_state("networkidle")
        return lever_page