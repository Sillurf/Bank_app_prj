def filter_by_state(id_state_date_list: list[dict], state: str ='EXECUTED') -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state.
Возвращает новый список словарей, содержащий только те словари, у которых ключ
state
 соответствует указанному значению."""
    filtered_by_state_list = []
    for id_state_date in id_state_date_list:
        if id_state_date.get("state") == state:
            filtered_by_state_list.append(id_state_date)
    return filtered_by_state_list
