import time
import pytest
from locators.elements_page_locators import LoginPage, AddUsers, DeleteUser, FindUser, UpdateUserData
from pages.base_page import BasePage
from resources.data_json_on_python import NAME_ADMIN, PASSWORD_ADMIN, USER_POPRAVKA, PASSWORD_POPRAVKA


class TextBoxPage(BasePage):

    def fill_all_fields(self):
        self.element_is_visible(LoginPage.LOGIN_FIELD).send_keys(NAME_ADMIN)
        self.element_is_visible(LoginPage.PASSWORD_FIELD).send_keys(PASSWORD_ADMIN)
        self.element_is_visible(LoginPage.SUBMIT_BUTTON).click()
        time.sleep(1)

    def check_field(self):
        result = self.element_is_visible(LoginPage.SUBMIT_RESULT).text
        return result

    def create_new_user(self):
        self.element_is_visible(AddUsers.BUTTON_ADD_USERS).click()
        self.element_is_visible(AddUsers.ADD_USERNAME).send_keys(USER_POPRAVKA)
        self.element_is_visible(AddUsers.ADD_PASSWORD).send_keys(PASSWORD_POPRAVKA)
        self.element_is_visible(AddUsers.ADD_PASSWORD_CONFIRM).send_keys(PASSWORD_POPRAVKA)
        self.element_is_visible(AddUsers.BUTTON_SAVE).click()
        time.sleep(1)

    def check_new_user(self):
        result = self.element_is_visible(AddUsers.ADDED_SUCCESSFULLY).text
        return result

    def find_new_user(self):
        self.element_is_visible(FindUser.BUTTON_USERS).click()
        self.element_is_visible(FindUser.SEARCH_WINDOW_USERS).send_keys(USER_POPRAVKA)
        self.element_is_visible(FindUser.BUTTON_SEARCH).click()
        time.sleep(1)

    def check_find_new_user(self):
        result = self.element_is_visible(FindUser.RESULT_FIND_USER).text
        return result

    def update_data_user(self):
        self.element_is_visible(UpdateUserData.BUTTON_USERS).click()
        self.element_is_visible(UpdateUserData.SEARCH_WINDOW_USERS).send_keys(USER_POPRAVKA)
        self.element_is_visible(UpdateUserData.BUTTON_SEARCH).click()
        self.element_is_visible(UpdateUserData.RESULT_FIND_USER).click()
        self.element_is_visible(UpdateUserData.FIRST_NAME).send_keys('test')
        self.element_is_visible(UpdateUserData.LAST_NAME).send_keys('test')
        self.element_is_visible(UpdateUserData.EMAIL_ADDRESS).send_keys('test@test.test')
        self.element_is_visible(UpdateUserData.STAFF_STATUS).click()
        self.element_is_visible(UpdateUserData.SAVE_AND_CONTINUE_EDITING).click()

    def check_update_data_first_name(self):
        result = self.element_is_visible(UpdateUserData.FIRST_NAME).get_attribute("value")
        return result

    def check_update_data_lastname(self):
        result = self.element_is_visible(UpdateUserData.LAST_NAME).get_attribute("value")
        return result

    def check_update_data_email(self):
        result = self.element_is_visible(UpdateUserData.EMAIL_ADDRESS).get_attribute("value")
        return result

    def check_update_data_first_staff_status(self):
        result = self.element_is_visible(UpdateUserData.STAFF_STATUS).get_attribute("checked")
        return result

    def delete_user(self):
        self.element_is_visible(DeleteUser.BUTTON_PAGE_USERS).click()
        self.element_is_visible(DeleteUser.SEARCH_WINDOW_USERS).send_keys(USER_POPRAVKA)
        self.element_is_visible(DeleteUser.BUTTON_SEARCH).click()
        self.element_is_visible(DeleteUser.CHOOSE_USERNAME).click()
        self.element_is_visible(DeleteUser.CHOOSE_ACTION).click()
        self.element_is_visible(DeleteUser.CHOOSE_ACTION_DELETE).click()
        self.element_is_visible(DeleteUser.BUTTON_GO).click()
        self.element_is_visible(DeleteUser.BUTTON_YES_IM_SURE).click()
        time.sleep(2)

    def check_delete_user(self):
        result = self.element_is_visible(DeleteUser.RESULT_TEXT).text
        return result
