# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_name = row["first_name"]
        last_name = row["last_name"]
        email = f"{first_name}.{last_name}@example.com"
        new_employee_data.append(
            {
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "ssn": row["ssn"],
                "email": email
            }
        )


        # Hint: You can use csv.DictReader
        # This will require a little bit of independent research (by design)
        # In the real world, you will encounter situations like this

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    headernames = ["first_name", "last_name", "ssn", "email"]
    writer = csv.DictWriter(csvfile, headernames=headernames)
    writer.writeheader()
    writer.writerows(new_employee_data)
    # Hint: You can use csv.DictWriter