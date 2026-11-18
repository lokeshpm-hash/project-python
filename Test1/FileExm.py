import csv
import json
with open("names.txt","w") as file:
    file.write("Arun\n")
    file.write("priya\n")
    file.write("Rahul\n")
    file.write("Divya\n")
    file.write("karthik")
    
    
with open("names.txt","r") as file:
    count=0
    for row in file:
        count=count+1
        print(count,row)
    
    
students=[
          ["lokesh","95"],
          ["jyothi","93"],
          ["vikki","82"],
          ["raghu","80"],
          ["kamalesh",'50']]  
with open("students.csv", "w", newline="") as file:
    dictWriter = csv.DictWriter( file, fieldnames=["name", "marks"]    )

    dictWriter.writeheader()

    for student in students:
        dictWriter.writerow({
            "name": student[0],
            "marks": student[1]
        })

with open("students.csv", "r", newline="") as file:
    dictReader = csv.DictReader(file)

    for row in dictReader:
        if int(row["marks"])>60:
            print(row)
            
            
with open("students.json","w") as file:
    json.dump(students,file,indent=2)
    
try:
    with open("students.json","r") as file:
        data=json.load(file)
    print(data)
    
except FileNotFoundError:
    print("Sorry! file not found")
finally:
    print("program executed")