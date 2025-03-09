#using the max()

def find_max(num_list):
     return max(num_list) if num_list else None

num_list=[2,3,4,5,6]
print("largest num:",find_max(num_list))