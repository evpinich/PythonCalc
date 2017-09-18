#!/usr/bin/env python
# -*- coding: utf-8 -*-


import calculator


def _save_history(stack_for_saving):
    file = open("hystory.txt", "w+", encoding='utf-8')
    for i in stack_for_saving:
        file.writelines(i + "\n")
    file.close
    return ""


def _load_history():
    hystory_from_file = []
    file = open("hystory.txt", "r", encoding='utf-8')
    if file:
        for line in file:
            line = line.rstrip('\n')
            hystory_from_file.append(line)
    file.close
    return hystory_from_file


stack = _load_history()
counter = len(stack)
ClassCalc = calculator.Calculator()
print("Введите выражение в формате ПРИМЕР: 23-(34*34)/(30-5)+23-(34*34)/(30-5)")
print("------------------------------------------------------------")
while True:
    user_expression = input("> ")
    counter += 1
    if user_expression == "exit":
        _save_history(stack)
        break
    if user_expression == "history":
        for i in stack:
            print(i)
        print("------------------------------------------------------------")
        continue
    result = str(ClassCalc._calc_expression(user_expression))
    print("ОТВЕТ =", result)

    if counter > 10:
        stack.append(result)
        stack.pop(0)
    else:
        stack.append(result)
    print("------------------------------------------------------------")
