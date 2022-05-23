from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import traceback


class AppiumUtil():
    driver = None

    # Appium 서버 연결
    def get_driver(self, capabilityset, server_ip="localhost", server_port="4723"):

        driver = webdriver.Remote(
            f'http://{server_ip}:{server_port}/wd/hub', capabilityset)
        driver.implicitly_wait(10)
        self.driver = driver
        return driver

    # Capability Set 반환
    def get_default_capability(self, udid):
        capabilityset = {
            "platformName": "iOS",
            "appium:platformVersion": "15.2",
            "appium:deviceName": "iPhone",
            "appium:app": "com.jawebs.baedal",
            "appium:automationName": "XCUITest",
            "appium:noReset": "true",
            "appium:newCommandTimeout": "7200",
            "appium:udid": "00008030-000531810E88802E"
        }
        return capabilityset

    # App 실행

    def start_app(self, app_packagename):
        print("==============")
        print(f"[start_app] App실행 {app_packagename}")
        self.driver.activate_app(app_packagename)

    # App 종료
    def terminate_app(self, app_packagename):
        print("==============")
        print(f"[terminate_app] App종료 {app_packagename}")
        self.driver.terminate_app(app_packagename)

    # 대기후 클릭
    def wait_and_click(self, desc="", path="", by=By.XPATH, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        print("==============")
        print(f"[wait_and_click] {desc}, {by}")

        start_time = time.time()

        try:
            el1 = wait.until(EC.element_to_be_clickable((by, path)))
            print(el1)
            el1.click()
        except Exception as e:
            print(f"--error : {desc}------------")
            traceback.print_exc()
            print("--------------")
            return -1

        elapsed_time = time.time() - start_time
        print(f"desc:{desc}, elapsed_time:{elapsed_time}")
        return elapsed_time

    # 항목 나타날때 까지 대기
    def wait(self, desc="", path="", by=By.XPATH, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        print("==============")
        print(f"[wait] {desc}, {by}")

        start_time = time.time()

        try:
            el1 = wait.until(EC.element_to_be_clickable((by, path)))
        except Exception as e:
            print(f"--error : {desc}------------")
            traceback.print_exc()
            print("--------------")
            return -1

        elapsed_time = time.time() - start_time
        print(f"desc:{desc}, elapsed_time:{elapsed_time}")
        return elapsed_time

    # 대기후 Text 넣기
    def wati_and_set_text(self, desc="", text="Test", path="", by=By.XPATH, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        print("==============")
        print(f"[wati_and_set_text] {desc}, {by}, {text}")

        start_time = time.time()

        try:
            el1 = wait.until(EC.element_to_be_clickable((by, path)))
        except Exception as e:
            print(f"--error : {desc}------------")
            traceback.print_exc()
            print("--------------")
            return -1

        el1.set_value(text)
        elapsed_time = time.time() - start_time
        print(f"desc:{desc}, elapsed_time:{elapsed_time}")
        return elapsed_time
