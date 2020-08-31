from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client
from twilio import twiml

ACCOUNT_SID='AC5d8e6b86d6f466ea2cfff62ebc0959cf'
AUTH_TOKEN='e0fdccac53cfa2ca3129ea1212ac4936'

def meet():
    url='https://meet.jit.si/projectblind'
    browser = webdriver.Firefox()
    browser.get(url)
    found=True

    while found:
        try:
            join_button=browser.find_element_by_class_name('action-btn')
            join_button.click()
            found=False
        except ElementClickInterceptedException:
            continue

    client = Client(ACCOUNT_SID,AUTH_TOKEN)

    message = client.messages \
                .create(
                    body='\nHey there Bilal wants some help in doing something.Join using the link to help him out\n {}'.format(url),
                    from_='+12058437986', #use your twilio no here
                    to='+919995153948', #use your verified phone no. here
                    )
    print("message sent")
    time.sleep(540)
    browser.close()