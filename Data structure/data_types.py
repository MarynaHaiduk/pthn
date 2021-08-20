# convert to string
to_str = str(12345)
print(to_str, type(to_str))

# convert to integer
to_integer = int("12345")
print(to_integer, type(to_integer))

# convert to float
to_float = float("12345")
print(to_float, type(to_float))

# convert to complex number
to_complex = complex(2, -3)
print(to_complex, type(to_complex))

# convert to boolean
to_bool = bool("12345")
print(to_bool, type(to_bool))

# convert to list
to_list = list("12345")
print(to_list, type(to_list))

# convert to tuple
to_tuple = tuple("12345")
print(to_tuple, type(to_tuple))

# convert to dictionary
to_dict = dict.fromkeys("12345")
print(to_dict, type(to_dict))

# convert to set
to_set = set("12345")
print(to_set, type(to_set))

# convert to immutable frozenset
to_frozen_set = frozenset("12345")
print(to_frozen_set, type(to_frozen_set))

# array of the given bytes
array_of_bytes = bytearray("12345", 'utf-8')
print(array_of_bytes, type(array_of_bytes))

# convert string to bytes
str_to_bytes = bytes("12345", 'utf-8')
print(str_to_bytes, type(str_to_bytes))
