
# find the first duplicate

listing = [4, 1, 9, 9, 7, 3]

def find_duplicate(x):
    count = 1
    for i_a in x:
        for i_b in x[count::]:
            if i_a == i_b:
                return i_b  
        count += 1

    return f"no duplicates"        

print(find_duplicate(listing))
