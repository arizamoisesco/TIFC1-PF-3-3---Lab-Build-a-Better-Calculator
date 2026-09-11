# Instructions
Now is your opportunity to build a better calculator. Your calculator can work however you wish it to but it should be usable as a calculator.

Firstly, we're going to separate out of our *interactive* logic into the `main()` function, like so:

```
def main():
  print("Hello learners!")

if __name__=="__main__":
  main()
```

This is Python *boilerplate* code, which will only run when the program is invoked by a person. All your code should now be inside a function - either this `main()` function (where you can put things like input statements) or another function.

Automatic grading will be scored out of 8, and will test the functionality of the following functions:

* `addmultiplenumbers([num, num, ..])` - this function must exist in your program, it should take a list of numbers as input, and it should output the sum of those numbers.
* `multiplymultiplenumbers([num, num, ..])` - this function must exist in your program, it should take a list of numbers as input, and it should output the result of multiplying each number in turn with the following number.
* `isiteven(num)` - this function must exist in your program, it should take a single number as input, and it should output a boolean value - `True` if the number is an even, whole number, `False` otherwise.
* `isitaninteger(num)` - this function must exist in your program, it should take a single number as input, and it should output a boolean value - `True` if the number is an integer, `False` otherwise.

**Remember** This project will be automatically graded, and computers are very literal!

**Note:** Use the tests! There's nothing wrong with running the tests until they pass. It's not cheating!

**Note:** If you get stuck getting one function to work, try working on a different one. You might find you can solve later functions more quickly than earlier ones.

#------------------------------------------------------------------------------


InstruccionesAhora tienes la oportunidad de construir una calculadora mejor. Tu calculadora puede funcionar como tú desees, pero debe ser utilizable como tal.En primer lugar, vamos a separar nuestra lógica interactiva dentro de la función main(), de esta manera:

pythondef main():
  print("Hello learners!")

if __name__=="__main__":
  main()

Este es un código plantilla (boilerplate) de Python, que solo se ejecutará cuando una persona invoque el programa. Todo tu código debe estar ahora dentro de una función — ya sea en esta función main() (donde puedes colocar cosas como declaraciones de entrada/inputs) o en otra función.

La calificación automática se puntuará sobre 8 y evaluará la funcionalidad de las siguientes funciones:

addmultiplenumbers([num, num, ..]) - esta función debe existir en tu programa, debe recibir una lista de números como entrada y debe devolver la suma de esos números.

multiplymultiplenumbers([num, num, ..]) - esta función debe existir en tu programa, debe recibir una lista de números como entrada y debe devolver el resultado de multiplicar cada número consecutivamente con el siguiente número.

isiteven(num) - esta función debe existir en tu programa, debe recibir un solo número como entrada y debe devolver un valor booleano: True si el número es un número entero y par, False en caso contrario.

isitaninteger(num) - esta función debe existir en tu programa, debe recibir un solo número como entrada y debe devolver un valor booleano: True si el número es un entero, False en caso contrario.

Recuerda: ¡Este proyecto se calificará automáticamente y las computadoras son muy literales!Nota: ¡Usa las pruebas (tests)! No hay nada malo en ejecutar las pruebas hasta que pasen. ¡No es hacer trampa!Nota: Si te quedas atascado intentando hacer funcionar una función, intenta trabajar en una diferente. Es posible que descubras que puedes resolver las funciones posteriores más rápido que las primeras.Si tienes dudas con lo que significa alguna regla técnica (como lo de "número entero y par" o la multiplicación de listas), dime y lo revisamos con ejemplos detallados.