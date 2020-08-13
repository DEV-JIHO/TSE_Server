from urllib.parse import urlencode, quote_plus, unquote
import requests
import json


def api_Living_Reading(key, feature, time, areano='1100000000'): \
        # I used api from Korea Meteorological Administration
    # https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043583

    # -*- coding:utf-8 -*-
    url = f"http://apis.data.go.kr/1360000/LivingWthrIdxService/{feature}"

    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): key, quote_plus('pageNo'): '1', quote_plus('dataType'): 'JSON',
         quote_plus('areaNo'): areano, quote_plus('time'): time, quote_plus('requestCode'): 'A20'})
    request = requests.get(url + queryParams)
    json_data = json.loads(request.text)

    if feature == 'getUVIdx':
        return json_data["response"]['body']["items"]["item"][0]['today']
    else:
        return json_data["response"]['body']["items"]["item"][0]['h3']


def get_living_weather_data(key, query, time, lasttime, result, areano='1100000000'):
    print("Get living weather data...")
    for feature in query:
        result[feature] = api_Living_Reading(key, feature, time)
    print("Done.")
    return result, lasttime


def api_air_pullution(key, item_code):
    # Used api made by Korea Environment Corporation
    # https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000581
    url = f"http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst"
    # -*- coding:utf-8 -*-
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): key, quote_plus('itemCode'): item_code, quote_plus('dataGubun'): 'HOUR',
         quote_plus('_returnType'): 'json'})
    request = requests.get(url + queryParams)

    json_data = json.loads(request.text)
    return json_data['list'][0]


def get_air_pollution_data(key, item_code, result, station="seoul"):
    print("Get air pollution data...")
    for item in item_code:
        value = api_air_pullution(key, item)
        result[item] = value[station]
    print("Done.")

    return result


def get_all_api_data(date, lasttime):
    DECODE_KEY = unquote(
        'cELHrfnETp70pjPK90A%2F%2B2h4u9%2FNYVQ6o4e%2B1icLTH6TodaaaxmUvLfsCsRVvH4XvI6NqZSl4jC3grykXKEVTg%3D%3D')
    DATE = date
    QUERY = ['getHeatFeelingIdx', 'getDiscomfortIdx', 'getUVIdx', 'getSenTaIdx', 'getAirDiffusionIdx']
    ITEM_CODE = ['SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']
    result = {}

    result, lasttime = get_living_weather_data(DECODE_KEY, QUERY, DATE, lasttime, result)
    result = get_air_pollution_data(DECODE_KEY, ITEM_CODE, result, station='seoul')

    return result, lasttime
