from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
#returns distance in kilometers
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...
import db
from status import Status

db_interface = db.DBInterface()

def row_to_message(row, dist):
    message = """{} приглашает тебя в гости и дарит скидку в 20%!
Подходи по адресу: {}
Заведение всего в {}  метрах от тебя!
    """.format(row[1], row[5], '%.0f' % (dist * 1000))
    return message

def get_top_of_places(status, location):
    lon = location.longitude
    lat = location.latitude
    if status == Status.beauty_choosed:
        type = 'beauty'
    elif status == Status.party_choosed:
        type = 'party'
    else:
        type = 'cafe'
    query = """
        select *
        from places
        where type='{}';
        """.format(type)
    places_list = db_interface.execute_fetchall_close(query)
    places_list.sort(
        key=lambda x:
            distance(x[3], x[4], lat, lon),
        )
    return list(map(lambda x: (x[0], row_to_message(x,
    distance(x[3], x[4], lat, lon))), places_list[:3]))
