from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time
import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED)
print("Sürümünüze göre önce sürücü yüklemelisiniz  \n \n1) Chrome girin \n2) Sağ üstteki ··· noktaya tıklayın \n3) Yardım sekmesinden hakkında bölümüne tıklayın ve sürümü öğrenin\n4) 'https://chromedriver.chromium.org/downloads' sitesinden sürümünüze göre olan sürücüyü yükleyin \n5) yüklediğiniz rar dosyasını açın ve içindeki dosyakarı F-NE dosyasının içine atın... ")
bitis =input("Yükledim... Enter ")
os.system(" {}".format(bitis))

while True:
    
    browserProfile = webdriver.ChromeOptions()
    browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})

    service = Service("./chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://google.com")
    
    #
    # browser = webdriver.Chrome('./chromedriver.exe', chrome_options=browserProfile)
    #driver = webdriver.Chrome(service=service)

    il = input("İl: ")
    ilce = input("İlçe: ")
    url = driver.get(f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}")
    kaynak = driver.page_source
    soup = BeautifulSoup(kaynak, "html.parser") 
    time.sleep(1)

    anliknobetci = soup.find("span",{"class":"isim"})
    tel = soup.find("div",{"class":"col-lg-3 py-lg-2"})
    acik = soup.find("div",{"class":"mt-4 text-center"}).text.strip()

    print(f"""

    Nöbetçi: {anliknobetci.text}

    Tel: {tel.text}

    {acik}

    """)

    bitis =input("Geri... Enter ")
    os.system(" {}".format(bitis))
    





  








