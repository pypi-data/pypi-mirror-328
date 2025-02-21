from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class GiftRecords:
    def __init__(self, config, web_driver):
        self.config = config
        "配置文件"
        self.driver = web_driver
        "WebDriver对象"
        self.prizes = []
        "记录所有奖品"
        self.record_path = config['record_path']
        "奖品记录保存路径"

    # 点击我的奖品按钮，弹出我的奖品弹窗
    def my_gifts_btn(self):
        try:
            my_gifts_btn = self.driver.find_element(By.XPATH, '//li[@class="go_area6 px_getbag"]')
            my_gifts_btn.click()
            print("点击我的奖品按钮")

            # 等待弹窗出现
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="popcont popcont1"]'))
            )
            print("我的获奖记录弹窗已出现")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"操作失败: {str(e)}")

    # 点击下一页按钮
    def next_page_btn(self):
        try:
            next_page_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@class="pagination"]/a[@class="next" and text()="下一页"]'))
            )
            next_page_btn.click()
            print("点击下一页按钮")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"无法点击下一页按钮: {str(e)}")

    # 解析奖品记录
    def records_gift_content(self):
        try:
            rows = self.driver.find_elements(By.XPATH, '//table[@id="baglist"]/tbody/tr')
            for row in rows:
                prize = {
                    '序号': row.find_element(By.XPATH, './td[1]').text,
                    '获得物品名称': row.find_element(By.XPATH, './td[2]').text,
                    '卡号': row.find_element(By.XPATH, './td[3]').text
                }
                self.prizes.append(prize)
        except NoSuchElementException as e:
            print(f"解析奖品记录失败: {str(e)}")

    def wait_for_color_change(self, locator, expected_color, timeout=3):
        """等待指定元素的颜色变为期望的颜色"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.find_element(*locator).value_of_css_property('color') == expected_color
            )
            print(f"颜色已变为: {expected_color}")
        except TimeoutException:
            print(f"在 {timeout} 秒内未检测到颜色变更为: {expected_color}")

    def save_records(self):
        """保存奖品记录到文件"""
        if self.prizes:
            print(f"所有奖品记录: {self.prizes}")
            try:
                # 使用配置文件中的具体文件名
                records_file_name = self.config.get('records_file_name', 'gift_records.txt')
                full_file_path = f"{self.record_path}{records_file_name}"

                with open(full_file_path, 'w', encoding='utf-8') as f:
                    for prize in self.prizes:
                        f.write(f"{prize['序号']}, {prize['获得物品名称']}, {prize['卡号']}\n")
                print("奖品记录已保存")
            except IOError as e:
                print(f"保存记录失败: {str(e)}")
        else:
            print("没有记录到任何奖品。")

    def record_all_gifts(self):
        """记录所有奖品"""
        self.my_gifts_btn()

        next_page_locator = (By.XPATH, '//a[@class="next"]')

        while True:
            self.records_gift_content()

            try:
                next_page_element = WebDriverWait(self.driver, 3).until(
                    EC.visibility_of_element_located(next_page_locator)
                )
                next_page_color = next_page_element.value_of_css_property('color')

                if next_page_color == 'rgb(255, 153, 51)':  # 假设的结束色
                    print("已达到最后一页，停止记录")
                    break

                self.next_page_btn()

            except TimeoutException:
                print("未能找到'下一页'按钮，停止记录")
                break

        self.save_records()


