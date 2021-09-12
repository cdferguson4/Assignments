Course_Info = {'CS101':[
    {"Room_Number": 3001},
     {"Instructor": "Haynes"},
     {"Meeting Time":"8:00 a.m."}    
    
    ],
    'CS102':[
        {"Room_Number": 4501},
        {"Instructor": "Alvarado"},
        {"Meeting Time": "9:00 a.m."}

    ],
    'CS103':[
        {"Room_Number": 6755},
        {"Instructor": "Rich"},
        {"Meeting Time": "10:00 a.m."}
        

    ],
    'NT110':[
        {"Room_Number":1244},
        {"Instructor":"Burke"},
        {"Meeting Time":"11:00 a.m."}


    ],
    'CM241':[
        {"Room_Number":241},
        {"Instructor":"Lee"},
        {"Meeting Time":"1:00 p.m."}

    ]      
    }


course_num = str(input("What Course are you looking for?"))
course = ""

for course in Course_Info:
    if course_num == course:
        print(Course_Info[course_num])





