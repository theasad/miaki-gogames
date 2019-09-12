import csv
import datetime
import sys
from urllib.request import urlretrieve

csv_file_name = "bicycle-travels-jan-2018.csv"

url = "https://press.radiocut.fm/bicycle-travels-jan-2018.csv"

error = False

# Check file if exist then save to disk
try:
    print("Downloading csv.....................")
    urlretrieve(url, csv_file_name)
except Exception as e:
    error = True
    print(e)  # File doesn't exists

if not error:
    with open(csv_file_name, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        results = {}
        print("Filtering data...........................")
        for row in csv_reader:
            hour = datetime.datetime.strptime(
                row['pickup_time'], '%Y-%m-%d %H:%M:%S').time().hour  # Get Hour from pickup time
            if 6 <= hour < 12:  # filter all values where time start from 6AM to 11:59:59

                # Check station code already exists or not in result disctionary
                if row['source_station_code'] in results:
                    # station already exists then increase total trip values
                    results[row['source_station_code']]['total_trip'] += 1
                else:
                    # set inital value for new station
                    results[row['source_station_code']] = {
                        'source_station_code': row['source_station_code'],
                        'source_station_name': row['source_station_name'],
                        'total_trip': 1
                    }

        # Get top five
        top_source_stations = dict(
            sorted(results.items(), key=lambda x: -x[1]['total_trip'])[:5])

        sys.stdout.write('\n')
        sys.stdout.write('Top five source stations:')
        sys.stdout.write('\n')
        for key in top_source_stations:
            station = top_source_stations[key]
            sys.stdout.write('{} (code: {}): {} trips'.format(
                station['source_station_name'], station['source_station_code'], str(station['total_trip'])))
            sys.stdout.write('\n')
