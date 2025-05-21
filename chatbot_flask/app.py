from flask import Flask, request, jsonify

app = Flask(__name__)

jawabanBot = { 
  "hai": "Hai juga! Ada yang bisa saya bantu?",
  "kamu siapa": "Saya adalah chatbot Flask buatan manusia.",
  "apa itu llm": "LLM adalah model bahasa besar seperti GPT.",
  "terima kasih": "Sama-sama!",
}

@app.route("/webhook", methods=["POST"])
def chatbotWebhook():
  data = request.json
  userMessage = data.get("message", "").lower().strip()

  reply = jawabanBot.get(userMessage, "Maaf, saya tidak mengerti.")

  return jsonify({"message": reply})

if __name__ == '__main__':
  app.run(port=5000, debug=True)
