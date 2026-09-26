import pandas as pd
import numpy as np

# Data_Cleaning_Practice_1200_Rows
file_name = input("Enter file name (csv / xlsx) : ")

try:
    if file_name.endswith(".csv"):
        df = pd.read_csv(file_name)

    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(file_name)

    else:
        print("Unsupported file")
        exit()

except FileNotFoundError:
    print("File not found.")
    exit()


while True :
    print("========= DATA CLEANING TOOL =========")

    print("1. Dataset Information")
    print("2. Describe Dataset")
    print("3. Unique Values Count")
    print("4. Rename Column")
    print("5. Delete Column")
    print("6. Sort Data")
    print("7. Search Data")
    print("8. Replace Value")
    print("9. Remove Special Characters")
    print("10. Remove Blank Rows/Columns")
    print("11. Correlation Matrix")
    print("12. Dataset Shape")
    print("13. Show All Columns")
    print("14. Show Duplicate Rows")
    print("15. Count Duplicate Rows")
    print("16. Remove Duplicate Rows")
    print("17. Missing Value Handling")
    print("18. Convert Text to Title Case")
    print("19. Remove Extra Spaces")
    print("20. Convert Data Type")
    print("21. Filter Numeric Range")
    print("22. Filter by Length")
    print("23. Undo Last Change")
    print("24. Save File")
    print("25. Find Non-Numeric Values")
    print("26. Find Numeric Values in Text Columns")
    print("27. Handle Negative Values")
    print("28. Outlier Detection")
    print("29. Invlaid Date")
    print("30. Exit")


    choice = input("Enter you option:")

    if choice == "1":
        try:
            df.info()
        
        except Exception as e:
            print(e)
            print("Information not found")

    elif choice == "2":
        try:
            print(df.describe(include="all"))
            # (include = all )column matlab sare column
        
        except Exception as e:
            print(e)
            print("Not Describe about df")

    elif choice == "3":
        column = input("Column Name : ")

        if column in df.columns:
            print("Column is present.")
            
            # print(df.groupby(column).size()) का काम किसी column के हर unique value की कितनी rows हैं, यह बताना होता है।
            print(df.groupby(column).size())

        else:
            print("Column not found")

    elif choice == "4":
        old = input("Old column Name : ")
        new = input("New column Name : ")

        if old in df.columns:
            backup = df.copy()
            df.rename(columns={old:new}, inplace=True)
            print("Renamed Successfully")
        
        else:
            print("Column not found")

    elif choice == "5":
        column = input("Column Name : ")
        
        if column in df.columns:
            print("Column is present.")
            backup = df.copy()

            df.drop(column, axis=1, inplace=True)
            print("Column Deleted successfully.")

        else:
            print("Column not found")
        

    elif choice == "6":
        column = input("Column Name : ")

        if column in df.columns:
            print("Column is present.")

        
            Asc_Des = input("Enter (Asc) for Ascending oder\nEnter (Des) for Descending order)")
        
            if Asc_Des.lower() == "asc":
        
                backup = df.copy()
            
                df.sort_values(column, inplace=True)
                print("Data sorted successfully.")
        
            elif Asc_Des.lower() == "des":
            
                backup = df.copy()

                df.sort_values(column, ascending=False, inplace=True)
                print("Data sorted successfully.")
        
            else :
                print("Please correctly enter.")
        
        else:
            print("Column is not present")
        
    elif choice == "7":
        column = input("Enter column name : ")

        if column in df.columns:
            print("Column is present.")


            value = input("Enter value : ")

            print(df[df[column].astype(str).str.contains(value,
                                                case=False,
                                                na=False)])

        else:
            print("Column is not present")
    
    elif choice == "8":
        column_name = input("Column name:")

        old = input("Enter old value:")
        new = input("Enter new value:")

        if column_name in df.columns:
            print("Column is present.")

            backup = df.copy()

            df[column_name] = df[column_name].replace(old, new)

            print("Value replaced successfully.")
        
        else:
            print("Column not found.")

    elif choice == "9":
        backup = df.copy()
        
        for col in df.select_dtypes(include="object"):

            df[col]=df[col].str.replace(
                                r'[^A-Za-z0-9 ]',
                                '',
                                regex=True
            )
        
        print("Successfully Remove special Characters.")

    elif choice == "10":

        backup = df.copy()

        df.dropna(how="all", inplace=True)
        df.dropna(axis=1, how="all", inplace=True)
        
        print("Blank rows and columns removed successfully.")

    elif choice == "11":
        print(df.corr(numeric_only=True))

    elif choice == "12":

        
        print(df.shape)

    elif choice == "13":
        
        print(df.columns)

    elif choice == "14":
        try:
            print(df[df.duplicated()])
        except Exception as e:
            print(e)
            print("Duplicate not found")

    elif choice == "15":

        print(df.duplicated().sum())

    elif choice == "16":
        before = len(df)

        backup = df.copy()
        df.drop_duplicates(inplace=True)

        removed = before - len(df)

        print(f"{removed} duplicate rows removed.")

    elif choice == "17":

        print("Missing Values Before Handling:")
        print(df.isnull().sum())

        # Backup only once
        backup = df.copy()

        # Blank strings ko NaN me convert karo
        df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

        # Fill missing values
        for col in df.columns:

            if df[col].dtype == "object" or "string":
                df[col] = df[col].fillna("Unknown")

            else:
                df[col] = df[col].fillna(df[col].median())

        print("\nMissing Values After Handling:")
        print(df.isnull().sum())

        print("Missing values handled successfully.")

    elif choice == "18":
        column_name = input("Enter column name to convert into Title Case: ").strip()

        if column_name in df.columns:

            backup = df.copy()

            try:
                # Convert selected column to string first
                df[column_name] = df[column_name].astype("string")

                # Apply Title Case
                df[column_name] = df[column_name].str.title()

                print(f"✅ '{column_name}' converted into Title Case successfully.")

            except Exception as e:
                df = backup.copy()
                print("❌ Conversion failed.")
                print("Error:", e)

        else:
            print(f"❌ Column '{column_name}' is not present.")

    elif choice == "19":

        backup = df.copy()

        # Remove spaces from column names
        df.columns = df.columns.str.strip()

        # Remove spaces from object column values
        for col in df.select_dtypes(include="object"):
            df[col] = df[col].str.strip()

        print("Extra spaces removed successfully.")

    elif choice == "20":

        column_name = input("Enter column name which you want to convert: ").strip()

        if column_name in df.columns:
            print("✅ Column is present")

            print("\nAvailable data types:")
            print("1. int")
            print("2. float")
            print("3. str")
            print("4. datetime")

            d_type = input("Enter your dtype: ").strip().lower()

            if d_type not in ["int", "float", "str", "datetime"]:
                print("❌ Invalid datatype.")
                continue

            try:
                # Save backup before making changes
                backup = df.copy()

                # Integer conversion
                if d_type == "int":
                    df[column_name] = pd.to_numeric(
                        df[column_name],
                        errors="coerce"
                    ).round().astype("Int64")

                # Float conversion
                elif d_type == "float":
                    df[column_name] = pd.to_numeric(
                        df[column_name],
                        errors="coerce"
                    ).astype("float64")

                # String conversion
                elif d_type == "str":
                    df[column_name] = df[column_name].astype("string")

                # Date conversion
                elif d_type == "datetime":
                    df[column_name] = pd.to_datetime(
                        df[column_name],
                        errors="coerce",
                        dayfirst=True
                    )

                print("✅ Converted Successfully")
                print("Column dtype conversion successfully.")
                print(f"Column: {column_name}")
                print(f"New dtype: {df[column_name].dtype}")

            except Exception as e:
                # Restore backup if conversion fails
                df = backup.copy()
                print("❌ Conversion Failed")
                print("Error:", e)

        else:
            print("❌ Column is not present.")

    elif choice == "21":

        column_name = input("Enter your column name:")

        if column_name in df.columns:
            print("Column is present.")

            backup = df.copy()
        
            df[column_name] = pd.to_numeric(df[column_name], errors="coerce")

            # n1 <= x >= n2 
            try:
                n1 = int(input("Enter Minimum value:"))
                n2 = int(input("Enter Maximum value:"))

                if n1 < 0 or n2 < 0:
                    print(" Range can not be negative.")
                    continue

            except ValueError:
                print("Please enter only number.")
                continue
            

            filtered_df = df[(df[column_name] >= n1) &
                (df[column_name] <= n2)]

            print(filtered_df)

            option = input("Enter (Yes) for this new DATAFRAME in your File as a sheet\nEnter (No) for this DATAFRAME not get sheet in your file:")
        
            if option.lower() in ["yes", "y"]:

                filtered_df = df[(df[column_name] >= n1) & (df[column_name] <= n2)]
 
                with pd.ExcelWriter("Ultimate_Data_Cleaning_Practice.xlsx", engine="openpyxl") as writer:
                    df.to_excel(writer, sheet_name="Original_Data", index=False)
                    filtered_df.to_excel(writer, sheet_name="Filtered_Data", index=False)
            
                print("Sheet add successfully.")
        
            elif option.lower() in ["no","n"]:
                continue

        else:
            print("Column is not present.")


    elif choice == "22":

        column_name = input("Enter your column name: ").strip()

        if column_name in df.columns:
            print("Column is present.")

            backup = df.copy()

            try:
                print("Length me sabhi characters count honge, jaise (.), (@), (-), space etc.")
                length = int(input("Enter length of column value: "))

                if length < 0:
                    print("Length cannot be negative.")
                    continue

                else:
                    filtered_df = df[df[column_name].astype(str).str.len() == length]

                    print("\nFiltered Data:\n")
                    print(filtered_df)

            except ValueError:
                print("Please enter only a number.")

        else:
            print("Column is not present.")
    
    elif choice == "23":

        if 'backup' in locals():
            df = backup.copy()
            print("Undo Successful")
        
        else:
            print("No backup available")

    elif choice=="24":

        file=input("Enter file name : ")

        try:
            if file.endswith(".csv"):
                df.to_csv(file, index=False)

            elif file.endswith(".xlsx"):
                df.to_excel(file, index=False)

            else:
                print("Unsupported file.")
                continue

            print("Saved Successfully.")

        except Exception as e:
            print("Error:", e)
        
    elif choice == "25":

        column_name = input("Enter numeric column name: ").strip()

        if column_name in df.columns:
            print("Column is present.")

            backup = df.copy()

            temp = pd.to_numeric(df[column_name], errors="coerce")

            invalid = df.loc[
                temp.isna() & df[column_name].notna(),
                [column_name]
            ]

            if invalid.empty:
               print("No invalid values found.")
 
            else:
                print("\nInvalid values found:\n")
                print(invalid)

                while True:

                    old = input("\nEnter invalid value to replace (or 'exit'): ")

                    if old.lower() == "exit":
                        break

                    new = input("Enter new numeric value: ")

                    df[column_name] = df[column_name].replace(old, new)

                    temp = pd.to_numeric(df[column_name], errors="coerce")

                    invalid = df.loc[
                        temp.isna() & df[column_name].notna(),
                        [column_name]
                    ]

                    if invalid.empty:
                        print("All invalid values corrected.")
                        break

                    else:
                        print("\nStill invalid values remaining:")
                        print(invalid)

        else:
            print("Column not found.")

    elif choice == "26":

        backup = df.copy()

        for col in df.select_dtypes(include="object"):

            # Object column me jahan bhi number ho detect karo
            mask = df[col].astype(str).str.contains(
                r"[+-]?\d+(\.\d+)?",
                regex=True,
                na=False
            )

            if mask.any():

                print(f"\nNumeric values found in '{col}':")
                print(df.loc[mask, [col]])

                option = input("Replace with (Unknown/NaN/Skip): ").strip().lower()

                if option == "unknown":
                    df.loc[mask, col] = "Unknown"
                    print(f"{col} updated successfully.")

                elif option == "nan":
                    df.loc[mask, col] = np.nan
                    print(f"{col} updated successfully.")

                elif option == "skip":
                    continue

                else:
                    print("Invalid option. Skipped.")

        print("\nChecking completed.")

    elif choice == "27":

        column = input("Enter numeric column name: ").strip()

        if column in df.columns:

            df[column] = pd.to_numeric(df[column], errors="coerce")

            negative = df[df[column] < 0]

            if negative.empty:
                print("No negative values found.")

            else:
                print("\nNegative values found:\n")
                print(negative[[column]])

                option = input(
                    "\nReplace with (0 / abs / median / delete / skip): "
                ).lower()

                backup = df.copy()

                if option == "0":
                    df.loc[df[column] < 0, column] = 0
                    print("Negative values replaced with 0.")

                elif option == "abs":
                    df[column] = df[column].abs()
                    print("Converted to absolute values.")

                elif option == "median":
                    median = df.loc[df[column] >= 0, column].median()
                    df.loc[df[column] < 0, column] = median
                    print("Negative values replaced with median.")

                elif option == "delete":
                    df = df[df[column] >= 0]
                    print("Rows containing negative values deleted.")

                elif option == "skip":
                    print("Skipped.")

                else:
                    print("Invalid option.")

        else:
            print("Column not found.")

    elif choice == "28":

        column = input("Enter numeric column name: ").strip()

        if column in df.columns:

            # Convert column to numeric
            df[column] = pd.to_numeric(df[column], errors="coerce")

            # Backup for Undo
            backup = df.copy()

            # Calculate IQR
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - (1.5 * IQR)
            upper = Q3 + (1.5 * IQR)

            # Find outliers
            outliers = df[(df[column] < lower) | (df[column] > upper)]

            if outliers.empty:
                print("No outliers found.")

            else:
                print("\nOutliers Found:\n")
                print(outliers)

                print(f"\nTotal Outliers : {len(outliers)}")

                print("\nChoose an option")
                print("1. Delete Outliers")
                print("2. Replace with Median")
                print("3. Replace with Mean")
                print("4. Skip")

                option = input("Enter choice : ")

                if option == "1":

                    df = df[(df[column] >= lower) & (df[column] <= upper)]

                    print("Outliers deleted successfully.")

                elif option == "2":

                    median = df[column].median()

                    df.loc[df[column] < lower, column] = median
                    df.loc[df[column] > upper, column] = median

                    print("Outliers replaced with median.")

                elif option == "3":
 
                    mean = df[column].mean()

                    df.loc[df[column] < lower, column] = mean
                    df.loc[df[column] > upper, column] = mean

                    print("Outliers replaced with mean.")

                elif option == "4":

                    print("Operation skipped.")

                else:

                    print("Invalid choice.")

        else:

            print("Column not found.")
    
    elif choice=="29":
        date_column = input("Enter Date column name:")
        
        if date_column in df.columns:
            print("Column is present")
        
            # Date column ko datetime me convert
            df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce",
            dayfirst=True
            )

            # Invalid dates check karo
            invalid_dates = df[df[date_column].isna()]

            print("Invalid Dates:")
            print(invalid_dates)


            # Ya invalid dates ko blank/NaT hi rakhna ho:
            df[date_column] = df[date_column].fillna(pd.NaT)

            print("\nCleaned Order Date:")
            print(df[date_column])
        else:
            print("Column is not present")
            
    elif choice=="30":

        print("Thank You")

        break

    else:
        print("Invalid option. Please try again.")