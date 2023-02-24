from sarufi import Sarufi

sarufi = Sarufi(username="dev.blax@gmail.com", password="sarSAR2020@")

# chatbot = sarufi.create_bot(name='blaxDog')  give id=423 name=blaxDog
# print(chatbot)

chatbot = sarufi.get_bot(423)

# chatbot.intents = {
#     'greets': ['hey', 'hello', 'hi', 'howdy', 'hola', 'greetings', 'good morning', 'good afternoon', 'good evening'], 
#     'goodbye': ['bye', 'goodbye', 'see you later', 'see you soon', 'see you', 'talk to you later', 'talk to you soon', 'talk to you'], 
#     'order_pizza': ['I need a pizza', 'I want a pizza', 'order a pizza', 'I want to order a pizza']
#     }

# print(chatbot.intents)

# chatbot.flow = {
#      'greets': {
#          'message': ['Hi, How can I help you?'],
#          'next_state': 'end'
#      },
#      'order_pizza': {
#          'message': ['Sure, How many pizzas would you like to order?'],
#          'next_state': 'number_of_pizzas'
#      },
#      'number_of_pizzas': {
#          'message': ['Sure, What would you like to have on your pizza?'],
#          'next_state': 'pizza_toppings'
#      },
#      'pizza_toppings': {
#          'message': ['Cool, Whats your address ?'],
#          'next_state': 'address'
#      },
#      'address': {
#          'message': ['Sure, What is your phone number ?'],
#          'next_state': 'phone_number'
#      },
#      'phone_number': {
#          'message': ['Your order has been placed.', 'Thank you for ordering with us.'],
#          'next_state': 'end'
#      },
#      'goodbye': {
#          'message': ['Bye', 'See you soon'],
#          'next_state': 'end'
#      }
#  }

# print(chatbot.flow)

chatbot.respond('Hey')

