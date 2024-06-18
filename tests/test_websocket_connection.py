import pytest
import websockets
import json


@pytest.mark.asyncio
async def test_websocket_connection():
    # GIVEN
    uri = "wss://www.onetwotrip.com/_bus/ws/run/search?startGeoId=16&endGeoId=100&date=2024-06-18&adults=1&children=0"
    headers = {
        "Origin": "https://www.onetwotrip.com"
    }

    async with websockets.connect(uri, extra_headers=headers) as websocket:
        # WHEN
        # Отправка сообщения
        await websocket.send("ok")

        # Ожидание и получение ответа
        response = await websocket.recv()

        # Десериализация JSON-ответа в словарь
        response_dict = json.loads(response)

        # THEN
        # Проверяем, что в словаре есть ключ "type" со значением "calendar"
        assert response_dict.get("type") == "calendar"
