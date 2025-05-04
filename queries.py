from database import Session
from models import Station, Measurement

def run_queries():
    session = Session()

    print(f"Liczba stacji: {session.query(Station).count()}")

    print("\n--------------------------------------")
    print("Stacje w USA:")
    for station in session.query(Station).filter_by(country='US'):
        print(station.station, station.name)

    print("\n--------------------------------------")
    print("5 pierwszych stacji:")
    for station in session.query(Station).limit(5):
        print(station.station, station.name)

    print("\n--------------------------------------")
    print("Stacje z opadem większym niż 4:")
    for m in session.query(Measurement).filter(Measurement.precip > 4):
        print(m.station, m.date, m.precip)

    session.close()
