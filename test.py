def main():
    list1 = []
    list2 = []
    sum_dist = 0
    with(open("input.txt", 'r')) as f:
        for line in f:
            list1.append(int(line.strip().split()[0]))
            list2.append(int(line.strip().split()[1]))

    for num in list1:
        sum_dist += num * list2.count(num)
    print(sum_dist)

if __name__ == '__main__':
    main()