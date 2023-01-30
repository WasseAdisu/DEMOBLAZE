import time

import pytest
from selenium.webdriver.common.by import By

from demobl.Basse.basse import BasePage
from demobl.Locator.locater import Locator



class EndToEnd(Locator, BasePage):

    ## sign up 1

    def execute_sign_upp(self):
        pytest.skip('skipping test..later i will check it')
        # self._open()
        # # self._click(By.XPATH, self.home)
        # self._click(By.XPATH, self.sign_up)
        # time.sleep(1)
        # self._write(By.XPATH, self.signUp_name, 'hakappp')
        # self._write(By.XPATH, self.signUp_password, 'h3783h')
        # self._click(By.XPATH, self.sign_up_button)
        # time.sleep(1)
        # self.alert_ok()
        # time.sleep(1)

    ## sign up with out name and password 2
    def execute_sign_up_incorrectly(self):
        self._open()
        self._click(By.XPATH, self.signUp_without_nameAndPw_home)
        self._click(By.XPATH, self.signUp_without_nameAndPw)
        self._click(By.XPATH, self.signUp_without_nameAndPw_button)
        assert (self.alert_get(), "Please fill out Username and Password.")
        self.alert_ok()  # OK on alert box
        self._click(By.XPATH, self.signUp_without_nameAndPw_close)
        time.sleep(1)

    ## sign up without password 3

    def execute_sign_up_withoutPassword(self):
        self._click(By.XPATH, self.sign_up_withoutPassword_home)
        self._click(By.XPATH, self.sign_up_withoutPassword)
        time.sleep(1)
        self._write(By.XPATH, self.sign_up_withoutPassword_name, 'wass')
        self._click(By.XPATH, self.sign_up_withoutPassword_button)
        assert (self.alert_get(), "Please fill out Username and Password.")
        self.alert_ok()
        self._click(By.XPATH, self.sign_up_withoutPassword_close)
        time.sleep(1)

    ## login corrrectly 4
    def execute_login(self):
        self._click(By.XPATH, self.home)
        self._click(By.XPATH, self.loginn)
        time.sleep(1)
        self._write(By.XPATH, self.loginn_name, 'wasse')
        self._write(By.XPATH, self.loginn_password, '123was')
        self._click(By.XPATH, self.loginn_button)
        time.sleep(1)

    ## login incorect without password 5
    def execute_login_inc(self):
        self._click(By.XPATH, self.loginn_incorrect_home)
        self._click(By.XPATH, self.loginn_incorrect)
        time.sleep(1)
        self._write(By.XPATH, self.loginn_name_correct, 'wasse')
        self._click(By.XPATH, self.loginn_button_inc)
        assert (self.alert_get(), "Please fill out Username and Password.")
        self.alert_ok()
        self._click(By.XPATH, self.loginn_button_close)
        time.sleep(2)

    ## checking product add to cart 6)
    def execute_prodact_addingTo_cart(self):
        pytest.skip('skipping test..later i will check it')
        # self._click(By.XPATH, self.home)
        # self._click(By.XPATH, self.phones)
        # self._click(By.XPATH, self.sumsung_item)
        # self._click(By.XPATH, self.sumsung_name)
        # assert self.message(self.sumsung_name) == "Samsung galaxy s6"
        # self._click(By.XPATH, self.sumsung_add)
        # self.alert_ok()  # OK on alert box
        # self._click(By.XPATH, self.view_cart)
        # self._click(By.XPATH, self.place_order)
        # time.sleep(1)
        # self._write(By.XPATH, self.user_name, 'wasse')
        # self._write(By.XPATH, self.user_country, 'israel')
        # self._write(By.XPATH, self.user_city, 'beersheva')
        # self._write(By.XPATH, self.credit_card, '12345')
        # self._write(By.XPATH, self.month, '7')
        # self._write(By.XPATH, self.year, '2023')
        # self._click(By.XPATH, self.purchase)
        # time.sleep(2)
        # assert self.message(self.order_correct) == "Thank you for your purchase!"
        # self._click(By.XPATH, self.order_product_ok)
        # time.sleep(2)


    def execute_order_incorect_ccard(self):      ## cheking order 7
        pytest.skip('skipping test..later i will check it')
        # self._click(By.XPATH, self.incorrect_credit_hom)
        # self._click(By.XPATH, self.incorrect_credit_product)
        # assert self.message(self.incorrect_credit_place_name2) == "Sony xperia z5"
        # self._click(By.XPATH, self.incorrect_credit_add)
        # self.alert_ok()  # OK on alert box
        # self._click(By.XPATH, self.incorrect_credit_view_cart)
        # self._click(By.XPATH, self.incorrect_credit_place_order)
        # time.sleep(1)
        # self._write(By.XPATH, self.incorrect_credit_name, 'wasse')
        # self._write(By.XPATH, self.incorrect_credit_country, 'israel')
        # self._write(By.XPATH, self.incorrect_credit_city, 'telavive')
        # self._write(By.XPATH, self.incorrect_credit_month, '7')
        # self._write(By.XPATH, self.incorrect_credit_year, '2023')
        # self._click(By.XPATH, self.incorrect_credit_purchase)
        # self.alert_ok()  # OK on alert box
        # #self._click(By.XPATH, self.incorrect_credit_close)
        # time.sleep(2)


    def execute_orderWithout_country(self):   # cheking order without country 8
        pytest.skip('skipping test..later i will check it')
        # self._click(By.XPATH, self.orderWithout_country_home)
        # self._click(By.XPATH, self.orderWithout_country_product)
        # self._click(By.XPATH, self.orderWithout_country_name)
        # self._click(By.XPATH, self.orderWithout_country_add)
        # self.alert_ok()
        # self._click(By.XPATH, self.orderWithout_country_view_cart)
        # time.sleep(1)
        # self._click(By.XPATH, self.orderWithout_country_place_order)
        # time.sleep(1)
        # self._write(By.XPATH, self.orderWithout_country_name_cos, 'adis')
        # self._write(By.XPATH, self.orderWithout_country_city, 'jerusalem')
        # self._write(By.XPATH, self.orderWithout_country_card, '12355')
        # self._write(By.XPATH, self.orderWithout_country_month, '2')
        # self._write(By.XPATH, self.orderWithout_country_year, '2014')
        # self._click(By.XPATH, self.orderWithout_country_purchase)
        # time.sleep(3)
        # # self._click(By.XPATH, self.orderWithout_country_ok)
        # test_failed = self.message(self.order_correct) != "Thank you for your purchase!"
        # if not test_failed:
        #     pytest.fail("This should fail and not show 'Thank you for your purchase!'", pytrace=False)
        # self._click(By.XPATH, self.orderWith_cCardLetter_ok)
        # self.alert_ok()
        # time.sleep(2)




    def execute_next(self):           ## cheking nex button 9
        self._click(By.XPATH, self.home)
        previous_name = self.message(self.next_item_name)  # page 1
        self._click(By.XPATH, self.next_next_page)
        time.sleep(1)
        current_name = self.message(self.next_item_name)  # page 2
        assert (current_name != previous_name)
        time.sleep(1)
        # click next
        # read id 1 of page 2
        # check name are not equal


    def execute_delete(self):          ## checking delet from cart 10
        self._click(By.XPATH, self.home)
        self._click(By.XPATH, self.cart_select)
        self._click(By.XPATH, self.cart_add)
        self.alert_ok()
        self._click(By.XPATH, self.cart_add)
        self.alert_ok()
        self._click(By.XPATH, self.cart_add)
        self.alert_ok()
        self._click(By.XPATH, self.cart_view)
        time.sleep(1)
        self._click(By.XPATH, self.cart_delete)
        # self._click(By.XPATH, self.cart_home)
        self.tea_dowm()
        time.sleep(1)



    def execute_chekinbuttons(self):      ## cheking forward buttons11
        pytest.skip('skipping test..later i will check it')
        # self._click(By.XPATH, self.cheking_button_hom)
        # self._click(By.XPATH, self.cheking_backward_button)
        # img1 = self.get_image_path(self.cheking_image_class_name)
        # self._click(By.XPATH, self.cheking_backward_button)
        # img2 = self.get_image_path(self.cheking_image_class_name)
        # equal = img1 == img2
        # self._click(By.XPATH, self.cheking_forward_button)
        # time.sleep(2)



    def execute_orderWith_cCardLetter(self):      ##orderWith_cCardLetter 12
        self._click(By.XPATH, self.orderWith_cCardLetter_home)
        self._click(By.XPATH, self.orderWith_cCardLetter_product)
        self._click(By.XPATH, self.orderWith_cCardLetter_name)
        self._click(By.XPATH, self.orderWith_cCardLetter_add)
        self.alert_ok()
        self._click(By.XPATH, self.orderWith_cCardLetter_view_cart)
        time.sleep(1)
        self._click(By.XPATH, self.orderWith_cCardLetter_place_order)
        time.sleep(1)
        self._write(By.XPATH, self.orderWith_cCardLetter_name_cos, 'adis')
        self._write(By.XPATH, self.orderWith_cCardLetter_country, 'jerusalem')
        self._write(By.XPATH, self.orderWith_cCardLetter_city, 'jerusalem')
        self._write(By.XPATH, self.orderWith_cCardLetter_card, '12355')
        self._write(By.XPATH, self.orderWith_cCardLetter_month, '2')
        self._write(By.XPATH, self.orderWith_cCardLetter_year, '2014')
        self._click(By.XPATH, self.orderWith_cCardLetter_purchase)
        time.sleep(1)
        test_failed = self.message(self.order_correct) != "Thank you for your purchase!"
        if not test_failed:
            pytest.fail("This should fail and not show 'Thank you for your purchase!'", pytrace=False)
        self._click(By.XPATH, self.orderWith_cCardLetter_ok)
        time.sleep(2)


    def execute_about_us(self):        ## cheking about us 13
        pytest.skip('skipping test..later i will check it')
        # self._click(By.XPATH, self.about_us_home)
        # self._click(By.XPATH, self.about_us_play)
        # self._click(By.XPATH, self.about_us_fulscreen)
        # self._click(By.XPATH, self.about_us_miniScreen)
        # self._click(By.XPATH, self.about_us_mute)
        # self._click(By.XPATH, self.about_us_pause)
        # self._click(By.XPATH, self.about_us_screenshut)
        # self._click(By.XPATH, self.about_us_close)
        # time.sleep(1)
        # self.tea_dowm()


    def execute_display(self):     ## display 14
        self._click(By.XPATH, self.display_home)
        self._click(By.XPATH, self.display_text)
        assert self.message(self.display_text) == "PRODUCT STORE"
        time.sleep(1)


    def execute_login_incName(self):    # login incorect without name 15
        self._click(By.XPATH, self.login_wName_home)
        self._click(By.XPATH, self.login_wName_login)
        time.sleep(1)
        self._write(By.XPATH, self.login_wName_psw, '123was')
        self._click(By.XPATH, self.login_wname_lgEnter)
        assert (self.alert_get(), "Please fill out Username and Password.")
        self.alert_ok()
        self._click(By.XPATH, self.login_wname_close)
        time.sleep(1)


    def execute_waCcount(self): ## login without account 16
        self._click(By.XPATH, self.login_waccount_home)
        self._click(By.XPATH, self.login_waccount_login)
        time.sleep(1)
        self._click(By.XPATH, self.login_waccount_lgEnter)
        assert (self.alert_get(), "Please fill out Username and Password.")
        self.alert_ok()
        self._click(By.XPATH, self.login_waccount_close)
        time.sleep(1)


    def execute_dButton(self):     ## check display button 17
        self._click(By.XPATH, self.disButton_home)
        self._click(By.XPATH, self.disButton_1)
        self._click(By.XPATH, self.disButton_2)
        self._click(By.XPATH, self.disButton_3)
        time.sleep(1)


    def execute_contactUs(self):    ## contactus 18
        self._click(By.XPATH, self.contactUs_home)
        self._click(By.XPATH, self.contactUs_cont)
        time.sleep(1)
        self._write(By.XPATH, self.contactUs_email, "adce@gmail.com")
        self._write(By.XPATH, self.contactUs_name, 'wass')
        self._write(By.XPATH, self.contactUs_message, 'hello i want to order products by special design')
        self._click(By.XPATH, self.contactUs_sendMessage)
        assert (self.alert_get(), "Thanks for the message!!")
        self.alert_ok()
        time.sleep(1)


    def execute_contactUs_noText(self): ## try to send message without text 19
        self._click(By.XPATH, self.contactUs_noText_home)
        self._click(By.XPATH, self.contactUs_noText_cont)
        time.sleep(1)
        self._write(By.XPATH, self.contactUs_noText_email, "adce@gmail.com")
        self._write(By.XPATH, self.contactUs_noText_name, 'wass')
        #self._write(By.XPATH, self.contactUs_noText_message, 'hello i want to order products by special design')
        self._click(By.XPATH, self.contactUs_noText_sendMessage)
        test_failed = self.alert_get() != "Thanks for the message!!"
        if not test_failed:
            pytest.fail("This should fail and not show 'Thanks for the message!!'", pytrace=False)
        time.sleep(2)


    def execute_contactUs_no_name(self):  ## try to send message without text 20
        self._click(By.XPATH, self.contactUs_nonam_home)
        self._click(By.XPATH, self.contactUs_nonam_cont)
        time.sleep(1)
        self._write(By.XPATH, self.contactUs_nonam_email, "adce@gmail.com")
        #self._write(By.XPATH, self.contactUs_nonam_name, 'wass')
        self._write(By.XPATH, self.contactUs_nonam_message, 'hello i want to order products by special design')
        self._click(By.XPATH, self.contactUs_nonam_sendMessage)
        test_failed = self.alert_get() != "Thanks for the message!!"
        if not test_failed:
            pytest.fail("This should fail and not show 'Thanks for the message!!'", pytrace=False)
        time.sleep(2)


    def execute_contactUs_no_email(self):  ## try to send message without text 21
        self._click(By.XPATH, self.contactUs_noemail_home)
        self._click(By.XPATH, self.contactUs_noemail_cont)
        time.sleep(1)
        #self._write(By.XPATH, self.contactUs_noemail_email, "adce@gmail.com")
        self._write(By.XPATH, self.contactUs_noemail_name, 'wass')
        self._write(By.XPATH, self.contactUs_noemail_message, 'hello i want to order products by special design')
        self._click(By.XPATH, self.contactUs_noemail_sendMessage)
        test_failed = self.alert_get() != "Thanks for the message!!"
        if not test_failed:
            pytest.fail("This should fail and not show 'Thanks for the message!!'", pytrace=False)
        time.sleep(2)


    def execute_contactUs_no_account(self):  ## try to send message without account 21
        self._click(By.XPATH, self.contactUs_noac_home)
        self._click(By.XPATH, self.contactUs_noac_cont)
        time.sleep(1)
        self._write(By.XPATH, self.contactUs_noac_message, 'hello i want to order products by special design')
        self._click(By.XPATH, self.contactUs_noac_sendMessage)
        test_failed = self.alert_get() != "Thanks for the message!!"
        if not test_failed:
            pytest.fail("This should fail and not show 'Thanks for the message!!'", pytrace=False)
        time.sleep(2)











