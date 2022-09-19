from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_FIELD = (By.ID, 'id_username')
    PASSWORD_FIELD = By.XPATH, '//*[@id="id_password"]'
    SUBMIT_BUTTON = By.XPATH, '//*[@id="login-form"]/div[3]/input'
    SUBMIT_RESULT = By.XPATH, '//*[@id="site-name"]/a'


class AdminPage:
    PAGE_HEADER = By.XPATH, '//*[@id="site-name"]/a'


class AddUsers:
    BUTTON_ADD_USERS = By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a'
    ADD_USERNAME = By.XPATH, '//*[@id="id_username"]'
    ADD_PASSWORD = By.XPATH, '//*[@id="id_password1"]'
    ADD_PASSWORD_CONFIRM = By.XPATH, '//*[@id="id_password2"]'
    BUTTON_SAVE = By.XPATH, '//*[@id="user_form"]/div/div/input[1]'
    BUTTON_SAVE_AND_CONTINUE = By.XPATH, '//*[@id="user_form"]/div/div/input[3]'
    BUTTON_SAVE_AND_ANOTHER = By.XPATH, '//*[@id="user_form"]/div/div/input[2]'
    ADDED_SUCCESSFULLY = By.XPATH, '//*[@id="main"]/div/ul/li'


class DeleteUser:
    BUTTON_PAGE_USERS = By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    SEARCH_WINDOW_USERS = By.XPATH, '//*[@id="searchbar"]'
    BUTTON_SEARCH = By.XPATH, '//*[@id="changelist-search"]/div/input[2]'
    CHOOSE_USERNAME = By.XPATH, '//*[@id="action-toggle"]'
    CHOOSE_ACTION = By.XPATH, '//*[@id="changelist-form"]/div[1]/label/select'
    CHOOSE_ACTION_DELETE = By.XPATH, '//*[@id="changelist-form"]/div[1]/label/select/option[2]'
    BUTTON_GO = By.XPATH, '//*[@id="changelist-form"]/div[1]/button'
    BUTTON_YES_IM_SURE = By.XPATH, '//*[@id="content"]/form/div/input[4]'
    RESULT_TEXT = By.XPATH, '//*[@id="main"]/div/ul/li'


class FindUser:
    BUTTON_USERS = By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    SEARCH_WINDOW_USERS = By.XPATH, '//*[@id="searchbar"]'
    BUTTON_SEARCH = By.XPATH, '//*[@id="changelist-search"]/div/input[2]'
    RESULT_FIND_USER = By.XPATH, '//*[@id="result_list"]/tbody/tr/th/a'

class UpdateUserData:
    BUTTON_USERS = By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    SEARCH_WINDOW_USERS = By.XPATH, '//*[@id="searchbar"]'
    BUTTON_SEARCH = By.XPATH, '//*[@id="changelist-search"]/div/input[2]'
    RESULT_FIND_USER = By.XPATH, '//*[@id="result_list"]/tbody/tr/th/a'
    #Personal info
    FIRST_NAME = By.XPATH, '//*[@id="id_first_name"]'
    FIRST_NAME_RESULT = By.XPATH, '//*[@id="id_first_name"]'
    LAST_NAME = By.XPATH, '//*[@id="id_last_name"]'
    EMAIL_ADDRESS = By.XPATH, '//*[@id="id_email"]'
    #Permissions
    ACTIVE = By.XPATH, '//*[@id="id_is_active"]'
    STAFF_STATUS = By.XPATH, '//*[@id="id_is_staff"]'
    SUPERUSER_STATUS = By.XPATH, '//*[@id="id_is_superuser"]'

    #Button SAVE
    SAVE = By.XPATH, '//*[@id="user_form"]/div/div/input[3]'
    SAVE_AND_CONTINUE_EDITING = By.XPATH, '//*[@id="user_form"]/div/div/input[3]'
    SAVE_AND_ADD_ANOTHER = By.XPATH, '//*[@id="user_form"]/div/div/input[2]'



