import json
import os
from urllib import parse
import requests

class GeoCoder(object):
    def __init__(self, api_file):
        api_cfg = {}
        with open(api_file) as api_file:
            api_cfg.update(json.load(api_file))
        self.__API_Key = api_cfg['API_Key']

    def geocode(self, address, version=1):
        if address == '':
            return []
        return self._geocode_amap(address)

    def _geocode_amap(self, address):
        url = f'https://restapi.amap.com/v3/geocode/geo?address={parse.quote(address)}&key={self.__API_Key}'
        resp = requests.get(url)
        data = resp.json()
        if data['status'] == '1' and data['geocodes']:
            return data['geocodes']
        return []

    def rev_geocode(self, latlng, version=1):
        return self._rev_geocode_amap(latlng)

    def _rev_geocode_amap(self, latlng):
        lat, lng = latlng
        url = f'https://restapi.amap.com/v3/geocode/regeo?location={lng},{lat}&key={self.__API_Key}'
        resp = requests.get(url)
        data = resp.json()
        if data['status'] == '1' and 'regeocode' in data:
            return [data['regeocode']]
        return []

    def address_to_gps(self, address, version=1):
        res = self.geocode(address)
        if not res:
            return ()
        location = res[0]['location'].split(',')
        return float(location[1]), float(location[0])

    @staticmethod
    def __geores_to_city(res):
        if not res:
            return {}
        city = {}
        # 针对 geocode/geo 返回
        if 'province' in res[0]:
            city['country'] = '中国'
            city['province'] = res[0].get('province', '')
            city['city'] = res[0].get('city', '') or city['province']
            location = res[0]['location'].split(',')
            city["latitude"] = float(location[1])
            city["longitude"] = float(location[0])
        # 针对 geocode/regeo 返回
        elif 'addressComponent' in res[0]:
            comp = res[0]['addressComponent']
            city['country'] = comp.get('country', '中国')
            city['province'] = comp.get('province', '')
            city['city'] = comp.get('city', '') or city['province']
            location = res[0]['location'].split(',')
            city["latitude"] = float(location[1])
            city["longitude"] = float(location[0])
        return city

    def address_to_city(self, address, version=1):
        geo_res = self.geocode(address)
        return self.__geores_to_city(geo_res)

    def gps_to_city(self, latlng, version=1):
        geo_res = self.rev_geocode(latlng)
        return self.__geores_to_city(geo_res)

    def address_to_city_list(self, address, version=1):
        geo_res = self.geocode(address)
        city_list = []
        for gr in geo_res:
            temp = self.__geores_to_city([gr])
            flag = True
            for c in city_list:
                if compare_city(c, temp):
                    flag = False
                    break
            if flag:
                city_list.append(temp)
        return city_list

def compare_city(city1, city2):
    if city1.get('country') != city2.get('country'):
        return False
    if city1.get('province') != city2.get('province'):
        return False
    if city1.get('city') != city2.get('city'):
        return False
    return True

if __name__ == '__main__':
    api_file = os.path.join(os.path.dirname(__file__), 'yang.gapi')
    gc = GeoCoder(api_file=api_file)
    print(f'Address to City: 北京大学物理学院->{gc.address_to_city("北京大学物理学院")}')
    print(f'Address to City List: 肯德基->{gc.address_to_city_list("肯德基")}')
