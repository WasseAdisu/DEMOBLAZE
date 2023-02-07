import allure
import pytest

from demobl.Page.demoblaze_page import EndToEnd

class TestBase3:
    demoblaz = EndToEnd()
    demoblaz._open()

class TestAllDemb(EndToEnd, TestBase3):

    @allure.severity(allure.severity_level.NORMAL)
    def test_home(self):  # order product 6
        self.execute_prodact_addingTo_cart()
        # pytest.skip('skipping test..later i will check it')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_withotCcard(self):  # # order without credit card 7
        self.execute_order_incorect_ccard()
        # pytest.skip('skipping test..later i will check it')

    ## order with card letters 12        expected error message but no       (fail)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_cardletters(self):
        self.execute_orderWith_cCardLetter()

    @allure.severity(allure.severity_level.NORMAL)
    def test_order_wcontry(self):  # page preview 8              expected error but no     (fail)
        self.execute_orderWithout_country()
        # pytest.skip('skipping test..later i will check it')

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_phon(self):  ## cheking about us 13
        self.execute_phones()
        # pytest.skip('skipping test..later i will check it')

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_laps(self):  ## cheking about us 13
        self.execute_lapto()
        # pytest.skip('skipping test..later i will check it')

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.functional
    def test_mont(self):  ## cheking about us 13
        self.execute_monitor()
        # pytest.skip('skipping test..later i will check it')