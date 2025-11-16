class Emailerror(Exception):
    #Пользовательское исключение для проверки email адресов
    def __init__(self, email, message="Некорректный формат email адреса"):
        self.email = email # Сохраняем проблемный email для возможного дальнейшего анализа
        self.message = f"{message}: {email}"
        # Вызываем конструктор родительского класса Exception и передаем ему финальное сообщение об ошибке
        super().__init__(self.message)

def validate_email(email):
    # Разбиваем email по символу '@' и проверяем наличие точки в доменной части
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise Emailerror(email)
    return True

def register_user(email, username):
    #Функция регистрации пользователя с проверкой email
    try:
        # попытка волидации email
        # validate_email может выбросить EmailError
        validate_email(email)
        print(f"Пользователь {username} с email {email} успешно зарегистрирован")
    except Emailerror as e:
        print(f"Ошибка регистрации: {e}")

def send_notification(email, message):
    #Функция отправки уведомления с проверкой email
    try:
        validate_email(email)
        print(f"Уведомление '{message}' отправлено на {email}")
    except Emailerror as e:
        print(f"Ошибка отправки: {e}")


print("\nкорректный email:")
register_user("miyaby@zzz.com", "Miyabi")

print("\nнекорректный email:")
register_user("haker-email", "Haker")

print("\nотправка уведомления:")
send_notification("test@awdawda.com", "Добро пожаловать!")
send_notification("bad-email", "Важное сообщение")