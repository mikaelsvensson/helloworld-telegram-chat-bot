# coding=utf-8
import json
import random

from flask import request, Response
from twx.botapi import Message, ReplyKeyboardMarkup, ReplyKeyboardHide

from app import application
from app import bot


def process_text(message):
    incomming_text = message.text

    adjective = ['roliga ', 'knasiga ', 'smarta ', 'super-']
    subject = ['katten', 'hjälten', 'bananen', 'boten', 'jag']

    my_response = 'Vad sägs om att kalla din bot för "%s%s"?' % (random.choice(adjective), random.choice(subject))
    return my_response


@application.route('/incoming', methods=['POST'])
def incoming():
    j = json.loads(request.get_data())
    m = j['message']
    msg = Message.from_result(m)
    print('Raw message:', msg)
    try:
        print('Received this message from user %d (%s): %s' % (msg.sender.id, msg.sender.first_name, msg.text))
        chat_id = msg.chat.id
        print('Responding to chat %i using token %s' % (chat_id, bot.token))
        response_text = process_text(msg)

        custom_keyboard = [['Fler förslag, tack', 'Nu får det vara nog']]
        if msg.text != 'Nu får det vara nog':
            reply_markup = ReplyKeyboardMarkup.create(custom_keyboard)
        else:
            reply_markup = ReplyKeyboardHide.create()

        resp = bot.send_message(
            chat_id=chat_id,
            text=response_text,
            parse_mode=None,
            disable_web_page_preview=None,
            reply_to_message_id=None,
            reply_markup=reply_markup,
            disable_notification=False).wait()
    except Exception as e:
        print("ERROR: ", e.message)

    print("send_message returned ", resp)

    return Response(status=200)
