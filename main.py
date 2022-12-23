import iskander, jamshid
from iskander import *
from jamshid import get_otnosheniye, get_conclusion

name = get_name()
weight = get_weight()
qoff = get_koldr()
age = get_age()

print("Hellooooo", name)
print("Interesting that", get_otnosheniye(age, weight))
print(get_conclusion(weight, qoff))

