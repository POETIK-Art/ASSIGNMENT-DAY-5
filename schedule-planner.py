def study_schedule(total_pages=200, pages_per_15min=5):
    time_per_block = 15  # minutes
    blocks_needed = total_pages // pages_per_15min
    schedule = []

    for i in range(1, blocks_needed + 1):
        start_min = (i - 1) * time_per_block
        end_min = i * time_per_block
        schedule.append((f\"{start_min // 60:02d}:{start_min % 60:02d} - {end_min // 60:02d}:{end_min % 60:02d}\", f\"Read pages {((i - 1) * pages_per_15min + 1)} - {i * pages_per_15min}\"))

    return schedule

# Example usage
for block in study_schedule():
    print(block)
