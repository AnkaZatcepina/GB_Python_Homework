def check_prime_imperitive(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def check_prime_declarative(number):
    gen_list = [i for i in range(2, int(number ** 0.5) + 1)]
    if number < 2:
        return False
    list_of_bool = list(map(lambda x: number % x != 0, gen_list))
    return all(list_of_bool)