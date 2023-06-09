import openai

openai.api_key = "API_TOKEN"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {
                "role": "user",
                "content": "Employees should be taken using the following logical checks:\n\n1) If total employees "
                           "count given, we needs to take the full time/full-time employees count needs to take.\n2) "
                           "If the employees count given for various department-wise we needs to add all the "
                           "count.\n3) If both 2021 and 2022 employees count given, consider only 2022 count for the "
                           "total number of employees.\n4) If different locations given we need to add the employees "
                           "count of different locations\n5) we do not consider the contract employees as "
                           "employees.\n6) we do not consider the part time employees as employees.\n7) we do not "
                           "consider the consultants as employees.\n8) we do not consider the temporary employees as "
                           "employees.\n9) Please exclude the employees of our Manager or any other third party "
                           "employees. In this case, our employees count = 0.\n10) If the total employees comprised "
                           "of salary, hourly and seasonal employees. \nPlease consider the salary employees (or) "
                           "salaried employees.\n11)In the total employees count, some employees are classified as "
                           "salary or salaried employees. \nwe need to consider only the salary employees (or) "
                           "salaried employees.\n12) We should not take the anticipated employees count, we take only "
                           "confirmed employees count.\n13) Please exclude (part time/ part-time) employees from the "
                           "total employees.\n14) We need to add the employees of the subsidaries also with the "
                           "company.\n15) If both the company and the group employees are given we have to take the "
                           "group employees.\n16) If both full-time employees and hourly employees given we need to "
                           "consider full-time employees or full time employees alone.\n\nSEC URL: "
                           "https://www.sec.gov/Archives/edgar/data/1365916/000136591623000023/amrs-20221231.htm\n"
                           "\nUsing the above logics please extract the \"employees count\" from the sec website\n "
             }
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)