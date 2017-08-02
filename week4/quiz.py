from collections import defaultdict

table = defaultdict(list)

def hash_function(x):
    return x%3000

def hash_table(table,value):
    table[(hash_function(value))].append(value)

def search(table,t):
    for i in table:
        for l in table[i]:
            t_key = (t-l)%3000
    #     c = table.get(t_key,())
            if t_key in table:
                 n = table.get(t_key,())
                 if (t-l) in n:
                    if (t-l) != l: 
                        return 1
    return 0
    

if __name__ == "__main__":
    file = open("quiz.txt")
    for number in file:
        hash_table(table,int(number))

    count = 0
    t = -10000
    while t <= 10000:
        if search(table,t) == 1:
            count +=1
        t +=1
        print(count)
    print(count)

        


