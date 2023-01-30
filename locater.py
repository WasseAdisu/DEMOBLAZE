
class Locator:
    # sign up 1
    home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    url = "https://www.demoblaze.com/index.html"
    sign_up = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]"
    signUp_name = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    signUp_password = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    sign_up_button = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/button[2]"
    sign_up_close = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/button[1]"

### sign up without name and password 2
    signUp_without_nameAndPw_home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    signUp_without_nameAndPw = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]"
    signUp_without_nameAndPw_button = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/button[2]"
    signUp_without_nameAndPw_close = "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[1]"

##sign_up_withoutPassword 3
    sign_up_withoutPassword_home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    sign_up_withoutPassword = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]"
    sign_up_withoutPassword_name = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    sign_up_withoutPassword_button = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/button[2]"
    sign_up_withoutPassword_close = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/button[1]"

#login correctly 4
    loginn = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]"
    loginn_name = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    loginn_password = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    loginn_button = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"

    # login incorrect password 5
    loginn_incorrect_home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    loginn_incorrect = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]"
    loginn_name_correct = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    #loginn_password_incorrect = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    loginn_button_inc = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    loginn_button_close = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]"

#order product 6
    phones = "//a[contains(text(),'Phones')]"
    sumsung_item = "//body/div[@id='contcont']/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/img[1]"
    sumsung_name = "/html[1]/body[1]/div[5]/div[1]/div[2]/h2[1]"
    sumsung_add = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]"
    view_cart = "//a[@id='cartur']"
    place_order = "/html[1]/body[1]/div[6]/div[1]/div[2]/button[1]"
    user_name = "//input[@id='name']"
    user_country = "//input[@id='country']"
    user_city = "//input[@id='city']"
    credit_card = "//input[@id='card']"
    month = "//input[@id='month']"
    year = "//input[@id='year']"
    purchase = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    order_correct = "//h2[contains(text(),'Thank you for your purchase!')]"
    order_product_ok = "/html[1]/body[1]/div[10]/div[7]/div[1]/button[1]"


    #order incorrect credit card 7
    incorrect_credit_hom = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    incorrect_credit_product = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[6]/div[1]/a[1]/img[1]"
    incorrect_credit_place_name2 = "/html[1]/body[1]/div[5]/div[1]/div[2]/h2[1]"
    incorrect_credit_add = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]"
    incorrect_credit_view_cart = "/html[1]/body[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]"
    incorrect_credit_place_order = "/html[1]/body[1]/div[6]/div[1]/div[2]/button[1]"
    incorrect_credit_name = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    incorrect_credit_country = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    incorrect_credit_city = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]"
    incorrect_credit_month = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[5]/input[1]"
    incorrect_credit_year = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[6]/input[1]"
    incorrect_credit_purchase= "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    incorrect_credit_close = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]"

    #cheking order without country 8
    orderWithout_country_home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    orderWithout_country_product = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[3]/div[1]/a[1]/img[1]"
    orderWithout_country_name = "/html[1]/body[1]/div[5]/div[1]/div[2]/h2[1]"
    orderWithout_country_add = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]"
    orderWithout_country_view_cart = "/html[1]/body[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]"
    orderWithout_country_place_order = "/html[1]/body[1]/div[6]/div[1]/div[2]/button[1]"
    orderWithout_country_name_cos = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    orderWithout_country_city = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]"
    orderWithout_country_card = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[4]/input[1]"
    orderWithout_country_month = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[5]/input[1]"
    orderWithout_country_year = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[6]/input[1]"
    orderWithout_country_purchase = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    orderWithout_country_ok = "/html[1]/body[1]/div[10]/div[7]/div[1]/button[1]"


# checking Nextg button 9
    next_item_name = '//*[@id="tbodyid"]/div[1]/div/div/h4/a'
    next_next_page = "/html/body/div[5]/div/div[2]/form/ul/li[2]/button"

    # delet from cart 10
    cart_delete = f"//*[@id='tbodyid']/tr[1]/td[4]/a"
    cart_select = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/img[1]"
    cart_add = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]"
    cart_view = view_cart
    cart_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"

    # cheking order credit with card letters 11
    orderWith_cCardLetter_home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    orderWith_cCardLetter_product = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[3]/div[1]/a[1]/img[1]"
    orderWith_cCardLetter_name = "/html[1]/body[1]/div[5]/div[1]/div[2]/h2[1]"
    orderWith_cCardLetter_add = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]"
    orderWith_cCardLetter_view_cart = "/html[1]/body[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]"
    orderWith_cCardLetter_place_order = "/html[1]/body[1]/div[6]/div[1]/div[2]/button[1]"
    orderWith_cCardLetter_name_cos = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    orderWith_cCardLetter_country = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    orderWith_cCardLetter_city = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]"
    orderWith_cCardLetter_card = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[4]/input[1]"
    orderWith_cCardLetter_month = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[5]/input[1]"
    orderWith_cCardLetter_year = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[6]/input[1]"
    orderWith_cCardLetter_purchase = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    orderWith_cCardLetter_ok = "/html[1]/body[1]/div[10]/div[7]/div[1]/button[1]"


    ## cheking forward buttons 12
    cheking_button_hom = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    cheking_forward_button = "/html[1]/body[1]/nav[1]/div[2]/div[1]/a[2]/span[1]"
    cheking_backward_button = "/html[1]/body[1]/nav[1]/div[2]/div[1]/a[1]/span[1]"
    cheking_image_class_name = "carousel-item.active"
    # cheking_image_path = '/html/body/nav/div[2]/div/div/div[3]/img'

    ### cheking about us 13
    about_us_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]"
    about_us_play = "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/button[1]/span[1]"
    about_us_fulscreen = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/button[4]/span[1]"
    about_us_miniScreen = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/button[4]/span[1]"
    about_us_mute = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/button[1]/span[1]"
    about_us_pause = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/button[1]/span[1]"
    about_us_screenshut = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/button[3]/span[1]"
    about_us_close = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[3]/button[1]"

    ## is display 14
    display_home = "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]"
    display_text = "/html[1]/body[1]/nav[1]/a[1]"

    ## login without name 15
    login_wName_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    login_wName_login = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]"
    login_wName_psw = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    login_wname_lgEnter = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    login_wname_close = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]"

    ## login without account 16
    login_waccount_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    login_waccount_login = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]"
    login_waccount_lgEnter = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    login_waccount_close = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]"

    ## check display button 17
    disButton_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    disButton_1 =  "/html[1]/body[1]/nav[1]/div[2]/div[1]/ol[1]/li[1]"
    disButton_2 = "/html[1]/body[1]/nav[1]/div[2]/div[1]/ol[1]/li[2]"
    disButton_3 = "/html[1]/body[1]/nav[1]/div[2]/div[1]/ol[1]/li[3]"

    ## contact us 18
    contactUs_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    contactUs_cont = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
    contactUs_email = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    contactUs_name = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    contactUs_message = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/textarea[1]"
    contactUs_sendMessage = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/button[2]"

    ## contact us without text
    contactUs_noText_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    contactUs_noText_cont = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
    contactUs_noText_email = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    contactUs_noText_name = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    ##contactUs_noText_message = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/textarea[1]"
    contactUs_noText_sendMessage = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/button[2]"

    ## contact us without text
    contactUs_nonam_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    contactUs_nonam_cont = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
    contactUs_nonam_email = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    #contactUs_nonam_name = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    contactUs_nonam_message = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/textarea[1]"
    contactUs_nonam_sendMessage = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/button[2]"

    ## contact us without email
    contactUs_noemail_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    contactUs_noemail_cont = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
    #contactUs_nonam_email = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    contactUs_noemail_name = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"
    contactUs_noemail_message = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/textarea[1]"
    contactUs_noemail_sendMessage = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/button[2]"

    ## contact us without email
    contactUs_noac_home = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]"
    contactUs_noac_cont = "/html[1]/body[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
    contactUs_noac_message = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/textarea[1]"
    contactUs_noac_sendMessage = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/button[2]"




