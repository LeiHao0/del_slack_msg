# delete slack msg on macOS

`del_slack_msg.py` is a Python script designed to automate the process of deleting messages from a Slack chat interface using the PyAutoGUI library. This script identifies specific messages and performs deletion actions based on certain detected text patterns.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

-   Python (3.x recommended)
-   Required Python packages: `pyautogui`, `pytesseract`, and `Pillow`

You can install the required packages using the following command:

```bash 
pip install pyautogui pytesseract Pillow
```

Additionally, you need to have Google's Tesseract OCR engine installed on your system. You can download it from the [official Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

## Usage


1.  Clone or download the repository containing the `del_slack_msg.py` script.
2. Open Chrome / Slack and resize the window to fill left-side screen
3. Find the (x, y) (press shift+command+4) for the last message under **More actions**
4. Open a terminal or command prompt and navigate to the directory where the script is located.
5. modify `pyautogui.moveTo(x=212, y=50)` and `x, y = 1565, 1640`
6. Run the script using the following command:
    
```bash
python del_slack_msg.py
```

4.  The script will execute and interact with a Slack chat interface open in your web browser.

## Configuration

-   `num_iterations`: Number of message deletion iterations to perform.
-   `min_delay` and `max_delay`: Minimum and maximum delay between actions to simulate human-like interaction.

## Script Workflow

1.  The script moves the mouse cursor to a specific position to activate the Slack tab in the Chrome browser.
2.  It iterates through the specified number of iterations.
3.  For each iteration, the script performs the following steps:
    -   Moves the cursor to a target message.
    -   Simulates clicks and delays to navigate to the message's "Delete" option.
    -   Captures a screenshot around the "Delete" option and uses OCR to detect text.
    -   Based on the detected text, performs deletion actions like clicking "Remove" or pressing "Enter."
    -   If no relevant text is detected, the script attempts alternative deletion actions.

## Important Notes

-   This script assumes a specific Slack chat interface layout and positioning of UI elements. Any changes to Slack's layout may require script adjustments.
-   The script uses OCR for text detection in screenshots. Text detection accuracy may vary based on factors like image quality and font.
-   Use this script responsibly and in accordance with Slack's terms of service. Automated mass deletion of messages may violate Slack's policies.

**Disclaimer:** This script is provided as-is and may require adjustments based on your environment and use case. Use at your own risk.

## License

This project is licensed under the [MIT License](https://chat.openai.com//LICENSE).
