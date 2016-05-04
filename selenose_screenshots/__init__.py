from nose.plugins import Plugin
from selenium.common.exceptions import WebDriverException

from datetime import datetime
import os


class SeleNoseScreenshots(Plugin):
    name = 'selenose-screenshots'
    score = 200

    def options(self, parser, env=os.environ):
        default_screenshot_dir = os.path.abspath(os.path.join(os.getcwd(), 'selenose_screenshots'))
        parser.add_option('--screenshot-on-error', action='store_true',
                          help="Make a selenium screenshot on webdriver errrors")
        parser.add_option('--screenshot-dir', default=default_screenshot_dir,
                          help="Folder to store screenshots in")

    def configure(self, options, conf):
        setattr(options, self.enableOpt, bool(options.screenshot_on_error))
        self.screenshot_dir = options.screenshot_dir
        super().configure(options, conf)

    def addError(self, test, err):
        etype, evalue, etraceback = err
        if issubclass(etype, WebDriverException) or etype == WebDriverException:
            try:
                driver = test.test.driver
            except:
                return
            if not os.path.exists(self.screenshot_dir):
                os.makedirs(self.screenshot_dir)

            filename = '{0}_{1}.png'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), test.id())
            driver.get_screenshot_as_file(os.path.join(self.screenshot_dir, filename))
