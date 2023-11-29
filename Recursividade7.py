def permutations(string, prefix=""):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            new_prefix = prefix + string[i]
            remaining_chars = string[:i] + string[i + 1:]
            permutations(remaining_chars, new_prefix)

input_string = "ABC"
permutations(input_string)