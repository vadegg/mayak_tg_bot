# moscow: lat 55..., lon 37...
def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

top = 55.902373
left = 37.332002
bottom = 55.580870
right = 37.877198

cafe_number = 20
beauty_number = 15
party_number = 30

def return_ll_list(number):
    return [(lat, lon)
        for lat in frange(
            bottom,
            top,
            (top-bottom) / number
        )
        for lon in frange(
            left,
            right,
            (right - left) / number
        )
    ]
cafe_list = return_ll_list(cafe_number)
beauty_list = return_ll_list(beauty_number)
party_list = return_ll_list(party_number)
