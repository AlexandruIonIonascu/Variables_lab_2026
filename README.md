# Lab 2 — Variables, input, arithmetic, and f-strings

Practise storing values, reading input, doing calculations, and displaying
results in Python. Start with individual exercises, then work with Copilot,
and finish with the homework. You may start the homework during the lab if
you finish the other exercises early.

## How to work

1. Follow the instructor's explanation and demo.
2. Open the exercise files in numerical order. Each file contains its task,
   reading links, and sample output or checks.
3. Read the linked sections, then write your solution under **YOUR CODE**.
   Keep the task comments. For exercises with starter code, edit the indicated
   section instead.
4. Save the file and run that file on its own. For example, from the repository
   root in the terminal:

   ```bash
   python lab/individual/01_print.py
   ```

5. When the program asks a question, type the answer in the terminal and press
   **Enter**. Use a decimal point for decimal numbers, such as `2.5`.
6. Compare your result with the example. Where a second test is provided, run
   that test too. Use variables and calculations rather than printing the
   sample answers as fixed text.

Use the concepts covered in this lab: `print()`, comments, variables, `str`,
`int`, `float`, `bool`, `type()`, `input()`, arithmetic, and f-strings.
Assume numeric inputs are valid; input validation is not required.

## Folder structure

| Folder | Contents |
| --- | --- |
| [lab/individual/](lab/individual/) | Exercises 01–10: write the solutions yourself after the reading and demo. |
| [lab/copilot/](lab/copilot/) | Exercises 11–12: use Copilot as described in each file, then review and test the result. |
| [homework/](homework/) | Exercises 13–18: practise arithmetic and f-strings; finish by the instructor's deadline. |

Each exercise has its own Python file, so running one exercise does not run
the others. Keep the existing filenames and folders.

## Part A — Individual exercises

Write these solutions yourself. Dismiss inline AI suggestions with **Esc**
and ask the instructor for help if you get stuck.

| Exercise | What you will practise |
| --- | --- |
| [01_print.py](lab/individual/01_print.py) | Use four `print()` statements to reproduce four lines of text. |
| [02_comments.py](lab/individual/02_comments.py) | Add `#` to each line of a finished block so it stays in the file but no longer runs. |
| [03_variables.py](lab/individual/03_variables.py) | Store fictional details in three variables and print their values. |
| [04_data_types.py](lab/individual/04_data_types.py) | Create text, integer, decimal, and Boolean values; inspect them with `type()`. |
| [05_reassignment.py](lab/individual/05_reassignment.py) | Assign a new value to an existing variable and observe the output. |
| [06_name_twice.py](lab/individual/06_name_twice.py) | Read a name once with `input()`, store it, and print it twice. |
| [07_address_card.py](lab/individual/07_address_card.py) | Keep several inputs in separate variables and print a fictional address card. |
| [08_story.py](lab/individual/08_story.py) | Insert a supplied name and year into a short story. |
| [09_arithmetic.py](lab/individual/09_arithmetic.py) | Compare expressions with text and explore multiplication and parentheses. |
| [10_numeric_input.py](lab/individual/10_numeric_input.py) | Convert two inputs with `int()`, calculate their sum, and print the result. |

## Part B — Copilot exercises

| Exercise | What you will practise |
| --- | --- |
| [11_fix_strings.py](lab/copilot/11_fix_strings.py) | Ask Copilot Chat why inputs are overwritten, request a hint, then fix the code yourself. |
| [12_fstrings.py](lab/copilot/12_fstrings.py) | Ask Copilot to edit only the marked OUTPUT section, using f-strings and two decimal places. |

Include the relevant file as context in Chat. Follow the instructions in the
file, read the explanation or proposed changes, and test both sample cases.
For exercise 12, the code must be added to the Python file; a reply in Chat
alone does not complete the exercise. Be ready to explain the code you keep.

## Part C — Homework

Start in class if you are ready. Attempt the tasks yourself; you may ask
Copilot for explanations or hints, but write your own homework solutions.

| Exercise | What you will practise |
| --- | --- |
| [13_minutes.py](homework/13_minutes.py) | Calculate the minutes in 365 and 366 days using variables. |
| [14_times_five.py](homework/14_times_five.py) | Read an integer and display its multiplication by five. |
| [15_fix_product.py](homework/15_fix_product.py) | Repair a program that overwrites three inputs and calculates the wrong product. |
| [16_sum_and_product.py](homework/16_sum_and_product.py) | Calculate both the sum and product of two input numbers. |
| [17_job_profile.py](homework/17_job_profile.py) | Repair a job profile's output using f-strings, spacing, and blank lines. |
| [18_receipt.py](homework/18_receipt.py) | Read an item, quantity, and price; calculate a total and format a receipt. |

## Reading links

Read only the relevant parts below. The exercise files also contain the links
needed for each task.

| Reading | Relevant parts |
| --- | --- |
| [print()](https://www.w3schools.com/python/ref_func_print.asp) | Printing text and variables, multiple values, and blank lines. |
| [Comments](https://www.w3schools.com/python/python_comments.asp) | Creating comments with `#` and preventing code from running. |
| [Variables](https://www.w3schools.com/python/python_variables.asp) | Creating variables, assigning values, and changing a stored value. |
| [Data Types](https://www.w3schools.com/python/python_datatypes.asp) | `str`, `int`, `float`, `bool`, and checking a type with `type()`. |
| [User Input](https://www.w3schools.com/python/python_user_input.asp) | `input()`, prompts, storing replies, and numeric input; stop before validation. |
| [Casting](https://www.w3schools.com/python/python_casting.asp) | Converting values with `int()` and `float()`. |
| [Strings](https://www.w3schools.com/python/python_strings.asp) | Text in quotation marks and assigning strings to variables. |
| [String Concatenation](https://www.w3schools.com/python/python_strings_concatenate.asp) | Joining strings with `+` and adding spaces or separators. |
| [Arithmetic Operators](https://www.w3schools.com/python/python_operators_arithmetic.asp) | Addition, multiplication, and grouping calculations with parentheses. |
| [Format Strings](https://www.w3schools.com/python/python_strings_format.asp) | F-strings, variable placeholders, and `:.2f` for two decimal places. |

## Save and submit

1. Click **File → Save All**.
2. Open **Source Control**. Review your changed files and click **+** beside
   the files you want to include.
3. Enter a short message, such as **Complete individual exercises**, and click
   **Commit**.
4. Open the Source Control **…** menu and choose **Push** (it may appear under
   **Pull, Push**).
5. Refresh your assignment repository on GitHub and open your changed files
   to confirm that your latest code was uploaded.

Repeat for the Copilot exercises and homework. Follow the instructor's
instructions for the deadline and submission link. Verify your work on GitHub
before stopping your Codespace.
