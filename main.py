def addmultiplenumbers(numbers):
    
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
   
    if not isinstance(num, (int, float)) or num % 1 != 0:
        return False
    return int(num) % 2 == 0

def isitaninteger(num):
    
    if isinstance(num, bool):
        return False
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

def main():
    print("Hello learners!")
    
    lista_ejemplo = [2, 3, 4]
    print(f"Suma de {lista_ejemplo}: {addmultiplenumbers(lista_ejemplo)}")
    print(f"Multiplicación de {lista_ejemplo}: {multiplymultiplenumbers(lista_ejemplo)}")
    print(f"¿Es 4 par?: {isiteven(4)}")
    print(f"¿Es 4.5 un entero?: {isitaninteger(4.5)}")

if __name__ == "__main__":
    main()
