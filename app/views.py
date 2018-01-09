import json
import os

import pokebase as pb
from flask import request, Response
from fuzzywuzzy import process
from twx.botapi import Message, InputFile, InputFileInfo

from app import application
from app import bot


def process_text(message):
    possible_name = message.text

    response = {}

    # Get list of pokemons from precompiled file
    current_path = os.path.dirname(os.path.realpath(__file__))
    print (current_path + '/../pokemons.json')
    with open(current_path + '/../pokemons.json') as pokemons_file:
        pokemons = json.load(pokemons_file)

    # get only the name arry from the json
    pnames = [x['name'] for x in pokemons['results']]

    # initialise name and caption
    name = possible_name
    response["caption"] = possible_name

    # fix name and caption if it does not match
    if possible_name not in pnames:
        fuzzy_result = process.extractOne(possible_name, pnames)
        name = fuzzy_result[0]
        response["caption"] = "Did you mean: " + name
        print ("fuzzy result", fuzzy_result)

    # get pokemon image (sprite)
    pb.api.set_cache(".")
    poke = pb.pokemon(name)
    path = pb.pokemon_sprite(poke.id).path
    response["photo"] = "sprite/pokemon/" + str(poke.id) + ".png"

    return response


@application.route('/incoming', methods=['POST'])
def incoming():
    j = json.loads(request.get_data())
    m = j['message']
    msg = Message.from_result(m)
    print('Raw message:', msg)
    try:
        print('Received this message from user %d (%s): %s' % (msg.sender.id, msg.sender.first_name, msg.text))
        chat_id = msg.chat.id
        msgid = msg.message_id
        print('Responding to chat %i using token %s' % (chat_id, bot.token))
        response = process_text(msg)

        with open(response["photo"], 'rb') as fp:
            file_info = InputFileInfo(response["photo"], fp, 'image/png')

            photo_file = InputFile('photo', file_info)

            resp = bot.send_photo(
                chat_id=chat_id,
                photo=photo_file,
                caption=(response["caption"]),
                reply_to_message_id=msgid
            ).wait()

    except Exception as e:
        print("ERROR: ", e)

    return Response(status=200)
