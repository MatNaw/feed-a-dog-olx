from selenium import webdriver
from selenium.webdriver.common.by import By

ITERATIONS = 2


def setup_webdriver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")

    options = webdriver.FirefoxOptions()
    options.profile = profile
    # options.add_argument("--headless")

    return webdriver.Firefox(options=options, service=webdriver.FirefoxService())


def find_and_click_feeding_button(driver):
    button = driver.find_element(by=By.CLASS_NAME, value="single-pet-control-feed_button")
    if button is None:
        raise Exception("Feeding button not found!")
    print("Button found!")

    button.click()
    if driver.find_element(by=By.CLASS_NAME, value="single-pet-control-thank_you_message") is not None:
        print("Click succeeded (\"thank_you_message\" found)!")


def feed_a_dog():
    driver = setup_webdriver()
    driver.get("https://nakarmpsa.olx.pl/")

    find_and_click_feeding_button(driver)

    driver.close()


if __name__ == "__main__":
    print("Feeding script starts...")
    for i in range(1, ITERATIONS + 1):
        print("Iteration number: {}".format(i))
        feed_a_dog()
    print("Feeding script finished successfully with following number of iterations: {}".format(ITERATIONS))
