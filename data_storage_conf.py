import pandas as pd

# write scraped page to an Excel file
def append_data_to_excel(filename, data):
    filepath = rf'{filename}'
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filepath, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        if 'mysheet' in writer.sheets:
            start_row = writer.sheets['mysheet'].max_row
        else:
            start_row = 0
        header = True if start_row == 0 else False
        df.to_excel(writer, startrow=start_row, index=False, header=header, sheet_name='mysheet')