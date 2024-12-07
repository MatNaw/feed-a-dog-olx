# Project summary
A simple Python script using [Selenium](https://www.selenium.dev/) to automate clicks for OLX's annual campaign (https://nakarmpsa.olx.pl/).
As part of this campaign, the company buys food for animals residing in shelters.
More details about the campaign can be found in its [terms and conditions](https://nakarmpsa.olx.pl/regulamin/).

# Prerequisites
* Python with Selenium library

# Usage
Run the `main.py` script either via IDE (e.g. [PyCharm](https://www.jetbrains.com/pycharm/)) or via terminal from the 
project's root directory (`python main.py`).

Default number of iterations within the script is set to 15 (see corresponding `ITERATIONS` variable at the top of the script).
For more verbose logging while script is running, set `DEBUG_MODE` variable to `True`.