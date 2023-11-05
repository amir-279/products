total_marks = 0
num_subjects = 10
passing_marks = 20

while True:
    for i in range(num_subjects):
        marks = int(input("Enter your nomreh {}:".format(i + 1)))
        total_marks += marks
    
    average = total_marks / num_subjects
    
    if average >= passing_marks:
        print("tabrik shoma yek bicycle jayezeh gereftid")
        break
    
    print("nomreh shoma : ", average)
    print("dobareh bekhon")
    total_marks = 0