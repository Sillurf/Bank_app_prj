from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_num: str) -> str:
    """Функция принимает номер карты или счёта и выводит их с соответствующей маской."""
    card_or_account_num_list = card_or_account_num.split()

    if "Счет" in card_or_account_num:
        masked_account = "Счет " + get_mask_account(card_or_account_num_list[-1])
        return masked_account
    else:
        card_num = card_or_account_num_list[-1]
        card_or_account_num_list[-1] = get_mask_card_number(card_num)
        masked_card_number = " ".join(card_or_account_num_list)
        return masked_card_number


def get_date(date_in: str) -> str:
    """функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате
    "11.03.2024"."""
    date_out = date_in[8:10] + "." + date_in[5:7] + "." + date_in[0:4]
    return date_out
