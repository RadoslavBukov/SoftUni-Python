"""
Input	                            Output

SoftUni -> AA12345                  SoftUni
SoftUni -> BB12345                  -- AA12345
Microsoft -> CC12345                -- BB12345
HP -> BB12345                       Microsoft
End	                                -- CC12345
                                    HP
                                    -- BB12345

SoftUni -> AA12345                  SoftUni
SoftUni -> CC12344                  -- AA12345
Lenovo -> XX23456                   -- CC12344
SoftUni -> AA12345                  Lenovo
Movement -> DD11111                 -- XX23456
End	                                Movement
                                    -- DD11111
"""
text = input().split(" -> ")
company = dict()

while text[0] != "End":

    company_name = text[0]
    id = text[1]
    if company_name not in company.keys():
        company[company_name] = list()
    if id not in company[company_name]:
        company[company_name].append(id)

    text = input().split(" -> ")

for (key, value) in company.items():
    print(f"{key}")
    for names in (value):
        print(f"-- {names}")
