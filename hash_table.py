# Audrey Hababag  ID # 001428031

# HashTable class using chaining to handle collisions.
class ChainingHashTable:

    # Hash table constructor
    # Assigns all packages with an empty list.
    # O(n)
    def __init__(self, length=10):
        # initialize the hash table with empty package list entries.
        self.table = []
        for i in range(length):
            self.table.append([])

    # Inserts or updates item in the hash table.
    # O(n)
    def insert(self, key, item):
        # get the package list where this item will go.
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        # update key if it is already in the package
        for kv in package_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the package list.
        value = [key, item]
        package_list.append(value)
        return True

    # Searches the hash table for an item with a matching key
    # Returns the item if found, or None if not found.
    # O(n)
    def search(self, key):
        # get the package list where this key would be.
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        # search for the key in the package list
        for kv in package_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item from the hash table using key as parameter
    # O(n)
    def remove(self, key):
        # get the package list where this item will be removed from.
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        # remove the item from the package list if it is present.
        for kv in package_list:
            if kv[0] == key:
                package_list.remove([kv[0], kv[1]])



