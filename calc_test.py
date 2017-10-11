#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import calculator
import unittest
from mock import Mock


class MyCalcTest(unittest.TestCase):
    """Test for Calculator class"""
    calc = calculator.Calculator()

    def test_exeption_brackets_error_1(self):
        result = self.calc._calc_expression("(12-23))")
        self.assertEqual(result, {'ERROR: обнаружены непарные скопки внутри выражения'})

    def test_exeption_brackets_error_2(self):
        result = self.calc._calc_expression("((232-23)")
        self.assertEqual(result, {'ERROR: обнаружены непарные скопки внутри выражения'})

    def test_unknown_sintaxis_error(self):
        result = self.calc._calc_expression("(23-20)//(-3)+23-((16*4)*(120/12))/2-2")
        self.assertEqual(result, {'ERROR: обнаружена неизвесная синтаксическая ошибка'})

    def test_dev_by_zero_error(self):
        result = self.calc._calc_expression("(23-20)/(-3)+23-((16*4)*(120/(12-3*4)))/2-2")
        self.assertEqual(result, {'ERROR: обнаружено деление на ноль внутри выражения'})

    def test_invalid_symbol_error(self):
        result = self.calc._calc_expression("(23-20)/(-3)+23-((16$4)*(120/12))/2-2")
        self.assertEqual(result, {'ERROR: обнаружен недопустимый символ внутри выражения'})

    def test_calculation_easie_lexem(self):
        result = self.calc._calc_expression("100/5-19")
        self.assertEqual(result, 1)

    def test_calculation_expression(self):
        result = self.calc._calc_expression("(23-20)/(-3)+23-((16*4)*(120/12))/2-2")
        self.assertEqual(result, -300)

    def test_method_of_calc_lexem(self):
        result = self.calc._calc_lexem("22/11+2*-1-1")
        self.assertEqual(result, -1)

    def test_method_of_find_lexem_lnside_expression(self):
        result = self.calc._find_lexem_lnside_expression("(1-(2-(4/23*-2)))")
        self.assertEqual(result, "4/23*-2")

    def test_method_of_calc_bash(self):
        result = self.calc._calc_bash("(23-20)/(-3)+23-((16*4)*(120/12))/2-2")
        self.assertEqual(result, -300.0)

    def test_method_of_save_history(self):
        result = self.calc._save_history()
        self.assertEqual(result, "file history saved successfully")

    def test_method_of_load_history(self):
        result = self.calc._load_history()
        self.assertEqual(result, True)

    def test_exit(self):
        self.calc._save_history = Mock(return_value="file history saved successfully")
        result = self.calc._calc_bash("exit")
        self.assertEqual(result, "file history saved successfully")


if __name__ == '__main__':
    unittest.main()
