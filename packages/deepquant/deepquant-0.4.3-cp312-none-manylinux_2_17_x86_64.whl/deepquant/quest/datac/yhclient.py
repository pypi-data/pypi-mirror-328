import logging
import requests

import pandas as pd

class YhClient():

    def __init__(self, host):
        self.host = host

    def get(self, api_name, **params):
        try:
            res = requests.get(f"{self.host}/gid/yhdatas/api/{api_name}")
            res = res.json()
            return res["data"]
        except Exception as e:
            logging.getLogger("yhdatac").info(e)
            return []

client = YhClient("http://yhds.inner.prodxc.chinastock.com.cn")

def all_instruments(type_='stock', date=None, market="cn", **kwargs):
    """
    获取合约信息
    >>> all_instruments('stock', cache=True)
    """
    ins_list = client.get("instruments", **{
        "instrument_type": type_,
        "cache": kwargs.get("cache", True)
    })
    df = pd.DataFrame(ins_list)
    return df

def main():
    df = all_instruments('stock', cache=True)
    print(df.head())

if __name__ == "__main__":
    main()