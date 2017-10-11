#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


class Calculator(object):
    """"Class of calculating text expression  """
    HISTORY_NAME_FILE_DIRECTION = 'history.csv'
    _history_stack = []
    _file_history_was_loaded = False
    _launcher_done_calculations = False
    _error_state = False
    _error_masage = set()

    def _start(self):
        if not self._file_history_was_loaded:
            if self._load_history():
                self._file_history_was_loaded = True
                print("history_file_was_loaded_successful")
        while not self._launcher_done_calculations:
            self._calc_bash(input(">"))
        self._launcher_done_calculations = False
        return

    def _save_history(self):
        with open(self.HISTORY_NAME_FILE_DIRECTION, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for item in self._history_stack:
                writer.writerow([item])
        return True

    def _load_history(self):
        history_from_file = []
        try:
            my_file = open(self.HISTORY_NAME_FILE_DIRECTION, 'r')
            reader = csv.reader(my_file)
            for row in reader:
                for index in row:
                    history_from_file.append(index)
        except FileNotFoundError:
            history_from_file = []
        self._history_stack = history_from_file
        return True

    def _calc_bash(self, comand_line):
        counter = len(self._history_stack) + 1

        if comand_line == "exit":
            self._launcher_done_calculations = True
            return self._save_history()

        if comand_line == "history":
            for i in self._history_stack:
                print(i)
            return

        result = self._calc_expression(comand_line)
        print("RESULT =", result)

        if counter > 10:
            self._history_stack.append(str(result))
            self._history_stack.pop(0)
        else:
            self._history_stack.append(str(result))
        print("------------------------------------------------------------")
        return result

    def _calc_expression(self, expression):
        """"Method for calculating expression  """
        self._error_status = False
        self._error_masage = set()
        proxy_expression = expression.strip(" \t\n")
        count_left_brackets = proxy_expression.count("(")
        count_right_brackets = proxy_expression.count(")")
        if count_left_brackets != count_right_brackets:
            self._error_status = True
            self._error_masage.add("ERROR: обнаружены непарные скопки внутри выражения")
        else:
            try:
                while "(" in proxy_expression:
                    lexem = "(" + self._find_lexem_lnside_expression(proxy_expression) + ")"
                    result_of_lexem = str(self._calc_lexem(lexem))
                    proxy_expression = proxy_expression.replace(lexem, result_of_lexem)
                result = self._calc_lexem(proxy_expression)
            except BaseException:
                self._error_status = True
                self._error_masage.add("ERROR: обнаружена неизвесная синтаксическая ошибка")
        if (self._error_status):
            return self._error_masage
        return result

    def _calc_lexem(self, lexem):
        """"Method that doing calculation of simple lexem  ------------"""
        list_element = []
        symbol_bufer = ""
        for symbol in lexem:
            if symbol not in "()-+*/.1234567890":
                self._error_status = True
                self._error_masage.add("ERROR: обнаружен недопустимый символ внутри выражения")
                return 0
            if (len(symbol_bufer) > 0) and (symbol in "+-"):
                list_element.append(symbol_bufer)
                symbol_bufer = ""
            if (symbol in "*/"):
                list_element.append(symbol_bufer)
                list_element.append(symbol)
                symbol_bufer = ""
            if symbol in "-+1234567890.":
                symbol_bufer += symbol
        list_element.append(symbol_bufer)
        for i in range(len(list_element) - 1):
            if (i > 0) and (list_element[i] == "*")and (len(list_element)):
                list_element[i + 1] = str(float(list_element[i - 1]) * float(list_element[i + 1]))
                list_element[i - 1] = "0"
                list_element[i] = "0"
            if (i > 0) and (list_element[i] == "/")and (len(list_element)):
                try:
                    list_element[i + 1] = str(float(list_element[i - 1]) / float(list_element[i + 1]))
                except ZeroDivisionError:
                    self._error_status = True
                    self._error_masage.add("ERROR: обнаружено деление на ноль внутри выражения")
                list_element[i - 1] = "0"
                list_element[i] = "0"
        ansver = 0

        for i in list_element:
            ansver += float(i)
        return ansver

    def _find_lexem_lnside_expression(self, expression):
        """"Method that extractoring simple lexem from expression  --------"""
        counter, lexem = 0, ""
        begin_index_lexem, end_index_lexem, lexem_field_flag = 0, 0, False
        for i in expression:
            counter += 1
            if (i == "("):
                lexem_field_flag = True
                begin_index_lexem = counter
            elif lexem_field_flag and (i == ")"):
                lexem_field_flag = False
                end_index_lexem = counter - 1
                lexem = expression[begin_index_lexem:end_index_lexem]
                break
        return lexem
