import sqlite3
import csv

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS stations (
    station TEXT PRIMARY KEY,
    latitude REAL,
    longitude REAL,
    elevation REAL,
    name TEXT,
    country TEXT,
    state TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS measurements (
    station TEXT,
    date TEXT,
    precip REAL,
    tobs REAL,
    FOREIGN KEY (station) REFERENCES stations (station)
)
''')

with open('clean_stations.csv', mode='r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute('''
        INSERT OR REPLACE INTO stations (station, latitude, longitude, elevation, name, country, state)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
        row['station'], row['latitude'], row['longitude'], row['elevation'], row['name'], row['country'], row['state']))

with open('clean_measure.csv', mode='r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute('''
        INSERT OR REPLACE INTO measurements (station, date, precip, tobs)
        VALUES (?, ?, ?, ?)
        ''', (row['station'], row['date'], row['precip'], row['tobs']))

conn.commit()


count_stations = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()
print(f"Liczba stacji: {count_stations[0]}")
country = 'US'
stations_in_country = cursor.execute("SELECT * FROM stations WHERE country = ?", (country,)).fetchall()
print("--------------------------------------")
print("Stacje w USA")
for station in stations_in_country:
    print(station)

rows = cursor.execute("SELECT * FROM stations LIMIT 5").fetchall()
print("--------------------------------------")
print("5 pierwszych stacji:")
for row in rows:
    print(row)

heavy_precip = cursor.execute("""
    SELECT station, date, precip FROM measurements
    WHERE precip > 4
""").fetchall()
print("--------------------------------------")
print("Stacje z opadem większym niż 4")
for data in heavy_precip:
    print(data)

conn.close()
