# IPython log file

import cafes_mining as c
len(c.beauty_list)
import requests
params = {
    "geocode": '{},{}'.format(str(c.cafe_list[0][0]), str(c.cafe_list[0][1])),
'apikey': '',
'sco': 'lonlat'
}
req = 'https://geocode-maps.yandex.ru/1.x/'
params = {
    "geocode": '55.700524,37.529664'
'apikey': '',
'sco': 'lonlat'
}
params = {
    "geocode": '55.700524,37.529664',
'apikey': '',
'sco': 'lonlat'
}
res = requests.get(req, params=params)
res.text
params = {
    "geocode": '55.700524, 37.529664',
'apikey': '',
'sco': 'lonlat'
}
res = requests.get(req, params=params)
res.text
params = {
    "geocode": '55.700524,37.529664',
'apikey': '',
'sco': 'latlon'
}
res = requests.get(req, params=params)
res.tet
res.text
req = 'https://geocode-maps.yandex.ru/1.0/'
res = requests.get(req, params=params)
res.text
params = {
    "geocode": '55.700524,37.529664',
'apikey': '',
'sco': 'latlon',
'format':'json'
}
res = requests.get(req, params=params)
res.text
params = {
    "geocode": '37.611,55.758',
'apikey': '',
'sco': 'latlon',
'format':'json'
}
res = requests.get(req, params=params)
res.text
req = 'https://geocode-maps.yandex.ru/1.x/'
res = requests.get(req, params=params)
res.text
params = {
    "geocode": '37.611,55.758',
'apikey': '',
'sco': 'lonlat',
'format':'json'
}
res = requests.get(req, params=params)
res.text
params = {
    "geocode": '37.611,55.758',
'apikey': '',
'format':'json'
}
res = requests.get(req, params=params)
res.text
c.beauty_list[0][0]
c.beauty_list[0][1]
params = {
    "geocode": '37.332002,55.58087',
'apikey': '',
'format':'json'
}
res = requests.get(req, params=params)
res.text
import json
j = json.loads(res.text)
j
j[0]
j.get()
j.items()[0]
j.items()
j.items().keay()
j.items().keys()
j.items()
j.keys()
j['keys']
j['respone']
j['respone']
j['response']
j['response'].keys()
j['response']['GeoObjectCollection']
j['response']['GeoObjectCollection'].keys()
j['response']['GeoObjectCollection'].keys()
j['response']['GeoObjectCollection']['featureMember']
j['response']['GeoObjectCollection']['featureMember'].keys()
j['response']['GeoObjectCollection']['featureMember'][0]
j['response']['GeoObjectCollection']['featureMember'][0].keys()
j['response']['GeoObjectCollection']['featureMember'][0].keys()['GeoObject']
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['text']
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'].keys()
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'].keys()
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'].keys()
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData'].keys()
j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
def get_address(res):
    j = json.loads(res.text)
    return j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
res.text
get_address(res)
params = {
    "geocode": '37.529664, 55.700524',
'apikey': '',
'format':'json'
}
res = requests.get(req, params=params)
res.text
get_address(res)
def get_addr_from_ll(ll):
    params = {                                                                                                                 
        "geocode": '{}, {}'.format(ll[1], ll[0]),
        'apikey': '',                                                                             'format':'json'
    }
    res = requests.get(req, params=params)
    return get_address(res)
c.cafe_list[0]
get_addr_from_ll(c.cafe_list[0])
import sqlite3
conn = sqlite3.connect('db/main.db')
def add_all_to_db(l):
    for i, ll in enumerate(l):
        print(i, ll)
        
add_all_to_db(c.cafe_list[0])
def add_all_to_db(l):
    for i, ll in enumerate(l, 1):
        print(i, ll)
        
add_all_to_db(c.cafe_list[0])
def add_all_to_db(l, t):
    for i, ll in enumerate(l, 1):
        print(i, ll)
        
def add_all_to_db(l, t, name):
    for i, ll in enumerate(l, 1):
        print("++++++")
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        print(query)
        
        
add_all_to_db(c.cafe_list, 'cafe', 'Кафе Ёлочка')
def add_all_to_db(l, t, name):
    for i, ll in enumerate(l, 1):
        print("++++++")
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        conn.execute(query)
        print('\tProcess: {}'.format(i), end='')
        
        
        
add_all_to_db(c.cafe_list, 'cafe', 'Кафе Ёлочка')
conn.commit()
def add_all_to_db(l, t, name):
    for i, ll in enumerate(l, 1):
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        conn.execute(query)
        print('\tProcess: {}'.format(i), end='')
    conn.commit()
    
        
        
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
def add_all_to_db(l, t, name):
    for i, ll in enumerate(l, 1):
        print('\tProcess: {}'.format(i), end='')
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        conn.execute(query)
    conn.commit()
    
        
        
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
conn.close()
conn = sqlite3.connect('db/main.db')
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
def add_all_to_db(l, t, name):
    print("Start")
    for i, ll in enumerate(l, 1):
        print('\tProcess: {}'.format(i), end='')
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        conn.execute(query)
    conn.commit()
           
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
c.beauty_list
def add_all_to_db(l, t, name):
    print("Start")
    for i, ll in enumerate(l, 1):
        print('\tProcess: {}'.format(i), end='')
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        print(query)
        #conn.execute(query)
    conn.commit()
           
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
def add_all_to_db(l, t, name):
    print("Start")
    for i, ll in enumerate(l, 1):
        print('\tProcess: {}'.format(i), end='')
        query = """
        
        insert into places (name, type, lat, lon, address)
        values ('{}', '{}', {}, {}, '{}');
        """.format(
            str(name) + " " + str(i),
            t,
            ll[0],
            ll[1],
            get_addr_from_ll(ll)
        )
        #print(query)
        conn.execute(query)
    conn.commit()
           
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
conn.close()
conn = sqlite3.connect('db/main.db')
add_all_to_db(c.beauty_list, 'beauty', 'Салон красоты Горыныч')
add_all_to_db(c.beauty_list, 'party', 'Квест-клуб Бункер')
add_all_to_db(c.party_list, 'party', 'Квест-клуб Бункер')
conn.commit()
conn.close()
get_ipython().run_line_magic('logstart', './mine_places.py')
get_ipython().run_line_magic('logon', '')
