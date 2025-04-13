def egg_drop(max_floors=102, eggs=7):
    drops = 0
    current_floor = 0
    interval = 14
    floors_checked = []

    # Simulate egg breaking floor (for testing purposes)
    breaking_point = 72  # You can change this

    while eggs > 1 and current_floor + interval < max_floors:
        drops += 1
        current_floor += interval
        floors_checked.append(current_floor)
        if current_floor >= breaking_point:
            # Egg breaks, start linear search from last safe floor
            current_floor -= interval
            for i in range(1, interval):
                drops += 1
                floors_checked.append(current_floor + i)
                if current_floor + i >= breaking_point:
                    return current_floor + i - 1, drops, floors_checked
            return current_floor + interval - 1, drops, floors_checked
        interval -= 1

    return current_floor, drops, floors_checked

# Example use
floor_found, total_drops, checked = egg_drop()
print(f\"Max safe floor is: {floor_found}, found in {total_drops} drops.\")
print(f\"Floors tested: {checked}\")
