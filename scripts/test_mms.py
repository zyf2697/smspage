# 从appium库里面导入driver对象
from appium import webdriver
# 导入time
import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
import base
from appium.webdriver.common.touch_action import TouchAction
from page.mms_page import MmsPage


class TestMms:
    def setup(self):
        self.driver = init_driver(base.app_package, base.app_activity)
        self.mms_pages = MmsPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_mms(self):
        self.mms_pages.new_mms()
        self.mms_pages.receive()
        self.mms_pages.input_text()
        # self.mms_pages.last_one()
        self.mms_pages.delete()
        # self.mms_pages.accept_delete()
        # self.mms_pages.all_mms()

        # self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
        # input = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        # input.clear()
        # input.send_keys("17319260071")
        # send_list = ["123","2222","cccc"]
        # send_sms = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        # send_btn = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        # for i in send_list:
        #     send_sms.clear()
        #     send_sms.send_keys(i)
        #     send_btn.click()
        # cccc_ele = self.driver.find_element_by_xpath("//*[contains(@text,'cccc')]")
        # TouchAction(self.driver).long_press(cccc_ele).perform()
        # self.driver.find_element_by_xpath("//*[contains(@text,'删除')]").click()
        # self.driver.find_element_by_id("android:id/button1").click()
        # data_lists = self.driver.find_elements_by_id("com.android.mms:id/text_view")
        # if "cccc" in [i.text for i in data_lists]:
        #     print("删除失败")
        # else:
        #     print("删除成功")
