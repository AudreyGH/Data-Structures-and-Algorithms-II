# Audrey Hababag  ID # 001428031

import csv
from hash_table import ChainingHashTable

package_hash = ChainingHashTable()  # Instance of hash table
# Empty trucks
truck_one = []
truck_two = []
truck_three = []
all_packages = []


# Load all trucks with packages following certain conditions or constraints.
# The packages are loaded according to their special notes and deadlines
# Truck 1 is loaded with all the packages with urgent deadlines. The the remaining space filled with
# packages that have 'EOD' deadlines.
# Truck 2 is loaded with packages that can only go into truck 2, and packages are delayed until 9:05 AM
# Truck 3 is loaded with package 9, and all the remaining packages until full. The rest goes to truck 2.
# Final load: Truck 1 = 16, Truck 2 = 8, Truck 3 = 16
# O(n)
def load_trucks():
    global package_hash
    global truck_one
    global truck_two
    global truck_three
    global all_packages


    truck_one.clear()
    truck_two.clear()
    truck_three.clear()
    all_packages.clear()

    # Load package data
    with open('package.csv') as packages:
        package_data = csv.reader(packages)

        # O(n)
        for package in package_data:
            pId = package[0]
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pNotes = package[7]
            pStatus = ''
            pTime = ''

            if 'Delayed' not in pNotes:
                pStatus = 'At the hub'  # default status
            else:
                pStatus = 'Awaiting arrival'

            # Package object
            p = [pId, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus, pTime]

            # Insert into hash table
            package_hash.insert(pId, p)  # ID as key

            all_packages.append(p)

            # Package with wrong address to third truck
            if 'Wrong' in p[7]:
                truck_three.append(p)

            # All delayed packages and 'can only be in truck 2' packages goes to second truck
            elif 'Can' in p[7] or 'Delayed' in p[7]:
                truck_two.append(p)

            # Fill first truck with dearly deadline packages and packages that must be delivered with others
            elif p[5] != 'EOD' and 'Delayed' not in p[7] and 'Can' not in p[7] and 'Wrong' not in p[7]:
                truck_one.append(p)
            elif p[0] == '19':
                truck_one.append(p)

            # Fill first truck's  with standard EOD packages until fucll
            elif p[5] == 'EOD' and 'Delayed' not in p[7] and 'Wrong' not in p[7] and 'Can' not in p[7] and len(
                    truck_one) <= 3:
                truck_one.append(p)

            # Fill truck three with standard packages until full
            elif len(truck_three) != 16:
                truck_three.append(p)
            # Any remaining packages go to truck two
            else:
                truck_two.append(p)


# Truck 1 getter
# O(1)
def get_first():
    return truck_one


# Truck 2 getter
# O(1)
def get_second():
    return truck_two


# Truck 3 getter
# O(1)
def get_third():
    return truck_three


# Hash table getter
# O(1)
def get_hash_table():
    return package_hash


# All packages getter
# O(1)
def get_all_packages():
    return all_packages



