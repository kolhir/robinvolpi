from flask import Flask, render_template, request
from config import Confiruration
import json
import vk_api

from somewhere import access_token
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

app = Flask(__name__)
app.config.from_object(Confiruration)

import time
@app.route("/")
def test():
    return render_template("index.html")

@app.route("/bronirovanie", methods = ['POST'])
def ajax_bron():
	# send_message()
	vk.messages.send( #Отправляем сообщение
                    user_id=134592780,
                    message=("Имя: " + (request.form['name']) + 
                    	     "\nТелефон: " +(request.form['phone'])+
                    	     "\nКомментарий: " +(request.form['comment'])),
                    random_id = int(time.time())
		)
	vk.messages.send( #Отправляем сообщение
                    user_id=59921086,
                    message=("Имя: " + (request.form['name']) + 
                    	     "\nТелефон: " +(request.form['phone'])+
                    	     "\nКомментарий: " +(request.form['comment'])),
                    random_id = int(time.time())
		)
	
	print(request.form['name'], request.form['phone'])
	return json.dumps(200)
# from users import models, views
