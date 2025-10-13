# Импортируем библиотеку time для работы с временными метками
import time
# Импортируем библиотеку httpx для выполнения HTTP-запросов
import httpx

# Шаг 1. Создание пользователя
# Формируем данные (payload) для создания нового пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",  # Генерируем уникальный email с временной меткой
    "lastName": "string",     # Фамилия пользователя
    "firstName": "string",    # Имя пользователя
    "middleName": "string",   # Отчество пользователя
    "phoneNumber": "string"   # Номер телефона пользователя
}

# Отправляем POST-запрос на сервер для создания пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)

# Преобразуем ответ сервера из JSON формата в Python словарь
create_user_response_data = create_user_response.json()

# Шаг 2. Открытие дебетового счёта
# Формируем данные для открытия дебетового счета
# Используем ID пользователя, полученный на предыдущем шаге
open_debit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]  # Берем ID созданного пользователя
}

# Отправляем POST-запрос для открытия дебетового счета
open_debit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-debit-card-account",
    json=open_debit_card_account_payload
)

# Преобразуем ответ сервера из JSON формата в Python словарь
open_debit_card_account_response_data = open_debit_card_account_response.json()

# Шаг 3. Выпуск виртуальной карты
# Формируем данные для выпуска виртуальной карты
# Используем ID пользователя и ID счета, полученные на предыдущих шагах
issue_virtual_card_payload = {
    "userId": create_user_response_data["user"]["id"],     # ID пользователя из первого шага
    "accountId": open_debit_card_account_response_data["account"]["id"]  # ID счета из второго шага
}

# Отправляем POST-запрос для выпуска виртуальной карты
# URL: http://localhost:8003/api/v1/cards/issue-virtual-card
issue_virtual_card_response = httpx.post(
    "http://localhost:8003/api/v1/cards/issue-virtual-card",
    json=issue_virtual_card_payload
)

# Преобразуем ответ сервера из JSON формата в Python словарь
issue_virtual_card_response_data = issue_virtual_card_response.json()

# Выводим результат в консоль
print("Issue virtual card response:", issue_virtual_card_response_data)  # JSON-ответ с данными карты
print("Issue virtual card status code:", issue_virtual_card_response.status_code)  # Статус код HTTP ответа