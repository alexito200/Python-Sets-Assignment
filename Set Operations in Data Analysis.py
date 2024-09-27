# Task 1: Duplicate Entries Cleanup
# Write a Python script to remove duplicates and display the unique customer IDs.


def order_to_chaos(): 
    customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
    
    new_set = set(customer_ids)
    
    for index, customer_id in enumerate(sorted(new_set)):
        print(f'Customer ID {index}: is {customer_id}')

order_to_chaos()

