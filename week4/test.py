if __name__ == "__main__":
    file = open("quiz.txt")
    array = [int(number) for number in file]
    array = set(array)
    result = []
    for n1 in array:
        for n2 in array:
            target = n1+n2
            if target in range(-10000,10001) and n1 != n2:
                if target not in result:
                    result.append(target)

    print(len(result))