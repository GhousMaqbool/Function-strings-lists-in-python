"""Task 2: Class Marks Analyzer.

Reads names and marks for a class and reports average, highest, lowest,
pass/fail counts, above-average students and a ranked list.
"""

PASS_MARK = 50


def get_valid_count():
    """Ask for the number of students until a positive whole number is given."""
    while True:
        raw = input("How many students are in the class? ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a whole number greater than 0.")


def get_valid_mark(student_name):
    """Ask for one student's mark until it is a number between 0 and 100."""
    while True:
        raw = input(f"Enter marks for {student_name} (0-100): ").strip()
        try:
            mark = float(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("Marks must be between 0 and 100.")


def find_students_with_mark(names, marks, target):
    """Return the list of student names whose mark equals target."""
    matches = []
    for i in range(len(marks)):
        if marks[i] == target:
            matches.append(names[i])
    return matches


def count_pass_fail(marks):
    """Return (passed, failed) counts using the pass mark of 50."""
    passed = 0
    failed = 0
    for mark in marks:
        if mark >= PASS_MARK:
            passed += 1
        else:
            failed += 1
    return passed, failed


def main():
    """Run the program: collect data, then display all statistics."""
    print("--- Class Marks Analyzer ---")
    total_students = get_valid_count()

    student_names = []
    student_marks = []

    # Collect data for every student
    for i in range(1, total_students + 1):
        name = input(f"Enter name of student {i}: ").strip().title()
        if name == "":
            name = f"Student {i}"  # fallback for empty names
        student_names.append(name)
        student_marks.append(get_valid_mark(name))

    # Class average
    average = sum(student_marks) / len(student_marks)
    print("\n========== CLASS REPORT ==========")
    print(f"Total students : {len(student_names)}")
    print(f"Class average  : {average:.2f}")

    # Highest and lowest (ties handled by listing all matching students)
    highest = max(student_marks)
    lowest = min(student_marks)
    print(f"Highest marks  : {highest:.1f} -> {', '.join(find_students_with_mark(student_names, student_marks, highest))}")
    print(f"Lowest marks   : {lowest:.1f} -> {', '.join(find_students_with_mark(student_names, student_marks, lowest))}")

    # Pass / fail counts
    passed, failed = count_pass_fail(student_marks)
    print(f"Passing (>= {PASS_MARK}) : {passed}")
    print(f"Failing (< {PASS_MARK})  : {failed}")

    # Students above average
    print("\nStudents above class average:")
    found = False
    for i in range(len(student_names)):
        if student_marks[i] > average:
            print(f"  {student_names[i]}: {student_marks[i]:.1f}")
            found = True
    if not found:
        print("  None")

    # Sorted highest to lowest: pair marks with names, then sort by marks
    ranked = sorted(zip(student_marks, student_names), reverse=True)
    print("\nMarks sorted from highest to lowest:")
    for position, (mark, name) in enumerate(ranked, start=1):
        print(f"  {position}. {name}: {mark:.1f}")
    print("==================================")


if __name__ == "__main__":
    main()
