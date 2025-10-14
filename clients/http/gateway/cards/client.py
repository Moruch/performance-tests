from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания виртуальной карты.
    """
    accountId: str
    type: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания физической карты.
    """
    accountId: str
    type: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    Предоставляет методы для выпуска виртуальных и физических карт.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Выпуск виртуальной карты для указанного счета.

        :param request: Словарь с данными для создания виртуальной карты.
                        Должен содержать:
                        - accountId: идентификатор счета
                        - type: тип карты
        :return: Ответ от сервера с данными созданной виртуальной карты.
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Выпуск физической карты для указанного счета.

        :param request: Словарь с данными для создания физической карты.
                        Должен содержать:
                        - accountId: идентификатор счета
                        - type: тип карты
        :return: Ответ от сервера с данными созданной физической карты.
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)