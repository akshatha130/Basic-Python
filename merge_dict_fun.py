def add_dicts(dict1, dict2):
    result = dict1.copy() 
    result.update(dict2)   
    return result

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 3, 'e': 4, 'f': 5}

merged_dict = add_dicts(dict1, dict2)
print(merged_dict)
