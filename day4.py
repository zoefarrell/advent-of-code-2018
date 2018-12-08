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
current_longest_time_slept = 0
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
		time_slept =  (int(split_entry[0][-2:]) - time_fell_asleep)
		if current_guard_id in guard_sleep_amounts.keys():
			guard_sleep_amounts[current_guard_id] += time_slept
		else:
			guard_sleep_amounts[current_guard_id] = time_slept
		#If adding this interval makes this guard the sleepiest so far, update
		if guard_sleep_amounts[current_guard_id] > current_longest_time_slept:
			current_longest_time_slept = guard_sleep_amounts[current_guard_id]
			current_sleepiest_guard = current_guard_id

sleepiest_guard = current_sleepiest_guard
print("sleepiest guard", current_sleepiest_guard)

#Find the minute this guard slept the most
times_guard_slept_during_this_minute = [0] * 60

current_guard_id = 0
time_fell_asleep = 0
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
		if current_guard_id == sleepiest_guard:
			for i in range(time_fell_asleep, int(split_entry[0][-2:])):
				times_guard_slept_during_this_minute[i] += 1

sleepiest_minute = times_guard_slept_during_this_minute.index(max(times_guard_slept_during_this_minute))
print("sleepiest minute", sleepiest_minute)
print("answer", int(sleepiest_guard) * sleepiest_minute)