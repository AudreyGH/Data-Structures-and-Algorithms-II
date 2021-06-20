# Audrey Hababag  ID # 001428031

from algorithm import nearest_address
from graph import Graph, get_weights
from hash_table import ChainingHashTable
from load_trucks import get_first, get_second, get_third, get_hash_table, get_all_packages, load_trucks
from datetime import time, timedelta, datetime

total_travelled_one = 0
total_travelled_two = 0
total_travelled_three = 0
truck_two_return = datetime(1900, 1, 1, 0, 0, 0)  # time that truck 2 returns to hub


# Retrieves the status of all packages according to the time entered by the user

# The function accepts datetime as a parameter
# Each truck is contained within their own separate loops to handle retrieval of delivery times and distances
# Truck loops execute at different times. While Truck 1 and Truck 2 loops can occur simultaneously, Truck 3 does not
# start until Truck 2 ends.

# The status of packages can change based on the following:

# 1. The time provide by the user
# If a truck does not leave before the time provided by the user. The status of packages remain unchanged
# If the time given is greater than the truck's departure time, all packages in that truck are marked 'En route'
# When the truck reaches its destination, the package is marked 'Delivered' and is removed from the truck list.

# 2. Package special notes
# Some packages are marked delayed and do not arrive at the hub until 09:05 AM. Their status change to 'En route' when
# they arrive as this is also the time Truck 2 departs for delivery.
# The street address and zip code for package 9 is incorrect. The address is updated at 10:20 AM.

# The function returns all the packages whose statuses are altered or remain unaltered based on the time provided by
# the user.


# O(n^2)
def deliver_packages(time_input):
    global total_travelled_one
    global total_travelled_two
    global total_travelled_three
    global truck_two_return
    all_packages = get_hash_table()
    first_truck = get_first()
    second_truck = get_second()
    third_truck = get_third()
    current_location1 = 'HUB'
    current_location2 = 'HUB'
    current_location3 = 'HUB'
    edge = get_weights()
    sum_distance_one = 0
    sum_distance_two = 0
    sum_distance_three = 0
    first_start_time = datetime(1900, 1, 1, 8, 0, 0)
    second_start_time = datetime(1900, 1, 1, 9, 5, 0)
    info_update = datetime(1900, 1, 1, 10, 20, 0)
    max_packages_one = len(first_truck)
    max_packages_two = len(second_truck)
    max_packages_three = len(third_truck)

    # Update package 9 address and zip code at 10:20 AM
    if time_input >= info_update:
        package_nine = all_packages.search('9')
        package_nine[1] = '410 S State St'
        package_nine[4] = '84111'

    # Returns all packages unaltered (loaded in trucks) if user time input < the first truck departure
    if time_input < first_start_time:
        return get_all_packages()

    # Change status of packages to En route at departure/start time
    if time_input >= first_start_time and max_packages_one == len(get_first()):
        for a in first_truck:
            change_one = all_packages.search(a[0])
            change_one[8] = 'En route Truck 1'
    if time_input >= second_start_time and max_packages_two == len(get_second()):
        for b in second_truck:
            change_two = all_packages.search(b[0])
            change_two[8] = 'En route Truck 2'

    # Update delivery status and save delivery time for each package until truck 1 is empty
    while len(first_truck) != 0:
        new_add1 = nearest_address(first_truck, current_location1)  # get nearest address from current location

        for i in first_truck:
            if new_add1 in i:
                package_search1 = all_packages.search(i[0])  # search for current package in the hash table
                distance1 = edge[current_location1, new_add1]
                current_location1 = new_add1  # previously nearest location now becomes that starting location
                sum_distance_one = sum_distance_one + distance1  # current sum of distance travelled
                minutes1 = (sum_distance_one / 18) * 60
                time1 = first_start_time + timedelta(minutes=minutes1, seconds=0)
                delivery_time1 = time1.replace(second=0)  # Set seconds to zero for comparison accuracy
                if time_input >= delivery_time1:
                    package_search1[8] = 'Delivered'
                    package_search1[9] = delivery_time1.strftime('%H:%M')

                first_truck.remove(i)

        # If all packages have been delivered, set destination to hub
        # Distance from last delivery location to hub is added to overall distance travelled
        if len(first_truck) == 0:
            distance1 = edge[new_add1, 'HUB']
            sum_distance_one = sum_distance_one + distance1
            total_travelled_one = sum_distance_one

    # Update delivery status and save delivery time for each package until truck 2 is empty
    while len(second_truck) != 0:
        new_add2 = nearest_address(second_truck, current_location2)

        for j in second_truck:
            if new_add2 in j:
                package_search2 = all_packages.search(j[0])
                distance2 = edge[current_location2, new_add2]
                current_location2 = new_add2
                sum_distance_two = sum_distance_two + distance2
                minutes2 = (sum_distance_two / 18) * 60
                time2 = second_start_time + timedelta(minutes=minutes2)
                delivery_time2 = time2.replace(second=0)

                if time_input >= delivery_time2:
                    package_search2[8] = 'Delivered'
                    package_search2[9] = delivery_time2.strftime('%H:%M')

                second_truck.remove(j)

        # If all packages have been delivered, set destination to hub
        # Distance from last delivery location to hub is added to overall distance travelled
        # Truck 2's arrival time at the hub becomes the departure time for Truck 3
        if len(second_truck) == 0:
            distance2 = edge[new_add2, 'HUB']
            sum_distance_two = sum_distance_two + distance2
            mph = (sum_distance_two / 18) * 60
            time2_2 = second_start_time + timedelta(minutes=mph)
            delivery_time2 = time2_2.replace(second=0)
            total_travelled_two = sum_distance_two
            truck_two_return = delivery_time2  # Time truck 2 returned to hub
            third_start_time = truck_two_return

            if time_input >= third_start_time and max_packages_three == len(get_third()):
                for c in third_truck:
                    change_three = all_packages.search(c[0])
                    change_three[8] = 'En route Truck 3'

            # Update delivery status and save delivery time for each package until truck 3 is empty
            # Start Truck 3's delivery when Truck 2 returns to hub
            while len(third_truck) != 0:
                new_add3 = nearest_address(third_truck, current_location3)

                for k in third_truck:
                    if new_add3 in k:
                        package_search3 = all_packages.search(k[0])
                        distance3 = edge[current_location3, new_add3]
                        current_location3 = new_add3
                        sum_distance_three = sum_distance_three + distance3
                        minutes3 = (sum_distance_three / 18) * 60
                        time3 = third_start_time + timedelta(minutes=minutes3)
                        delivery_time3 = time3.replace(second=0)

                        if time_input >= delivery_time3:
                            package_search3[8] = 'Delivered'
                            package_search3[9] = delivery_time3.strftime('%H:%M')

                        third_truck.remove(k)

                # If all packages have been delivered, set destination to hub
                # Distance from last delivery location to hub is added to overall distance travelled
                if len(third_truck) == 0:
                    distance3 = edge[new_add3, 'HUB']
                    sum_distance_three = sum_distance_three + distance3
                    total_travelled_three = sum_distance_three

    return get_all_packages()


# Truck one total distance travelled getter
# O(1)
def get_total_miles_one():
    return total_travelled_one


# Truck two total distance travelled getter
# O(1)
def get_total_miles_two():
    return total_travelled_two


# Truck three total distance travelled getter
# 0(1)
def get_total_miles_three():
    return total_travelled_three
