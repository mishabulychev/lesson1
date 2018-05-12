user_info = {"first name": "Misha" , "last name": "Bulychev"}
print (user_info ["first name"])
first_name = input("Введите ваше имя: ")
user_info ["first name"] = first_name
last_name = input("Введите вашу фамилию: ")
user_info ["last name"] = last_name
print(user_info)


phrase = get_summ ("Hello", "World")
print(phrase.upper())