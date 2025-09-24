"""
页面元素
"""
from selenium.webdriver.common.by import By

login_link = By.ID,"link"
username=By.ID,"username"
pwd=By.ID,"password"
verify_code=By.ID,"verify_code"
login_btn=By.CSS_SELECTOR,".login_btn"
error_info=By.CSS_SELECTOR,"#error_info"
