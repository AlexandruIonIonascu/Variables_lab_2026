# 12 — Review an AI edit with f-strings
# COPILOT — ask it to edit OUTPUT only, then review and test.
#
# Read: https://www.w3schools.com/python/python_strings_format.asp
# Relevant: F-Strings, placeholders, and :.2f for two decimal places.
# Read: https://www.w3schools.com/python/python_casting.asp
# Relevant: The float() examples for valid decimal input.
#
# TASK
# Keep INPUT AND CALCULATION unchanged. Ask Copilot to complete OUTPUT with
# three print statements using f-strings. Include this file as context in
# Chat and request a file edit. Review the proposed changes before keeping
# them, then run both tests below. Use the stored variables:
# 1. "Learner: " followed by learner_name.
# 2. "Course: " followed by course_name.
# 3. "Two lessons cost " followed by two_lesson_cost with two decimal places,
#    followed by " euros.".
#
# SAMPLE TRANSCRIPT
# Learner name: Alex
# Course name: Python
# Price per lesson: 12.5
# Learner: Alex
# Course: Python
# Two lessons cost 25.00 euros.
#
# SECOND TEST
# Use Sam / Art / 3.75. Final lines:
# Learner: Sam
# Course: Art
# Two lessons cost 7.50 euros.
#
# CHECK
# The f prefix activates placeholders; {name} inserts a value, and :.2f
# formats a number with two decimal places. These features are needed again
# in homework. Explain one generated statement to the instructor.

# === YOUR CODE ===
# === INPUT AND CALCULATION — keep unchanged ===
learner_name = input("Learner name: ")
course_name = input("Course name: ")
price_per_lesson = float(input("Price per lesson: "))
two_lesson_cost = price_per_lesson * 2

# === OUTPUT — Copilot edits here ===
# TODO: add the three required f-string print statements.
