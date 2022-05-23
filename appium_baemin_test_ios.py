# -*- coding: utf8 -*-
from time import sleep
from appium_util_ios import *

# =================================
# baemin app 정보
app_packagename = "com.jawebs.baedal"

# 단말 UDID
udid = "00008030-000531810E88802E"

# Appium 서버 정보
appium_server_ip="127.0.0.1"
appium_server_port="4723"

# =================================

au = AppiumUtil()

#Appium Driver
capability = au.get_default_capability(udid)
driver = au.get_driver(capabilityset=capability, server_ip=appium_server_ip, server_port=appium_server_port)

path = '쇼핑라이브'
au.wait(desc="App 실행시간(쇼핑라이브)", path=path, by=By.NAME, timeout=10)

path = '한 번에 한 집만 빠르게 배달해요!, 배민1'
au.wait_and_click(desc="배민 클릭", path=path, by=By.NAME, timeout=10)

path = "치킨"
au.wait_and_click(desc="치킨 클릭", path=path,  by=By.NAME, timeout=10)

path = "배달 빠른 순"
au.wait_and_click(desc="배달 빠른 순 클릭", path=path,  by=By.NAME, timeout=10)

path = "초기화"
au.wait_and_click(desc="초기화 클릭", path=path,  by=By.NAME, timeout=10)

#뒤로가기 버튼
path = "뒤로가기"
au.wait_and_click(desc="뒤로가기 클릭", path=path,  by=By.NAME, timeout=10)

path = '//XCUIElementTypeOther[@name="검색 하단탭, 총 5개중 1번째"]'
au.wait_and_click(desc="검색", path=path, by=By.XPATH, timeout=10)

path = '//XCUIElementTypeImage[@name="icon24Search"]'
au.wait_and_click(desc="검색", path=path, by=By.XPATH, timeout=10)

path = '//XCUIElementTypeApplication[@name="배달의민족"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField'
au.wati_and_set_text(desc="검색어 입력", text="이삭", path=path, by=By.XPATH, timeout=10)

path = '//XCUIElementTypeApplication[@name="배달의민족"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeOther'
au.wait_and_click(desc="이삭토스트 클릭", path=path, by=By.XPATH, timeout=10)

path = '//XCUIElementTypeApplication[@name="배달의민족"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'
au.wait_and_click(desc="맨 위에 항목 클릭", path=path,  by=By.XPATH, timeout=10)

time.sleep(2)

au.driver.swipe(132,1971, 27,528, 100) # 좌표 지정해서 스크롤

time.sleep(2)

path ='(//XCUIElementTypeButton[@name="커피"])[1]'
au.wait_and_click(desc="커피 클릭", path=path,  by=By.XPATH, timeout=10)

path = "H.아메리카노"
au.wait_and_click(desc="H.아메리카노 클릭", path=path,  by=By.NAME, timeout=10)

path = '1개 담기'
au.wait_and_click(desc="담기 클릭", path=path,  by=By.NAME, timeout=10)

time.sleep(2)

for i in range(3):
    path = "뒤로가기"
    au.wait_and_click(desc="뒤로가기 클릭", path=path, by=By.NAME, timeout=10)
    time.sleep(2)
# App 종료
au.terminate_app(app_packagename)
driver.quit()