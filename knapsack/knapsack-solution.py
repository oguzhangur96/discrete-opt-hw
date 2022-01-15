import os

def read_problem(file_name):
    lines = open(file_name).readlines()

    # get the number of items and total capacity
    tokens = lines[0].split()
    n_items = int(tokens[0])
    capacity = int(tokens[1])

    # collect the values and weights of each item
    items = []
    for i, line in enumerate(lines[1 : n_items+1]):
        tokens = line.split()
        value = int(tokens[0])
        weight = int(tokens[1])
        if weight > capacity:
            continue
        item = (value, weight, i, value/weight, 0)
        items.append(item)

    return (n_items, capacity, items)


file_path = f"data{os.sep}ks_4_0"

n_items, capacity, items = read_problem(file_path)

def greedy_solver(n_items: int, capacity: int, items: list):
    """Select most efficient items in terms of value/weight ratio. 

    Args:
        n_items (int): [description]
        capacity (int): [description]
        items (list): [description]

    Returns:
        [type]: [description]
    """
    
    taken = None
    value = None
    
    return (taken, value) 

