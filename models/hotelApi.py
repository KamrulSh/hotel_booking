import random
import requests
from odoo import models, fields


class HotelApi(models.Model):
    _name = 'hotels.api'
    _description = 'Hotel api'
    _rec_name = 'hotel_name'

    url = "https://leejaew-hotels-in-singapore-v1.p.rapidapi.com/hotels"
    querystring = {"country": "Singapore", "name": "*copthorne*"}
    headers = {
        'x-rapidapi-host': "leejaew-hotels-in-singapore-v1.p.rapidapi.com",
        'x-rapidapi-key': "300090a95bmshb5201dfd264f1c4p10e53fjsn851b5de5bb2e"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    random_num = random.randint(0, 2)

    hotel_name = fields.Char(string="Hotels name", default=response.json()[random_num]['name'])
    total_rooms = fields.Char(string="Total rooms", default=response.json()[random_num]['totalrooms'])
    country = fields.Char(string="Country", default=response.json()[random_num]['country'])
    phone = fields.Char(string="Phone Number", default=response.json()[random_num]['phone'])
    social = fields.Char(string="Address", default=response.json()[random_num]['social']['facebook'])
