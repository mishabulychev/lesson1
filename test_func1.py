def get_answer(question, answers):
    return answers.get(question.lower(), "Не найдено")
answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
question=input("Введите что-либо: ")
print(get_answer(question, answers))
    