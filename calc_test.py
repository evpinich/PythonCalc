#!/usr/bin/python
import calculator
import unittest


class MyCalcTest(unittest.TestCase):
    """Test for Calculator class"""
    def test_exeption_brackets_error_1(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("(12-23))")
        self.assertEqual(result, {'ERROR: обнаружены непарные скопки внутри выражения'})

    def test_exeption_brackets_error_2(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("((232-23)")
        self.assertEqual(result, {'ERROR: обнаружены непарные скопки внутри выражения'})

    def test_unknown_sintaxis_error(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("(23-20)//(-3)+23-((16*4)*(120/12))/2-2")
        self.assertEqual(result, {'ERROR: обнаружена неизвесная синтаксическая ошибка'})

    def test_dev_by_zero_error(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("(23-20)/(-3)+23-((16*4)*(120/(12-3*4)))/2-2")
        self.assertEqual(result, {'ERROR: обнаружено деление на ноль внутри выражения'})

    def test_invalid_symbol_error(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("(23-20)/(-3)+23-((16$4)*(120/12))/2-2")
        self.assertEqual(result, {'ERROR: обнаружен недопустимый символ внутри выражения'})

    def test_calculation_easie_lexem(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("100/5-19")
        self.assertEqual(result, 1)

    def test_calculation_expression(self):
        calc = calculator.Calculator()
        result = calc._calc_expression("(23-20)/(-3)+23-((16*4)*(120/12))/2-2")
        self.assertEqual(result, -300)


if __name__ == '__main__':
    unittest.main()
