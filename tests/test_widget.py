from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize(
    "card_or_account_num, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),                            # Стандартный счет
        ("Фирма карты 1234123412341234", "Фирма карты 1234 12** **** 1234"),     # Стандартная карта
        ("", "Некорректное значение"),                                           # Пустая строка
        ("Счет  Иванова", "Некорректное значение номера счёта")                  # Случайное значение номера счета
    ]
)
def test_mask_account_card(card_or_account_num, expected):
    assert mask_account_card(card_or_account_num) == expected

@pytest.mark.parametrize(
    "date_in, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),                 # Стандартный ввод
        ("", "Некорректный формат даты"),                             # Пустая строка
        ("2023.12.12", "12.12.2023"),                                 # Дата без времени и не через дефис
        ("2021-13-01T02:26:18.671407", "Некорректный формат даты"),   # 13й месяц
        ("2021-10-32T02:26:18.671407", "Некорректный формат даты"),   # 32ой день
        ("sdasdsadsdsadsad", "Некорректный формат даты")              # Случайная строка
    ]
)
def test_get_date(date_in, expected):
    assert get_date(date_in) == expected
