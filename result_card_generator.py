"""Task 1: Student Result Card Generator.

Collects a student's details and marks in five subjects, validates the input,
and prints a formatted result card.
"""

SUBJECTS = ["English", "Urdu", "Mathematics", "Science", "Computer"]
MAX_MARKS_PER_SUBJECT = 100
SUBJECT_PASS_MARK = 40  # Any subject below this makes the final result Fail


def format_name(name):
    """Clean a name by trimming extra spaces and applying Title Case."""
    return name.strip().title()


def get_valid_name():
    """Keep asking until the user enters a non-empty name."""
    while True:
        name = format_name(input("Enter student name: "))
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_valid_roll_number():
    """Keep asking until the roll number contains digits only."""
    while True:
        roll_no = input("Enter roll number: ").strip()
        if roll_no.isdigit():  # digits only, no letters/symbols/negatives
            return roll_no
        print("Invalid roll number. Use digits only (e.g. 1024).")


def get_valid_marks(subject):
    """Ask for marks in one subject until a number between 0 and 100 is given."""
    while True:
        raw = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            marks = float(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
            return marks
        print("Marks must be between 0 and 100.")


def calculate_percentage(total, max_total):
    """Return the percentage of total obtained out of max_total."""
    if max_total == 0:  # avoid division by zero
        return 0.0
    return (total / max_total) * 100


def get_grade(percentage):
    """Return the letter grade for a given percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def get_final_status(marks_list, grade):
    """Return 'Fail' if any subject is below 40 or the grade is Fail, else 'Pass'."""
    if min(marks_list) < SUBJECT_PASS_MARK or grade == "Fail":
        return "Fail"
    return "Pass"


def print_result_card(name, roll_no, marks_list, total, max_total, percentage, grade, status):
    """Print the formatted result card using f-strings."""
    line = "=" * 44
    print("\n" + line)
    print(f"{'STUDENT RESULT CARD':^44}")
    print(line)
    print(f"{'Name':<20}: {name}")
    print(f"{'Roll Number':<20}: {roll_no}")
    print("-" * 44)
    print(f"{'Subject':<20}{'Marks':>10}{'Out of':>10}")
    print("-" * 44)
    for subject, marks in zip(SUBJECTS, marks_list):
        print(f"{subject:<20}{marks:>10.1f}{MAX_MARKS_PER_SUBJECT:>10}")
    print("-" * 44)
    print(f"{'Total Obtained':<20}: {total:.1f} / {max_total}")
    print(f"{'Percentage':<20}: {percentage:.2f}%")
    print(f"{'Grade':<20}: {grade}")
    print(f"{'Final Status':<20}: {status}")
    # Explain the subject-level rule if it caused the failure
    if status == "Fail" and min(marks_list) < SUBJECT_PASS_MARK:
        print(f"Note: Scored below {SUBJECT_PASS_MARK} in at least one subject.")
    print(line)


def main():
    """Run the program: collect input, compute results, show the card."""
    print("--- Student Result Card Generator ---")
    name = get_valid_name()
    roll_no = get_valid_roll_number()

    marks_list = []  # stores marks of all five subjects
    for subject in SUBJECTS:
        marks_list.append(get_valid_marks(subject))

    total = sum(marks_list)
    max_total = MAX_MARKS_PER_SUBJECT * len(SUBJECTS)
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    status = get_final_status(marks_list, grade)

    print_result_card(name, roll_no, marks_list, total, max_total, percentage, grade, status)


if __name__ == "__main__":
    main()
