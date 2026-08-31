import csv

valid_students=[]
invalid_students=[]
error_reports=[]


with open("data/students.csv","r") as file:
    reader =csv.DictReader(file)

    for student in reader:
        errors = []

        if not student["Student Name"]:
           errors.append("Student Name is missing")

        if not student["College"]:
           errors.append("College is missing")

        if not student["Course"]:
           errors.append("Course is missing")  

        if not student["Phone"]:
           errors.append("Phone is missing")

        if not student["Attendance"]:
           errors.append("Attendance is missing")  

        if not student["Email"]:
           # print(student["Student Name"],"Email is missing")
           errors.append("Email is missing")

        elif "@" not in student["Email"] or "." not in student["Email"]:
           # print(student["Student Name"],"invalid email")
           errors.append("Invalid email")

        if not student["Marks"]:
           errors.append("Marks is missing")

        else:

            try:
           
                marks =float(student["Marks"])

                if marks <0 or marks >100:
                # print(student["Student Name"],"Invalid marks")
                  errors.append("Invalid marks") 

            except ValueError:
               errors.append("Invalid marks")

       # print(student["Student Name"],errors)

        if errors:
         invalid_students.append(student)

         error_reports.append({
             "Student Name":student["Student Name"],
             "Error": ", ".join(errors)
          })
        
        else:
         valid_students.append(student) 

#print("valid", valid_students)
#print("invalid",invalid_students)

fieldnames =reader.fieldnames
with open("output/valid_students.csv","w", newline="") as file:
   writer =csv.DictWriter(file,fieldnames=fieldnames)

   writer.writeheader()
   writer.writerows(valid_students)


with open("output/invalid_students.csv","w",newline="")as file:
   writer=csv.DictWriter(file,fieldnames=fieldnames)

   writer.writeheader()
   writer.writerows(invalid_students)

with open("output/error_report.csv","w", newline="") as file:
   writer=csv.DictWriter(file,fieldnames=["Student Name" ,"Error"])

   writer.writeheader()
   writer.writerows(error_reports)


total_records =len(valid_students)+len(invalid_students)

print("Student Data Processing Summary")
print("--------------------------------")
print("Total Records:" , total_records)
print("Valid Records:",len(valid_students))
print("Invalid Records", len(invalid_students))