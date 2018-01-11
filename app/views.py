import json
import os

import requests
from flask import request, Response
from twx.botapi import Message

from app import application
from app import bot


def process_text(message):
    city = message.text

    # getting an environment variable - do not store secrets in plain text
    # set with  heroku config:set OPENWEATHERMAP_API_KEY=...your_openweathermap_api_key... --app young-refuge-39625
    openweathermap_api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

    # request current weather from openweathermap
    r = requests.get(
        url='http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=' + openweathermap_api_key)

    # convert weather data json to a dictionary
    data = r.json()

    # if successful extract weather data
    if data["cod"] == 200:
        hours_sun = str(round((data["sys"]["sunset"] - data["sys"]["sunrise"]) / (60 * 60)))
        deg = ""
        if "deg" in data["wind"].keys():
            deg = "(" + str(data["wind"]["deg"]) + "°)"

        # response would be formated with html
        my_response = "<code><b>" + data["name"] + "</b>, <>" + data["sys"]["country"] + \
                      "\n  <b>temperature</b>: " + str(round(data["main"]["temp"])) + " °C" + \
                      "\n  <b>humidity</b>: " + str(data["main"]["humidity"]) + " % " + \
                      "\n  <b>wind speed</b>: " + str(data["wind"]["speed"]) + " m/s " + deg + \
                      "\n  <b>weather</b>: " + data["weather"][0]["main"] + \
                      "\n  <b>hours of sunlight</b>: " + hours_sun + " hours" + \
                      "</code>\n"
    else:
        # for a more personal touch one can use the users name when replying
        my_response = "I am sorry {}, I could not find a city with the name: {}" \
            .format(message.sender.first_name, city)
    print ("response", my_response)
    return my_response


@application.route('/incoming', methods=['POST'])
def incoming():
    j = json.loads(request.get_data())
    if 'message' in j.keys():
        m = j['message']
        msg = Message.from_result(m)
        print('Raw message:', msg)
        try:
            print('Received this message from user %d (%s): %s' % (msg.sender.id, msg.sender.first_name, msg.text))
            chat_id = msg.chat.id
            print('Responding to chat %i using token %s' % (chat_id, bot.token))
            response_text = process_text(msg)
            resp = bot.send_message(
                chat_id=chat_id,
                text=response_text,
                parse_mode="HTML",
                disable_web_page_preview=None,
                reply_to_message_id=None,
                reply_markup=None,
                disable_notification=False).wait()
        except Exception as e:
            print("ERROR: ", e)
    return Response(status=200)
