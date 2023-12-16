import random 
import csv

def DataGenrator() :
    cgpa = random.randint(5,10)
    iq = random.randint(85,120)

    studentInstance = {
        "cgpa": cgpa ,
        "iq" : iq 
    }

    return studentInstance

def write_student(file_path , number_of_student = 500):
    # Generate fake student data
    student = [DataGenrator() for _ in range(number_of_student)]

    # Specify the CSV file header
    fieldnames = ['cgpa' , 'iq']

    # Write data to CSV file
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write student instances
        writer.writerows(student)


csv_file_path = 'students.csv'
write_student(csv_file_path)
print(f'Students Data are written  in {csv_file_path}')