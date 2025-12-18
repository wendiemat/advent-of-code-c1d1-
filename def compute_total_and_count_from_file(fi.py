def compute_password(input, target=0):
    total=50
     
    counter=0
    with open(input, 'r') as i:
        for line in i:
            line = line.strip()
            if not line:
                continue
            operation = line[0]
            try:
                #get the integer value after the first character
                value = int(line[1:])
            # skip invalid lines
            except ValueError:
                continue
            # if R then add value
            if operation == 'R':
                total += value
            # if L then subtract value
            elif operation == 'L':
                total -= value 
            # Wrap total between 0 and 99
            total = total % 100
            if total == target:
                counter += 1
        
    return total, counter

# Get and Display the result
target = 0
total, counter = compute_password("advent-of-code-c1d1-/input.txt", target)
print("Your password is:", counter)