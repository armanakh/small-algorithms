
# find the largest number

listing = [7, 3, 11, 4, 9, 2]

count = 0
current = listing[0]

while count < len(listing):
    if current < listing[count]:
        current = listing[count]
    count += 1

print(current)        

