def addmultiplenumbers(numeros):
  total = 0
  for numero in numeros:
    total = total + numero
  return total


def multiplymultiplenumbers(numeros):
  resultado = 1
  for numero in numeros:
    resultado = resultado * numero
  return resultado


def isiteven(num):
  if num % 2 == 0:
    return True
  else:
    return False


def isitaninteger(num):
  if num == int(num):
    return True
  else:
    return False


def pedir_numeros():
  numeros = []
  print("Escriba los números uno por uno. Cuando termine, escriba 'listo'.")
  while True:
    entrada = input("Número: ")
    if entrada == "listo":
      break
    try:
      numeros.append(float(entrada))
    except ValueError:
      print("Eso no es un número, intente de nuevo.")
  return numeros


def main():
  print("¡Bienvenido a la calculadora!")

  while True:
    print("\n¿Qué desea hacer?")
    print("1. Sumar varios números")
    print("2. Multiplicar varios números")
    print("3. Saber si un número es par")
    print("4. Saber si un número es entero")
    print("5. Salir")
    opcion = input("Escriba el número de la opción: ")

    if opcion == "1":
      numeros = pedir_numeros()
      print("El resultado de la suma es:", addmultiplenumbers(numeros))

    elif opcion == "2":
      numeros = pedir_numeros()
      print("El resultado de la multiplicación es:", multiplymultiplenumbers(numeros))

    elif opcion == "3":
      try:
        numero = float(input("Escriba un número: "))
        if isiteven(numero):
          print("Sí, el número es par.")
        else:
          print("No, el número no es par.")
      except ValueError:
        print("Eso no es un número.")

    elif opcion == "4":
      try:
        numero = float(input("Escriba un número: "))
        if isitaninteger(numero):
          print("Sí, el número es entero.")
        else:
          print("No, el número no es entero.")
      except ValueError:
        print("Eso no es un número.")

    elif opcion == "5":
      print("Hasta luego!")
      break

    else:
      print("Opción no válida.")


if __name__=="__main__":
  main()
