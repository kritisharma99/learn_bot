#To be installed with administrative privillages : pip3 install requests
import requests as req


last_update_id = 425321905


def sendMessage(to, text):

	to   = str(to)
	text = str(text)

	web_data = req.get("https://api.telegram.org/bot802479885:AAHoArHLvmA5EUnUYwhV5KJWO-UD_4jQrl4/sendMessage?chat_id=%s&text=%s" % (to, text) )

	if web_data.status_code == 200:

		data = web_data.json()
		#print(data["ok"], data["ok"].__class__)

		if data["ok"] == True:
			print("Message sent")
		else:
			print("Message  not sent")

def getWeather(city):

	web_data = req.get("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=201c46b4909de89d97b3ad8965c200ca" % city)

	if web_data.status_code == 200:
		try:
			data = web_data.json()

			temp = data["main"]["temp"]
			hum  = data["main"]["humidity"]

			temp, hum = str(temp), str(hum)

			return temp, hum
		except Exception as ex:
			print(ex)
			return "unable to get temp", "unable to get hum"
	else:
		return "unable", "unable"

from chapter_reader import *

def getContentfromTopic(topic):

	files = search_topic(topic)

	texts_for_message = []
	for file in files:

		texts_for_message.append( whole_chapter(file) )

	return  texts_for_message

def getContentfromSubTopic(topic):
	pass

def getContentfromContent(words):
	pass



while True:

	web_data = req.get("https://api.telegram.org/bot802479885:AAHoArHLvmA5EUnUYwhV5KJWO-UD_4jQrl4/getUpdates?offset=%s" % (last_update_id + 1) )

	status = web_data.status_code #returns http codes ike 200, 404, 301, 501, 303, 401

	if status == 200: #everything is well  so webpage returns 200 status code

		data = web_data.json()

		all_updates = data["result"]

		for single in all_updates:
			try:
				update_id  = single["update_id"]
				last_update_id = update_id

				user_id    = single["message"]["from"]["id"]
				first_name = single["message"]["from"]["first_name"]
				message    = single["message"]["text"]


				chapters_list = getContentfromTopic( message )
				if chapters_list == []:
					pass

				for chapter_text in chapters_list:
					sendMessage(user_id, chapter_text)
					#print("Message from %s saying %s" % (first_name, message) )

			except Exception as ex:

				print(ex)

	else:
		print("Error while loading webpafge : ", status)
