#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


myGames = []

class GameInfo:
    def __init__(self, gameName, gameInfoVoice, gameInfo):
        self.gameName = gameName
        self.gameInfoVoice = gameInfoVoice
        self.gameInfo = gameInfo

myGames.append("Haberdashery - Endless Arcade Runner", "Available on iOS and Android!", "iOS: http://apple.co/1UrkmPR \nAndroid: http://bit.ly/1RqflCQ")
myGames.append("Target Crack", "Available on iOS and Android!", "iOS: http://apple.co/1Lvgapx \nAndroid: http://bit.ly/1ttbDTt")
myGames.append("Turbo Hobo Cannon", "Available on Android and Newgrounds!", "Android: http://bit.ly/1S35i53 \nNewgrounds: http://bit.ly/1VW2vSh")
myGames.append("Fungeon Crawler", "Available on Indie Game Stand for PC and MAC!", "PC/MAC: http://bit.ly/1Yn7cVr")
myGames.append("A World Apart", "Available on Indie Game Stand for PC and MAC!", "PC/MAC: http://bit.ly/1MhMy02")
myGames.append("Zap it", "Available on iOS and Android!", "iOS: http://apple.co/1VW28qB \nAndroid: http://bit.ly/1UPvi5G")
myGames.append("Switch it", "Available on iOS and Android!", "iOS: http://apple.co/1UPvt0G \nAndroid: http://bit.ly/1UMB1fg")
myGames.append("Defuse it", "Available on iOS and Android!", "iOS: http://apple.co/1D1kOtD \nAndroid: http://bit.ly/1Ua6z1N")
myGames.append("Don't Touch the Button", "Available on iOS!", "iOS: http://apple.co/1ttcNhH")
myGames.append("Welcome to Undercog", "by Geek Monster Games!", "by Geek monster Games! \nLearn more at: http://bit.ly/1VW2HAL")
myGames.append("Rocket Rambler", "by Heavy Key Studios!", "by Heavy Key Studios! \niOS: http://apple.co/1UPw5DG \nAndroid: http://bit.ly/1YoohP8")

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    res = processRequest(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "displayGameInfo":
        return {}

    res = makeWebhookResult(req)
    return res

def makeWebhookResult(req):
    result = req.get("result")
    parameters = result.get("parameters")
    gameName = parameters.get("gameName")

    for game in myGames:
        if (game.gameName == gameName):
            gameInfoVoice = game.gameName + "! " + game.gameInfoVoice
            gameInfo = game.gameName + "!\n" + game.gameInfo


    return {
        "speech": gameInfo,
        "displayText": gameInfo,
        # "data": {"slack": gameInfo},
        # "data": {"facebook": gameInfo},
        "source": "LunaBot"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    app.run(debug=False, port=port, host='0.0.0.0')
