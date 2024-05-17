
days = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
    21: [],
    22: [],
    23: [],
    24: [],
    25: [],
    26: [],
    27: [],
    28: [],
    29: [],
    30: []
}

while True:
    cmd = input("Calendar > ")
    if cmd == "quit" or cmd == "exit":
        break
    if cmd == "add_task":
        day = int(input("Which day? "))
        task = input("What is the task? ")
        days[day].append(task)
    if cmd == "view_all":
        for d in days:
            print(f"{d}: {days[d]}")
    if cmd == "view":
        day = int(input("Which day? "))
        for i in days[day]:
            print(days[day])