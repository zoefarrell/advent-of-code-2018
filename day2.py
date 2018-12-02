#For part 1
def checksum(ids):
    total_double_letter_words = 0
    total_triple_letter_words = 0
    for single_id in ids:
        letter_counts = {}
        for letter in single_id:
            if letter in letter_counts.keys():
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        if has_exactly_n_of_any_letter(letter_counts, 2):
            total_double_letter_words += 1
        if has_exactly_n_of_any_letter(letter_counts, 3):
            total_triple_letter_words += 1

    return (total_double_letter_words * total_triple_letter_words)

def has_exactly_n_of_any_letter(letter_counts, n):
    for key in letter_counts:
        if letter_counts[key] == n:
            return True
    return False

#For part 2
def find_common_letters(ids):
    for i in range(len(ids[0])):
        ids_without_character_set = set()
        for single_id in ids:
            id_without_character = single_id[:i] + single_id[i + 1:]
            if id_without_character in ids_without_character_set:
                return id_without_character
            else:
                ids_without_character_set.add(id_without_character)

file_object = open("input_day_2.txt", "r")
ids = file_object.readlines()
print(find_common_letters(ids))
file_object.close()