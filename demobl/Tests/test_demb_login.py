import allure
import pytest
from selenium.webdriver.common.by import By

from demobl.Page.demoblaze_page import EndToEnd

class TestBase2:
    demoblaz = EndToEnd()
    demoblaz._open()

class TestProducts(EndToEnd, TestBase2):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signUp(self):  # signup 1
        self.execute_sign_upp()

    @allure.severity(allure.severity_level.MINOR)
    def test_singnUp_inco(self):  # singnUP incorrectly without name and password 2
        self.execute_sign_up_incorrectly()

    @allure.severity(allure.severity_level.NORMAL)
    def test_singnUp_withotPasword(self):  # singnUP incorrectly 3
        self.execute_sign_up_withoutPassword()

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):  # login correctly 4
        self.execute_login()

    @allure.severity(allure.severity_level.NORMAL)
    def test_logio(self):  # login correctly 4
        self.execute_loginout()

    @allure.severity(allure.severity_level.MINOR)
    def test_login_incorrect(self):  # login incorrectly  5
        self.execute_login_inc()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_logwNmane(self):  # login without name 15
        self.execute_login_incName()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_no_namPw(self):  ## try to logn without name and password 16
        self.execute_waCcount()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_contactus_nomil(self):  ## try to send message without Nmae to contact Us 21  (fail)
        self.execute_contactUs_no_email()


    def test_gcolor(self):
        assert self.back_col == "#fff"