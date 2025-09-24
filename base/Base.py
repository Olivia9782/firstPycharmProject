import time

from selenium.webdriver.support.wait import WebDriverWait

class Base:
     def __init__(self,driver):
         # 获取driver
         self.driver = driver
         # self.driver = webdriver.Chrome()
         # #最大化窗口
         # self.driver.maximize_window()
         #
         # self.driver.get("http://www.baidu.com")

     def base_get_element(self,loc,timeout=30,poll=0.5):
         return WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x:x.find_element(*loc))

     def base_click(self,loc):
         self.base_get_element(loc).click()

     def base_get_img(self):
         self.driver.get_screenshot_as_file("../image/{}".format(time.strftime("%Y_%m_%d %H:%M:%S")))


     def base_set_value(self,loc,value):
         el = self.base_get_element(loc)
         el.clear()
         el.send_keys(value)

     def base_get_info(self,loc):
         return self.base_get_element(loc).text

     def base_element_is_exists(self,loc):
         try:
             if self.base_get_element(loc):
                 return True
         except :
             return False

