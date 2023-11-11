# This file will be visible for the student
import os

from course_section.course_framework_lesson.programming_task.invisible_main import say_bye


def invoke_say_bye(how_many_times: int):
    print(os.linesep.join([say_bye() for _ in range(how_many_times)]))


if __name__ == '__main__':
    print("How many times should I print Bye?")
    how_many_times = int(input())
    invoke_say_bye(how_many_times)
