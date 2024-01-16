import os
import unittest
from unittest.mock import patch

from course_section.course_lesson.programming_task.invisible_main import say_hello
from course_section.course_lesson.programming_task.main import invoke_say_hello


class TestAddFunction(unittest.TestCase):
    test_cases = [2, 4, 20, 1900, 400, 2004, 2000, 2001]

    @staticmethod
    def correct_invoke_say_bye(how_many_times: int):
        return os.linesep.join([say_hello() for _ in range(how_many_times)])

    @patch('builtins.print')
    def test_parametrized(self, mock_print):
        for how_many_times in self.test_cases:
            with self.subTest(how_many_times):
                correct_solution = self.correct_invoke_say_bye(how_many_times)
                invoke_say_hello(how_many_times)
                mock_print.assert_called_once_with(correct_solution)
                mock_print.reset_mock()
