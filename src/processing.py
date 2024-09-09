def filter_by_state(id_state_date_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    filtered_by_state_list = []
    for id_state_date in id_state_date_list:
        if id_state_date.get("state") == state:
            filtered_by_state_list.append(id_state_date)
    return filtered_by_state_list


def sort_by_date(id_state_date_list: list[dict], sort_is_reversed: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр порядока сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате"""
    sorted_by_date_list = sorted(id_state_date_list, key=lambda x: x["date"], reverse=sort_is_reversed)
    return sorted_by_date_list
