import random

# Define a class for individual entries in the hash table
class Entry:
    def __init__(self, id, name):
        self.id = id      # Initialize entry id
        self.name = name  # Initialize entry name

# Define the main hash table class
class HashTable:
    def __init__(self, size):
        self.size = size               # Initialize the table size
        self.table = [None] * size     # Create a list to represent the hash table, initially filled with None values

    # Define a hash function to calculate the initial index for an entry
    def hash(self, key):
        return key % self.size        # Return the remainder of the key divided by the table size

    # Define the insert method to add an entry to the hash table
    def insert(self, entry):
        key = entry.id                 # Get the id of the entry to be inserted
        index = self.hash(key)         # Calculate the initial index using the hash function
        i = 0                          # Initialize a variable i for quadratic probing

        # Loop to find an empty slot for the entry
        while self.table[index] is not None:
            index = (index + i**2) % self.size  # Use quadratic probing to calculate the next index
            i += 1

        # Once an empty slot is found, insert the entry into the table
        self.table[index] = entry

    # Define the search method to find an entry in the hash table by its id
    def search(self, id):
        index = self.hash(id)          # Calculate the initial index using the hash function
        i = 0                          # Initialize a variable i for quadratic probing
        operations = 0                # Initialize operations count

        # Loop to search for the entry by its id
        while self.table[index] is not None:
            operations += 1
            if self.table[index].id == id:
                return operations, self.table[index]   # Return the number of operations performed and the element
            index = (index + i**2) % self.size  # Use quadratic probing to calculate the next index
            i += 1

        return operations, None
   
    # Define a method to calculate the current fill factor of the hash table
    def get_fill_factor(self):
        filled_slots = sum(1 for slot in self.table if slot is not None and slot.id >= 0)
        return filled_slots / self.size

# Function to delete an entry by its ID
def delete_entry_by_id(hash_table, id):
    index = hash_table.hash(id)
    i = 0

    while hash_table.table[index] is not None:

        if hash_table.table[index].id == id:
            hash_table.table[index].id = -1  # Mark the slot as deleted
            return

        index = (index + i**2) % hash_table.size
        i += 1

# Function to delete elements from the hash table until a desired fill factor is achieved
def delete_until_fill_factor(hash_table, desired_fill_factor):
    # Iterate through the table and delete entries until the desired fill factor is reached
    while hash_table.get_fill_factor() > desired_fill_factor:
        for i in range(len(hash_table.table)):
            if hash_table.get_fill_factor() <= desired_fill_factor:
                break
            random_i = random.randint(1, len(hash_table.table) - 1) 
            entry = hash_table.table[random_i]
            if entry is not None:
                id_to_delete = entry.id
                delete_entry_by_id(hash_table, id_to_delete)

# Function to fill the hash table with elements to achieve a specific filling factor
def fill_hash_table(hash_table, desired_fill_factor):
    N = hash_table.size
    n = int(desired_fill_factor * N)
    for _ in range(n):
        id = random.randint(1, 500000)
        name = f"Bebo-{id}"
        entry = Entry(id, name)
        hash_table.insert(entry)

# Task 1: Evaluate search operation for a single fill factor 95%, non-uniform selection
def task_1():
    # Create an instance of the HashTable class with a specified size
    hash_table = HashTable(10007)  # Choose a prime number as the table size
    desired_fill_factor = 0.95
    fill_hash_table(hash_table, desired_fill_factor)
    num_runs= 5

    total_effort_found_list = []
    total_effort_not_found_list = []

    max_effort_found_list = []
    max_effort_not_found_list = []

    num_searches = 3000

    for _ in range(num_runs):
        counter_found =0
        counter_not_found =0
        total_effort_found = 0
        total_effort_not_found = 0  
        max_effort_found = 0
        max_effort_not_found = 0

        for _ in range(num_searches):
            search_id = random.randint(1, 100000)
            effort,result  = hash_table.search(search_id)
            

            if result is not None:
                max_effort_found = max(max_effort_found, effort)
                total_effort_found += effort
                counter_found += 1
            else:
                max_effort_not_found = max(max_effort_not_found, effort)
                total_effort_not_found += effort
                counter_not_found += 1

        

        avg_effort_found = total_effort_found / counter_found
        avg_effort_not_found = total_effort_not_found / counter_not_found

        max_effort_found_list.append(max_effort_found)
        max_effort_not_found_list.append(max_effort_not_found)

        total_effort_found_list.append(avg_effort_found)
        total_effort_not_found_list.append(avg_effort_not_found)
        
    print("Evaluate search operation for a single fill factor 95%, non-uniform selection")
    print(f"Filling Factor: {desired_fill_factor}")
    print(f"Avg. Effort (Found): {sum(total_effort_found_list)/num_runs:.2f}")
    print(f"Max Effort (Found): {max(max_effort_found_list)}")
    print(f"Avg. Effort (Not Found): {sum(total_effort_not_found_list)/num_runs:.2f}")
    print(f"Max Effort (Not Found): {max(max_effort_not_found_list)}")

# Task 2: Evaluate search operation for all fill factors with uniform selection
def task_2():
    
    fill_factors = [0.80, 0.85, 0.90, 0.95, 0.99]
    results = []

    for desired_fill_factor in fill_factors:
        HT = HashTable(10007)  # Choose a prime number as the table size
        fill_hash_table(HT, desired_fill_factor)
        num_runs = 5

        total_effort_found_list = []
        total_effort_not_found_list = []

        max_effort_found_list = []
        max_effort_not_found_list = []

        num_searches = 3000
        for _ in range(num_runs):
            counter_found = 0
            counter_not_found = 0
            total_effort_found = 0
            total_effort_not_found = 0
            max_effort_found = 0
            max_effort_not_found = 0

            # Ensure that approximately half of the searched elements are found
            for _ in range(num_searches // 2):
                # Search for an element that is in the table
                search_id = random.choice([entry.id for entry in HT.table if entry is not None])
                effort, result = HT.search(search_id)

                if result is not None:
                    max_effort_found = max(max_effort_found, effort)
                    total_effort_found += effort
                    counter_found += 1
                else:
                    max_effort_not_found = max(max_effort_not_found, effort)
                    total_effort_not_found += effort
                    counter_not_found += 1

            # Ensure that approximately half of the searched elements are not found
            for _ in range(num_searches // 2):
                # Search for an element that is not in the table
                search_id = random.randint(500001, 1000000)
                effort, result = HT.search(search_id)

                if result is not None:
                    max_effort_found = max(max_effort_found, effort)
                    total_effort_found += effort
                    counter_found += 1
                else:
                    max_effort_not_found = max(max_effort_not_found, effort)
                    total_effort_not_found += effort
                    counter_not_found += 1

            avg_effort_found = total_effort_found / counter_found
            avg_effort_not_found = total_effort_not_found / counter_not_found

            max_effort_found_list.append(max_effort_found)
            max_effort_not_found_list.append(max_effort_not_found)

            total_effort_found_list.append(avg_effort_found)
            total_effort_not_found_list.append(avg_effort_not_found)
        # Store the results for this fill factor
        results.append([desired_fill_factor, 
                        sum(total_effort_found_list) / num_runs,
                        max(max_effort_found_list), 
                        sum(total_effort_not_found_list) / num_runs,  
                        max(max_effort_not_found_list)])

    # Print the results for all fill factors
    print("Filling Factor || Avg. Effort (Found) || Max Effort (Found) || Avg. Effort (Not Found) || Max Effort (Not Found)")
    print('='*120)
    for result in results:
        print(f"{result[0]:.2f}           || {result[1]:.2f}                || {result[2]}                 || {result[3]:.2f}                    || {result[4]}")
        print('='*120)

def task_3():
        
   
    # Create an instance of the HashTable class with a specified size
    hash_table = HashTable(10007)  # Choose a prime number as the table size

    # Insert elements to achieve a 99% fill factor
    desired_fill_factor = 0.99
    fill_hash_table(hash_table, desired_fill_factor)

    # Delete elements until a filling factor of 0.8 is reached
    desired_fill_factor2 = 0.8
    delete_until_fill_factor(hash_table, desired_fill_factor2)

    # Perform searches for both found and not-found elements
    num_runs= 5

    total_effort_found_list = []
    total_effort_not_found_list = []

    max_effort_found_list = []
    max_effort_not_found_list = []

    num_searches = 3000

    for _ in range(num_runs):
        counter_found =0
        counter_not_found =0
        total_effort_found = 0
        total_effort_not_found = 0  
        max_effort_found = 0
        max_effort_not_found = 0

        
        # Ensure that approximately half of the searched elements are found
        for _ in range(num_searches // 2):
            # Search for an element that is in the table
            search_id = random.choice([entry.id for entry in hash_table.table if entry is not None and entry.id >=0])
            effort, result = hash_table.search(search_id)

            if result is not None:
                max_effort_found = max(max_effort_found, effort)
                total_effort_found += effort
                counter_found += 1
            else:
                max_effort_not_found = max(max_effort_not_found, effort)
                total_effort_not_found += effort
                counter_not_found += 1

        # Ensure that approximately half of the searched elements are not found
        for _ in range(num_searches // 2):
            # Search for an element that is not in the table
            search_id = random.randint(500001, 1000000)
            effort, result = hash_table.search(search_id)

            if result is not None:
                max_effort_found = max(max_effort_found, effort)
                total_effort_found += effort
                counter_found += 1
            else:
                max_effort_not_found = max(max_effort_not_found, effort)
                total_effort_not_found += effort
                counter_not_found += 1

    

        avg_effort_found = total_effort_found / counter_found
        avg_effort_not_found = total_effort_not_found / counter_not_found

        max_effort_found_list.append(max_effort_found)
        max_effort_not_found_list.append(max_effort_not_found)

        total_effort_found_list.append(avg_effort_found)
        total_effort_not_found_list.append(avg_effort_not_found)
        
    print("Evaluate search operation for a single fill factor 99% then delet untill 80%, uniform selection")
    print(f"Filling Factor: {desired_fill_factor}")
    print(f"delete untill Filling Factor: {desired_fill_factor2}")
    print(f"Avg. Effort (Found): {sum(total_effort_found_list)/num_runs:.2f}")
    print(f"Max Effort (Found): {max(max_effort_found_list)}")
    print(f"Avg. Effort (Not Found): {sum(total_effort_not_found_list)/num_runs:.2f}")
    print(f"Max Effort (Not Found): {max(max_effort_not_found_list)}")

def draw():
    print('='*120)
    task_1()
    print('='*120)
    print("\n")
    print('='*120)
    task_2()
    print("\n")
    print('='*120)
    task_3()
    print('='*120)

draw()