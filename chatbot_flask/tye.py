from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Kamus respons
jawabanBot = {
    "hai": "Hai juga! Ada yang bisa saya bantu?",
    "kamu siapa": "Saya adalah chatbot WhatsApp.",
    "apa itu llm": "LLM adalah model bahasa besar seperti GPT.",
    "terima kasih": "Sama-sama!",
}

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    # Ambil pesan dari user
    pesan_user = request.form.get("Body", "").lower().strip()
    nomor_user = request.form.get("From", "")  # bisa dipakai untuk identifikasi

    # Cari balasan
    jawaban = jawabanBot.get(pesan_user, "Maaf, saya tidak mengerti.")

    # Buat dan kirim balasan
    response = MessagingResponse()
    response.message(jawaban)

    return str(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
