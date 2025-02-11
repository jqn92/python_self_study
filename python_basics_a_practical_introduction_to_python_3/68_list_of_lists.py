# Unfinished
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

def enrollment_stats(list_of_universities):
    total_students = []
    total_tuition = []
    for university in list_of_universities:
        total_students.append(university[1])
        total_tuition.append(university[2])
    return print(sum(total_students)), print(sum(total_tuition))



enrollment_stats(universities)
print(f"total students: {total_students}")
print(f"total tuition: ${total_tuition}")
