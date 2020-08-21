import requests
from Util.GetDataFromXls import *
from requests.packages import urllib3


class Request:
    def requestGet(self, row):
        getDataFromXls = GetDataFromXls()
        url = getDataFromXls.getDataByCellData(row, 3)
        urllib3.disable_warnings()
        param = getDataFromXls.getDataByCellData(row, 6)
        result = requests.get(url + param)  # 发get请求
        print(result.status_code)
        return result

    def requestPost(self, row):
        getDataFromXls = GetDataFromXls()
        url = getDataFromXls.getDataByCellData(row, 3)
        param = getDataFromXls.getDataByCellData(row, 6)
        result = requests.post(url, data=json.dumps(param),
                               headers={"Content-Type": "application/json", "X-AUTH-TOKEN": ""})
        print(result.status_code)
        return result

