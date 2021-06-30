if __name__ == '__main__':
    students = dict()
    flag = 0
    while 1:
        # Take user's input through the console
        input_data = input()
        # Break statement
        if input_data == 'end':
            break

        # Split the input data and add it to a list
        split_data = input_data.split(",")
        personal_info = split_data[:3]
        subject_info = split_data[3:]
        key = split_data[2]
        dict_value = [personal_info, subject_info]

        # If there is already a student with the same key, then just add info about the new subject that isn't there,
        # otherwise add all data about the student
        for x in list(students.keys()):
            if key == x:
                students[key].append(subject_info)
                flag = 1
            # else:
            # student[key] = dict_value // doesn't work

        if flag == 0:
            students[key] = dict_value
        else:
            flag = 0

    # Search the dictionary and print the wanted data
    for x in students.values():
        print("Student: " + x[0][0] + " " + x[0][1])
        for y in range(1, len(x)):
            ocenka = 5
            vkupno_poeni = int(x[y][1]) + int(x[y][2]) + int(x[y][3])
            if 50 < vkupno_poeni <= 60:
                ocenka = 6
            elif 60 < vkupno_poeni <= 70:
                ocenka = 7
            elif 70 < vkupno_poeni <= 80:
                ocenka = 8
            elif 80 < vkupno_poeni <= 90:
                ocenka = 9
            elif 90 < vkupno_poeni <= 100:
                ocenka = 10
            print("----" + x[y][0] + ":", ocenka)
        print()
