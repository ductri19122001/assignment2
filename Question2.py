
#qn2

import csv
import os

# Directory
directory = "./temperature_data"
temperature_data = []

# Sorts Files in Directory
files = sorted(os.listdir(directory))

# Process each file in the folder
for file in files:
    if file.endswith(".csv"):
        file_path = os.path.join(directory,file)

        with open(file_path, mode = 'r') as file:
            reader = csv.DictReader(file)
            
            #Extracts temperatures for each month
            for row in reader:
                temps={}
                stations={}
                for month in ["January","February","March","April","May","June","July","August","September","October","November","December"]:
                    if month in row:
                        temps[month] = float(row[month])

                #Extract station name
                if "STATION_NAME" in row:
                    stations = row["STATION_NAME"]

                #Stores data for each station
                if stations:
                    station_data = {
                        "Station_Name" : stations,
                        "Temperatures" : temps
                        }
                temperature_data.append(station_data)


def avg():
    # Summer : Dec to Feb
    # Autumn : Mar to May
    # Winter : Jun to Aug
    # Spring : Sep to Nov

    # Seasons
    seasons = {
        "Summer" : ["December","January","February"],
        "Autumn" : ["March", "April", "May"],
        "Winter" : ["June","July","August"],
        "Spring" : ["September","October","November"]
    }

    # Data in each season
    seasons_data={
        "Summer" : {"sum": 0, "count": 0},
        "Autumn" : {"sum": 0, "count": 0},
        "Winter" : {"sum": 0, "count": 0},
        "Spring" : {"sum": 0, "count": 0}
    }
    # Go through each temp in each station
    for station in temperature_data:
        temperatures = station["Temperatures"]

    # Adds temps for each month in the season
        for month, temp in temperatures.items():
            if month in seasons["Summer"]:
                seasons_data["Summer"]["sum"] +=temp
                seasons_data["Summer"]["count"] +=1
            elif month in seasons["Autumn"]:
                seasons_data["Autumn"]["sum"] +=temp
                seasons_data["Autumn"]["count"] +=1
            elif month in seasons["Winter"]:
                seasons_data["Winter"]["sum"] +=temp
                seasons_data["Winter"]["count"] +=1
            elif month in seasons["Spring"]:
                seasons_data["Spring"]["sum"] +=temp
                seasons_data["Spring"]["count"] +=1

    # Calculate averages for each season
    averages = {}
    
    for season, data in seasons_data.items():
        averages[season] = data["sum"] / data["count"]
        print(averages)
    # Results to text file
    with open("average_temp.txt", "w") as f:
     for season, avg_temp in averages.items():
            f.write(f"{season}: {avg_temp:.2f}C\n")
            

    print("avg temps have been save as 'average_temp.txt'")
avg()
def temp_range():
    
    station_ranges = {}

    # Range for each station
    for station in temperature_data:
        station_name = station["Station_Name"]
        temperatures = station["Temperatures"].values()

        # Finding the range
        temp_range = max(temperatures) - min(temperatures)
        station_ranges[station_name] = temp_range

    # Maximum temperature range
    max_range = max(station_ranges.values())

    # In case of multiple maximum ranges
    largest_stations_ranges = [
        station for station, temp_range in station_ranges.items() if temp_range == max_range
    ]

    # Save results to file
    output_path = "largest_temp_range_station.txt"
    with open(output_path, "w") as f:
        f.write(f"Largest Temperature Range: {max_range:.2f}C\n")
        f.write("Station(s):\n")
        for station in largest_stations_ranges:
            f.write(f"{station}\n")
temp_range()
def warm_cool():
    # Store average temp for each station
    station_avg = {}

    # Calculate average temp
    for station in temperature_data:
        station_name = station["Station_Name"]
        temperatures = station["Temperatures"].values()
        
        avg_temp = sum(temperatures)/ len(temperatures)
        station_avg[station_name] = avg_temp

    # Find warmest and coolest stations
    max_avg = max(station_avg.values())
    min_avg = min(station_avg.values())

    # Identify stations with highest and lowest average temps

    warmest = [
        station for station, avg_temp in station_avg.items() if avg_temp == max_avg
    ]
    coolest = [
        station for station, avg_temp in station_avg.items() if avg_temp == min_avg
    ]

    # Save results to file
    with open("warmest_and_coolest_station.txt", "w") as f:
     f.write(f"Warmest Station(s) - Average Temperature: {max_avg:.2f}C\n")
     for station in warmest:
            f.write(f"{station}\n")
     f.write("\n")
     f.write(f"Coolest Station(s) - Average Temperature: {min_avg:.2f}C\n")
     for station in coolest:
            f.write(f"{station}\n")

warm_cool()

