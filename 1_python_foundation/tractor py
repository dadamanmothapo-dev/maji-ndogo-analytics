# Maji Ndogo - Python Foundation

def check_fuel_status(fuel):
    if fuel < 20:
        return "Low fuel - refuel needed"
    return "Fuel OK"

def count_planted_cells(field):
    count = 0
    for row in field:
        for cell in row:
            if cell == 1:
                count += 1
    return count

def drive_and_plant(field):
    path = []
    for r in range(len(field)):
        if r % 2 == 0:
            for c in range(len(field[r])):
                path.append((r,c))
        else:
            for c in range(len(field[r])-1, -1, -1):
                path.append((r,c))
    return path

# test
field = [[0,0,1],[1,0,0]]
print(check_fuel_status(15))
print(count_planted_cells(field))
print(drive_and_plant(field))
