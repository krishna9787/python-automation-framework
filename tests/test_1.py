import allure
import pytest
from allure_commons.types import AttachmentType 

@pytest.mark.usefixtures('setup_and_teardown')
class TestSearch:
    @allure.epic("Orders")
    @allure.testcase("TMS-436")
    def test_1(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="test_1", attachment_type=AttachmentType.PNG)
        print("This is test")