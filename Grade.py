Last_Semester_Gradebook = [["physics", 70], ["calculus", 80], ["Poetry", 99], ["history", 100]]



Gradebook = [["physics", 98], ["caculas", 97], ["poetry",85], ["history", 88]]

print(Gradebook)

Gradebook.append(["computer science", 100])
Gradebook.append(["visual arts", 93])
Gradebook[-1][-1] += 5
Gradebook[2].remove(85)
Gradebook[2].append("Pass")


print(Gradebook)

Full_Gradebook = Last_Semester_Gradebook + Gradebook
print(Full_Gradebook)
print(Full_Gradebook)