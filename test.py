with open('comp.txt', 'r') as f:
    line = f.readline()
    saved = []
    high = 0
    while line:
        term = line.strip('\n')
        number = int(f.readline().strip('\n'))
        if number > high:
            saved = [term, number]
            high = number
        line = f.readline()
    print(f'Term: {saved[0]}. Occurences: {saved[1]}')