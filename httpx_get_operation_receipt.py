import time
import httpx

# Шаг 1 создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2 создать кредитный счёт для пользователя
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()
# Извлекаем необходимые ID из ответа
account_id = open_credit_card_account_response_data["account"]["id"]
card_id = open_credit_card_account_response_data["account"]["cards"][0]["id"]  # Берем первую карту из массива
print("Счёт пользователя:", account_id)
print("Карт ИД:", card_id )

# Шаг 3 Совершить операцию покупки (purchase)
make_purchase_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": card_id,
    "accountId": account_id
}
make_purchase_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_payload
)
make_purchase_response_data = make_purchase_response.json()
operation_id = make_purchase_response_data["operation"]["id"]
print(f"Операция с ID:", operation_id)
print("Статус код", make_purchase_response.status_code)

# Шаг 4 получение чека по операции
get_receipt_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}"
)
receipt_data = get_receipt_response.json()
print("Чек по операции:", receipt_data)
print("Статус код:", get_receipt_response.status_code)
