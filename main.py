# Домашняя работа по уроку "Способы вызова функции"

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка корректности e-mail
    valid_domains = [".com", ".ru", ".net"]
    if "@" not in recipient or not any(recipient.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if "@" not in sender or not any(sender.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Пример выполнения функции с вымышленными адресами
send_email('Это сообщение для проверки связи', 'example1@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'example2@mail.ru', sender='example3@gmail.com')
send_email('Пожалуйста, исправьте задание', 'example4@mail.ru', sender='example5@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'example6@mail.ru', sender='example6@mail.ru')