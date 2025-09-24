import page
from base import Base


class PageLogin(Base):
    def page_login_link_click(self):
        self.base_click(page.login_link)

    def page_username_input(self,user):
        self.base_set_value(page.username,user)

    def page_password_input(self,pwd):
        self.base_set_value(page.pwd, pwd)

    def page_verify_code_input(self,vfcode):
        self.base_set_value(page.verify_code,vfcode)


    def page_login_btn_click(self):
        self.base_click(page.login_btn)

    def page_get_image(self):
        self.base_get_img()

    def page_get_error_info(self):
        return self.base_get_info(page.error_info)

    def page_login(self,user,pwd,vfcode):
        self.page_login_link_click()
        self.page_username_input(user)
        self.page_password_input(pwd)
        self.page_verify_code_input(vfcode)
        self.page_login_btn_click()

