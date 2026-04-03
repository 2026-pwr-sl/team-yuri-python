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
