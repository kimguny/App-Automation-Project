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

        driver = webdriver.Remote(f'http://{server_ip}:{server_port}/wd/hub', capabilityset)
        driver.implicitly_wait(10)
        self.driver = driver
        return driver

    # Capability Set 반환
    def get_default_capability(self, udid):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = '퀀텀2'
        desired_caps["udid"] = udid
        desired_caps["automationName"] = 'UiAutomator2'
        return desired_caps

    # ADB device lsit 생성
    def get_adb_devices(self):
        import subprocess
        cmd_get_version = 'adb devices'
        device_list = subprocess.check_output(cmd_get_version, shell=True)
        device_list = [x.split("\t")[0] for x in device_list.decode().split("\n") if("\t" in x)  ]
        print(device_list)
        return device_list

    # App 실행
    def start_app(self, app_packagename, app_activity):
        print("==============")
        print(f"[start_app] App실행 {app_packagename}, {app_activity}")
        self.driver.activate_app(app_packagename)
        self.driver.start_activity(app_packagename, app_activity)

    # App 종료
    def terminate_app(self, app_packagename):
        print("==============")
        print(f"[terminate_app] App종료 {app_packagename}")
        self.driver.terminate_app(app_packagename)

    # App 버전 추출
    def get_app_version(self, app_packagename):
        args = {"command": "dumpsys", "args": f"package {app_packagename} | grep versionName"}
        version = self.driver.execute_script("mobile: shell", args)
        version = version.split("=")[1].replace("\r\n","")
        print(f'App버전 : {app_packagename}, {version}' )
        return version

    # 단말 모델병 추출
    def get_device_model(self):
        model = self.driver.session["deviceModel"]
        print(f'단말 모델명 : {model}')
        return model

    # 뒤로가기 버튼
    def back_button(self):
        print("==============")
        print(f"[back_button] 뒤로가기")
        self.driver.back()

    # 대기후 클릭
    def wait_and_click(self, desc="",path="", by=By.XPATH, timeout=5 ):
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
    def wait(self, desc="", path="", by=By.XPATH , timeout=5 ):
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
    def wati_and_set_text(self, desc="", text="Test", path="", by=By.XPATH , timeout=5 ):
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