from collections import Counter

count = int(input())
for i in range(count):
    no_of_pets = input()
    pet_sizes_input = input()
    pet_sizes = list(map(int,pet_sizes_input.split()))
    pet_sizes.sort()
    pet_sizes_counter = Counter(pet_sizes)
    sorted_sizes = list(pet_sizes_counter.values())
    
    
    max_treats = 0
    max_list = len(sorted_sizes)
    # for j,i in enumerate(sorted_sizes):
    #     max_treats+=pet_sizes_counter.get(i)*(max_list-j)
    
    print("Case #{} : {}".format(i, sum([j*(i+1) for i, j in enumerate(sorted_sizes)])))