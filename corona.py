def main():
    virus_composition = input().lower()
    if len(virus_composition) <= 0 and len(virus_composition) > 10 ** 5:
        print("Invalid input")
    total_no_of_people = int(input())
    if total_no_of_people <= 0 and total_no_of_people > 10:
        print("Invalid input")

    list_of_blood_type = []
    for i in range(0, total_no_of_people):
        list_of_blood_type.append(input().lower())

    for blood_com in list_of_blood_type:
        if len(virus_composition) <= 0 and len(virus_composition) > 10 ** 5:
            print(f"{(list_of_blood_type.index(blood_com)) + 1} invalid input")

    virus_comp = []
    for i in range(len(virus_composition)):
        virus_comp.append(virus_composition[i])

    for blood_comp in list_of_blood_type:

        i = 0
        j = 0
        while i < len(virus_comp) and j < len(blood_comp):
            if blood_comp[j] == virus_comp[i]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(blood_comp):
            print("POSITIVE")
        else:
            print("NEGATIVE")


main()
