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
```
lab9.py:30:1: E302 expected 2 blank lines, found 1
lab9.py:40:1: E302 expected 2 blank lines, found 1
lab9.py:107:80: E501 line too long (80 > 79 characters)
lab9.py:113:1: E302 expected 2 blank lines, found 1
lab9.py:124:1: E302 expected 2 blank lines, found 1
lab9.py:126:1: W293 blank line contains whitespace
lab9.py:159:1: E302 expected 2 blank lines, found 1
lab9.py:171:1: E302 expected 2 blank lines, found 1
lab9.py:223:80: E501 line too long (86 > 79 characters)
lab9.py:273:5: E303 too many blank lines (2)
lab9.py:273:50: E231 missing whitespace after ','
lab9.py:273:66: E231 missing whitespace after ','
lab9.py:273:80: E501 line too long (83 > 79 characters)
lab9.py:276:1: E305 expected 2 blank lines after class or function definition, found 1
lab9.py:277:11: W292 no newline at end of file
```

## second pycodestyle run
```
All fixed :)
```

## data link
https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download

## Lab10 Dataset

Dataset: Video Game Sales

The dataset contains information about video game sales. Each row represents one video game and includes the game's name, platform, release year, genre, publisher, regional sales, and global sales.

Dataset link:
https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download

## Lab10 Environment Variables

The application uses a `.env` file to configure selected analysis options.

### `STAT_COLUMN`

Defines which numeric column is used for the average calculation.

Possible values:
- `Global_Sales`
- `NA_Sales`
- `EU_Sales`
- `JP_Sales`
- `Other_Sales`

Example:

```env
STAT_COLUMN=Global_Sales
```

### `GROUP_BY_COLUMN`

Defines which column is used to group the data for aggregation.

Possible values:
- `Genre`
- `Platform`
- `Publisher`
- `Year`

Example:

```env
GROUP_BY_COLUMN=Genre
```

Example `.env` file:

```env
STAT_COLUMN=Global_Sales
GROUP_BY_COLUMN=Genre
```

## Lab10 How to Run

From the `src` folder:

```bash
python lab10.py vgsales.csv
```
