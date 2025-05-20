def chatbot ():
  print("Hallo saya bot buatan rian, silahkan tanya sesuatu")

  jawaban = { 
    "hai" : "hai juga, apa kabar?",
    "hallo": "hallo juga",
    "kamu siapa": "saya chat bot"
  }

  while True:
    user_input = input(">").lower().strip()

    if user_input == "jak wo":
      print("sampai jumpa gam")
      break

    if user_input in jawaban:
      print(f"Bot: {jawaban[user_input]}")
    else:
      print("Maaf, saya tidak mengerti")

chatbot()