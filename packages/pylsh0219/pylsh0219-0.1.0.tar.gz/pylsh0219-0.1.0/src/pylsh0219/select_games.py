import os
import time
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_gift_1 import GetGiftButton

class SelectGames:
    def __init__(self, config, web_driver):
        self.config = config
        "配置文件"
        self.driver = web_driver
        "浏览器驱动"
        self.gift_btn = GetGiftButton(config, web_driver)
        "礼物按钮"
        self.gift_numbers = config.get('gift_numbers', [1])
        "礼包数量"
        self.games = []
        "游戏列表"

    def click_bind_game_btn(self):
        """点击绑定游戏按钮"""
        try:
            bind_game_btn = self.driver.find_element(By.XPATH, '//li[@class="toBind_btn go_area3"]')
            bind_game_btn.click()
            print("点击 '绑定游戏'")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'pop-share'))
            )
        except Exception as e:
            print(f"点击绑定游戏按钮失败: {e}")

    def extract_game_list(self):
        """提取游戏列表"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'pop-share'))
            )
            games = self.driver.find_elements(By.CSS_SELECTOR, '.gameList .item')
            game_names = [(game.get_attribute('data-name'), game.get_attribute('data-url')) for game in games]
            for game_name, game_url in game_names:
                print(f"游戏名称: {game_name}, 游戏网址: {game_url}")
            return game_names
        except Exception as e:
            print(f"提取游戏列表失败: {e}")
            return []

    def take_screenshot(self, folder_name, game_name, html_name, current_date):
        """截图并保存到指定路径"""
        screenshot_file_name = f"{game_name}_{html_name}_{current_date}.png"
        screenshot_path = os.path.join(folder_name, screenshot_file_name)
        self.driver.save_screenshot(screenshot_path)
        print(f"截图已保存为: {screenshot_path}")

    def _receive_reward(self, reward_type, game_name, xpath, reward_name):
        """领取奖励（礼包或优惠券）的通用逻辑"""
        try:
            print(f"正在等待 '{reward_name}' 出现...")
            reward_link = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            print(f"{reward_link} 的 class 属性: {reward_link.get_attribute('class')}")

            if 'done' in reward_link.get_attribute('class'):
                print(f"‘{game_name}’{reward_name}已领取。")
            else:
                print(f"找到‘{game_name}’{reward_name}，准备领取。")
                reward_link.click()
                print(f"正在领取‘{reward_name}’。")
                self.gift_btn.handle_confirmation()
                time.sleep(1)
                self.gift_btn.close_congratulation_window()
                time.sleep(1)
        except TimeoutException:
            print(f"未检测到‘{game_name}’的{reward_name}。")
        except Exception as e:
            print(f"领取{reward_name}失败: {e}")

    def receive_gift(self, game_name):
        """根据配置领取多个礼包"""
        for gift_num in self.gift_numbers:
            xpath = f"//div[contains(@class, 'sd{gift_num}')]//a[@data-name='{game_name}']"
            self._receive_reward("礼包", game_name, xpath, f"礼包{gift_num}")
        # self._receive_reward("礼包", game_name, f"//div[@class='sd sd1']//a[@data-name='{game_name}']", "礼包1")

    def validate_gift_numbers(self):
        """验证礼包序号配置有效性"""
        valid_numbers = []
        for num in self.gift_numbers:
            try:
                n = int(num)
                if 1 <= n <= 3:  # 根据实际最大礼包数调整
                    valid_numbers.append(n)
                else:
                    print(f"忽略无效礼包序号: {num} (超出范围)")
            except ValueError:
                print(f"忽略无效礼包序号: {num} (非数字)")
        self.gift_numbers = valid_numbers or [1]  # 无效配置时默认领取第一个

    def receive_coupon(self, game_name):
        """领取优惠券"""
        self._receive_reward("优惠券", game_name, "//a[@data-name='满30减10优惠券']", "优惠券")

    def gift_or_coupon(self, game_name):
        """根据页面判断是领取礼包还是领取优惠券"""
        self.receive_coupon(game_name)
        self.receive_gift(game_name)

    def close_browser(self):
        """关闭浏览器"""
        self.driver.quit()
        print("关闭浏览器")

    def click_all_games(self):
        """点击所有游戏并领取礼包"""
        self.validate_gift_numbers()  # 在开始前验证配置有效性
        try:
            print(f"准备领取礼包: {self.gift_numbers}")
            print("开始点击所有游戏")
            game_items = self.driver.find_elements(By.CSS_SELECTOR, '.gameList .item')

            if not game_items:
                print("游戏列表为空，未找到任何游戏可供点击。")
                return

            current_url = self.driver.current_url
            html_name = current_url.split('/')[-1].split('.')[0]
            current_date = datetime.now().strftime("%m%d")
            folder_name = f"{html_name}_{current_date}"

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            for index, game in enumerate(game_items):
                try:
                    self.click_bind_game_btn()
                    self.driver.execute_script("arguments[0].scrollIntoView();", game)
                    time.sleep(1)

                    game.click()
                    game_name = game.get_attribute('data-name')
                    print(f"点击了第 {index + 1} 个游戏：{game_name}")

                    # 截图逻辑（如果需要,已作废）
                    # self.take_screenshot(folder_name, game_name, html_name, current_date)

                    # 领取礼包或优惠券
                    self.gift_or_coupon(game_name)

                except Exception as e:
                    print(f"点击第 {index + 1} 个游戏时发生错误: {e}")

        except Exception as e:
            print(f"点击所有游戏时发生错误: {e}")