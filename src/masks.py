from typing import Union

from mypy.types import NoneType


def get_mask_card_number(card_num: Union[str, int]) -> str:
    """Функция, создающая маску номера карты в формате XXXX XX** **** XXXX"""
    card_num_str = "".join((str(card_num)).split()) #приводим к строке без пробелов

    if  not len(card_num_str) == 16 or not card_num_str.isdigit(): #проверка на 16 цифр в номере
        return "Некорректное значение номера карты"
    mask_card_num = card_num_str[0:4] + " " + card_num_str[4:6] + card_num_str[6:].replace(card_num_str[6:12], "** **** ")
    return mask_card_num


def get_mask_account(account_num: Union[str, int]) -> str:
    """Функция, создающая маску номера счёта в формате **XXXX"""
    account_num_str = "".join((str(account_num)).split())
    if not account_num_str.isdigit() or len(account_num_str) < 6:
        return "Некорректное значение номера счёта"
    mask_account = "**" + account_num_str[-4:]
    return mask_account
