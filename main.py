base = input('Base:')
exp = input('Expoente:')

from dispatcher import are_integers

if not are_integers(base, exp):
    exit()
else:
    base = int(base)
    exp = int(exp)

def positive_potence_tail_head(accumulator = 1, numbers=[]):
    head, *tail = numbers
    accumulator = head * accumulator
    if len(tail) > 0:
        accumulator = positive_potence_tail_head(accumulator, tail)
    return accumulator
    
def negative_potence_tail_head(accumulator = 1, numbers=[]):
    head, *tail = numbers
    accumulator = 1 / head * accumulator
    if len(tail) > 0:
        accumulator = negative_potence_tail_head(accumulator, tail)
    return accumulator
    
def potence(base, exp):
    numbers = [base]* abs(exp)
    if exp > 0:
        return positive_potence_tail_head(1, numbers)
    if exp < 0:
        return negative_potence_tail_head(1, numbers)
    return 0

print(
    f"{base} elevado a {exp} é igual à {potence(base, exp)}"
)

