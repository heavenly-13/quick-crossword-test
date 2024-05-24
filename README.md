# Deliverables
  - [**Manual Tests**](#manual-tests)
    - [Test Plan](#test-plan) - Test plan document in spreadsheet format.
    - [Bug Report](#bug-report) - Report of a bug found on the SUT.
    - [Observations](#observations) - Document with observations and comments.
  - [**Test Automation**](#test-automation)
    - [Automation Script](#automation-script) - Automation script written in Python using Playwright.
    - [Prerequisites](#prerequisites-and-running-the-script) - Any necessary instructions or dependencies for running the script.
    - [Test Execution Report](#test-execution-report) - A brief report of the test execution, including any observed issues or failures.
    - [Automation Video](#automation-video) - Automation video, showing the automation in progress.
    - [Automation Questionnaire](#automation-questionnaire) - Document with answer to provided automation question. 

## Manual Tests

### Test Plan

### Bug Report
[bug-report.docx](https://github.com/heavenly-13/quick-crossword-test/blob/main/bug-report.docx)
[bug-screenshot.png](https://github.com/heavenly-13/quick-crossword-test/blob/main/bug-screenshot.png)
[bug-recording.mp4](https://github.com/heavenly-13/quick-crossword-test/blob/main/bug-recording.mp4)
### Observations
[observations-and-comments](https://github.com/heavenly-13/quick-crossword-test/blob/main/observations-and-comments.docx)

## Test Automation

### Automation Script
[quick-crossword-test.py](https://github.com/heavenly-13/quick-crossword-test/blob/main/quick-crossword-test.py)

### Prerequisites and Running the Script

Before running the script, ensure you have the following dependencies installed:

1. **Python**: Make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

2. **Playwright for Python**: Install Playwright for Python. You can install Playwright by running the following command in your terminal:
   ```
   pip install playwright
   ```

3. **Pillow**: Install Pillow using pip. Pillow is a Python Imaging Library (PIL), which is required for capturing screenshots. You can install Pillow by running the following command:
   ```
   pip install Pillow
   ```

Once you have installed the dependencies, follow these steps to run the script:

1. Download the provided script ([quick-crossword-test.py](https://github.com/heavenly-13/quick-crossword-test/blob/main/quick-crossword-test.py)).
2. Open a terminal.
3. Navigate to the directory where the script is saved.
4. Run the script using Python by executing the following command:
   ```
   python quick-crossword-test.py
   ```
   
## Test Execution Report

1. **Navigation and Page Loading:**
   - The script successfully navigated to the target webpage (`https://www.gamelab.com/games/daily-quick-crossword`) and waited for the page to load completely.
   - No issues observed during the page loading process.

2. **Advertisement Handling:**
     - The script handled closing of a privacy confirmation window.
   - The script attempted to close three types of ads if present on the page.
   - Each ad close button was clicked if found, and appropriate messages were printed indicating success or failure.
   - No issues observed in handling the advertisements.
     - Rarely an advertisement might appear that's not handled by the code, in such edge case the terminal will provide an error and the script has to be restarted.
     - The code can be optimized to not wait for each ad.

4. **Game Start:**
   - The script clicked on the "Start game" button.
   - No issues observed during the game start process.

5. **Date Extraction and Comparison:**
   - The script successfully extracted the date from the webpage and the current date.
   - The extracted date was compared with the current date, and a message was printed indicating whether they matched or not.
   - No discrepancies observed between the extracted date and the current date.

6. **Screenshot Capturing:**
   - The script successfully captured a screenshot of the webpage after completing the necessary actions.
   - The screenshot was saved to the Desktop.
   - No issues observed during the screenshot capturing process.

7. **Browser Closure:**
   - The browser was closed at the end of the script execution.
   - No issues observed during the browser closure.
     - The time the test took is printed.

#### Overall Observations:
- The script executed all the required actions successfully without encountering any errors or failures.
- All expected functionalities, including page navigation, ad handling, date extraction, and screenshot capturing, were performed as intended.

### Automation Video
[quick-crossword-automation-video.mp4](https://github.com/heavenly-13/quick-crossword-test/blob/main/quick-crossword-automation-video.mp4)

### Automation Questionnaire
[questionnaire-automation.docx](https://github.com/heavenly-13/quick-crossword-test/blob/main/questionnaire-automation.docx)
