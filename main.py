# Audrey Hababag  ID # 001428031

from load_trucks import get_first, get_second, get_third, get_hash_table, get_all_packages, load_trucks
from time_and_distance import deliver_packages
from time_and_distance import get_total_miles_one, get_total_miles_two, get_total_miles_three
from datetime import timedelta, datetime, time

hash_table = get_hash_table()


# Main Menu
# O(n)
def main_menu():
    print('\n*********************************************************')
    print('                     WGUPS MAIN MENU')
    print('*********************************************************\n')
    print(' 1. Look up a package with package with ID #')
    print(' 2. Check delivery status of all packages')
    print(' 3. Mileage travelled by delivery trucks')
    print(' 4. Exit Program')
    print('\n   How may we assist you today? Type number: ', end=' ')

    while True:
        try:
            input_one = int(input())

            if input_one in range(1, 5):
                if input_one == 1:
                    load_trucks()
                    package_search()
                if input_one == 2:
                    load_trucks()
                    print_all_packages()
                if input_one == 3:
                    load_trucks()
                    truck_mileage()
                if input_one == 4:
                    quit()
                break
            else:
                print('   Please type a number between 1 to 4:', end=' ')
                continue
        except ValueError:
            print('   Not a number! Try again:', end=' ')
            continue


# Package Search
# Searches the hash table for a package using ID #
# O(n)
def package_search():
    print('\n*********************************************************')
    print('                     Package Search ')
    print('*********************************************************')
    print('\nEnter Package ID: ', end=' ')

    while True:
        try:
            input_id = int(input())
            if input_id in range(1, 41):
                i = hash_table.search(str(input_id))
                print('\nPackage ID # ' + i[0], )
                print('Address:', i[1] + ',', i[2] + ',', i[3], i[4])
                print('Deadline:', i[5])
                print('Weight:', i[6], 'kg')
                print('Special Notes:', i[7])
                print('Status:', i[8], i[9])
                print('*********************************************************\n')
                break
            else:
                print('   That package does not exist! Try gain:', end=' ')
                continue
        except ValueError:
            print('   Integers only! Try again:', end=' ')
            continue

    print(' 1. Search for another package')
    print(' 2. Return to main menu')
    print(' 3. Exit program')
    print('\n   Is there anything else we can help you with? Type number: ', end=' ')

    while True:
        try:
            input_two = int(input())

            if input_two in range(1, 4):
                if input_two == 1:
                    package_search()
                elif input_two == 2:
                    main_menu()
                elif input_two == 3:
                    quit()
                break
            else:
                print('   Please type a number between 1 to 3:', end=' ')
                continue
        except ValueError:
            print('   Not a number! Try again:', end=' ')
            continue


# Delivery status menu
# Retrieves status of all packages according to time input
# O(n)
def print_all_packages():
    print('\n*********************************************************')
    print('                      Delivery Status ')
    print('*********************************************************')
    print('Truck 1 with', len(get_first()), 'packages departs at 08:00')
    print('Truck 2 with', len(get_second()), 'packages departs at 09:00')
    print('Truck 3 with', len(get_third()), 'packages departs when Truck 2 returns to hub\n')
    print('Enter time (HHMM) between 0000 and 2359: ', end=' ')

    while True:
        try:
            input_time = str(input())
            end_time = datetime(1900, 1, 1, 23, 59, 0)
            converted_time = datetime.strptime(input_time, '%H%M')

            if len(input_time) == 4 and converted_time <= end_time:
                print('')
                for i in deliver_packages(converted_time):
                    print('Package ID # ' + i[0], )
                    print('Address:', i[1] + ',', i[2] + ',', i[3], i[4])
                    print('Deadline:', i[5])
                    print('Weight:', i[6], 'kg')
                    print('Special Notes:', i[7])
                    print('Status:', i[8], i[9])
                    print('-------------------------------------------------------------------------')
                break
            else:
                print('Invalid entry! Try again:', end=' ')
                continue
        except ValueError:
            print('Invalid entry! Try again:', end=' ')
            continue

    print('\n 1. Enter a different time')
    print(' 2. Return to main menu')
    print(' 3. Exit program')
    print('\n   Is there anything else we can help you with? Type number: ', end=' ')

    while True:
        try:
            input_three = int(input())

            if input_three in range(1, 4):
                if input_three == 1:
                    load_trucks()
                    print_all_packages()
                if input_three == 2:
                    main_menu()
                if input_three == 3:
                    quit()
                break
            else:
                print('   Please type number 1 to 3:', end=' ')
                continue
        except ValueError:
            print('   Not a number! Try again:', end=' ')
            continue


# Mileage menu
# Retrieves distance travelled b all trucks
# O(n)
def truck_mileage():
    print('\n*********************************************************')
    print('                      Mileage Data ')
    print('*********************************************************\n')

    deliver_packages(datetime(1900, 1, 1, 23, 59, 0))
    overall = get_total_miles_one() + get_total_miles_two() + get_total_miles_three()

    print(' First truck:', end=' ')
    print('{0:.1f}'.format(get_total_miles_one()), 'miles')
    print(' Second truck:', end=' ')
    print('{0:.1f}'.format(get_total_miles_two()), 'miles')
    print(' Third truck:', end=' ')
    print('{0:.1f}'.format(get_total_miles_three()), 'miles\n')
    print(' Total distance travelled :', overall)
    print(' Total includes distance travelled while returning to hub. ')
    print('*********************************************************\n')
    print(' 1. Return to main menu')
    print(' 2. Exit program')
    print('\n   Is there anything else we can help you with? Type number: ', end=' ')

    while True:
        try:
            input_four = int(input())

            if input_four in range(1, 3):
                if input_four == 1:
                    main_menu()
                if input_four == 2:
                    quit()
                break
            else:
                print('   Please type number 1 or 2:', end=' ')
                continue
        except ValueError:
            print('   Not a number! Try again:', end=' ')
            continue


main_menu()


