import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetGiftButton:
    def __init__(self, config, web_driver):
        self.config = config
        "配置文件"
        self.driver = web_driver
        "浏览器驱动"

    def click_gift_1(self):
        try:
            print("正在等待 '礼包1' 链接出现...")

            # 等待< div >的出现
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='sd sd1']"))
            )

            # 等待并获取“礼包1”的链接
            gift_link = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='sd sd1']//a[@class='icons  px_getcardsp_gft' and @data-name='梦回江湖']")
                )
            )

            if gift_link:
                print("成功找到礼包1按钮。")

                # 确保链接可点击
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(gift_link)
                )

                # 点击链接
                gift_link.click()
                print("成功点击‘礼包1’链接。")
            else:
                print("未找到礼包1按钮。")
        except Exception as e:
            print(f"查找或点击礼包链接时出错: {e}")

    def handle_confirmation(self):
        try:
            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'shinfo shinfo_other')]//a[contains(@class, 'addBt addBt1 confirm') and text()='确定']"))
            )
            if confirm_button:
                print("确认按钮存在，点击确认")
                time.sleep(2)
                confirm_button.click()
        except Exception as e:
            print("未找到确认按钮或点击失败:", e)

    def handle_inactive(self):
        try:
            inactive_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'addBt addBt1 cancel') and text()='确定']"))
            )
            if inactive_button:
                print("活动未开启，点击确定")
                inactive_button.click()
        except Exception as e:
            print("未找到活动未开启按钮或点击失败:", e)

    def close_congratulation_window(self):
        try:
            print("正在等待弹窗出现...")

            # 等待包含特定类和标题的 div 出现
            popup_div = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'lottery_pubpop')]//h3[text()='恭喜您']")
                )
            )

            # 确保找到了弹窗
            if popup_div:
                print("弹窗标题 '恭喜您' 出现，准备点击关闭按钮...")
                time.sleep(2)  # 等待一秒，等待弹窗完全加载

                # 在弹窗内部查找关闭按钮并点击
                close_button = self.driver.find_element(By.XPATH,
                                                        "//div[contains(@class, 'lottery_pubpop')]//a[contains(@class, 'close1 cancel')]")
                close_button.click()  # 点击关闭按钮
                print("成功点击关闭按钮")
        except Exception as e:
            print(f"查找或点击关闭按钮时出错: {e}")