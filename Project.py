import pandas as pd
import numpy as np


# You are provided with a dataset containing information about products in a CSV file.
# The dataset has the following columns: Product ID, Product Name, Category, Price, and Description.
#
# Your task is to review the dataset and identify the cells with the following errors:
#
# 1. Missing values in any of the columns
# 2. Some product Names start with a blank space before the text
# 3. Incorrect data types in the Price column (e.g., non-numeric values)
# 4. Duplicate Product ID entries (indicate both cells)

def review_dataset(filename):
    df = pd.read_csv(filename)
    errors = []

    # 1. Missing values in any of the columns
    missing_values = df.isnull().any()
    for column, has_missing_values in missing_values.items():
        print(f"{column} a {has_missing_values}")
        if has_missing_values:
            error_cells = df[df[column].isnull()].index
            errors.append(f"Chybějící hodnoty ve sloupci '{column}': {', '.join(map(str, error_cells + 2))}")

    # 2. Product Names starting with a blank space
    leading_spaces = np.where(df['Product Name'].astype(str).str.startswith(' '))
    if leading_spaces[0].size > 0:
        error_cells = leading_spaces[0]
        errors.append(f"Názvy produktů začínající mezerou: {', '.join(map(str, error_cells + 2))}")

    # 3. Incorrect data types in the Price column
    incorrect_data_types = pd.to_numeric(df['Price'], errors='coerce').isnull()
    if incorrect_data_types.any():
        error_cells = df[incorrect_data_types].index
        errors.append(f"Špatné datové typy ve sloupci Price: {', '.join(map(str, error_cells + 2))}")

    # 4. Duplicate Product ID entries
    duplicate_ids = df.duplicated(subset='Product ID', keep=False)
    if duplicate_ids.any():
        duplicates = df[duplicate_ids]['Product ID'].unique()
        for id_value in duplicates:
            duplicate_indices = df[df['Product ID'] == id_value].index + 2
            errors.append(
                f"Duplicitní záznam produktového ID '{id_value}' v buňkách: {', '.join(map(str, duplicate_indices))}")

    return errors


if __name__ == '__main__':
    FILE_NAME = "assignment-database.csv"
    errors = review_dataset(FILE_NAME)
    if errors:
        error_report = "\n".join(errors)
        email_content = f"Níže najdete indentifikované chyby v datasetu:\n\n{error_report}\n"
        print(email_content)
    else:
        print("Žádné chyby v datasetu nebyly nalezeny.")
