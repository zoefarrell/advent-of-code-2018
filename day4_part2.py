file_object = open("input_day_4.txt", "r")
entries = file_object.readlines()
file_object.close()

#We need to put the entries in time order
entries_list = []
for entry in entries:
	entries_list.append(entry)
entries_list.sort()

current_guard_id = 0
time_fell_asleep = 0
guard_sleep_amounts = {}
current_sleepiest_guard = 0
current_sleepiest_minute_for_one_guard = 0
for entry in entries_list:
	split_entry = entry.strip().replace('[', "").split(']')
	#Case for "Guard #1871 begins shift"
	if split_entry[1][1] == "G":
		current_guard_id = split_entry[1].split()[1][1:]
	#Case for falls asleep
	elif split_entry[1].strip() == "falls asleep":
		time_fell_asleep = int(split_entry[0][-2:])
	#Case for wakes up
	else:
		if not current_guard_id in guard_sleep_amounts.keys():
			guard_sleep_amounts[current_guard_id] = [0] * 60

		for i in range(time_fell_asleep, int(split_entry[0][-2:])):
			guard_sleep_amounts[current_guard_id][i] += 1
			if guard_sleep_amounts[current_guard_id][i] > current_sleepiest_minute_for_one_guard:
				current_sleepiest_minute_for_one_guard = guard_sleep_amounts[current_guard_id][i]
				current_sleepiest_guard = current_guard_id

sleepiest_guard = current_sleepiest_guard
print("sleepiest guard", sleepiest_guard)
sleepiest_minute =  guard_sleep_amounts[sleepiest_guard].index(max(guard_sleep_amounts[sleepiest_guard]))
print("sleepiest minute", sleepiest_minute)
print("answer", int(sleepiest_guard) * sleepiest_minute)