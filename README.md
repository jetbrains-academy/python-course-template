[![official project](https://jb.gg/badges/official.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# JetBrains Academy Python Course Template

**JetBrains Academy Python course template** is a repository that provides a
pure template to make it easier to create a new Python course with the [JetBrains Academy
plugin](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy) (check out the [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) article).

This template is designed to help educators, both new and experienced, 
quickly start developing courses by providing technical examples.

If you're unfamiliar with the plugin, read our introduction: [What is the JetBrains Academy plugin?](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/jetbrains-academy-plugin-faq.html#what_is_the_jetbrains_academy_plugin)

> **Note**
>
> Click the <kbd>Use this template</kbd> button to create your own repository based on this template.

## Docs
Learn more about course creation with the JetBrains Academy plugin in the [Course creator start guide](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html).

## Files structure
### Course structure
```text
.
├── course-info.yaml   # Contains metadata like the course title, language, etc.
├── requirements.txt   # Python dependencies for the course.
├── course_lesson/
│   ├── theory_task/      # A theory-based task.
│   ├── quiz_task         # A multiple-choice quiz task.
│   ├── edu_task/         # A task that includes unit tests.
│   ├── output_task/      # A task with checks through stdin/stdout
│   └── lesson-info.yaml  # Defines the structure and order of tasks in this lesson. 
└── course_guided_project/      # Guided project lesson
    ├── theory_task/
    ├── first_task/
    ├── second_task/
    └── lesson-info.yaml
```

### Typical task structure
```text
├── main.py         # Task source code file.
├── task.md         # Task description text displayed by the plugin.
├── task-info.yaml  # Contains task and placeholder metadata.
└── tests/
    └── test.py     # Unit tests (if applicable for the task type).
```

## Examples of tasks
We've included example tasks that demonstrate how to create engaging online course content. Feel free to explore each task and its associated files.

### [Theory task](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html#theory_task) (course_lesson/theory_task/)
Contains a minimal set of the files typically used in a task:
- Source code file `main.py` (empty for theory tasks).
- Text displayed in task description: `task.md`.
- Metadata file for the current task: `task-info.yaml`.

### [Multiple-choice quiz](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html#multiple_choice_task) (course_lesson/quiz_task/)
Similar to the theory task, but the `task-info.yaml` file contains answer options.

### [Task with unit tests](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html#edu_task) (course_lesson/edu_task/)
Includes a test file (`tests/test.py`), which is executed when the `Check` button is clicked. The [unittest](https://docs.python.org/3/library/unittest.html) testing framework is used.
The `task-info.yaml` file contains placeholders.

### [Output testing task](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html#output_task) (course_lesson/output_task/)
Indludes two files: `tests/input.txt` and `tests/output.txt`.
When the `Check` button is clicked, the program is run with the contents of `tests/input.txt` file as an input.
The actual output of the program is compared with the expected from the `tests/output.txt` file.

### [Course guided project](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/framework-lessons-guide-for-course-creators.html)
In this lesson you can see a demonstration of a guided project in which tasks are linked together within a lesson
, and the user's solutions in one step are transferred to the next. 
