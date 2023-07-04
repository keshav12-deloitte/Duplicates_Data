import pandas as pd
import json


def excel_to_jsonl(excel_file, jsonl_file):
    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Convert DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')

    # Write data to JSONL file
    with open(jsonl_file, 'w') as outfile:
        for entry in data:
            json.dump(entry, outfile)
            outfile.write('\n')


# Specify the paths of the Excel and JSONL files
excel_file = '/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/resources/Duplicate_generator.xlsx'
jsonl_file = '/Users/amananand7/PycharmProjects/automatAI_Duplicate_DRY/resources/data.jsonl'

# Call the function to convert Excel to JSONL
excel_to_jsonl(excel_file, jsonl_file)
