from flask import Flask, request,jsonify #import somehings to run our server

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def hello_bot():
	return "Welcome, Abubakar to Data Science and Machine Learning "

qa={
	"ukimwi ni nini" : "Upungufu wa kings mwilini",
	"vvu ni nini" : "Virusi vya ukimwi  ni virusi vinavyosambaza ugonjwa",
	"je ukimwi ni nini":"Ukimwi ni Maradhi yanayosababisha upungufu wa kinga Mwilini",
	"je ukimwi husabishwa na nini":"Ukimwi husbabishwa na mambo yanayopelekea kukutana na damu ya muathirika",
	"je ni ipi dawa ya kimwi":"Ukimwi hauna dawa, ila kuna dawa za kuuongezea Mwili nguvu",
	"je ni zipi njia za kujikinga na ukimwi":"Utajikinga na ukimwi kwa kuepuka njia zote zinazopelekea kukutana na damu ya muathirika"
}


@app.route("/ask", methods=["POST","GET"])
def ask():
	#return "Virusi vya Ukimwi ni virusi vinavyosambaza ugonjwa"
	question=request.get_json()["question"].lower().replace("?","").strip()
	return qa[question]
	#print(request.get_json())
	