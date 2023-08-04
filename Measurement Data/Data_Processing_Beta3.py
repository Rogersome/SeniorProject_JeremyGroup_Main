import pandas as pd
import numpy as np
import sqlite3

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 50)

# Create a list of file names
filenames = ["TripA01.csv", "TripA02.csv", "TripA03.csv", "TripA04.csv", "TripA05.csv", "TripA06.csv", "TripA07.csv",
             "TripA08.csv", "TripA09.csv", "TripA10.csv", "TripA11.csv", "TripA12.csv", "TripA13.csv", "TripA14.csv",
             "TripA15.csv", "TripA16.csv", "TripA17.csv", "TripA18.csv", "TripA19.csv", "TripA20.csv", "TripA21.csv",
             "TripA22.csv", "TripA23.csv", "TripA24.csv", "TripA25.csv", "TripA26.csv", "TripA27.csv", "TripA28.csv",
             "TripA29.csv", "TripA30.csv", "TripA31.csv", "TripA32.csv"]

data = []
for file in filenames:
    df_TripA = pd.read_csv(file, sep=';', index_col='Time [s]', encoding="ANSI")
    data.append(df_TripA)

col_names = df_TripA.columns.values


def connect_to_db():
    conn = sqlite3.connect("Trips_A.DB")
    return conn


class Trips_A:
    conn = connect_to_db()
    cur = conn.cursor()

    # Create trip01 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip01(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()


class AllTrip:
    conn = connect_to_db()
    cur = conn.cursor()

    # Create trip01 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip01(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create trip02 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip02(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create trip03 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip03(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create trip04 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip04(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip05 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip05(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip06 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip06(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip07 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip07(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip08 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip08(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip09 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip09(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip10 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip10(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip11 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip11(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip12 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip12(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip13 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip13(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip14 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip14(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip15 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip15(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip16 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip16(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip17 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip17(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip18 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip18(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip19 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip19(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip20 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip20(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip21 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip21(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip22 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip22(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip23 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip23(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip24 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip24(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip25 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip25(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip26 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip26(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip27 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip27(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip28 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip28(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip29 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip29(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip30 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip30(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip31 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip31(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()

    # Create Trip32 table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Trip32(
            Trip TEXT PRIMARY KEY NOT NULL,
            Time Float NOT NULL,
            Velocity [km/h] Float NOT NULL,
            Elevation [m] Float NOT NULL,
            Throttle [%] Float NOT NULL,
            Motor_Torque [Nm] Float NOT NULL,
            Longitudinal_Acceleration [m/s^2] Float NOT NULL,
            Regenerative_Braking Signal  Float NOT NULL,
            Battery_Voltage [V] Float NOT NULL,
            Battery_Current [A] Float NOT NULL,
            Battery_Temperature [C] Float NOT NULL,
            max_Battery_Temperature [C] Float NOT NULL,
            SoC [%] Float NOT NULL,
            displayed_SoC [%] Float NOT NULL,
            min_SoC [%] Float NOT NULL,
            max_SoC [%) Float NOT NULL,
            Heating_Power_CAN [kW] Float NOT NULL,
            Heating_Power_LIN [W] Float NOT NULL,
            Requested_Heating Power [W] Float NOT NULL,
            AirCon_Power [kW] Float NOT NULL,
            Heater_Signal Float NOT NULL,
            Heater_Voltage [V] Float NOT NULL,
            Heater_Current [A] Float NOT NULL,
            Ambient_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Heatercore [C] Float NOT NULL,
            Requested_Coolant_Temperature [C] Float NOT NULL,
            Coolant_Temperature_Inlet [C] Float NOT NULL,
            Heat_Exchanger_Temperature [C] Float NOT NULL,
            Cabin_Temperature_Sensor [C] Float NOT NULL
            )
        """
    )
    conn.commit()
