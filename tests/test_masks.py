from src.masks import get_mask_card_number, get_mask_account
import pytest

@pytest.mark.parametrize("card_num, expected", [("1234123412341234", "1234 12** **** 1234"), ("1234 1234 1234 1234", "1234 12** **** 1234"), (1234123412341234, "1234 12** **** 1234"), ("", "Некорректное значение номера карты"), ("123412341234123", "Некорректное значение номера карты"), ("abcd123412341234", "Некорректное значение номера карты")])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize("account_num, expected", [("12131412421412", "**1412"), ("231412", "**1412"), (12346523, "**6523"), ("sadsdasdds", "Некорректное значение номера счёта"), ("", "Некорректное значение номера счёта")])
def test_get_mask_account(account_num, expected):
    assert get_mask_account(account_num) == expected
