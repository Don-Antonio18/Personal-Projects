#list containing student info
s=[62000001, ["Jane","Doe"], [ ["COMP1126",[7, 8, 10,50] ], ["COMP1127",[0,6,9,20] ] ] ]

print (s[2])

#list all courses done by a given student
def get_courses(s):
    clist = []
    for i in s[2]:
        clist = clist + [i[0]]
    return clist