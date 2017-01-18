def prime_numbers(n):
    result = [2]
    current_number = 2
    if not isinstance(n, int):
        return "only Integers alowed"
    if n < 0:
        return "negative numbers are not allowed"
    if n == 0 or n == 1:
        return "Prime numbers start from 2"

    while True:
        isprime = True
        for i in result:
            if current_number % i == 0:
                isprime = False
                break
        if isprime:
            result.append(current_number)
        current_number += 1
        if current_number > n:
            break
    return result
