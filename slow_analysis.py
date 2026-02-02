import pandas as pd
import math
import time


def haversine(lat_1, lon_1, lat_2, lon_2):
    """Calculate the Haversine Distance between two latitude and longitude points"""
    lat_1_rad = math.radians(lat_1)
    lon_1_rad = math.radians(lon_1)
    lat_2_rad = math.radians(lat_2)
    lon_2_rad = math.radians(lon_2)

    delta_lat = lat_2_rad - lat_1_rad
    delta_lon = lon_2_rad - lon_1_rad

    R = 6371  # Radius of the earth in km

    return 2*R*math.asin(math.sqrt(math.sin(delta_lat/2)**2 + math.cos(lat_1_rad)*math.cos(lat_2_rad)*(math.sin(delta_lon/2))**2))


if __name__ == '__main__':
    # Load in flight data to a dataframe
    flight_data_file = r"./data/2025_flight_data.csv"
    flights_df = pd.read_csv(flight_data_file)

    # Start timer to see how long analysis takes
    start = time.time()

    # Calculate the haversine distance between each flight's start and end airport
    haversine_dists = []
    for i, row in flights_df.iterrows():
        haversine_dists.append(haversine(lat_1=row["LATITUDE_ORIGIN"],
                                         lon_1=row["LONGITUDE_ORIGIN"],
                                         lat_2=row["LATITUDE_DEST"],
                                         lon_2=row["LONGITUDE_DEST"]))

    flights_df["Distance"] = haversine_dists

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
