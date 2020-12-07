def get_id(seat: str):
    seat = seat.replace('F', '0')
    seat = seat.replace('B', '1')
    seat = seat.replace('L', '0')
    seat = seat.replace('R', '1')

    return int(seat, base=2)

with open('./inputs/day05') as data:
    seat_ids = [get_id(line.rstrip()) for line in data]
    print(max(seat_ids))

    free_ids = set(range(2**10)) - set(seat_ids) - set([0, 2**10 - 1])

    for free_id in free_ids:
        if (free_id - 1) in free_ids or (free_id + 1) in free_ids:
            continue
        print(free_id)