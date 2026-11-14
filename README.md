# Python Functions, Strings and Lists Assessment

## Overview
Two beginner-friendly Python console programs that practise **functions, string manipulation, lists and loops**, with input validation throughout.

## Programs

### 1. `result_card_generator.py` – Student Result Card Generator
Asks for a student's name, roll number and marks in five subjects, then prints a formatted result card showing the marks, total, percentage (2 decimals), letter grade and Pass/Fail status.

- Name is cleaned with `.strip()` and `.title()`.
- Roll number must be digits only (`.isdigit()`).
- Marks must be between 0 and 100 (re-asked if invalid).
- If any subject is **below 40**, the final status is **Fail**, whatever the percentage.

| Percentage | Grade |
|---|---|
| 90+ | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | Fail |

**Functions:** `get_valid_marks(subject)`, `calculate_percentage(total, max_total)`, `get_grade(percentage)`, `format_name(name)`, `get_valid_name()`, `get_valid_roll_number()`, `get_final_status()`, `print_result_card()`, `main()`

### 2. `class_marks_analyzer.py` – Class Marks Analyzer
Reads names and marks for a whole class using two parallel lists (`student_names`, `student_marks`) and displays:

- Class average
- Highest and lowest marks with the student(s) who got them (ties handled)
- Number of passing (>= 50) and failing (< 50) students
- Students above the class average
- Marks sorted from highest to lowest

**Custom functions:** `get_valid_count()`, `get_valid_mark()`, `find_students_with_mark()`, `count_pass_fail()`, `main()`

## Python Concepts Used
- Functions: `def`, parameters, `return`
- Strings: `.strip()`, `.title()`, `.isdigit()`, f-string formatting (alignment, `:.2f`)
- Lists: `append()`, `len()`, `sum()`, `max()`, `min()`, `sorted()`, `zip()`
- Loops: `while True` for validation, `for` with `range()` and `enumerate()`
- Conditionals, `try/except` for invalid numbers

## How to Run
Requires Python 3.8+.

```bash
python result_card_generator.py
python class_marks_analyzer.py
```

## Sample Input / Output

### Result Card Generator
```
Enter student name:   waleed shehbaz
Enter roll number: 1024
Enter marks for English (0-100): 95
Enter marks for Urdu (0-100): 88
Enter marks for Mathematics (0-100): 76
Enter marks for Science (0-100): 91
Enter marks for Computer (0-100): 85

============================================
            STUDENT RESULT CARD
============================================
Name                : Waleed Shehbaz
Roll Number         : 1024
--------------------------------------------
Subject                  Marks    Out of
--------------------------------------------
English                   95.0       100
Urdu                      88.0       100
Mathematics               76.0       100
Science                   91.0       100
Computer                  85.0       100
--------------------------------------------
Total Obtained      : 435.0 / 500
Percentage          : 87.00%
Grade               : A
Final Status        : Pass
============================================
```

### Class Marks Analyzer
```
How many students are in the class? 4
Enter name of student 1: ali
Enter marks for Ali (0-100): 80
Enter name of student 2: sara
Enter marks for Sara (0-100): 95
Enter name of student 3: usman
Enter marks for Usman (0-100): 95
Enter name of student 4: hina
Enter marks for Hina (0-100): 30

========== CLASS REPORT ==========
Total students : 4
Class average  : 75.00
Highest marks  : 95.0 -> Sara, Usman
Lowest marks   : 30.0 -> Hina
Passing (>= 50) : 3
Failing (< 50)  : 1

Students above class average:
  Ali: 80.0
  Sara: 95.0
  Usman: 95.0

Marks sorted from highest to lowest:
  1. Usman: 95.0
  2. Sara: 95.0
  3. Ali: 80.0
  4. Hina: 30.0
==================================
```
