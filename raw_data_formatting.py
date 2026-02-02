import pandas as pd

airports_data_file = "./data/airport_info.csv"

flight_data_files = [r".\data\01_2025_flight_data.csv",
                     r".\data\02_2025_flight_data.csv",
                     r".\data\03_2025_flight_data.csv",
                     r".\data\04_2025_flight_data.csv",
                     r".\data\05_2025_flight_data.csv",
                     r".\data\06_2025_flight_data.csv"]

airports_df = pd.read_csv(airports_data_file)

flights_dfs = []
for flights_df in flight_data_files:
    flights_dfs.append(pd.read_csv(flights_df))

flights_df = (
    pd.concat(flights_dfs)
    .merge(airports_df.filter(["AIRPORT_SEQ_ID", "DISPLAY_AIRPORT_NAME", "LATITUDE", "LONGITUDE"]),
           left_on="ORIGIN_AIRPORT_SEQ_ID", right_on="AIRPORT_SEQ_ID")
    .merge(airports_df.filter(["AIRPORT_SEQ_ID", "DISPLAY_AIRPORT_NAME", "LATITUDE", "LONGITUDE"]),
           left_on="DEST_AIRPORT_SEQ_ID", right_on="AIRPORT_SEQ_ID", suffixes=("_ORIGIN", "_DEST"))
    .filter(["FL_DATE", "ORIGIN", "DISPLAY_AIRPORT_NAME_ORIGIN", "LATITUDE_ORIGIN", "LONGITUDE_ORIGIN",
             "DEST", "DISPLAY_AIRPORT_NAME_DEST", "LATITUDE_DEST", "LONGITUDE_DEST"])
)

out_file = r".\data\2025_flight_data.csv"
flights_df.to_csv(out_file, index=False)
