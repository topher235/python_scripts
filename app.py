# Links used:
# https://github.com/danieldiekmeier/memegenerator/blob/master/memegenerator.py
# http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
# https://www.reddit.com/r/ProgrammerHumor/comments/7zvz8a/my_coworkers_dont_seem_to_appreciate_my_python/

import os
import json
import requests
import random

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from flask import Flask, request

app = Flask(__name__)

def send_to_groupme(memeage):
    ''' send meme to discord room '''
    url = 'https://api.groupme.com/v3/bots/post' 
    data = {
    	'attachments': [{
    		"type" : "image",
    		"url"  : memeage,
    	}],
    	'bot_id': '25a40dcb12802694af0e84f407', #os.getenv('GROUPME_BOT_ID'),
    	'text' : '',
    }
    headers = {'Content-Type': 'application/json'}
    req = requests.post(url, json.dumps(data), headers=headers)
    print(req.status_code)

def upload_meme_to_groupme():
	imageFile = "marked_image.jpg"

	# send image
	url = 'https://image.groupme.com/pictures'
	data = open(imageFile, 'rb').read() #{'file': open(imageFile, 'rb')}
	headers = {
		'X-Access-Token': '2hqQ1HFkIVuVWfMaHW6T3hr4msxreGVLCwhLganK',
		'Content-Type': 'image/jpeg'
	}
	r = requests.post(url, data=data, headers=headers)
	imageurl = r.json()['payload']['url']
	return imageurl

def generate_meme(message):
	# open blank meme image and get size
	imageFile = "meme.png"
	im = Image.open(imageFile)
	imgSize = im.size

	# font size
	fontSize = int(imgSize[1]/2)
	font = ImageFont.load_default()
	font.size = fontSize
	bottomTextSize = font.getsize(message)

	# find bottom centered position for bottom text
	bottomTextPositionX = (imgSize[0]/2) - (bottomTextSize[0]/2)
	bottomTextPositionY = imgSize[1] - bottomTextSize[1]
	bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

	# draw the text on the image
	draw = ImageDraw.Draw(im)
	draw.text(bottomTextPosition, message, (255, 255, 255), font=font)
	draw = ImageDraw.Draw(im)

	# save the new image
	im.save("marked_image.jpg")

def generate_message(msg):
	# create the mockery message
    message = ' '.join(''.join(random.choice([c.upper, c.lower])() for c in word) for word in msg)[:200]
    return message

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()

	if data['name'] != 'Mock':
		message = data['text']
		message = generate_message(message)
		generate_meme(message)
		memeage = upload_meme_to_groupme()
		send_to_groupme(memeage)

	return "OK", 200