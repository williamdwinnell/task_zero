# Project README

## Overview

This Python project is designed to process and analyze data from CSV files. The script provides various statistical insights and data summaries, including data types, missing values, unique values, modes, counts of values less than and equal to zero, and basic statistics like mean, median, minimum, and maximum. The results are exported to a new CSV file for easy review.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Function Definitions](#function-definitions)
3. [Main Code](#main-code)
4. [Exporting Results](#exporting-results)
5. [Dependencies](#dependencies)
6. [Usage](#usage)

## Getting Started

To get started with this project, you will need to have Python installed on your system along with the `csv` and `statistics` modules. This project was last updated on November 21st, 2021, by Liam Dwinnell.

### Prerequisites

- Python 3.x
- `csv` module (standard library)
- `statistics` module (standard library)

### Installation

No installation is required other than having Python and the necessary modules mentioned above.

## Function Definitions

The script defines several functions to process and analyze the CSV data:

1. **open_csv(dir)**: Opens a CSV file and returns its content as a list of lists.
2. **convert(val)**: Converts a value to `int`, `float`, or `str` as appropriate.
3. **render_values(data)**: Converts all values in the list of lists to their appropriate types.
4. **get_col(data, col)**: Extracts a column from the data.
5. **get_variable_names(data)**: Returns the variable names from the first row of the data.
6. **get_variable_types(data)**: Determines the data types of each variable.
7. **get_missing_col(data, col)**: Counts missing values in a specified column.
8. **get_missing(data)**: Counts total missing values for each variable.
9. **get_unique_strings(data, types)**: Counts unique string values for each variable.
10. **get_mode(data, col, modes)**: Finds the top modes for a given column.
11. **get_modes(data, uniques, max_modes)**: Finds the modes for each variable.
12. **get_under_zero(data, types)**: Counts values under zero for numerical variables.
13. **get_equal_zero(data, types)**: Counts values equal to zero for numerical variables.
14. **get_mean(data)**: Calculates the mean of a list.
15. **get_median(data)**: Calculates the median of a list.
16. **get_stats(data, types)**: Calculates mean, median, min, and max for numerical variables.

## Main Code

The main part of the script performs the following tasks:

1. Prompts the user to enter the directory of the CSV file.
2. Opens the CSV file and loads the data.
3. Processes the data to determine variable names, types, and various statistical measures.
4. Outputs the results to the console.
5. Prompts the user for the export directory and report name.
6. Exports the results to a new CSV file.

## Exporting Results

The script exports the processed data and analysis results to a new CSV file. The output CSV includes:

- Variable names
- Data types
- Missing value counts
- Unique string value counts
- Modes and their counts
- Counts of values under zero and equal to zero
- Mean, median, min, and max for numerical variables

## Dependencies

- Python 3.x
- `csv` module
- `statistics` module

## Usage

To use this script, follow these steps:

1. Ensure you have Python 3.x installed on your system.
2. Save the script to a `.py` file.
3. Open a terminal or command prompt.
4. Run the script using `task_0.py`.
5. Enter the required inputs when prompted (CSV file directory, export directory, and report name).

Example usage:
```sh
$ python data_analysis.py
Enter The CSV's Directory: path/to/your/csvfile.csv
['Variable1', 'Variable2', 'Variable3', ...]
['int', 'float', 'str', ...]
[0, 2, 0, ...]
[5, '', 3, ...]
[[['val1', 10], ['val2', 8], ...], [], [['valA', 5], ['valB', 3], ...], ...]
Less Than Zero: [0, 1, '', ...]
Equals Zero: [3, 0, '', ...]
Means: [10.5, 20.3, '', ...]
Medians: [10.0, 20.0, '', ...]
Mins: [1, 10, '', ...]
Maxs: [20, 30, '', ...]
Enter The Export Directory: path/to/export
Enter The Report's Name: analysis_report
