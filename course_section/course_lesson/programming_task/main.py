# This file will be visible for the student
import os

from course_section.course_framework_lesson.theory_task.invisible_main import say_hello


def invoke_say_hello(how_many_times: int):
    print(os.linesep.join([say_hello() for _ in range(how_many_times)]))


if __name__ == '__main__':
    print("How many times should I print Hello?")
    how_many_times = int(input())
    invoke_say_hello(how_many_times)
