#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


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

    if (gameName == "Haberdashery"):
        gameInfoVoice = "Haberdashery - Endless Arcade Runner! Available on iOS and Android!"
        gameInfo = "Haberdashery - Endless Arcade Runner! \niOS: http://apple.co/1UrkmPR \nAndroid: http://bit.ly/1RqflCQ"
    elif (gameName == "Target Crack"):
        gameInfoVoice = "Target Crack! Available on iOS and Android!"
        gameInfo = "Target Crack! \niOS: http://apple.co/1Lvgapx \nAndroid: http://bit.ly/1ttbDTt"
    elif (gameName == "Turbo Hobo Cannon"):
        gameInfoVoice = "Turbo Hobo Cannon! Available on Android and Newgrounds!"
        gameInfo = "Turbo Hobo Cannon! \nAndroid: http://bit.ly/1S35i53 \nNewgrounds: http://bit.ly/1VW2vSh"
    elif (gameName == "Fungeon Crawler"):
        gameInfoVoice = "Fungeon Crawler! Available on Indie Game Stand for PC and MAC!"
        gameInfo = "Fungeon Crawler \nPC/MAC: http://bit.ly/1Yn7cVr"
    elif (gameName == "A World Apart"):
        gameInfoVoice = "A World Apart! Available on Indie Game Stand for PC and MAC!"
        gameInfo = "A World Apart \nPC/MAC: http://bit.ly/1MhMy02"
    elif (gameName == "Zap it"):
        gameInfoVoice = "Zap it! Available on iOS and Android!"
        gameInfo = "Zap it \niOS: http://apple.co/1VW28qB \nAndroid: http://bit.ly/1UPvi5G"
    elif (gameName == "Switch it"):
        gameInfoVoice = "Switch it! Available on iOS and Android!"
        gameInfo = "Switch it \niOS: http://apple.co/1UPvt0G \nAndroid: http://bit.ly/1UMB1fg"
    elif (gameName == "Defuse it"):
        gameInfoVoice = "Defuse it! Available on iOS and Android!"
        gameInfo = "Defuse it \niOS: http://apple.co/1D1kOtD \nAndroid: http://bit.ly/1Ua6z1N"
    elif (gameName == "Don't Touch the Button"):
        gameInfoVoice = "Don't Touch the Button! Available on iOS!"
        gameInfo = "Don't Touch the Button \niOS: http://apple.co/1ttcNhH"
    elif (gameName == "Welcome to Undercog"):
        gameInfoVoice = "Welcome to Undercog!"
        gameInfo = "Geek Monster Games - Welcome to Undercog \nLearn more at: http://bit.ly/1VW2HAL"
    elif (gameName == "Rocket Rambler"):
        gameInfoVoice = "Rocket Rambler! Available on iOS and Android!"
        gameInfo = "Heavy Key Studios - Rocket Rambler \niOS: http://apple.co/1UPw5DG \nAndroid: http://bit.ly/1YoohP8" 
    else:
        gameInfo = "Game not found"

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
