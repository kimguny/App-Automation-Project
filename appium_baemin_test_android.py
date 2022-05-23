# -*- coding: utf8 -*-
import time
from appium_util_android import *

# =================================
# baemin App 정보
app_packagename = "com.sampleapp"
app_activity = "com.baemin.presentation.ui.RouterActivity"

# 단말 UDID, adb devices 로 확인 가능
udid = "192.168.35.178:5555"

# Appium 서버 정보
appium_server_ip="127.0.0.1"
appium_server_port="4723"

# =================================
au = AppiumUtil()

#Appium Driver
capability = au.get_default_capability(udid)
driver = au.get_driver(capabilityset=capability, server_ip=appium_server_ip, server_port=appium_server_port)

# App 실행
#au.start_app(app_packagename, app_activity)
au.driver.activate_app(app_packagename)

# App 버전 체크
# Appium 서버 실행시 '--relaxed-security' 옵션 추가 필요
app_version = au.get_app_version(app_packagename)

# 단말 모델 체크
ue_model = au.get_device_model()

path = 'com.sampleapp:id/baeminNowButton'
au.wait(desc="App 실행시간", path=path, by=By.ID, timeout=10)

path = "com.sampleapp:id/backgroundImageView"
au.wait_and_click(desc="배민 버튼 클릭", path=path,  by=By.ID, timeout=10)

path = "//android.widget.ImageView[@content-desc='치킨']"
au.wait_and_click(desc="치킨 버튼 클릭", path=path,  by=By.XPATH, timeout=10)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView"
au.wait_and_click(desc="배달 빠른 순 버튼 클릭", path=path,  by=By.XPATH, timeout=10)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView"
au.wait_and_click(desc="초기화 버튼 클릭", path=path,  by=By.XPATH, timeout=10)

#뒤로가기 버튼
au.back_button()

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout"
au.wait_and_click(desc="검색", path=path,  by=By.XPATH, timeout=10)

path = "com.sampleapp:id/keywordEditTextView"
au.wati_and_set_text(desc="검색어 입력", text="이삭", path=path, by=By.ID, timeout=10)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[1]"
au.wait_and_click(desc="항목 클릭", path=path, by=By.XPATH, timeout=10)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView"
au.wait_and_click(desc="맨 위에 항목 클릭", path=path,  by=By.XPATH, timeout=10)

time.sleep(2)

for i in range(2):
    au.driver.swipe(132,1971, 27,528, 100) # 좌표 지정해서 스크롤
    time.sleep(3)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.Button[4]"
au.wait_and_click(desc="커피 클릭", path=path,  by=By.XPATH, timeout=10)

path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
au.wait_and_click(desc="H.아메리카노 클릭", path=path,  by=By.XPATH, timeout=10)

path = '//android.widget.Button[@content-desc="1개 담기2,500원"]'
au.wait_and_click(desc="담기 클릭", path=path,  by=By.XPATH, timeout=10)

time.sleep(2)

for i in range(3):
    au.back_button()
    time.sleep(1)

time.sleep(1)

# App 종료
au.terminate_app(app_packagename)
driver.quit()