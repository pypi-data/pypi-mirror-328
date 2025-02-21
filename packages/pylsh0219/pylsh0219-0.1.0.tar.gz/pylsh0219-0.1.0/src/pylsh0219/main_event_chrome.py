import os
import time
import json
import shutil
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from select_games import SelectGames
from gift_records import GiftRecords


class WebGameAutomation:
    def __init__(self, config):
        self.config = config

        # 在初始化浏览器前清空目录
        profile_path = os.path.normpath(config['chrome_profile_path'])
        if os.path.exists(profile_path):
            shutil.rmtree(profile_path)
        os.makedirs(profile_path, exist_ok=True)

        "配置文件"
        self.service = Service(config['webdriver_path'])
        "设置 webdriver 路径"
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"--user-data-dir={config['chrome_profile_path']}")
        chrome_options.add_argument("--profile-directory=Default")
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        "创建 webdriver 对象"
        self.driver.implicitly_wait(3)
        "设置隐式等待时间"

        self.select_games = SelectGames(config, self.driver)
        "游戏选择模块"
        print("WebDriver 已启动")
        self.gift_records = GiftRecords(config, self.driver)
        "礼包记录模块"
        print("礼包记录模块已初始化")

    # 从指定路径下导入json格式的cookie
    def load_cookies(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
            for cookie in data['cookies']:
                cookie_dict = {
                    'domain': cookie['domain'],
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'path': cookie['path'],
                    'expires': cookie['expirationDate'] if 'expirationDate' in cookie else None,
                    'secure': cookie['secure'],
                    'httpOnly': cookie['httpOnly'],
                    'sameSite': cookie['sameSite'] if 'sameSite' in cookie else 'Lax'  # 默认 SameSite 策略
                }
                # 如果 sameSite 的值不在允许的范围内，设置为默认值
                if cookie_dict['sameSite'] not in ["Strict", "Lax", "None"]:
                    cookie_dict['sameSite'] = 'Lax'

                try:
                    self.driver.add_cookie(cookie_dict)
                    print(f"已添加 cookie: {cookie_dict['name']}")
                except Exception as e:
                    print(f"添加 cookie {cookie_dict['name']} 时出错: {e}")

    # 打开指定页面并最大化窗口
    def open_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    # 检查并点击活动已结束消息框中的确定按钮（活动已结束状态）
    def check_and_click_message_box(self):
        try:
            message_box_link = self.driver.find_element(By.XPATH, '//*[@id="_message_box_10002"]/div[1]/div/div/a')
            message_box_link.click()
            print("点击了消息框中的链接")
        except Exception as e:
            print("未找到消息框链接，可能未出现:", e)

    def run(self, url):
        # 清除所有当前的 cookies
        self.driver.delete_all_cookies()
        print("已清除所有 cookies")

        # 加载 cookies
        self.load_cookies(self.config['cookie_file_path'])

        # 刷新页面以应用 cookies
        self.driver.refresh()
        time.sleep(2)

        # 检查并点击消息框中的链接（活动已结束状态）
        self.check_and_click_message_box()

        # 获取指定页面html
        response = requests.get(url)
        response.raise_for_status()
        html = etree.HTML(response.text)

        # 找到目标元素并滚动至该元素至屏幕中间
        divs = html.xpath('//div[@class="sd sd2"]')

        if divs:
            element_xpath = divs[0].getroottree().getpath(divs[0])
            print("找到目标元素，准备滚动至:", element_xpath)
            self.driver.execute_script(f"document.evaluate('{element_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView({{block: 'center'}});")
            print("页面已滚动至指定标签")
            time.sleep(1)
        else:
            print("未找到指定标签")

    def click_bind_game_btn(self):
        bind_game_btn = self.driver.find_element(By.XPATH, '//li[@class="toBind_btn go_area3"]')
        bind_game_btn.click()

    def main(self):
        with open("./config.json", "r", encoding="utf-8") as config_file:
            config = json.load(config_file)

        # 打开活动页面
        self.open_page(config['event_url'])
        self.run(config['event_url'])
        time.sleep(1)

        # 对所有游戏循环：绑定游戏、选择游戏、礼包截图、领取礼包1
        self.select_games.click_all_games()
        self.gift_records.record_all_gifts()

        # 关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    with open("./config.json", "r", encoding="utf-8") as config_file:
        config = json.load(config_file)
    automation = WebGameAutomation(config)  # 直接传递加载的 config.json
    automation.main()
