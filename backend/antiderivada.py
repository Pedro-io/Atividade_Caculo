import sympy as sp 
from sympy import *
from IPython.display import display, Math

# Define a variável simbólica x
x = symbols('x')

# Define a expressão a ser integrada
print("digite a expressão a ser integrada")
expr = input()
# Realiza a integração indefinida da expressão
integral = integrate(expr, x)

# Exibe a expressão original e a integral indefinida com símbolos matemáticos
display(Math(r'Expressão\ original:\ {}\\'.format(latex(expr))))
display(Math(r'Integral\ indefinida:\ {}\\'.format(latex(integral))))

# Mostra os passos realizados para a integração
print("\nPassos realizados:\n")
for step in integral.lseries():
    display(Math(r'-\ {}\\'.format(latex(step))))