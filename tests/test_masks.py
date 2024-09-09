import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("1234123412341234", "1234 12** **** 1234"),                  # Стандартный ввод
        ("1234 1234 1234 1234", "1234 12** **** 1234"),               # Ввод через пробелы
        (1234123412341234, "1234 12** **** 1234"),                    # int значение
        ("", "Некорректное значение номера карты"),                   # Пустая строка
        ("123412341234123", "Некорректное значение номера карты"),    # Длина меньше 16
        ("abcd123412341234", "Некорректное значение номера карты"),   # Строка содержит буквы
    ],
)
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "account_num, expected",
    [
        ("73654108430135874305", "**4305"),                              # Стандартный ввод
        ("231412", "**1412"),                                            # Короче стандартного
        ("1212 1343 1323", "**1323"),                                    # Через пробелы
        (12346523, "**6523"),                                            # int значение
        ("sadsdasdds", "Некорректное значение номера счёта"),            # буквы
        ("", "Некорректное значение номера счёта"),                      # Пустая строка
    ],
)
def test_get_mask_account(account_num, expected):
    assert get_mask_account(account_num) == expected
