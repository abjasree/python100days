def main():
    # Write code here
    def prime_checker(number):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            return number
        else:
            break

    tot_num_to_check = int(input())
    if tot_num_to_check < 1 and tot_num_to_check > 10:
        return

    l = []
    for i in range(tot_num_to_check):
        num = input()
        i = num.split(" ")
        l.append(i)

    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] = int(l[i][j])
            if l[i][j] < 2 and l[i][j] > 10 ** 6:
                return
    m = []
    for i in l:
        k = []
        for j in range(i[0], i[1] + 1):
            k.append(prime_checker(j))
        m.append(k)

    for i in m:
        h = len(i)
        count = 0
        for j in range(h):
            if i[j] == 0:
                count += 1
        if count == len(i):
            print(-1)
        else:
            maxi = max(i)
            mini = min(i)
            end = True
            while end:
                if mini == 0:
                    i.remove(0)
                    mini = min(i)
                else:
                    end = False
            diff = maxi - mini
            print(diff)


main()
