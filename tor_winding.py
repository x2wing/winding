from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r"D:\Tor Browser\Browser\firefox.exe")
# profile = FirefoxProfile(r"D:\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

driver = webdriver.Firefox(firefox_binary=binary)
driver.get("http://csdb.ufanet.ru")
driver.save_screenshot("screenshot.png")
driver.quit()