import pandas as pd

def compare_excel_files(file_path1, file_path2):
    df1 = pd.read_excel(file_path1)
    df2 = pd.read_excel(file_path2)
    common_columns = df1.columns.intersection(df2.columns)
    merged_df = pd.merge(df1, df2, on=list(common_columns), how='inner', suffixes=('_file1', '_file2'))
    
    return merged_df

file_path1 = 'C:\\Users\\hp\\OneDrive\\Desktop\\excel project\\BOMB1 (1).xlsx'
file_path2 = 'C:\\Users\\hp\\OneDrive\\Desktop\\excel project\\BOMB2 (1).xlsx'

similarities = compare_excel_files(file_path1, file_path2)
print("Similarities between the two Excel files:")
print(similarities)
