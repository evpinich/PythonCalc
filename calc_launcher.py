#!/usr/bin/python
import calculator

ClassCalc = calculator.Calculator()
user_expression = input("Введите выражение в формате ПРИМЕР: 23-(34*34)/(30-5)+23-(34*34)/(30-5)\n")
print("*******************************************************")
print("ОТВЕТ=", ClassCalc._calc_expression(user_expression))
print("*******************************************************")
