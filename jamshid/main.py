def get_otnosheniye(age, weight):
    return age/weight

def get_conclusion(weight, q_of_fr):
    if q_of_fr >= weight:
        return f"Молодец,твой вес {weight} кг, а количество друзей {q_of_fr}"
    else:
        return f"У тебя всего лишь {q_of_fr} друзей, потому что ты жирный, {weight} кг"
