import time
import random
import pyautogui
import pytesseract
from PIL import ImageGrab

num_iterations = 2
min_delay = 0.03
max_delay = 0.1

total_elapsed_time = 0

pyautogui.moveTo(x=212, y=50)  # enable chrome tab
pyautogui.click()

for i in range(1, num_iterations + 1):
    iteration_start_time = time.time()

    print(f"Iteration {i}:")

    action_start_time = time.time()

    x, y = 1565, 1640  # last msg
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(min_delay, max_delay))

    x, y = x, y-30  # ...
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(min_delay, max_delay))
    pyautogui.click()
    time.sleep(random.uniform(min_delay, max_delay))

    x, y = x-215, y+150  # Delete message...
    pyautogui.moveTo(x, y)

    screenshot = ImageGrab.grab(bbox=(x-300, y-20, x+300, y+20))
    detected_text = pytesseract.image_to_string(screenshot).lower()

    print(f"  Detected Text: {detected_text.strip()}")

    if 'remove' in detected_text:
        pyautogui.click()
        time.sleep(random.uniform(min_delay, max_delay))
        pyautogui.moveTo(x-120, y-675)
        pyautogui.click()
    elif 'delete' in detected_text:
        pyautogui.click()
        time.sleep(random.uniform(min_delay, max_delay))
        pyautogui.press('enter')
    else:
        pyautogui.moveTo(x-200, y-130)
        pyautogui.click()
        pyautogui.press('up')

    time.sleep(random.uniform(min_delay, max_delay))

    action_elapsed_time = time.time() - action_start_time
    total_elapsed_time += action_elapsed_time

    print(f"  Action Elapsed Time: {action_elapsed_time:.2f} seconds")

    print("-" * 30)

print(
    f"Total Elapsed Time for {num_iterations} iterations: {total_elapsed_time:.2f} seconds")
