from selenium.webdriver.common.by import By
"""
1.应用的包名,启动名
"""
app_package = "com.android.mms"
app_activity = ".ui.ConversationList"

"""
2.短信应用
"""
new_mmsid = By.ID, "com.android.mms:id/action_compose_new"
receiveid = By.ID, "com.android.mms:id/recipients_editor"
input_text_smsid = By.ID, "com.android.mms:id/embedded_text_editor"
input_text_btnid = By.ID, "com.android.mms:id/send_button_sms"
last_onexpath = By.XPATH, "//*[contains(@text,'cccc')]"
deletexpath = By.XPATH, "//*[contains(@text,'删除')]"
accept_deleteid = By.ID, "android:id/button1"
all_mmsid = By.ID, "com.android.mms:id/text_view"