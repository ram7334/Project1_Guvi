# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class Suman_Data:
    username = "Admin"
    password = "admin123"
    invalid_password="invalid password"
    new_employee_first_name="ram"
    new_employee_last_name="kumar"
    new_employee_id="0123"
    other_id="2598"
    driving_licence_no="965874"


# Python Class for Selenium Selectors
class Suman_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    pim_xpath='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_xpath='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
    input_box_first_name="firstName"
    input_box_last_name="lastName"
    employee_id_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    save_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    otherid_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    smoker_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span'
    drivinglicense_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    new_save_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    edit_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]'
    employee_list_xpath='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'
    delete_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button'
    conf_delete_xpath='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    select_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/div/div/label/span/i'
