# session16.py
# imports
from datetime import datetime
from collections import namedtuple
from collections import Counter
from contextlib import contextmanager
import csv

def get_datetime_object(date_time):
    """Convert the datetime string to date time object"""
    datetime_str = date_time
    datetime_str = datetime_str[:10]+' '+datetime_str[11:-1]
    return(datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S'))

def cast_row(row,file_name):
    """Function to cast the Row into proper data type"""
    if file_name == 'vehicles.csv':
        row[3] = int(row[3]) # Year
    elif file_name == 'update_status.csv':
        row[1] = get_datetime_object(row[1]) # last_update
        row[2] = get_datetime_object(row[2]) # last_update
    return row

### 1st Iterator for personal_info.csv
def read_personal_info(file_name):
    """Generator to yield one row at a time from personal_info file as a named tuple"""
    with open(file_name) as file:
        dialect = csv.Sniffer().sniff(file.readline(), [',',';'])
        file.seek(0)
        rows = csv.reader(file, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
        headers = next(rows)
        headers = (item.replace(" ", "_") for item in headers)
        Personal_Info = namedtuple('Personal_Info', headers) # Create named tuple type
        for row in rows:
            personal_info = Personal_Info(*row) # Create named tuple type
            yield personal_info

### 2nd Iterator for vehicles.csv
def read_vehicles(file_name):
    """Generator to yeild one row at a time from vechicles file as a named tuple"""
    with open(file_name) as file:
        dialect = csv.Sniffer().sniff(file.readline(), [',',';'])
        file.seek(0)
        rows = csv.reader(file, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
        headers = next(rows)
        headers = (item.replace(" ", "_") for item in headers)
        Vehicles = namedtuple('Vehicles', headers) # Create named tuple type
        for row in rows:
            row = cast_row(row,file_name) # cast to the data types
            vehicles = Vehicles(*row) # Create named tuple type
            yield vehicles

### 3rd Iterator for employment.csv
def read_employment(file_name):
    """Generator to yeild one row at a time from employment file as a named tuple"""
    with open(file_name) as file:
        dialect = csv.Sniffer().sniff(file.readline(), [',',';'])
        file.seek(0)
        rows = csv.reader(file, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
        headers = next(rows)
        headers = (item.replace(" ", "_") for item in headers)
        Employment = namedtuple('Employment', headers) # Create named tuple type
        for row in rows:
            row = cast_row(row,file_name) # cast to the data types
            employment_info = Employment(*row) # Create named tuple type
            yield employment_info

### 4th Iterator for update_status.csv
def read_updated_status(file_name):
    """Generator to yeild one row at a time from updated_status file as a named tuple"""
    with open(file_name) as file:
        dialect = csv.Sniffer().sniff(file.readline(), [',',';'])
        file.seek(0)
        rows = csv.reader(file, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
        headers = next(rows)
        headers = (item.replace(" ", "_") for item in headers)
        Status = namedtuple('Status', headers) # Create named tuple type
        for row in rows:
            row = cast_row(row,file_name) # cast to the data types
            status_info = Status(*row) # Create named tuple type
            yield status_info

# Create a single iterable that combines all the columns from all the iterators.
def entire_information(f_personal_info,f_vehicles_info,f_emp_info,f_status):
    """
    Yield combined information from personal_info, vechiles, employement and updates_status files
    ('ssn', 'first_name', 'last_name', 'gender', 'language', 'vehicle_make', 'vehicle_model',
    'model_year', 'employer', 'department', 'employee_id', 'last_updated', 'created')
    """
    file_list = [f_personal_info,f_vehicles_info,f_emp_info,f_status]

    # Get header Info

    final_header=[]
    for file in file_list:
        with open(file) as f:
            dialect = csv.Sniffer().sniff(f.readline(), [',',';'])
            f.seek(0)
            rows = csv.reader(f, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
            headers = next(rows)
            if file != 'personal_info.csv':
                headers = [item.replace(" ", "_") for item in headers]
                headers.remove('ssn')
                final_header += headers # only one SSN
            else:
                headers = [item.replace(" ", "_") for item in headers]
                final_header = headers
    Total_Info = namedtuple('Total_Info', final_header) # Create named tuple type

    # Get information
    per_info = read_personal_info(file_list[0])
    vech_info = read_vehicles(file_list[1])
    emp_info = read_employment(file_list[2])
    status_info = read_updated_status(file_list[3])

    for  i in per_info: # Considering all files are of same length, iterate over
        info = next(per_info) + next(vech_info)[1:] + next(emp_info)[0:-1] + next(status_info)[1:]
        total_info = Total_Info(*info)

        yield total_info

# Create an iterator that only contains current records (i.e. not stale) based on the last_updated field from the status_update file.
def latest_information(f_personal_info,f_vehicles_info,f_emp_info,f_status):
    """
    Yield combined information latest from personal_info, vechiles, employement and updates_status files
    ('ssn', 'first_name', 'last_name', 'gender', 'language', 'vehicle_make', 'vehicle_model',
    'model_year', 'employer', 'department', 'employee_id', 'last_updated', 'created')
    """
    file_list = [f_personal_info,f_vehicles_info,f_emp_info,f_status]

    # Get header Info

    final_header=[]
    for file in file_list:
        with open(file) as f:
            dialect = csv.Sniffer().sniff(f.readline(), [',',';'])
            f.seek(0)
            rows = csv.reader(f, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
            headers = next(rows)
            if file != 'personal_info.csv':
                headers = [item.replace(" ", "_") for item in headers]
                headers.remove('ssn')
                final_header += headers # only one SSN
            else:
                headers = [item.replace(" ", "_") for item in headers]
                final_header = headers
    Total_Info = namedtuple('Total_Info', final_header) # Create named tuple type

    # Get information
    per_info = read_personal_info(file_list[0])
    vech_info = read_vehicles(file_list[1])
    emp_info = read_employment(file_list[2])
    status_info = read_updated_status(file_list[3])

    for  i in per_info: # Considering all files are of same length, iterate over
        info = next(per_info) + next(vech_info)[1:] + next(emp_info)[0:-1] + next(status_info)[1:]
        total_info = Total_Info(*info)
        if total_info.last_updated.date() > datetime.strptime('3/1/2017', '%m/%d/%Y').date(): # yield only current records
            yield total_info

# Find the largest group of car makes for each gender.
def largest_group(f_personal_info,f_vehicles_info,f_emp_info,f_status,gender):
    """
    Get the files and the gender type as input and return the largest groups for gender
    """

    total_info = entire_information(f_personal_info,f_vehicles_info,f_emp_info,f_status)
    info_list = (row.vehicle_make for row in total_info if row.gender == gender)
    car_makers = Counter(info_list)

    x = [v for v in car_makers.values()]

    highest_value = max(x)
    top_car_maker = [k for k,v in car_makers.items() if v == highest_value]

    return top_car_maker

# Assignment 2
# 1 create a context manager that you can use to produce the data from each file in a named tuple with field
# names corresponding to the header row field names.
class CustomContextManager:
    """Custom context manager class to read a read file"""
    def __init__(self, fname):
        self._fname = fname
        self._f = None

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._rows)

    def __enter__(self):
        print('opening file...')
        self._f = open(self._fname)
        dialect = csv.Sniffer().sniff(self._f.readline(), [',',';'])
        self._f.seek(0)
        self._rows = csv.reader(self._f, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('closing file...')
        if not self._f.closed:
            self._f.close()
        return False

def get_rows_from_file(fname):
    """Generator to parse file in lazy mode (generating one row at a time)"""
    with CustomContextManager(fname) as f:
        headers = next(f)
        headers = (item.replace(" ", "_") for item in headers)
        RowData = namedtuple('RowData', headers)
        for row in f:
            yield RowData(*row)

@contextmanager
def StandardContextManager(fname):
    """
    Use inbuilt context manager to read the file
    """
    print('opening file...')
    f = open(fname)
    dialect = csv.Sniffer().sniff(f.readline(), [',',';'])
    f.seek(0)
    rows = csv.reader(f, delimiter=dialect.delimiter, quotechar=dialect.quotechar)
    try:
        yield rows
    finally:
        print('closing file...')
        f.close()

def get_rows_from_file_standard(fname):
    """Generator to parse file in lazy mode (generating one row at a time)"""
    with StandardContextManager(fname) as f:
        headers = next(f)
        headers = (item.replace(" ", "_") for item in headers)
        RowData = namedtuple('RowData', headers)
        for row in f:
            yield RowData(*row)
