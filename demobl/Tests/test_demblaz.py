import allure
import pytest
from demobl.Page.demoblaze_page import EndToEnd


class TestBase:
    demoblaz = EndToEnd()
    demoblaz._open()

class TestlogninDemb(EndToEnd, TestBase):

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_del(self):  # deleting from cart 10 ####
        self.execute_delete()
        pytest.skip('skipping test..later i will check it')

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_display(self):  ## display 14
        self.execute_display()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_disbuton(self):  ##display button 17
        self.execute_dButton()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_contactuss(self):  ## try to send message to contact Us 18
        self.execute_contactUs()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_contactus_noText(self):  ## try to send message without text to contact Us 19  (fail)
        self.execute_contactUs_noText()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_contactus_noNme(self):  ## try to send message without Nmae to contact Us 20  (fail)
        self.execute_contactUs_no_name()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_contactus_noacc(self):  ## try to send message without Nmae to contact Us 22  (faill)
        self.execute_contactUs_no_account()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_g_color(self):
        self.execute_backGround_color()
        pytest.skip('skipping test..later i will check it')

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_chekinbuton(self):  # order product 11
        self.execute_chekinbuttons()

    # pytest.skip('skipping test..later i will check it')
    @allure.severity(allure.severity_level.MINOR)
    def test_next(self):  # page preview 9
        self.execute_next()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_aboutUs(self):  ## cheking about us 13
        self.execute_about_us()
        # pytest.skip('skipping test..later i will check it')