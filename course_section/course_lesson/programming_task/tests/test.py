import os
from unittest.mock import patch

import pytest

from course_section.course_lesson.programming_task.invisible_main import say_hello
from course_section.course_lesson.programming_task.main import invoke_say_hello


def correct_invoke_say_bye(how_many_times: int):
    return os.linesep.join([say_hello() for _ in range(how_many_times)])


@patch('builtins.print')
@pytest.mark.parametrize("how_many_times", [2, 4, 20, 1900, 400, 2004, 2000, 2001])
def test_invoke_say_buy(mock_print, how_many_times: int):
    correct_solution = correct_invoke_say_bye(how_many_times)
    invoke_say_hello(how_many_times)
    mock_print.assert_called_once_with(correct_solution)
    mock_print.reset_mock()
