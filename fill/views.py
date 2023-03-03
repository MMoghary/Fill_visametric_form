from django.shortcuts import render, redirect
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'fill/index.html', {})



def fill_form(request):
        if request.GET.get('ramz') == '22':
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            web = webdriver.Chrome(PATH)
            web.get("https://ir-appointment.visametric.com/ir")
            time.sleep(1)
            web.maximize_window()
            time.sleep(1)
            schengen = web.find_element("name", "schengenBtn")
            schengen.click()

            start1 = web.find_element("name", "surveyStart")
            start1.click()
            time.sleep(1)
            nationality = web.find_element("name", "nationality")
            nationality.click()
            time.sleep(10)
            """captha = web.find_element("id","recaptcha-anchor")
            captha.click()"""
            btnSubmit = web.find_element("id", "btnSubmit")
            btnSubmit.click()
            time.sleep(2)
            list1 = web.find_element("name", "city")
            list1.send_keys('تهران')
            list2 = web.find_element("name", "office")
            list2.send_keys('تهران')
            list3 = web.find_element("name", "officetype")
            list3.send_keys('عادی')
            list4 = web.find_element("name", "totalPerson")
            list4.send_keys('2 متقاضی')
            time.sleep(2)
            paytype = web.find_element("id", "atm")
            paytype.click()
            time.sleep(2)
            mycard = web.find_element("id", "paymentCardInput")
            mycard.send_keys("5022291040143602")
            time.sleep(1)
            cardDatepicker = web.find_element("name", "cardDatepicker")
            cardDatepicker.click()
            time.sleep(1)
            day = web.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[2]/td[3]/span')
            day.click()
            time.sleep(1)
            checkCardListBtn = web.find_element("id", "checkCardListBtn")
            checkCardListBtn.click()
            bankpayment = web.find_element("name", "bankpayment")
            bankpayment.click()
            time.sleep(1)
            next = web.find_element("id", "btnAppCountNext")
            next.click()
            time.sleep(2)

            # last page
            sheba_number = web.find_element("name", "sheba_number")
            sheba_number.send_keys('IR630570033280012059647101')
            sheba_name = web.find_element("name", "sheba_name")
            sheba_name.send_keys('مجید مقاری')
            name1 = web.find_element("name", "name1")
            name1.send_keys('MADJID')
            surname1 = web.find_element("name", "surname1")
            surname1.send_keys('MOGHARY')
            birthyear1 = web.find_element("name", "birthyear1")
            birthyear1.send_keys('1975')
            birthmonth1 = web.find_element("name", "birthmonth1")
            birthmonth1.send_keys('05')
            birthday1 = web.find_element("name", "birthday1")
            birthday1.send_keys('12')
            passport1 = web.find_element("name", "passport1")
            passport1.send_keys('F53554441')
            phone1 = web.find_element("name", "phone1")
            phone1.send_keys('09123887616')
            phone21 = web.find_element("name", "phone21")
            phone21.send_keys('02144852483')
            email1 = web.find_element("name", "email1")
            email1.send_keys('majid_moghary@yahoo.com')

            name2 = web.find_element("name", "name2")
            name2.send_keys('HAJAR')
            surname2 = web.find_element("name", "surname2")
            surname2.send_keys('MOHAMMADY')
            birthyear2 = web.find_element("name", "birthyear2")
            birthyear2.send_keys('1956')
            birthmonth2 = web.find_element("name", "birthmonth2")
            birthmonth2.send_keys('02')
            birthday2 = web.find_element("name", "birthday2")
            birthday2.send_keys('20')
            passport2 = web.find_element("name", "passport2")
            passport2.send_keys('E56400168')

            time.sleep(5)
            next = web.find_element("id", "btnAppPersonalNext")
            next.click()
            time.sleep(1)
            previewchk = web.find_element("name", "previewchk")
            previewchk.click()
            btnAppPreviewNext = web.find_element("id", "btnAppPreviewNext")
            btnAppPreviewNext.click()
            time.sleep(15)
        else:
            return HttpResponse('input is incorrect !!')
        return HttpResponse('finished')


    # web.quit()


