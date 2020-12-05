# EPAI Session 15 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Generators and Iteration tools". Here we went through concepts of Generators and Iter tools. The "yield" keyword is used to convert a function into a generator object. Generators are executed in a lazy manner and hence we have a benefits like no need to process the entire dataset unless needed and no need to hold the memory for entire objects. For this assignment we have two goals -
1. Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc..
2. Calculate the number of violations by car make.

Solution:-

**session15.pynb file**

https://github.com/SachinDangayach/session15-SachinDangayach/blob/master/session15.ipynb


### For goal one, We have implemented following function-
  - 1. Function cast_row: Function takes input as string for line of file and typecast the integer and date type objects from string to respective types.
  - 2. read_ticket_lazy: Generator object which takes input as file name. Creates a named tuple type of the header of file. reads the lines for file and yields the file rows and named tuple one at a time.
  - 3. We have implemented and tested the generator object in the session15.pynb file

### For goal two, We have implemented following function-
  - 1. Function get_voilations_by_car_make: Function takes make_name (example 'BMW') as input and returns the number of violations by this specific car make. We create a generator object with vehicle makes as elements. we use the collections counter object to count the violations.
