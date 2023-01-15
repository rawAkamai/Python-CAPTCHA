import requests
import time

url_POST = "http://2captcha.com/in.php"
url_GET = "http://2captcha.com/res.php"
api_key = "";
google_key = "";
page_url = "";

payload_POST = {
    'key': api_key, 
    'method': 'userrecaptcha',
    'googlekey': google_key,
    'pageurl': page_url
}


headers = {}

response = requests.request("POST", url_POST, params=payload_POST, headers=headers)
if response.text[:2] == "OK":
    recaptcha_code = response.text[3:]
    payload_GET={
    'key': api_key,
    'action': 'get',
    'id': recaptcha_code
    }
else : 
    print("error sending captcha")
print(recaptcha_code)  

initial_time = time.time()
status = False

while status != True :
   print("Trying to get recaptcha response....")
   response_GET = requests.request("GET", url_GET, params=payload_GET, headers=headers)
   if response_GET.text[:2] == 'OK':
       status = True
   else:
       print("Recaptcha NOT READY yet")
       time.sleep(10)
       


print(response_GET.text)
