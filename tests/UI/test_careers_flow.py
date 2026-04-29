import re
from pages.home_page import HomePage
from pages.careers_page import CareersPage

class TestCareersFlow:
    
    def test_verify_qa_jobs_location_and_department(self, page):
        """
        Verifies the QA job listing details and the application flow on the Careers page.
        """
        home_page = HomePage(page)
        home_page.navigate_to_careers()
        
        careers_page = CareersPage(page)
        careers_page.filter_qa_jobs()
        jobs = careers_page.get_all_job_listings()
        
        # Verify the presence and correctness of the job listings
        assert len(jobs) > 0, "Job list is empty, filtering might have failed!"
        
        for job in jobs:
            assert "quality assurance" in job.position.lower() or "qa" in job.position.lower(), \
                f"Job title should contain 'Quality Assurance' or 'QA', but found '{job.position}'."

            assert "quality assurance" in job.department.lower(), \
                f"Expected department is 'Quality Assurance', but found '{job.department}'."

            assert "istanbul" in job.location.lower(), \
                f"Expected location is 'Istanbul', but found '{job.location}'."
        # Click the Apply button and verify redirection to the Lever page
        lever_page = careers_page.click_first_job_apply()
        
        assert re.search(r".*jobs\.lever\.co.*", lever_page.url), "URL does not contain 'jobs.lever.co'!"