import requests
import time

class DifferentAcc:
    uuid =""
    uuserid = 0
    def __init__ (self,uuid,uuserid):
        self.uuid = uuid
        self.uuserid = uuserid

wechat = DifferentAcc("65c92bd5f5cf4b4d9770d02d94f0792f",50169478)
apple = DifferentAcc("d7d760fe293d4f88ae3983f5bf1fbc56",50169597)
accountList = []
accountList.append(wechat)
accountList.append(apple)

def changeAccount(a):
# Define new data to create
    new_data = {
    "aid":"6444e23dab578e00490ff3c9",
    "uid": a.uuid,
    "vid":"64db9836cb6121004bc3cc15",
    "userinfo":
        {
        "device_id":"80789239-7A08-4DE1-83F1-C024D2C23C07-WZUH",
        "user_id":a.uuserid,
        "token":a.uuid,
        "origin":"app"
        }
    }
    print("\n")
    print(new_data)
    print("\n")
    return new_data

new_data= changeAccount(accountList[0])
url_post = "https://actapi.thepage.cn/vote"

# A POST request to the API
i = accountList.__len__()*10
while(i>0):
    i=i-1
    post_response = requests.post(url_post, json=new_data)
    time.sleep(1)
    # Print the response
    post_response_json = post_response.json()
    print(post_response_json)
    if(i==0):
        break
    if(i%10==0):
        accountList.pop(0)
        new_data= changeAccount(accountList[0])
    