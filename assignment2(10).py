#create a dictionary to hold student details

Details = {
    1: {
        "name": "raksh",
        "age": 20,
        "section": "C"
    },
   
    2: {
        "name": "riya",
        "age": 19,
        "section": "B"
       
    },
    3: {
        "name": "vivan",
        "age": 20,
        "section": "C"
       
    },
    4: {
        "name": "vivan",
        "age": 20,
        "section": "C"
       
    }
}
for i in Details:
    if i % 2 == 0:
        print(i,":",Details[i])
