import csv

# This is how you open files in python. Open it and assign it as an alias
with open('list.csv') as csvfile:

    # You see here? There are no initializing variables
    # Depending on the datatype you need, you variable turns into the right one.
    # Ex.
    # foo = "this is a string"
    # bar = 5
    # Make sense?
    # This line right here turns a csv file into a dictionary.
    reader = csv.DictReader(csvfile)

    # Do you see that reader variable? That is now a dictionary.
    # Dictionaries are essentially key-value pairs
    # You can access the data inside by using their key
    # I have provided an example for you by printing the dictionary
    # and value inside after accessing the dictionary by the key.
    for row in reader:
        print(row)
        print(row["name"], row["email"], row["score"])

    # For more information:
    # https://www.python-course.eu/dictionaries.php
