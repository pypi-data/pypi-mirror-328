import math
import requests
from bs4 import BeautifulSoup


def clean_html(text: str) -> str:
    """
    Удаляет HTML-теги из текста.

    :param text: Строка с HTML-разметкой.
    :return: Текст без HTML-тегов.
    """
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def predict(texts, batch_size: int = 15, url: str = "https://xyandex.pythonanywhere.com/predict_sentiments",
            verbose: bool = False):
    """
    Отправляет батчами запросы на сервер для определения сентимента каждого текста.

    :param texts: Список строк (тексты, возможно с HTML-разметкой).
    :param batch_size: Количество текстов в одном запросе (по умолчанию 15).
    :param url: URL сервера для предсказания сентимента.
    :param verbose: Если True, выводит сообщения о прогрессе.
    :return: Список словарей вида {"text": <очищенный текст>, "sentiment": <результат>} для каждого текста.
    """
    # Очищаем тексты от HTML-тегов
    cleaned_texts = [clean_html(str(text)) for text in texts]

    results = [None] * len(cleaned_texts)
    total_batches = math.ceil(len(cleaned_texts) / batch_size)

    if verbose:
        print(f"Всего записей: {len(cleaned_texts)}, батчей: {total_batches}")

    for batch_num in range(total_batches):
        start = batch_num * batch_size
        end = start + batch_size
        batch_texts = cleaned_texts[start:end]

        # Формируем payload для запроса
        payload = [{"text": text} for text in batch_texts]

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            res_data = response.json()
        except Exception as e:
            if verbose:
                print(f"Ошибка запроса для батча {batch_num + 1}: {e}")
            for i in range(len(batch_texts)):
                results[start + i] = "error"
            continue

        if isinstance(res_data, list):
            for i, item in enumerate(res_data):
                if isinstance(item, dict) and "sentiment" in item:
                    results[start + i] = item["sentiment"]
                else:
                    results[start + i] = "error"
        else:
            if verbose:
                print(f"Неожиданный формат ответа в батче {batch_num + 1}: {res_data}")
            for i in range(len(batch_texts)):
                results[start + i] = "error"

        if verbose:
            print(f"Обработан батч {batch_num + 1}/{total_batches}")

    # Формируем итоговый список результатов
    output = []
    for text, sentiment in zip(cleaned_texts, results):
        output.append({"text": text, "sentiment": sentiment})

    return output
