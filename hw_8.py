#โจทย์
dic_list = [{"code": "CSE-401", 
            "name": "Multimedia", 
            "Credit": 2.0}, 
            {"code": "CSE-101", 
            "name": "Computer Fundamental", 
            "Credit": 1.5}, 
            {"code": "CSE-305", 
            "name": "Unix Programming", 
            "Credit": 3.0}]
#ไว้เก็บค่า
dic_sum = []

#ค่าCode
max_01 = 0
max_02 = 0
max_03 = 0

# codeที่รับมาตัวแรก
# ตัด Cse- ออกให้เหลือตัวเลข
# แปลงตัวเลข
code_01 = dic_list[0]["code"]
code_01_1 = code_01.split("-")
code_01_1_1 = int(code_01_1[1])

code_02 = dic_list[1]["code"]
code_02_1 = code_02.split("-")
code_02_1_1 = int(code_02_1[1])

code_03 = dic_list[2]["code"]
code_03_1 = code_03.split("-")
code_03_1_1 = int(code_03_1[1])

#ตรวจสอบมากที่สุด
if code_01_1_1>= code_02_1_1 and code_02_1_1 >=code_03_1_1:
    max_01 = code_01_1_1
    max_02 = code_02_1_1
    max_03 = code_03_1_1
    dic_sum.append(dic_list[0])
    dic_sum.append(dic_list[1])
    dic_sum.append(dic_list[2])
elif code_01_1_1>= code_03_1_1 and code_03_1_1 >=code_02_1_1:
    max_01 = code_01_1_1
    max_02 = code_03_1_1
    max_03 = code_02_1_1
    dic_sum.append(dic_list[0])
    dic_sum.append(dic_list[2])
    dic_sum.append(dic_list[1])
    
elif code_02_1_1>= code_01_1_1 and code_01_1_1 >=code_03_1_1:
    max_01 = code_02_1_1
    max_02 = code_01_1_1
    max_03 = code_03_1_1
    dic_sum.append(dic_list[1])
    dic_sum.append(dic_list[0])
    dic_sum.append(dic_list[2])

elif code_02_1_1>= code_03_1_1 and code_03_1_1 >=code_01_1_1:
    max_01 = code_02_1_1
    max_02 = code_03_1_1
    max_03 = code_01_1_1
    dic_sum.append(dic_list[1])
    dic_sum.append(dic_list[2])
    dic_sum.append(dic_list[0])

elif code_03_1_1>= code_01_1_1 and code_01_1_1 >=code_02_1_1:
    max_01 = code_03_1_1
    max_02 = code_01_1_1
    max_03 = code_02_1_1
    dic_sum.append(dic_list[2])
    dic_sum.append(dic_list[0])
    dic_sum.append(dic_list[1])

elif code_03_1_1>= code_02_1_1 and code_02_1_1 >=code_01_1_1:
    max_01 = code_03_1_1
    max_02 = code_02_1_1
    max_03 = code_01_1_1
    dic_sum.append(dic_list[2])
    dic_sum.append(dic_list[1])
    dic_sum.append(dic_list[0])

#แสดงผล
print(max_01,max_02,max_03)
print(dic_sum)