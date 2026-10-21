# 11 — Explain and fix overwritten input
# COPILOT — ask Chat for hints; make the edit yourself.
#
# Read: https://www.w3schools.com/python/python_variables.asp
# Relevant: Reassigning a name replaces its previous value.
# Read: https://www.w3schools.com/python/python_strings.asp
# Relevant: Text values in variables; use + to join the parts.
# Read: https://www.w3schools.com/python/python_strings_concatenate.asp
# Relevant: Join stored strings with + and include the needed spaces/separators.
#
# TASK
# The starter should read three text values and join them with hyphens,
# ending with an exclamation mark. It currently loses the first two inputs.
# Run the starter. In Copilot Chat, ask: "Why does this code lose my first
# two inputs? Give me a hint without writing the solution." Include this file
# as context. Read the explanation, then fix the code yourself. Correct the
# prompt labels too.
#
# EXPECTED TRANSCRIPT
# The 1st part: history
# The 2nd part: math
# The 3rd part: english
# history-math-english!
#
# SECOND TEST
# Inputs: red / green / blue
# Final output: red-green-blue!
# Do not replace the inputs with fixed sample text.

# === YOUR CODE ===
part = input("The 1st part: ")
part = input("The 2st part: ")
part = input("The 3st part: ")
print(part + part + part)
