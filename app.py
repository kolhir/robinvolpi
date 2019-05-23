from flask import Flask, render_template, request
from config import Confiruration
import json
import vk_api

access_token = "21e89565a45b859eff92a63865fd15bfa0bfb72987ea7b57fcd17762cdd1086993922e4eddab0df79451b"
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
	print(request.form['name'], request.form['phone'])
	return json.dumps(200)
# from users import models, views
