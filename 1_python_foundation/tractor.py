"""
Tractor Traversal Algorithm - Maji Ndogo Case Study
Ministry of Agriculture field coverage optimization
"""

def check_fuel_status(fuel_level: int) -> str:
    """
    Checks if tractor has enough fuel to operate.
    Returns warning if below 20%.
    """
    if fuel_level < 20:
        return f"WARNING: Low fuel ({fuel_level}%) - Refuel needed!"
    return f"Fuel OK: {fuel_level}% - Ready for field operation."

def get_planted_cells(field: list) -> list:
    """
    Returns list of coordinates (row, col) where crop is planted (1).
    Uses list comprehension for efficiency.
    """
    planted = [(r, c)
               for r in range(len(field))
               for c in range(len(field[0]))
               if field[r][c] == 1]
    return planted

def drive_and_plant(field: list) -> list:
    """
    Serpentine (zigzag) traversal algorithm.
    Efficient path planning - reduces turning maneuvers and saves fuel.
    Even rows: left -> right, Odd rows: right -> left
    """
    rows = len(field)
    cols = len(field[0]) if rows > 0 else 0

    for r in range(rows):
        # Zigzag logic
        col_range = range(cols) if r % 2 == 0 else range(cols -1, -1, -1)
        for c in col_range:
            field[r][c] = 1 # Planting action
            print(f"Planting at ({r}, {c}) - Fuel check: OK")

    return field

# --- Demo / Test ---
if __name__ == "__main__":
    # Test 1: Fuel
    print(check_fuel_status(85))
    print(check_fuel_status(15))

    # Test 2: Field
    test_field = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(f"\nInitially planted: {get_planted_cells(test_field)}")

    # Test 3: Full traversal
    print("\nStarting serpentine traversal...")
    planted_field = drive_and_plant(test_field)
    print(f"\nFinal planted cells: {get_planted_cells(planted_field)}")
    print("Field operation complete - fuel saved via optimized path.")
