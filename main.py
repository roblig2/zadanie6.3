from database import init_db
from load_data import load_stations, load_measurements
from queries import run_queries


def main():
    init_db()
    load_stations("clean_stations.csv")
    load_measurements("clean_measure.csv")
    run_queries()


if __name__ == "__main__":
    main()
