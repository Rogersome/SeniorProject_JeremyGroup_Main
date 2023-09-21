import pandas as pd
import numpy as np


def predict_battery_health(battery_temperature, battery_voltage, battery_current, battery_power, battery_energy_used):
    """Predicts the battery health of a BMW i3 from 5 independent trips.

  Args:
    battery_temperature: A list of 5 battery temperatures, each in degrees Celsius.
    battery_voltage: A list of 5 battery voltages, each in volts.
    battery_current: A list of 5 battery currents, each in amps.
    battery_power: A list of 5 battery powers, each in watts.
    battery_energy_used: A list of 5 battery energy used, each in watt-hours.

  Returns:
    A float representing the predicted battery health, as a percentage.
  """

    # Calculate the average battery temperature, voltage, current, power, and energy used.
    average_battery_temperature = np.mean(battery_temperature)
    average_battery_voltage = np.mean(battery_voltage)
    average_battery_current = np.mean(battery_current)
    average_battery_power = np.mean(battery_power)
    average_battery_energy_used = np.mean(battery_energy_used)

    # Calculate the predicted battery health.
    predicted_battery_health = average_battery_power / 18000

    return predicted_battery_health


# Create a list to store the predicted battery health for each file.
predicted_battery_health_list = []

# Iterate over the 70 CSV files.
for i in range(70):
    # Construct the CSV file name.
    file_name = 'Trip{}{:02d}.csv'.format('A' if i < 32 else 'B', i % 32 + 1)

    # Construct the CSV file path.
    file_path = './Measurement_Data/Trip{}/{}'.format('A' if i < 32 else 'B', file_name)

    # Import the CSV file.
    df = pd.read_csv(file_path, encoding='mbcs')

    # Rename the titles
    df = df.rename(columns={
        'Time [s]': 'time',
        'Velocity [km/h]': 'Velocity',
        'Elevation [m]': 'Elevation',
        'Throttle [%]': 'Throttle',
        'Motor Torque [Nm]': 'Motor_Torque',
        'Longitudinal Acceleration [m/s^2]': 'Longitudinal_Acceleration',
        'Regenerative Braking Signal': 'Regenerative_Braking_Signal',
        'Battery Voltage [V]': 'Battery_Voltage',
        'Battery Current [A]': 'Battery_Current',
        'Battery Temperature [°C]': 'Battery_Temperature',
        'max. Battery Temperature [°C]': 'max_Battery_Temperature',
        'SoC [%]': 'SoC',
        'displayed SoC [%]': 'displayed_SoC',
        'min. SoC [%]': 'min_SoC',
        'max. SoC [%]': 'max_SoC',
        'Heating Power CAN [kW]': 'Heating_Power_CAN',
        'Heating Power LIN [W]': 'Heating_Power_LIN',
        'Requested Heating Power [W]': 'Requested_Heating_Power',
        'AirCon Power [kW]': 'AirCon_Power',
        'Heater Signal': 'Heater_Signal',
        'Heater Voltage [V]': 'Heater_Voltage',
        'Heater Current [A]': 'Heater_Current',
        'Ambient Temperature [°C]': 'Ambient_Temperature',
        'Coolant Temperature Heatercore [°C]': 'Coolant_Temperature_Heatercore',
        'Requested Coolant Temperature [°C]': 'Requested_Coolant_Temperature',
        'Coolant Temperature Inlet [°C]': 'Coolant_Temperature_Inlet',
        'Heat Exchanger Temperature [°C]': 'Heat_Exchanger_Temperature',
        'Cabin Temperature Sensor [°C]': 'Cabin_Temperature_Sensor'
    })

    # df = df.rename(columns=lambda x: x.lower())

    print(df.head())
    #
    # # Extract the battery temperature, voltage, current, power, and energy used columns.
    # battery_temperature = df['battery_temperature'].tolist()
    # battery_voltage = df['battery_voltage'].tolist()
    # battery_current = df['battery_current'].tolist()
    # battery_power = df['battery_power'].tolist()
    # battery_energy_used = df['battery_energy_used'].tolist()
    #
    # # Predict the battery health.
    # predicted_battery_health = predict_battery_health(battery_temperature, battery_voltage, battery_current,
    #                                                   battery_power, battery_energy_used)
    #
    # # Add the predicted battery health to the list.
    # predicted_battery_health_list.append(predicted_battery_health)

# Calculate the average predicted battery health.
average_predicted_battery_health = np.mean(predicted_battery_health_list)

print("Average predicted battery health:", average_predicted_battery_health)
