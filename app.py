import os
from flask import Flask, redirect, render_template
from werkzeug.routing import BaseConverter
app = Flask(__name__)

class RegexConverter(BaseConverter):
	def __init__(self,url_map, *items):
		super(RegexConverter, self).__init__(url_map)
		self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

#On Load Function to show landing page
@app.route("/")
def welcome():
	return render_template('index.html')



#Below route rules defined to redirect urls ending with Integer such as /1920

@app.route("/<int:param>")
@app.route("/<int:param>/")
def goto_challenge(param):
	return redirect("http://www.cloudspokes.com/challenges/%d" % param)


#Below route rule defined to redirect Urls ending with Integer such as /asdjad/asdh/12jh/1920
@app.route("/<regex('.*\/([0-9]+)'):param>/")
def go_to_challenge(param):
	param = param.split("/")
	return redirect("http://www.cloudspokes.com/challenges/%s" % param[len(param)-1])

#Below two route rules defined to redirect /String 
@app.route("/<param>")
@app.route("/<param>/")
def go_to_member(param):
	return redirect("http://www.cloudspokes.com/members/%s" % param)


#Below route rule defined to redirect Urls ending with String such /subPath/path/rome
@app.route("/<regex('.*\/([a-zA-Z0-9_]+)'):param>/")
def goto_member(param):
	param = param.split("/")
	return redirect("http://www.cloudspokes.com/members/%s" % param[len(param)-1])


if __name__=="__main__":
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0',port=port)
