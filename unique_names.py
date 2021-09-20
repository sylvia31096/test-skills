def unique_names(names1, names2):
    unique_list = []
    for i,j in zip(names1,names2):
        if i not in unique_list:
            unique_list.append(i)
        if j not in unique_list:
            unique_list.append(j)


    return unique_list

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    
    print(unique_names(names1, names2))