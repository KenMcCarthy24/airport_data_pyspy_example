import pandas as pd
import numpy as np
import time


def haversine(lat_1, lon_1, lat_2, lon_2):
    """Calculate the Haversine Distance between two latitude and longitude points"""
    lat_1_rad = np.radians(lat_1)
    lon_1_rad = np.radians(lon_1)
    lat_2_rad = np.radians(lat_2)
    lon_2_rad = np.radians(lon_2)

    delta_lat = lat_2_rad - lat_1_rad
    delta_lon = lon_2_rad - lon_1_rad

    R = 6371  # Radius of the earth in km

    return 2*R*np.asin(np.sqrt(np.sin(delta_lat/2)**2 + np.cos(lat_1_rad)*np.cos(lat_2_rad)*(np.sin(delta_lon/2))**2))


if __name__ == '__main__':
    # Load in flight data to a dataframe
    flight_data_file = r"./data/2025_flight_data.csv"
    flights_df = pd.read_csv(flight_data_file)

    # Start timer to see how long analysis takes
    start = time.time()

    # Calculate the haversine distance between each flight's start and end airport
    flights_df["Distance"] = haversine(lat_1=flights_df["LATITUDE_ORIGIN"],
                                       lon_1=flights_df["LONGITUDE_ORIGIN"],
                                       lat_2=flights_df["LATITUDE_DEST"],
                                       lon_2=flights_df["LONGITUDE_DEST"])

    # Get result by grouping by origin airport, taking the average flight distance and printing the top 5
    result = (
        flights_df
        .groupby('DISPLAY_AIRPORT_NAME_ORIGIN').agg(avg_dist=('Distance', 'mean'))
        .sort_values('avg_dist', ascending=False)
    )

    print(result.head(5))

    # End timer and print analysis time
    end = time.time()
    print(f"Took {end - start} s")
