output_file = open("5letterwords.txt", "w")

# converts word-list into 5 letter ones only
with open("words_alpha.txt", "r") as f:
    write_count = 0
    print("Started writing")
    for word in f:
        if len(word) == 6:
            write_count = write_count + 1
            output_file.write(word)
            print(write_count)
