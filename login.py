from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import time

options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UiAutomator2",
	"appium:platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:app": "C:/Users/aa971/Downloads/pijar-sekolah-siswa.apk",
    # "appPackage": "com.instagram.android",
    # "appActivity": "com.instagram.mainactivity.MainActivity",
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

time.sleep(2) #waiting flash skrin
driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Masuk"]').click()

#Step Login
time.sleep(2) # give time for click to selectbox school
driver.hide_keyboard()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Pilih nama sekolah"]').click()
time.sleep(2)
driver.hide_keyboard()#hide keyboard for send key by code to form
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Cari sekolahmu"]').send_keys("SMK QA")
time.sleep(2)
driver.find_element(by=AppiumBy.XPATH, value ='//android.view.ViewGroup[@content-desc="SMK QA Manajemen"]').click()
time.sleep(2)

driver.hide_keyboard() #hide keyboard for send key by code to form

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Masukkan NISN/email/nomor telepon"]').send_keys("00111201")
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Masukkan password"]').send_keys("00111201")
driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@content-desc="Masuk"])[1]').click()
time.sleep(5)

#Step Access Profile Me
driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Profil Saya"]').click()
time.sleep(2)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
time.sleep(2)


#Logout Application
driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Keluar"]').click()
driver.find_element(by=AppiumBy.XPATH, value='(//android.view.ViewGroup[@content-desc="Keluar"])[1]').click()
time.sleep(3)
# driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Username, email or mobile number"]').send_keys("ardiansyah.scg@gmail.com")
# driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Password"]').send_keys("123Abcde")
# driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Masuk"]').click()
# driver.quit()