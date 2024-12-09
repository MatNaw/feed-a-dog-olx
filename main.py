import datetime
import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from input_options import InputOptions

COUNT_ITERATOR = count()


def setup_webdriver() -> WebDriver:
    # Create new Firefox profile with muted audio (target page runs the tone on successful click)
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")

    options = webdriver.FirefoxOptions()
    options.profile = profile
    # Headless mode allows to run the program in the background (without the WebDriver's browser window being sequentially opened and closed)
    if input_options.headless:
        options.add_argument("--headless")

    return webdriver.Firefox(options=options, service=webdriver.FirefoxService())


def find_and_click_feeding_button(driver: WebDriver):
    button = driver.find_element(by=By.CLASS_NAME, value="single-pet-control-feed_button")
    if button is None:
        raise Exception("Feeding button not found!")
    verbose_log("Feeding button found!")

    button.click()
    if driver.find_element(by=By.CLASS_NAME, value="single-pet-control-thank_you_message") is not None:
        verbose_log("Click succeeded (\"thank_you_message\" found)!")
        next(COUNT_ITERATOR)


def feed_a_dog():
    # Set up new browser instance and enter target webpage
    driver = setup_webdriver()
    driver.get("https://nakarmpsa.olx.pl/")

    # Find and click the first available feeding button
    find_and_click_feeding_button(driver)

    # Close the browser instance (only one click per browser instance is possible).
    # `quit()` method is chosen here over the `close()` method in order to terminate any WebDriver's resources
    # (background processes and sessions) and prevent them from staying alive after each script iteration.
    driver.quit()


def verbose_log(message: str):
    if input_options.verbose:
        print(message)


if __name__ == "__main__":
    print("Feeding script starts...")

    input_options = InputOptions()

    start = time.time()
    for i in range(1, input_options.iterations + 1):
        print("Iteration number: {}".format(i))
        feed_a_dog()
    end = time.time()
    elapsed_time = datetime.timedelta(seconds=end - start)

    print("Feeding script finished!")
    print("Elapsed time: {} (~{} seconds)".format(elapsed_time, elapsed_time.seconds))
    print("Iterations: {}".format(input_options.iterations))
    print("Successful clicks: {}".format(next(COUNT_ITERATOR)))
