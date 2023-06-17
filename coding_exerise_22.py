def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It is a prime numbeer")
    else:
        print(f"{number} is not a prime number")



number=int(input("Enter a number:\n"))
prime_checker(137)
