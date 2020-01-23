def split_fileB(line):
    # split the input line into word, date and count_string
    dateword_count = line.split(",")
    # Split the dateword part into date and word
    date_word = dateword_count[0].split(" ")
    date = date_word[0]
    word = date_word[1]
    count_string = dateword_count[1]
    return (word, date + " " + count_string) 
