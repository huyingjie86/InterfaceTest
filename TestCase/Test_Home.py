import os
import sys
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from Util.Request import *
from Util.GetDataFromXls import *
import pytest


class TestHome:
    # 将所有get方式的请求存入request_get_data
    getDataFromXls = GetDataFromXls()
    request_get_data = []
    for row in range(1, getDataFromXls.worksheet.nrows):
        if getDataFromXls.getDataByCellData(row, 4) == 'get' and getDataFromXls.getDataByCellData(row, 1) == \
                'Home':
            request_get_data.append(row)

    @pytest.mark.parametrize('row', request_get_data)
    def test_request_get(self, row):
        request = Request()
        r = request.requestGet(row)
        assert r.status_code == 200 or 206
