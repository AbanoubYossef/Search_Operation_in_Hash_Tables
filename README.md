# Hash Table Evaluation Script

This Python script implements a basic hash table with functionalities for insertion, searching, and deletion. It also includes three tasks to evaluate the performance of the hash table under different scenarios.

## Usage

1. Ensure you have Python installed on your machine.
2. Run the script using the following command:

   ```bash
   python script_name.py
   ```

## Script Overview

### Hash Table Implementation

The script defines a `HashTable` class with methods for hash calculation, insertion, searching, and calculating the fill factor.

### Task 1: Evaluate search operation for a single fill factor 95%, non-uniform selection

This task fills the hash table to a specified fill factor and performs searches with non-uniformly selected IDs. The average and maximum efforts for both found and not-found entries are measured.

### Task 2: Evaluate search operation for all fill factors with uniform selection

This task assesses the search operation for different fill factors using uniformly selected IDs. The script reports average and maximum efforts for both found and not-found entries across various fill factors.

### Task 3: Evaluate search operation for a single fill factor 99%, then delete until 80%, uniform selection

This task inserts elements into the hash table to achieve a 99% fill factor, deletes entries until the fill factor reaches 80%, and then evaluates search operations. It reports average and maximum efforts for both found and not-found entries.

## Results

The script prints the results of each task, providing insights into the hash table's performance under different conditions.
