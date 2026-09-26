# Ultimate Data Cleaning Tool 🧹

A Python-based **Interactive Data Cleaning Tool** built using **Pandas** and **NumPy** for cleaning, validating, transforming, and analyzing CSV and Excel datasets.

This project was developed to practice real-world **Data Cleaning and Data Preprocessing** using Python.

---

## 📌 Project Overview

Raw datasets can contain many data-quality problems such as:

* Missing values

* Duplicate rows

* Extra spaces

* Inconsistent capitalization

* Numeric values stored as text

* Invalid dates

* Negative values

* Inconsistent categories

* Mixed data types

* Outliers

This tool provides an interactive menu that allows the user to identify and handle many of these problems.

---

## ✨ Main Features

### 1. Dataset Information

Displays information about the dataset, including column names, data types, and non-null values.

### 2. Dataset Description

Generates statistical information using:

```python

df.describe()

```

### 3. Unique Values Count

Displays the number and frequency of unique values in a selected column.

### 4. Rename Column

Allows the user to rename an existing column.

### 5. Delete Column

Allows unwanted columns to be removed.

### 6. Sort Data

Sorts data in:

* Ascending order

* Descending order

### 7. Search Data

Searches for a specific value inside a selected column.

### 8. Replace Values

Allows specific values to be replaced with new values.

### 9. Remove Special Characters

Removes unwanted special characters from text columns.

### 10. Remove Blank Rows and Columns

Removes rows and columns that contain only blank values.

### 11. Correlation Matrix

Displays correlation between numeric columns.

```python

df.corr(numeric_only=True)

```

### 12. Dataset Shape

Displays the number of rows and columns.

### 13. Show All Columns

Displays all column names in the dataset.

### 14–16. Duplicate Handling

The tool can:

* Display duplicate rows

* Count duplicate rows

* Remove duplicate rows

```python

df.drop_duplicates()

```

---

# 🧹 Data Cleaning Performed

The project was also used with an Excel practice dataset to handle the following real-world data-quality problems.

## 1. Missing Values

Missing values are identified using:

```python

df.isnull().sum()

```

Depending on the data type, missing values can be handled using:

* `Unknown` for text data

* Median for numeric data

---

## 2. Duplicate Rows

Duplicate records are identified and removed.

```python

df.duplicated().sum()

df.drop_duplicates()

```

---

## 3. Extra Spaces

Unnecessary spaces are removed from column names and text values.

Example:

```text

"  Delhi  "

```

becomes:

```text

"Delhi"

```

---

## 4. Inconsistent Capitalization

Text values are standardized using Title Case.

Example:

```text

delhi

DELHI

Delhi

```

can be standardized to:

```text

Delhi

```

The project uses:

```python

.str.title()

```

---

## 5. Numeric Values Stored as Text

Some numeric values may be stored as strings.

The tool converts them into numeric data using:

```python

pd.to_numeric(errors="coerce")

```

This is useful for columns such as:

* Quantity

* Unit Price

* Discount

* Sales

* Cost

* Profit

---

## 6. Invalid Dates

The project checks date columns and identifies invalid date values.

```python

pd.to_datetime(
    df[column],
    errors="coerce",
    dayfirst=True
)

```

Invalid dates are converted to `NaT` and can then be identified.

---

## 7. Negative Unit Prices

Negative Unit Prices are detected separately.

Example:

```text

Unit Price = -500

```

The tool provides options for handling negative numeric values, such as:

* Replace with 0

* Convert to absolute value

* Replace with median

* Delete rows

* Skip

---

## 8. Negative Profits

Negative profits are **not automatically removed** because negative profit can represent a genuine business situation, such as a loss.

The tool allows the user to decide how negative values should be handled.

---

## 9. Inconsistent Order Status

Different values representing the same status can be standardized.

Example:

```text

complete

completed

```

can be standardized to:

```text

Completed

```

Similarly:

```text

canceled

cancelled

```

can be standardized to:

```text

Cancelled

```

---

## 10. Inconsistent Payment Modes

Payment mode values can also be checked and standardized so that different spellings or capitalization do not create separate categories.

Example:

```text

cash

Cash

CASH

```

can be standardized as:

```text

Cash

```

---

## 11. Mixed Data Types

The tool provides a **Convert Data Type** option that can convert columns into:

* Integer

* Float

* String

* Datetime

Example:

```python

pd.to_numeric()

```

and:

```python

pd.to_datetime()

```

---

# 📊 Additional Features

The tool also includes:

* Numeric range filtering

* Length-based filtering

* Undo last change

* File saving

* Finding non-numeric values

* Finding numeric values inside text columns

* Negative value handling

* Outlier detection

* Invalid date detection

* Unique value analysis

---

# 📈 Outlier Detection

The project uses the **IQR (Interquartile Range)** method to detect outliers.

```text

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

```

After detecting outliers, the user can choose to:

1. Delete outliers

2. Replace with median

3. Replace with mean

4. Skip

---

# 📂 Dataset Columns

The practice dataset contains columns such as:

| Column       | Description             |

| ------------ | ----------------------- |

| Order ID     | Unique order identifier |

| Customer ID  | Customer identifier     |

| City         | Customer city           |

| Order Date   | Date of order           |

| Category     | Product category        |

| Product      | Product name            |

| Quantity     | Number of products      |

| Unit Price   | Price per unit          |

| Discount     | Discount applied        |

| Sales        | Total sales             |

| Cost         | Product cost            |

| Profit       | Profit or loss          |

| Payment Mode | Payment method          |

| Order Status | Status of the order     |

---

# 🛠️ Technologies Used

* **Python**

* **Pandas**

* **NumPy**

* **Excel**

* **OpenPyXL**

---

# 🚀 Installation

Install the required Python libraries:

```bash

pip install pandas numpy openpyxl

```

---

# ▶️ How to Run

Run the Python file:

```bash

python data_cleaning.py

```

Then enter your CSV or Excel file name:

```text

Enter file name (csv / xlsx):

```

Example:

```text

Data_Cleaning_Practice_1200_Rows.xlsx

```

After that, the interactive menu will appear.

```text

========= DATA CLEANING TOOL =========

1. Dataset Information

2. Describe Dataset

3. Unique Values Count

4. Rename Column

5. Delete Column

...

28. Outlier Detection

29. Invalid Date

30. Exit

```

Select the required option by entering its number.

---

# 📁 Project Structure

```text

Ultimate-Data-Cleaning-Tool/

│

├── data_cleaning.py

├── Data_Cleaning_Practice_1200_Rows.xlsx

├── README.md

└── requirements.txt

```

---

# 🎯 Project Objective

The main objective of this project is to understand and implement practical **data cleaning and preprocessing techniques** using Python.

The cleaned data can later be used for:

* Data Analysis

* Data Visualization

* Excel Reporting

* Power BI Dashboards

* Business Analytics

---

# 🔮 Future Improvements

Possible future improvements include:

* Graphical User Interface (GUI)

* Automatic data-quality report

* Before-and-after cleaning summary

* Automatic column type detection

* More advanced validation rules

* Automated Excel cleaning reports

* Power BI integration

* AI-assisted data cleaning


---

# 👨‍💻 Author

**Bhola Kumar**

BCA 1st Year

**Skills:** Python | Pandas | NumPy | SQL | Data Cleaning | Data Analysis

---

## ⭐ Project

This project is created as a learning and portfolio project to demonstrate practical experience with **Python-based Data Cleaning and Data Preprocessing**.
