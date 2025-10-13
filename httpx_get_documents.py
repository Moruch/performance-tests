import time
import httpx

# Шаг 1: Создание пользователя в системе
create_user_payload = {
    "email": f"user.{time.time()}@example.com",  # Уникальный email на основе времени
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
# Отправка запроса на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
# Получение ответа от сервера в формате JSON
create_user_response_data = create_user_response.json()
# Теперь в create_user_response_data['user']['id'] хранится ID созданного пользователя

# Шаг 2: Открытие кредитного счета для пользователя
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]  # Используем ID из предыдущего шага
}
# Отправка запроса на открытие кредитного счета
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
# Получение данных о созданном счете
open_credit_card_account_response_data = open_credit_card_account_response.json()
# Теперь в open_credit_card_account_response_data['account']['id'] хранится ID счета

# Шаг 3: Получение тарифного документа для счета
get_tariff_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/tariff-document/{open_credit_card_account_response_data['account']['id']}"
)
get_tariff_document_response_data = get_tariff_document_response.json()

print("Тарифный документ:", get_tariff_document_response_data)
print("Статус код:", get_tariff_document_response.status_code)

# Шаг 4: Получение контракта для счета
get_contract_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/{open_credit_card_account_response_data['account']['id']}"
)
get_contract_document_response_data = get_contract_document_response.json()

print("Контракт:", get_contract_document_response_data)
print("Статус код:", get_contract_document_response.status_code)