# 17 — Repair a job profile
# HOMEWORK — use f-strings to fix the supplied output.
#
# Read: https://www.w3schools.com/python/python_strings_format.asp
# Relevant: F-Strings and variable placeholders; print() with no argument adds a blank line.
# Read: https://www.w3schools.com/python/ref_func_print.asp
# Relevant: A comma between values automatically inserts a separator.
#
# TASK
# The data values below are correct. Replace only the OUTPUT statements
# with f-strings so the result matches the sample, including the two blank
# lines and the two spaces before each hyphen. Keep the variables; do not
# replace the whole profile with one fixed block of text.
#
# EXPECTED OUTPUT
# my name is Tim Tester, I am 20 years old
#
# my skills are
#   - python (beginner)
#   - java (veteran)
#   - programming (semiprofessional)
#
# I am looking for a job with a salary of 2000-3000 euros per month
#
# SECOND TEST
# Temporarily set name to "Alex Example", age to 21, lower to 2500, and upper
# to 3500. Those four new values should appear without editing the print
# statements. Restore the original data before your final save and upload.

# === YOUR CODE ===
# === DATA — keep for the final submission ===
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

# === OUTPUT — replace these statements ===
print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")
