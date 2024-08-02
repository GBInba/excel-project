import pandas as pd

def find_differences(df1, df2):
    common_columns = df1.columns.intersection(df2.columns)
    merged = df1.merge(df2, on=list(common_columns), how='outer', indicator=True)
    diff_df1 = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])
    diff_df2 = merged[merged['_merge'] == 'right_only'].drop(columns=['_merge'])
    return diff_df1, diff_df2

def compare_excel_files(file_path1, file_path2):
    df1 = pd.read_excel(file_path1)
    df2 = pd.read_excel(file_path2)
    differences_file1, differences_file2 = find_differences(df1, df2)
    return differences_file1, differences_file2
file_path1 = 'C:\\Users\\hp\\OneDrive\\Desktop\\excel project\\BOMB1 (1).xlsx'
file_path2 = 'C:\\Users\\hp\\OneDrive\\Desktop\\excel project\\BOMB2 (1).xlsx'
differences_file1, differences_file2 = compare_excel_files(file_path1, file_path2)
print("Rows in the first file but not in the second file:")
print(differences_file1)
print("\nRows in the second file but not in the first file:")
print(differences_file2)
