# Импортируем библиотеку httpx для выполнения HTTP-запросов (аналог requests)
import httpx
# Импортируем библиотеку time для работы с временными метками
import time

# Создаем данные (payload) для запроса на создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",  # Генерируем уникальный email используя текущее время
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Отправляем POST-запрос на сервер для создания нового пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
# Преобразуем ответ от сервера из JSON формата
create_user_response_data = create_user_response.json()

# Выводим в консоль полный ответ от сервера после создания пользователя
print("Create user response:", create_user_response_data)
# Выводим статус код HTTP ответа (200 - OK, 201 - Created, 400 - Bad Request, etc.)
print("Status Code:", create_user_response.status_code)

# Отправляем GET-запрос для получения данных созданного пользователя
# В URL подставляем ID пользователя из предыдущего ответа
get_user_response = httpx.get(
    f"http://localhost:8003/api/v1/users/{create_user_response_data['user']['id']}"
)

# Преобразуем ответ от сервера (данные пользователя) из JSON в Python словарь
get_user_response_data = get_user_response.json()

# Выводим в консоль данные полученного пользователя
print("Get user response:", get_user_response_data)
# Выводим статус код HTTP ответа для GET-запроса
print("Status Code:", get_user_response.status_code)
