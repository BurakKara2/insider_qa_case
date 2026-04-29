import pytest
import uuid
import base64  # For encoding screenshots to base64
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

@pytest.fixture(scope="function")
def page(request):
    """
    Launches a new browser instance for each test function.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page_instance = context.new_page()
        
        request.node.page_instance = page_instance
        
        yield page_instance 
        
        context.close()
        browser.close()

# ==============================================================================
# GLOBAL AUTO-SCREENSHOT HOOK ON FAILURE (BASE64)
# ==============================================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture errors during both 'setup' and 'call' phases
    if report.when in ['setup', 'call'] and report.failed:
        
        page_instance = getattr(item, 'page_instance', None)
        
        if page_instance:
            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_id = str(uuid.uuid4())[:8] 
            
            screenshot_dir = "failed_screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            
            screenshot_path = os.path.join(screenshot_dir, f"FAIL_{test_name}_{timestamp}_{unique_id}.png")
            
            # Take a screenshot using Playwright and capture it as 'bytes'
            screenshot_bytes = page_instance.screenshot(path=screenshot_path, full_page=True)
            
            print(f"\n[GLOBAL AUTO-SCREENSHOT]: Test failed! Screenshot captured at: {screenshot_path}")
            
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                
                # Convert image to Base64 format to eliminate external file dependency
                encoded_img = base64.b64encode(screenshot_bytes).decode('utf-8')
                
                # Embed data directly instead of using an external link in HTML
                html = f'<div><img src="data:image/png;base64,{encoded_img}" alt="screenshot" style="width:600px;height:300px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                
                extra.append(pytest_html.extras.html(html))
                report.extra = extra