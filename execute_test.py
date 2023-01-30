import allure
import pytest

from demobl.Page.page import EndToEnd


@allure.severity(allure.severity_level.CRITICAL)
class TestBase:
    demoblaz = EndToEnd()
    demoblaz._open()

class TestProducts(EndToEnd, TestBase):

    def test_signUp(self):  # signup 1
        self.execute_sign_upp()
        pytest.skip('skipping test..later i will check it')

    def test_singnUp_inco(self):  # singnUP incorrectly without name and password 2
        self.execute_sign_up_incorrectly()

    def test_singnUp_withotPasword(self):  # singnUP incorrectly 3
        self.execute_sign_up_withoutPassword()

    def test_login(self):  # login correctly 4
        self.execute_login()

    def test_login_incorrect(self):  # login incorrectly  5
        self.execute_login_inc()

    def test_home(self):  # order product 6
        self.execute_prodact_addingTo_cart()
        pytest.skip('skipping test..later i will check it')

    def test_withotCcard(self):  # # order without credit card 7
        self.execute_order_incorect_ccard()
        pytest.skip('skipping test..later i will check it')

    def test_order_wcontry(self):  # page preview 8              expected error but no     (fail)
        self.execute_orderWithout_country()
        pytest.skip('skipping test..later i will check it')

    def test_next(self):  # page preview 9
        self.execute_next()

    def test_del(self):  # deleting from cart 10 ####
        self.execute_delete()

    def test_chekinbuton(self):  # order product 11
        self.execute_chekinbuttons()
        pytest.skip('skipping test..later i will check it')

    ## order with card letters 12        expected error message but no       (fail)
    def test_cardletters(self):
        self.execute_orderWith_cCardLetter()

    def test_aboutUs(self):   ## cheking about us 13
        self.execute_about_us()
        pytest.skip('skipping test..later i will check it')

    def test_display(self):  ## display 14
        self.execute_display()

    def test_logwNmane(self):  # login without name 15
        self.execute_login_incName()

    def test_no_namPw(self):  ## try to logn without name and password 16
        self.execute_waCcount()

    def test_disbuton(self):  ##display button 17
        self.execute_dButton()

    def test_contactuss(self):  ## try to send message to contact Us 18
        self.execute_contactUs()

    def test_contactus_noText(self):  ## try to send message without text to contact Us 19  (fail)
        self.execute_contactUs_noText()

    def test_contactus_noNme(self):  ## try to send message without Nmae to contact Us 20  (fail)
        self.execute_contactUs_no_name()

    def test_contactus_nomil(self):  ## try to send message without Nmae to contact Us 21  (fail)
        self.execute_contactUs_no_email()

    def test_contactus_noacc(self):  ## try to send message without Nmae to contact Us 22  (faill)
        self.execute_contactUs_no_account()
