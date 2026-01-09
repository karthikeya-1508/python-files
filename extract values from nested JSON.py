#JSON data:
data = {
   "student":{
       "name": "Cora",
        "marks":{
           "math":90,
           "chem":95
         }
      }
    }     

      
#Code to extract data from JSON:
name =  data['student']['name']
math_marks = data['student']['marks']['math']
chem_marks = data['student']['marks']['chem']

print("name of student", name)
print("math marks", math_marks)
print("chem marks", chem_marks)