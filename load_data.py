import csv
from models import Station, Measurement
from database import Session

def load_stations(csv_path):
    session = Session()
    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            station = Station(
                station=row['station'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                elevation=row['elevation'],
                name=row['name'],
                country=row['country'],
                state=row['state']
            )
            session.merge(station)
    session.commit()
    session.close()

def load_measurements(csv_path):
    session = Session()
    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            measurement = Measurement(
                station=row['station'],
                date=row['date'],
                precip=row['precip'] or None,
                tobs=row['tobs'] or None
            )
            session.merge(measurement)
    session.commit()
    session.close()
