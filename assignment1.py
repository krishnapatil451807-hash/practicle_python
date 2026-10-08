students={
    101:{"name":"aditi","scores":[78,85,90]},
    102:{"name":"rahul","scores":[45,60,50]},
    103:{"name":"karan","scores":[50,45,87]},
    104:{"name":"sharvil","scores":[55.67,75]}
}
for sid,details in students.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["avarage"]=avg
    details["passed"]=avg>=50
print("student who passed : ")
for sid,details in students.items():
    if details["passed"]:
        print(details["name"])