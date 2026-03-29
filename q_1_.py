# Quiz ID: Z75101

def class_grades() -> list:
    lst1 = []
    while True:

        try:
            a = int(input("Enter a grade: "))
            if a == -999:
                if len(lst1) >= 10:
                    break
                else:
                    print('need at least 10 grades')
            elif a < 0 or a > 100:
                print("not in range, skip")
            else:
                lst1.append(a)
        except ValueError:
            print("invalid input, skip")
            continue
    return lst1

def max_avg_valid(list):
    print(f'highest grade: {max(list)}')
    print(f'the class avg was: {sum(list) / len(list)}')
    print(f'the number of valid grades entered: {len(list)}')




grades = (class_grades())
max_avg_valid(grades)