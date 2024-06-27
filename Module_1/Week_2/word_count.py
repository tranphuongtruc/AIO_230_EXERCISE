def count_word(file_path):
    counter = {}

    # Your Code Here
    with open(file_path, 'r') as file:
        data = file.read().lower().split()
        for word in data:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    # End Code Here

    return counter


path = 'P1_data.txt'

word_count = count_word(path)
output = "{\n"
for (key, value) in word_count.items():
    output += f" '{key}' : {value},\n"
output += "}"
print(output)
