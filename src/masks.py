def get_mask_card_number(card_num: str) -> str:
    """Функция, создающая маску номера карты в формате XXXX XX** **** XXXX"""
    mask_card_num = card_num[0:4] + " " + card_num[5:7] + card_num[6:].replace(card_num[6:12], "** **** ")
    return mask_card_num


def get_mask_account(account_num: str) -> str:
    """Функция, создающая маску номера счёта в формате **XXXX"""
    mask_account = "**" + account_num[-4:]
    return mask_account
