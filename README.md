# Insider QA Automation Bootcamp'26 - Final Project

**Author:** Burak Karakoyunlu
**Email:** burakkrkynlu@gmail.com

---

## 🚀 Project Overview
This repository contains a professional E2E UI Automation Framework built for the Insider Career portal. It follows the **Page Object Model (POM)** pattern and integrates **CI/CD** pipelines with **AI-enhanced** error handling and reporting.

## 🛠 Tech Stack
* **Language:** Python 3.13
* **Framework:** Pytest
* **Automation Tool:** Playwright
* **Reporting:** Pytest-HTML (with Base64 Screenshot Embedding)
* **CI/CD:** GitHub Actions

## 📝 Test Scenario
The following automated flow verifies the integrity of the Quality Assurance job listings:
1. Navigate to [https://insiderone.com/](https://insiderone.com/) and verify the Home Page.
2. Navigate to the **Careers** page and verify the presence of "Locations", "Teams", and "Life at Insider" sections.
3. Filter jobs by **Category:** "Quality Assurance" and **Location:** "Istanbul, Turkey".
4. Verify that all listed jobs are correctly filtered by:
   - **Position:** Contains "Quality Assurance" or "QA".
   - **Department:** Matches "Quality Assurance".
   - **Location:** Matches "Istanbul, Turkey".
5. Click "View Role" for the first listing and verify redirection to the **Lever** application page.

## 🤖 AI-Supported Flow Integration
AI was strategically utilized during development to:
* **Architectural Guidance:** Optimize the Page Object Model structure.
* **Selector Stability:** Identify robust locators to prevent flakiness.
* **Smart Reporting:** Implement an AI-suggested custom hook in `conftest.py` that captures Base64-encoded screenshots upon failure and embeds them directly into the HTML report for instant debugging.

## 🔄 CI/CD Configuration
The project is fully integrated with **GitHub Actions**:
* **Triggers:** Automatically runs on every `push` and `pull_request` to the main branch.
* **Execution:** Installs dependencies, sets up Playwright browsers, and executes the test suite.
* **Artifacts:** Upon completion, the `report.html` file is published as a build artifact for review.

## 📊 Reporting & Outputs
* **HTML Report:** A self-contained `report.html` is generated after each run.
* **Screenshots:** If a test fails (e.g., encountering a non-Istanbul listing), a screenshot is automatically captured and displayed within the report.

## ⚙️ How to Run Locally
1. Clone the repository: `git clone https://github.com/BurakKara2/insider_qa_case.git`
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `playwright install`
6. Run tests: `pytest --html=report.html`