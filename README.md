# EPAI Session 16 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Context Manager". Context managers can be used in following scenarios-
- Open - Close
- Lock - Release
- Change - Reset
- Enter - Exit
- Start - Stop

## There are two assignment-
### Assignment 1
<p><i> The files are:

- personal_info.csv - personal information such as name, gender, etc. (one row per person)
- vehicles.csv - what vehicle people own (one row per person)
- employment.csv - where a person is employed (one row per person)
- update_status.csv - when the person's data was created and last updated

    Each file contains a key, SSN, which uniquely identifies a person. This key is present in all four files.
You are guaranteed that the same SSN value is present in every file, and that it only appears once per file.
In addition, the files are all sorted by SSN, i.e. the SSN values appear in the same order in each file. </p>

### Goal 1
<p> Your first task is to create iterators for each of the four files that contained cleaned up data, of the correct type (e.g. string, int, date, etc), and represented by a named tuple.
For now these four iterators are just separate, independent iterators.

### Solution Notebook: Session16.ipynb

### Solution:
We have created following iterators using Context managers while extracting data from files-

#### Helper functions
- get_datetime_object: Convert string into date time object
- cast_row: Function to cast the Row into proper data type

#### 1st Iterator for personal_info.csv
- read_personal_info: Generator to yield one row at a time from vechicles file as a named tuple
#### 2nd Iterator for vehicles.csv
- read_vehicles: Generator to yield one row at a time from personal_info file as a named tuple
#### 3rd Iterator for employment.csv
- Generator to yield one row at a time from employment file as a named tuple
#### 4th Iterator for update_status.csv
- read_updated_status: Generator to yield one row at a time from updated_status file as a named tuple

### Goal 2
<p>
Create a single iterable that combines all the columns from all the iterators.
The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match!
All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.
Make sure the SSN is not repeated 4 times - one time per row is enough!

### Solution:
We have created following iterators using Context managers while extracting data from files-
- entire_information: Yield combined information from personal_info, vechiles, employement and updates_status files
    ('ssn', 'first_name', 'last_name', 'gender', 'language', 'vehicle_make', 'vehicle_model',
    'model_year', 'employer', 'department', 'employee_id', 'last_updated', 'created')

### Goal 3
<p>
Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on the last_updated field from the status_update file.

### Solution:
We have created following iterators using Context managers while extracting data from files-
- latest_information: Yield latest combined information from personal_info, vechiles, employement and updates_status files
    ('ssn', 'first_name', 'last_name', 'gender', 'language', 'vehicle_make', 'vehicle_model',
    'model_year', 'employer', 'department', 'employee_id', 'last_updated', 'created')

### Goal 4
<p>
Find the largest group of car makes for each gender.
Possibly more than one such group per gender exists (equal sizes).

### Solution:
We have created following iterators using Context managers while extracting data from files-
- largest_group: Get the files and the gender type as input and return the largest groups for gender
