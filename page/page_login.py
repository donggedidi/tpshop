from base.base import Base
import page

class PageLogin(Base):
    def page_click_login_link(self):
        self.base_click(page.login_link)

    def page_input_username(self,username):
        self.base_input(page.username,username)

    def page_input_pwd(self,password):
        self.base_input(page.password,password)

    def page_input_verify_code(self,verify_code):
        self.base_input(page.verify_code,verify_code)

    def page_click_submit_btn(self):
        self.base_click(page.submit_btn)

    def page_click_logout(self):
        self.base_click(page.logout_link)

    def page_get_error_text(self):
        return self.base_get_text(page.error_text)

    def page_click_error_btn(self):
        self.base_click(page.error_btn)

    def page_get_screenshot(self):
        self.base_get_screenshot()


    def page_if_login_success(self):
        return self.base_if_exist(page.logout_link)


    def page_login(self,username,password,verify_code):
        self.page_input_username(username)
        self.page_input_pwd(password)
        self.page_input_verify_code(verify_code)
        self.page_click_submit_btn()


