import pandas as pd

# Create a list of all the CSV file names
csv_file_names = []
for i in range(70):
    # Construct the CSV file name.
    file_name = 'Trip{}{:02d}.csv'.format('A' if i < 32 else 'B', i % 32 + 1)
    csv_file_names.append(file_name)

# Create a dictionary of the old and new column names
column_name_map = {
    0: 'time',
    1: 'Velocity',
    2: 'Elevation',
    3: 'Throttle',
    4: 'Motor_Torque',
    5: 'Longitudinal_Acceleration',
    6: 'Regenerative_Braking_Signal',
    7: 'Battery_Voltage',
    8: 'Battery_Current',
    9: 'Battery_Temperature',
    10: 'max_Battery_Temperature',
    11: 'SoC',
    12: 'displayed_SoC',
    13: 'min_SoC',
    14: 'max_SoC',
    15: 'Heating_Power_CAN',
    16: 'Heating_Power_LIN',
    17: 'Requested_Heating_Power',
    18: 'AirCon_Power',
    19: 'Heater_Signal',
    20: 'Heater_Voltage',
    21: 'Heater_Current',
    22: 'Ambient_Temperature',
    23: 'Coolant_Temperature_Heatercore',
    24: 'Requested_Coolant_Temperature',
    25: 'Coolant_Temperature_Inlet',
    26: 'Heat_Exchanger_Temperature',
    27: 'Cabin_Temperature_Sensor'
}



# Iterate over all the CSV files and rename the column names
for csv_file_name in csv_file_names:

    # Check if the CSV file is in the `./Measurement_Data/TripA` directory
    if csv_file_name.startswith('TripA'):
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv('./Measurement_Data/TripA/' + csv_file_name, encoding='mbcs', sep=";")

    # Check if the CSV file is in the `./Measurement_Data/TripB` directory
    elif csv_file_name.startswith('TripB'):
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv('./Measurement_Data/TripB/' + csv_file_name, encoding='mbcs', sep=";")

    # Rename the column names
    # print(len(df.columns))
    for i in range(len(df.columns)+1):
        df.columns.values[i] = column_name_map[i]


    # Write the DataFrame back to the CSV file
    if csv_file_name.startswith('TripA'):
        df.to_csv('./Measurement_Data/TripA/' + csv_file_name, index=False)
    elif csv_file_name.startswith('TripB'):
        df.to_csv('./Measurement_Data/TripB/' + csv_file_name, index=False)
