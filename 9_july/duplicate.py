str=raw_input("enter the string : ")


def remove_dup(str):
    output = []
    for word in str.split():
        if word not in output:
            output.append(word)

    return ' '.join(output)


print remove_dup(str)


