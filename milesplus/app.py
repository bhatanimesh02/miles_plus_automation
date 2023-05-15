import csv, json, openpyxl, os, shutil, argparse
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Border, Side

#=============================  setting paths for folders =======================================================

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--source', type=str)
parser.add_argument('-b', '--destination', type=str)
args = parser.parse_args()
source_folder = args.source
# "https://github.com/bhatanimesh02/miles_plus_automation/tree/main/txt"
# "C:\Users\A200181885\Desktop\txt_to_csv\v2\txt\\"
os.chdir(source_folder)

destination_folder = args.destination
# "https://github.com/bhatanimesh02/miles_plus_automation/tree/main/csv"
# "C:\Users\A200181885\Desktop\txt_to_csv\v2\csv\\"

#=============================  fucntion to convert txt to csv ==================================================

def convert_files(file_path):
    with open(file_path, 'r') as file:
        file_name = os.path.basename(file_path)
        fname = os.path.splitext(file_name)[0]
        # print(fname)
        input_data = []
        for record in file.readlines()[1:]:
            input_record = record.split(";")[:-2]
            input_record = [x.replace('"', '') for x in input_record]
            input_data.append(input_record)
        # print(pd.DataFrame(input_data[1:], columns=input_data[0]))
        input_data = pd.DataFrame(input_data[1:], columns=input_data[0])
        # print(input_data.columns)
        
        #=============================  splitting into 2 columns =================================================

        contract_abbreviation_column = input_data.columns[-1]
        contract_no = input_data[contract_abbreviation_column].apply(lambda x:x.split(" ")[0])
        # print(contract_no)
        abbreviation = input_data[contract_abbreviation_column].apply(lambda x:x.split(" ")[1:])
        # print(abbreviation)
        abbreviation = [" ".join(x) for x in abbreviation]
        input_data['Miles+ Code'] = contract_no
        input_data['abbreviation'] = abbreviation
        input_data.drop(contract_abbreviation_column,axis=1, inplace=True)
        input_data.to_csv(fname+".csv", index=False)     #output_with_two_columns

        #=============================  splitting into 3 columns  =================================================

        new_abbreviation_column = input_data.columns[-1]
        first_abbreviation = input_data[new_abbreviation_column].apply(lambda x: '-'.join(x.split("-")[:-1]) )
        # print(first_abbreviation)
        second_abbreviation = input_data[new_abbreviation_column].apply(lambda x:x.split("-")[-1])
        # print(second_abbreviation)
        second_abbreviation = ["".join(x) for x in second_abbreviation]
        # print(second_abbreviation)   
        input_data['Activity- Rate type'] = first_abbreviation
        input_data['Activity Type'] = second_abbreviation
        input_data.drop(new_abbreviation_column,axis=1, inplace=True)
        input_data.to_csv(fname+".csv", index=False)     #output_with_three_columns

    #=============================  applying borders to CSV files =======================================================
    
    with open(fname+".csv", 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    wb = Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)
    border = Border(left=Side(style='thin'), 
                    right=Side(style='thin'), 
                    top=Side(style='thin'), 
                    bottom=Side(style='thin'))
    for row in ws.rows:
        for cell in row:
            cell.border = border
    wb.save(fname+".csv")

#=============================  End of the fucntion=================================================================

#=============================  Reading multiple files and calling the convert function ============================
for file in os.listdir():
   if file.endswith('.txt'):
      # Create the filepath of particular file
      file_path =f"{source_folder}/{file}" 
    #   print(file_path)
      convert_files(file_path)
    #   print(file+' : Converted')


#=============================  Moving CSV files to CSV folder =====================================================
for file in os.listdir(source_folder):
    if file.endswith(".csv"):
        source = source_folder + file
        destination = destination_folder + file
        shutil.move(source, destination)
        print(file+' : Moved to '+destination_folder)
