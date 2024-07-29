# JetBrains Academy Python Course Template

[![official project](https://jb.gg/badges/official.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Note**
>
> Click the <kbd>Use this template</kbd> button and clone it in IntelliJ IDEA.

**JetBrains Academy Python course template** is a repository that provides a
pure template to make it easier to create a new Python course with the [JetBrains Academy
plugin][ref:plugin.marketplace] (check out the [Creating a repository from a template][gh:template] article).

The main goal of this template is to speed up the setup phase
of Python course development for both new and experienced educators
by preconfiguring the project scaffold and CI,
linking to the proper documentation pages, and keeping everything organized.

If you're still not quite sure what this is all about, read our introduction: [What is the JetBrains Academy plugin?][docs:intro]

> **Note**
>
> Click the <kbd>Watch</kbd> button on the top to be notified about releases containing new features and fixes.

### Table of contents

In this README, we will highlight the following elements of template-project creation:

- [Getting started](#getting-started)
- [Course info configuration file](#course-info-configuration-file)
- [Course ignore file](#course-ignore-file)
- [Sample code](#sample-code)
- [Testing](#testing)
- [Useful links](#useful-links)

## Getting started

Before we dive into course development and everything related to it, it's worth mentioning the benefits of using GitHub Templates.
By creating a new project with the current template, you start with no history or reference to this repository.
This allows you to create a new repository easily, without copying and pasting previous content, cloning repositories, or clearing the history manually.

All you need to do is click the <kbd>Use this template</kbd> button (you must be logged in with your GitHub account).

![Use this template][file:use-template-blur]

The most convenient way of getting your new project from GitHub is the <kbd>Get from VCS</kbd> action available on the Welcome Screen,
where you can filter your GitHub repository by its name.

![Get from version control][file:get_from_vcs.png]


## Course template structure

A generated JetBrains Academy Python Course Template repository contains the following content structure:

```
.
├── LICENSE
├── README.md                      README
├── common                         Course sources common for all sections
│   └── resources                  Resources - images, icons
├── course-info.yaml               Course info configuration file
└── course_section                 An example of the course section
    ├── course_guided_project      An example of the course guided project
    │   ├── lesson-info.yaml       Lesson config file
    │   ├── programming_task       Example of programming task
    │   │   ├── main.py
    │   │   ├── task-info.yaml     Task info
    │   │   ├── task.md            Task text content
    │   │   └── tests              Task tests
    │   │       └── test.py
    │   └── theory_task            Example of theory task
    │       ├── main.py
    │       ├── task-info.yaml
    │       └── task.md
    ├── course_lesson              An example of the course lesson
    │   ├── lesson-info.yaml  
    │   ├── multi_file_task        Multiple file task example
    │   │   ├── main.py
    │   │   ├── task-info.yaml
    │   │   ├── task.md
    │   │   ├── task.py
    │   │   └── tests
    │   └── quiz_task              Quiz task example
    │       ├── main.py
    │       ├── task-info.yaml
    │       └── task.md
    └── section-info.yaml          Section information
```

## Course info configuration file

The course info configuration file is the [course-info.yaml][file:course-info.yaml] file located in the root directory.
It provides general information about the course, like description, language, etc.

```yaml
type: marketplace
title: JetBrains Academy Python course template
language: English
summary: Here you can put the course description. You can use HTML tags inside the
  description.
programming_language: Python
environment: unittest
content:
  - course_section
```

## Course ignore file

The course ignore file is the [.courseignore][file:courseignore] file located in the root directory.
It provides the list of files or directories that will be ignored in the final course preview or archive.

```text
README.md
```

You can find more information about the course preview in the [Course preview][ref:course.preview] section. Information
about creating a course archive and uploading it to the marketplace is in the [Course distribution][ref:course.distribution] section.

## Sample code

The prepared template provides an example of a course with one section, two lessons (regular and guided), and five tasks in total.

![Course structure in the course creator mode][file:course-structure-author]

Each course may have an unlimited number of sections, lessons, and tasks.
Students will see almost the same course structure as the educator (course author):

![Course structure in the course student mode][file:course-structure-student]

The main difference is in framework lessons, which display only task files, without intermediate steps.

You can read more about guided projects in the official documentation in the [Guided Projects Creation][ref:guided.projects.creation] section.

> **Note**
>
> Click <kbd>Course Creator</kbd> -> <kbd>Create Course Preview</kbd> in the context menu in the root of the repository to create a course preview.


The JetBrains Academy plugin provides five different types of tasks,
and you can combine them inside one lesson (whether regular or guided).
You can read more about tasks in the official documentation in the [Task][ref:tasks] section.

## Testing

To check the programming exercises for [**edu**][ref:tasks] tasks, you need to write tests using [unittest](https://docs.python.org/3/library/unittest.html) framework.

You can find little examples of programming tasks in the repository in the `test.py` files:
in [course lesson][file:course.lesson.tests] and [course guided project][file:course.guided.project.tests].

## Useful links

- [JetBrains Academy plugin][ref:plugin.marketplace]
- [Course creator start guide][ref:course.creator.start.guide]
- [Courses on Marketplace][ref:marketplace]

[gh:actions]: https://help.github.com/en/actions
[gh:template]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template

[ref:marketplace]: https://plugins.jetbrains.com/education
[ref:course.creator.start.guide]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html
[ref:plugin.marketplace]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy
[ref:course.preview]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html#preview_course
[ref:course.distribution]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html#course_distribution
[ref:guided.projects.creation]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/framework-lessons-guide-for-course-creators.html#a81e8983
[ref:tasks]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/framework-lessons-guide-for-course-creators.html#a81e8983

[docs:intro]: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/jetbrains-academy-plugin-faq.html#what_is_the_jetbrains_academy_plugin

[file:course-info.yaml]: ./course-info.yaml
[file:courseignore]: .courseignore
[file:course.lesson.tests]: course_section/course_lesson/programming_task/tests/test.py
[file:course.guided.project.tests]: course_section/course_guided_project/programming_task/tests/test.py

[semver]: https://semver.org

[file:get_from_vcs.png]: common/resources/images/get-from-version-control.png
[file:course-structure-author]: common/resources/images/course-structure-author.png
[file:course-structure-student]: common/resources/images/course-structure-student.png
[file:use-template-blur]: common/resources/images/use_template_blur.jpg
