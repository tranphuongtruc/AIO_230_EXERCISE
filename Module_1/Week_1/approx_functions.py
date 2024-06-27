
def factorial(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer


def approx_sin(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i + 1)
        answer += (-1)**i * ((x ** (2 * i + 1)) / giai_thua)
    print(answer)
# approx_sin(x = 3.14, n = 10)


def approx_cos(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i)
        answer += (-1)**i * ((x ** (2 * i)) / giai_thua)
    print(answer)
# approx_cos(x =3.14 , n =10)


def approx_sinh(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i + 1)
        answer += (x ** (2 * i + 1)) / giai_thua
    print(answer)
# approx_sinh(x =3.14 , n =10)


def approx_cosh(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i)
        answer += (x ** (2 * i)) / giai_thua
    print(answer)
# approx_cosh(x =3.14 , n =10)