Above CSV files are seperated with semicolon instead of comma
The encoding method used for the CSV files is ANSI

To read CSV file using python pandas:
pd.read_csv(file, sep=';', encoding="ANSI")

To read CSV file using python pandas and using 'Time [s]' column as index:
pd.read_csv(file, sep=';', index_col='Time [s]', encoding="ANSI")


##### ANY UPDATES ON ERRORS OR NON-DEFAULT METHOD WILL BE POSTED HERE #####