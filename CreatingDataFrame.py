# Any structure that has rows and columns is a data frame for pandas

# Creating Data frame using 2-D list
import pandas as pd

student_data =[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]



]
colum=['iq','marks','package']
obj = pd.DataFrame(student_data,columns=colum)

print(obj)

#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2

print("-----------------------------------------------------------------------------------")

# creating Data Frame using Dictionary

stu_dict = {
    'iq':[100,90,120,80],
    'marks':[80,70,100,50],
    'package':[10,7,14,2]


}

students =pd.DataFrame(stu_dict)
print(students)




# output

 
#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2
# -----------------------------------------------------------------------------------
#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2


