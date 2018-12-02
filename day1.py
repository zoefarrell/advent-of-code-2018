#coding: utf-8

def findDuplicateFrequency(lines):  
    frequencies_seen = set()
    total = 0
    #Keep looping through the lines in the file until you find a duplicate frequency
    while True:
        for line in lines:
            total += int(line)
            if total in frequencies_seen:
                return total
            else:
                frequencies_seen.add(total)


file_object = open("input_day_1.txt", "r")
lines = file_object.readlines()
print(findDuplicateFrequency(lines))
file_object.close()