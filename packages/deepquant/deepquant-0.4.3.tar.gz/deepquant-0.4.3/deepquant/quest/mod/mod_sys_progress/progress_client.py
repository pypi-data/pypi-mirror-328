import logging
import requests

import pandas as pd

class ProcessClient():

    def __init__(self, host):
        self.host = host
        
    def post(self, api_name, json=None):
        """发送 POST 请求"""
        try:
            res = requests.post(f"{self.host}/gid/strategyManager/backtest/{api_name}",json=json)
            json = res.json()
            return(res.status_code, json["meta"]["code"] , json)
        except Exception as e:
            logging.getLogger("ProcessClient").info(e)
            return None

client = ProcessClient("http://10.4.21.70:8288/")

def update_progress(progress, backtestId):
    json = {
    "backtestId": backtestId,
    "progress": progress/100,
    "rmrk": ""
   }
    print(json)
    httpcode, retcode, json = client.post(api_name = "updateProgress",  json=json)
    if httpcode != 200 or int(retcode) != 0:
        print("mod_progress更新回测进度失败!", json)

def update_status(status, backtestId):
    json = {
    "backtestId": backtestId,
    "runStatus": status,
    "rmrk": ""
   }
    print(json)
    httpcode, retcode, json  = client.post(api_name = "updateRunStatus",  json=json)
    if httpcode != 200 or int(retcode) != 0:
        print("mod_progress更新回测状态失败!", json)        
    

def main():
    update_status("fail","12345")
    

if __name__ == "__main__":
    main()