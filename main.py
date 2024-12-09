import datetime
import functools
import multiprocessing
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from input_options import InputOptions


def setup_webdriver(is_headless: bool) -> WebDriver:
    # Create new Firefox profile with muted audio (target page runs the tone on successful click)
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")

    options = webdriver.FirefoxOptions()
    options.profile = profile
    # Headless mode allows to run the program in the background (without the WebDriver's browser window being sequentially opened and closed)
    if is_headless:
        options.add_argument("--headless")

    return webdriver.Firefox(options=options, service=webdriver.FirefoxService())


def find_and_click_feeding_button(driver: WebDriver, is_verbose: bool) -> bool:
    button = driver.find_element(by=By.CLASS_NAME, value="single-pet-control-feed_button")
    if button is None:
        raise Exception("Feeding button not found!")
    if is_verbose:
        print("Feeding button found!")

    button.click()
    if driver.find_element(by=By.CLASS_NAME, value="single-pet-control-thank_you_message") is not None:
        if is_verbose:
            print("Click succeeded (\"thank_you_message\" found)!")
        return True
    return False


def feed_a_dog(options: InputOptions, iteration_number: int) -> bool:
    print("Running iteration number: {}".format(iteration_number))

    # Set up new browser instance and enter target webpage
    driver = setup_webdriver(options.headless)
    driver.get("https://nakarmpsa.olx.pl/")

    # Find and click the first available feeding button
    action_result = find_and_click_feeding_button(driver, options.verbose)

    # Close the browser instance (only one click per browser instance is possible).
    # `quit()` method is chosen here over the `close()` method in order to terminate any WebDriver's resources
    # (background processes and sessions) and prevent them from staying alive after each script iteration.
    driver.quit()

    return action_result


if __name__ == "__main__":
    print("Feeding script starts...\n")

    input_options = InputOptions()
    pool = multiprocessing.Pool(processes=input_options.threads)

    start = time.time()
    result = pool.map(functools.partial(feed_a_dog, input_options), range(1, input_options.iterations + 1))
    end = time.time()
    elapsed_time = datetime.timedelta(seconds=end - start)

    print("\nFeeding script finished!")
    print("Elapsed time: {} (~{} seconds)".format(elapsed_time, elapsed_time.seconds))
    print("Iterations: {}".format(input_options.iterations))
    print("Successful clicks: {}".format(result.count(True)))
