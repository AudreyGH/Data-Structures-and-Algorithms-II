# Audrey Hababag  ID # 001428031

from graph import Graph, get_weights
from hash_table import ChainingHashTable
from load_trucks import get_first, get_second, get_third, get_hash_table


# Greedy algorithm
# Determines the nearest location for delivery
# Returns the nearest address from the truck's current location.

# The function accepts 2 parameters:
# 1. The packages loaded in a truck
# 2. The current or start address

# The first loop copies the addresses in a temporary list. This list will contain only one occurrence of each address.
# The addresses in the temporary list will be used in the second loop to retrieve edge weights.

# The second loop (while loop) retrieves the distance or edge weight between the current address and the addresses in
# the temporary list. A graph accepting two addresses as parameters is used to retrieve edge weights. The distances
# are compared to one another, removing the address that gives a larger edge weight each loop. The loop will end
# when only the address with the shortest distance remains. The address is returned and the function ends.

# The returned address will be used by the deliver_packages() function, to, as the name suggests, deliver packages that
# are set for delivery to the address. The deliver_packages() function will call this function to retrieve the next
# nearest delivery location. The last address that this function returns will become the new starting location, accepted
# as the 'start' parameter. The two functions create a relationship where this function is called recursively until
# either all packages have been delivered, or the condition created by user input is met.

# O(N^2)
def nearest_address(truck, start):
    temp_truck = []  # Empty container for packages. Will be used to iterate through
    for a in truck:
        if a[1] not in temp_truck:
            temp_truck.append(a[1])  # Insert only unique addresses in temp truck
    current = start  # Starting location
    edge = get_weights()  # Variable to grab edge weight from graph
    nearest = temp_truck[0]  # Variable for nearest address
    temp_edge = edge[start, temp_truck[0]]  # Temporary edge weight for comparison.

    while len(temp_truck) > 1:
        for destination in temp_truck:
            distance = edge[current, destination]  # Distance between current address and the next

            # if destination is the same as current location, clear temp truck and return the current location
            if current == destination:
                temp_truck.clear()
                return current

            # If previous address is closer or equal to next address, remove next from the list
            if temp_edge <= distance:
                temp_truck.remove(destination)

            # If next address is closer than previous, remove previous from the list
            # Next becomes the current nearest address
            if temp_edge > distance:
                temp_edge = distance
                nearest = destination
                temp_truck.remove(nearest)
    return nearest




