# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-05 23:25:52
@describe 顺丰官网地址智能解析
"""
import json

import requests


def main():
    cookie='i18n_redirected=sc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218d1afaa80c26fe-068b0e8c0d347c-26001951-2073600-18d1afaa80d3191%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fe.zhiniuxue.com%2F%22%7D%2C%22%24device_id%22%3A%2218d1afaa80c26fe-068b0e8c0d347c-26001951-2073600-18d1afaa80d3191%22%7D; HWWAFSESID=7c557824daeafa9b40; HWWAFSESTIME=1709652051835; tgw_l7_route=1695cccd76db859e48821db6d304d41a; access-type=0; access-ip=123.112.65.56, 123.125.16.150, 123.249.52.84, 139.159.208.191, 10.240.243.0; OWFSESSION=9416df77e0ec491eb96e48a2d0750807; loginUser=18810951239; remember-me=MGEzM2MzYzA2Y2FjNGFhZDk1ZjU5MTU1Y2I1NTM0ZTI6OTdmN2Q2ZDhlNTc2NGMwOTgxNzE5ZWI0ZDg5NWM1Mjg='
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    headers = {
        "Cookie": cookie,
        "Host": "www.sf-express.com",
        "Content-Type": "application/json",
        "Origin": "https://www.sf-express.com",
        "Referer": "https://www.sf-express.com/chn/sc/address-book?from=page",
        "User-Agent": ua
    }

    address = "天津市和平区南京路239号宏瑞广场二层锐思教育 刘志勇 13241415309"
    data = json.dumps({"address": address})
    url = 'https://www.sf-express.com/sf-service-core-web/service/nlp/address/mainlandChina/resolve?lang=sc&region=cn&translate=sc'
    resp = requests.post(url, headers=headers, data=data)
    json_data = resp.json()
    print("原始响应:", json_data)
    if json_data.get("code") != 0:
        print("解析失败")
        return

    result = json_data.get("result")[0]
    resolve_data = {
        "name": result.get("name"),
        "mobile": result.get("mobile"),
        "province": result.get("province"),
        "city": result.get("city"),
        "district": result.get("district"),
        "address": result.get("address"),
    }
    print(resolve_data)


if __name__ == "__main__":
    main()
