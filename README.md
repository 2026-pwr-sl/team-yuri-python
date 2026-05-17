# Getting Started with Teamwork: Python + GitHub

## Group
Group 1 - Team Yuri

## Team Members
- Berke Mamal
- Metin Kaan Kulga
- Elif Karakas
- Urban Porocnik

## Project Goal
The goal of this project is to learn the basics of teamwork with GitHub and create a simple Python program in a shared repository.

## Project Structure
- `src/` – source code
- `tests/` – tests
- `docs/` – notes and documentation
- `data/` – optional input data
- `README.md` – project information
- `Requirements.txt`

## How to Run
   ```bash
   git clone https://github.com/2026-pwr-sl/team-yuri-python.git && \
   cd team-yuri-python && \
   python3 src/Main.py
   ```

## How to Test
   ```
   pip install pytest
   ```
then
   ```
   pytest
   ```

## Logging resources

- Documentation: https://docs.python.org/3/library/logging.html
- Tutorial: https://docs.python.org/3/howto/logging.html
- Cookbook: https://docs.python.org/3/howto/logging-cookbook.html

## task9
- successful_reads
- failed_reads
- html_entries
- read_log (if it reads the same input each time)
## why?
- These functions do not produce side effects (pure functions).
- If you give the same input, they will return the same output every time.

## !Function that should not be called multiple times:
- print_html_entries
## why?
- This function prints output to the screen (side effect).
Each time it is called, it prints again , leading to duplicated/unnecessary output.

## Summary:
- Pure functions → can be called as many times as you want
- Functions with side effects (print/log) → may cause issues when called repeatedly

## Exercises 
### ipaddress
- https://docs.python.org/3/library/ipaddress.html
### datetime
- https://docs.python.org/3/library/datetime.html

## first pycodestyle run
'''
- src\Lab04.py:40:60: W292 no newline at end of file
- src\LogReaderLAB6.py:92:1: E302 expected 2 blank lines, found 1
- src\config.py:18:5: E303 too many blank lines (2)
- src\config.py:19:6: E111 indentation is not a multiple of 4
- src\config.py:22:1: E305 expected 2 blank lines after class or function definition, found 1   
- src\config.py:23:4: E111 indentation is not a multiple of 4
- src\config.py:23:17: W292 no newline at end of file
- src\lab2-3.py:116:80: E501 line too long (84 > 79 characters)
- src\lab2-3.py:156:80: E501 line too long (88 > 79 characters)
- src\lab7.py:13:53: E225 missing whitespace around operator
- src\lab7.py:18:80: E501 line too long (109 > 79 characters)
- src\lab7.py:19:80: E501 line too long (81 > 79 characters)
- src\lab7.py:24:6: E111 indentation is not a multiple of 4
- src\lab7.py:29:42: E261 at least two spaces before inline comment
- src\lab7.py:32:1: W391 blank line at end of file
- src\log_entry.py:2:80: E501 line too long (95 > 79 characters)
- src\log_entry.py:12:80: E501 line too long (131 > 79 characters)
- src\menu.py:9:1: E302 expected 2 blank lines, found 1
- src\parser.py:61:80: E501 line too long (91 > 79 characters)
- src\parser.py:61:92: W292 no newline at end of file
- src\utils.py:29:80: E501 line too long (83 > 79 characters)
- src\lab9\lab9.py:30:1: E302 expected 2 blank lines, found 1
- src\lab9\lab9.py:40:1: E302 expected 2 blank lines, found 1
- src\lab9\lab9.py:107:80: E501 line too long (80 > 79 characters)
- src\lab9\lab9.py:113:1: E302 expected 2 blank lines, found 1
- src\lab9\lab9.py:124:1: E302 expected 2 blank lines, found 1
- src\lab9\lab9.py:126:1: W293 blank line contains whitespace
- src\lab9\lab9.py:159:1: E302 expected 2 blank lines, found 1
- src\lab9\lab9.py:171:1: E302 expected 2 blank lines, found 1
- src\lab9\lab9.py:223:80: E501 line too long (86 > 79 characters)
- src\lab9\lab9.py:273:5: E303 too many blank lines (2)
- src\lab9\lab9.py:273:50: E231 missing whitespace after ','
- src\lab9\lab9.py:273:66: E231 missing whitespace after ','
- src\lab9\lab9.py:273:80: E501 line too long (83 > 79 characters)
- src\lab9\lab9.py:276:1: E305 expected 2 blank lines after class or function definition, found 1
- src\lab9\lab9.py:277:11: W292 no newline at end of file
'''

## second pycodestyle run
'''
- src\lab2-3.py:116:80: E501 line too long (84 > 79 characters)
- src\lab2-3.py:156:80: E501 line too long (88 > 79 characters)
- src\lab7.py:18:80: E501 line too long (109 > 79 characters)
- src\lab7.py:19:80: E501 line too long (81 > 79 characters)
- src\log_entry.py:2:80: E501 line too long (95 > 79 characters)
- src\log_entry.py:12:80: E501 line too long (131 > 79 characters)
- src\parser.py:61:80: E501 line too long (91 > 79 characters)
- src\utils.py:29:80: E501 line too long (83 > 79 characters)
- src\lab9\lab9.py:107:80: E501 line too long (80 > 79 characters)
- src\lab9\lab9.py:223:80: E501 line too long (86 > 79 characters)
- src\lab9\lab9.py:273:80: E501 line too long (83 > 79 characters)
'''
