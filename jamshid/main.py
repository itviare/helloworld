def get_otnosheniye(age: int, weight: int) -> int:
    return age / weight


def get_conclusion(weight: int, q_of_fr: int) -> str:
    if q_of_fr >= weight:
        return f"Молодец,твой вес {weight} кг, а количество друзей {q_of_fr}"
    else:
        return f"У тебя всего лишь {q_of_fr} друзей, потому что ты жирный, {weight} кг"
