from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.base_action import BaseAction1

import base


class MmsPage(BaseAction1):
    # new_mmsid = By.ID,"com.android.mms:id/action_compose_new"
    # receiveid = By.ID,"com.android.mms:id/recipients_editor"
    # input_text_smsid = By.ID,"com.android.mms:id/embedded_text_editor"
    # input_text_btnid = By.ID,"com.android.mms:id/send_button_sms"
    # last_onexpath = By.XPATH,"//*[contains(@text,'cccc')]"
    # deletexpath = By.XPATH,"//*[contains(@text,'删除')]"
    # accept_deleteid = By.ID,"android:id/button1"
    # all_mmsid = By.ID,"com.android.mms:id/text_view"

    def __init__(self, driver):
        self.driver = driver
        BaseAction1.__init__(self, driver)

    def new_mms(self):
        self.click_element(base.new_mmsid)
        # self.find_element(self.new_mmsid).click()
        # self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()

    def receive(self):
        # input = self.find_element(base.receiveid)
        # input.clear()
        # input = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        self.input_element_content(base.receiveid,"17319260071")

    def input_text(self):
        send_list = ["123", "2222", "cccc"]
        # send_sms = self.find_element(base.input_text_smsid)
        # send_sms = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        # send_btn = self.find_element(base.input_text_btnid)
        # send_btn = self.driver.find_element_by_id("com.android.mms:id/send_button_sms")
        for i in send_list:
            self.input_element_content(base.input_text_smsid, i)
            self.click_element(base.input_text_btnid)

    # def last_one(self):
    #     cccc_ele = self.find_element(base.last_onexpath)
    #     # cccc_ele = self.driver.find_element_by_xpath("//*[contains(@text,'cccc')]")
    #     TouchAction(self.driver).long_press(cccc_ele).perform()
    #
    # def delete(self):
    #     self.click_element(base.deletexpath)
    #     # self.driver.find_element_by_xpath("//*[contains(@text,'删除')]").click()
    #
    # def accept_delete(self):
    #     self.click_element(base.accept_deleteid)
    #     # self.driver.find_element_by_id("android:id/button1").click()
    #
    # def all_mms(self):
    #     data_lists = self.find_elements(base.all_mmsid)
    #     # data_lists = self.driver.find_elements_by_id("com.android.mms:id/text_view")
    #     if "cccc" in [i.text for i in data_lists]:
    #         print("删除失败")
    #     else:
    #         print("删除成功")

    def delete(self):
        cccc_ele = self.find_element(base.last_onexpath)
        # cccc_ele = self.driver.find_element_by_xpath("//*[contains(@text,'cccc')]")
        TouchAction(self.driver).long_press(cccc_ele).perform()

        self.click_element(base.deletexpath)
        # self.driver.find_element_by_xpath("//*[contains(@text,'删除')]").click()

        self.click_element(base.accept_deleteid)
        # self.driver.find_element_by_id("android:id/button1").click()

        data_lists = self.find_elements(base.all_mmsid)
        # data_lists = self.driver.find_elements_by_id("com.android.mms:id/text_view")
        if "cccc" in [i.text for i in data_lists]:
            print("\n删除失败")
        else:
            print("\n删除成功")

