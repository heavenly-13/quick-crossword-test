from playwright.sync_api import sync_playwright
from PIL import ImageGrab
import datetime
import os
import time

def run(playwright):
    start_time = time.time()
    try:
        # Launch the browser
        browser = playwright.chromium.launch(headless=False)
        print("Browser launched.")

        # Open a new page
        page = browser.new_page()
        print("New page opened.")

        # Navigate to the target webpage
        print("Navigating to the target webpage...")
        page.goto("https://www.gamelab.com/games/daily-quick-crossword")
        print("Page loading...") # Documenting page loading
        # Wait for the page to load completely
        page.wait_for_load_state('networkidle')
        print("Page loaded successfully.")

        # Close the privacy close button if present
        close_privacy = '.css-47sehv'
        if page.query_selector(close_privacy):
            page.click(close_privacy)
            print("Privacy close button clicked.")
        else:
            print("Privacy close button not found.")

        # Wait for 1.5 seconds
        page.wait_for_timeout(1500)

        # Close ad if present (first type)
        try:
            close_ad_button_locator = page.frame_locator("#ark_pre-roll iframe").frame_locator(
                "iframe[name=\"google_ads_iframe_\\/100151972\\/www\\.gamelab\\.com\\/h5_0\"]").get_by_label("Close ad")
            close_ad_button_locator.click(timeout=5000) # Set timeout to 5 seconds
            print("Ad 1 close button clicked.")
        except Exception as e:
            print("Ad 1 close button not found.")

        # Wait for 1.5 seconds
        page.wait_for_timeout(1500)

        # Close ad if present (second type)
        try:
            close_ad_button_locator = page.frame_locator("#ark_pre-roll iframe").frame_locator(
                "iframe[title=\"\\33 rd party ad content\"]").get_by_label("Close ad")
            close_ad_button_locator.click(timeout=5000) # Set timeout to 5 seconds
            print("Ad 2 close button clicked.")
        except Exception as e:
            print("Ad 2 close button not found.")

        # Wait for 1.5 seconds
        page.wait_for_timeout(1500)

        # Close ad if present (third type)
        try:
            close_ad_button_locator = page.frame_locator("#ark_pre-roll iframe").frame_locator(
                "iframe[title=\"\\33 rd party ad content\"]").frame_locator(
                "iframe[name=\"ad_iframe\"]").get_by_label("Close ad")
            close_ad_button_locator.click(timeout=5000) # Set timeout to 5 seconds
            print("Ad 3 close button clicked.")
        except Exception as e:
            print("Ad 3 close button not found.")

        # Wait for 1.5 seconds
        page.wait_for_timeout(1500)

        # Start game
        start_game_button = page.frame_locator("#canvas-box").locator("li").filter(
            has_text="Daily Bonus+50 PTSPLAY").locator("div").nth(1)
        start_game_button.click()
        print("Start game button clicked.")

        # Wait for 1.5 seconds
        page.wait_for_timeout(1500)

        # Attempt to extract the date
        print("Attempting to extract the date...")
        date_text = page.frame_locator("#canvas-box").locator("span").filter(has_text="Daily Quick Crossword:").text_content()
        # Extracting the date from the text
        date_str = date_text.replace("Daily Quick Crossword: ", "").split("By")[0].strip()
        date_obj = datetime.datetime.strptime(date_str, "%d %B %Y")
        extracted_date = date_obj.date()
        print("Date extracted:", extracted_date.strftime("%d %B %Y"))

        # Print out the current date
        current_date = datetime.datetime.now().date()
        print("Current date:", current_date.strftime("%d %B %Y"))

        # Compare the extracted date with the current date
        if extracted_date != current_date:
            raise ValueError("Extracted date does not match the current date.")

        print("The extracted date matches the current date.")

        # Click on 'Reveal' button
        print("Clicking on 'Reveal' button...")
        page.frame_locator("#canvas-box").get_by_role("button", name="Reveal").click()
        page.wait_for_timeout(1500)
        print("'Reveal' button clicked.")

        # Click on 'Reveal puzzle' button
        print("Clicking on 'Reveal puzzle' button...")
        page.frame_locator("#canvas-box").locator("li").filter(
            has_text="Reveal puzzle").click()
        page.wait_for_timeout(1500)
        print("'Reveal puzzle' button clicked.")

        # Take a screenshot and save it to the desktop
        print("Taking screenshot...") # Documenting screenshot capturing
        # Capture the entire screen
        screenshot = ImageGrab.grab()

        # Get the path to the desktop directory
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Save the screenshot to the desktop
        screenshot_path = os.path.join(desktop_path, 'screenshot.png')
        screenshot.save(screenshot_path)

        print("Screenshot saved to desktop:", screenshot_path)

        # Close the screenshot
        screenshot.close()

        # Close the browser
        print("Closing the browser.")
        browser.close()
        
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"Test completed in {duration:.2f} seconds.")

with sync_playwright() as playwright:
    run(playwright)
