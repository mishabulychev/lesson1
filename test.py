user = {"Mike": {"city": "Moscow" , "temperature": "24", "wind":           "восточный"} ,
        "Alex" : {"city": "Smolensk" , "temperature": "28", "wind": "западный"}, 
        "Frank" : {"city": "Kazan" , "temperature": "21", "wind": "северо-западный"}}
name = input("Введите ваше имя: ")
print ("Привет, " + name)
print(user.get (name))