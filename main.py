import csv_pack
# Take
filename = raw_input("Enter File Name:")

csv_process = csv_pack.ProcessCSV(filename,"")
csv_process.read_file()

