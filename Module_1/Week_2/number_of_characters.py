def character_count(word):
    character_statistic = {}

    # Your Code Here
    word = word.strip()
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    # End Code Here

    return character_statistic
