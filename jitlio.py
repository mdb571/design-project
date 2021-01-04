from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from twilio.rest import Client
from twilio import twiml
import os
from dotenv import load_dotenv

load_dotenv()


ACCOUNT_SID=os.environ.get('ACCOUNT_SID')
AUTH_TOKEN=os.environ.get('AUTH_TOKEN')
opt=Options()

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 1
    })


def meet():
    url='https://meet.jit.si/projectblind'
    browser = webdriver.Chrome(options=opt,executable_path='/usr/bin/chromedriver')
    browser.get(url)
    found=True
    while found:
        try:
            join_button=browser.find_element_by_class_name('action-btn')
            join_button.click()
            found=False
        except:
            continue

    client = Client(ACCOUNT_SID,AUTH_TOKEN)

    message = client.messages \
                .create(
                    body='\nHey there Bilal wants some help in doing something.Join using the link to help him out\n {}'.format(url),
                    from_='+12058437986', #use your twilio no here
                    to='+919995153948', #use your verified phone no. here
                    )
    print("message sent")
    person_joined=False
    while not person_joined:
        if len(browser.find_elements_by_class_name('videocontainer__toptoolbar'))>1:
            print('Helper found...has joined the meeting...')
            person_joined=True
        else:
            print('Waiting for helper to join...')
    while person_joined:
        if len(browser.find_elements_by_class_name('videocontainer__toptoolbar'))==1:
            print('The person has left..') 
            browser.close()
            break


