# --- Day 13: Shuttle Search ---
# Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you discover that no ships embark from that port to your vacation island. You'll need to get from the port to the nearest airport.
#
# Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus has an ID number that also indicates how often the bus leaves for the airport.
#
# Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.
#
# The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!
#
# Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.
#
# To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be exactly one such bus.)
#
# For example, suppose you have the following notes:
#
# 939
# 7,13,x,x,59,x,31,19
# Here, the earliest timestamp you could depart is 939, and the bus IDs in service are 7, 13, 59, 31, and 19. Near timestamp 939, these bus IDs depart at the times marked D:
#
# time   bus 7   bus 13  bus 59  bus 31  bus 19
# 929      .       .       .       .       .
# 930      .       .       .       D       .
# 931      D       .       .       .       D
# 932      .       .       .       .       .
# 933      .       .       .       .       .
# 934      .       .       .       .       .
# 935      .       .       .       .       .
# 936      .       D       .       .       .
# 937      .       .       .       .       .
# 938      D       .       .       .       .
# 939      .       .       .       .       .
# 940      .       .       .       .       .
# 941      .       .       .       .       .
# 942      .       .       .       .       .
# 943      .       .       .       .       .
# 944      .       .       D       .       .
# 945      D       .       .       .       .
# 946      .       .       .       .       .
# 947      .       .       .       .       .
# 948      .       .       .       .       .
# 949      .       D       .       .       .
# The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944, so you would need to wait 944 - 939 = 5 minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives 295.
#
# What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
#
# Your puzzle answer was 3246.
#
# --- Part Two ---
# The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. (The first line in your input is no longer relevant.)
#
# For example, suppose you have the same list of bus IDs as above:
#
# 7,13,x,x,59,x,31,19
# An x in the schedule means there are no constraints on what bus IDs must depart at that time.
#
# This means you are looking for the earliest timestamp (called t) such that:
#
# Bus ID 7 departs at timestamp t.
# Bus ID 13 departs one minute after timestamp t.
# There are no requirements or restrictions on departures at two or three minutes after timestamp t.
# Bus ID 59 departs four minutes after timestamp t.
# There are no requirements or restrictions on departures at five minutes after timestamp t.
# Bus ID 31 departs six minutes after timestamp t.
# Bus ID 19 departs seven minutes after timestamp t.
# The only bus departures that matter are the listed bus IDs at their specific offsets from t. Those bus IDs can depart at other times, and other bus IDs can depart at those times. For example, in the list above, because bus ID 19 must depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7 will always also be departing with bus ID 19 at seven minutes after timestamp t.
#
# In this example, the earliest timestamp at which this occurs is 1068781:
#
# time     bus 7   bus 13  bus 59  bus 31  bus 19
# 1068773    .       .       .       .       .
# 1068774    D       .       .       .       .
# 1068775    .       .       .       .       .
# 1068776    .       .       .       .       .
# 1068777    .       .       .       .       .
# 1068778    .       .       .       .       .
# 1068779    .       .       .       .       .
# 1068780    .       .       .       .       .
# 1068781    D       .       .       .       .
# 1068782    .       D       .       .       .
# 1068783    .       .       .       .       .
# 1068784    .       .       .       .       .
# 1068785    .       .       D       .       .
# 1068786    .       .       .       .       .
# 1068787    .       .       .       D       .
# 1068788    D       .       .       .       D
# 1068789    .       .       .       .       .
# 1068790    .       .       .       .       .
# 1068791    .       .       .       .       .
# 1068792    .       .       .       .       .
# 1068793    .       .       .       .       .
# 1068794    .       .       .       .       .
# 1068795    D       D       .       .       .
# 1068796    .       .       .       .       .
# 1068797    .       .       .       .       .
# In the above example, bus ID 7 departs at timestamp 1068788 (seven minutes after t). This is fine; the only requirement on that minute is that bus ID 19 departs then, and it does.
#
# Here are some other examples:
#
# The earliest timestamp that matches the list 17,x,13,19 is 3417.
# 67,7,59,61 first occurs at timestamp 754018.
# 67,x,7,59,61 first occurs at timestamp 779210.
# 67,7,x,59,61 first occurs at timestamp 1261476.
# 1789,37,47,1889 first occurs at timestamp 1202161486.
# However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than 100000000000000!
#
# What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
#
# Your puzzle answer was 1010182346291467.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def get_match_counter(number):
    global bus_offset
    global max_bus_offset
    global max_bus_id

    match_counter = 1

    for bo in bus_offset:
        if max_bus_id != bo.get('bus'):
            # print("max_bus_offset: ", max_bus_offset)
            # print("bo.get('offset'): ", bo.get('offset'))
            # print("bo.get('bus'): ", bo.get('bus'))
            # print("(number - max_bus_offset + bo.get('offset')) % bo.get('bus'): ", (number - max_bus_offset + bo.get('offset')) % bo.get('bus'))
            if (number - max_bus_offset + bo.get('offset')) % bo.get('bus') == 0:
                match_counter += 1
            else:
                break
    return match_counter


if __name__ == '__main__':

    files = ['20201213-example.txt', '20201213-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            notes = f.readlines()


        len_notes = len(notes)
        #print("len_notes :", len_notes)

        arrival_time = int(notes[0].strip())
        #print("arrival_time: ", arrival_time)

        bus_ids = [int(bus.strip()) for bus in notes[1].split(',') if bus != 'x']
        #print("bus_ids: ", bus_ids)

        print("\nPart One")

        time_table = []

        for bus in bus_ids:
            time_before = arrival_time - (arrival_time % bus)
            time_after = arrival_time - (arrival_time % bus) + bus
            diff_before = time_before - arrival_time
            diff_after = time_after - arrival_time
            time_table.append({'time': time_before, 'bus': bus, 'diff': diff_before})
            time_table.append({'time': time_after, 'bus': bus, 'diff': diff_after})

        print("time_table: ")
        print("\n".join(str(j) for j in time_table))
        min_diff_after = min(int(t.get('diff')) for t in time_table if int(t.get('diff')) > 0)
        print("closet diff to arrival time: ", min_diff_after)
        print("bus with closet diff to arrival time: ", [t for t in time_table if int(t.get('diff')) == min_diff_after])
        print("bus id * diff: ", [t.get('bus') * t.get('diff') for t in time_table if int(t.get('diff')) == min_diff_after])

        print("\nPart Two")

        bus_offset = []
        counter = 0
        for e, s in enumerate(notes[1].split(',')):
            if s != 'x':
                bus_offset.append({'offset': counter, 'bus': int(s.strip()), 'bus_with_offset': counter + int(s.strip())})
            counter += 1
        #print("bus_offset: ", bus_offset)
        #print("bus_offset: ")
        #print("\n".join(str(j) for j in bus_offset))
        count_buses = len(bus_offset)
        #print("number of bus ids: ", count_buses)

        t = 0
        lcm = 1

        for bo in bus_offset:

            remainder = (bo.get('bus') - bo.get('offset')) % bo.get('bus')

            while t % bo.get('bus') - remainder != 0:
                t += lcm

            print("{} % {} = {}".format(t, bo.get('bus') - remainder, t % bo.get('bus') - remainder))
            lcm *= bo.get('bus')

        print("Timestamp: " + str(t))

        # Own solution just working for test data
        if file_name.find('example') > 0:

            print("\nPart Two Slow Solution Example Only")

            bus_offset = []
            counter = 0
            for s in notes[1].split(','):
                if s != 'x':
                    bus_offset.append({'offset': counter, 'bus': int(s.strip()), 'bus_with_offset': counter + int(s.strip())})
                counter += 1
            #print("bus_offset: ", bus_offset)
            #print("bus_offset: ")
            #print("\n".join(str(j) for j in bus_offset))
            count_buses = len(bus_offset)
            #print("number of bus ids: ", count_buses)
            max_bus_id = max([bo.get('bus') for bo in bus_offset])
            #print("max_bus_id: ", max_bus_id)
            max_bus = [bo for bo in bus_offset if bo.get('bus') == max_bus_id][0]
            #print("max_bus: ", max_bus)
            max_bus_offset = max_bus.get('offset')
            #print("max_bus_offset: ", max_bus_offset)

            # start = 1000000000000 - 1000000000000 % max_bus_id
            start = max_bus_id
            addition = max_bus_id
            next = start

            #print("start: ", start)
            #print("next: ", next)
            #print("addition: ", addition)

            searching = True

            while searching:
                # Print next each 10000000 iteration
                #if next > start + addition * 10000000:
                #    print("next: ", next)
                #    start = start + addition * 10000000
                # print("max_bus_id: ", max_bus_id)
                counts = get_match_counter(next)
                # print("counts: ", counts)
                if counts == count_buses:
                    print("Start timestamp found that matches schedules and offset of all buses !!!")
                    searching = False
                else:
                    # Continue with next highest bus iteration
                    next += addition

            print("Timestamp: ", next - max_bus_offset)
