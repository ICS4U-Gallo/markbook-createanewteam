room = {"smith john": "random shit", "adams bond": "random shit", "his may": "random shit", "dem boi": "random shit"}


assignments = {}


def add_assignment():

    name = input("name of assignment")
    due_date = input("due")
    points = input("points")

    assignments[name] = {}
    assignments[name]["name"] = name
    assignments[name]["due"] = due_date
    assignments[name]["points"] = points
    assignments[name]["marks"] = {}
    for i in room.keys():
        assignments[name]["marks"][i] = None


def delete_assignment():
    assignments.pop(input())


def update_marks():

    assignment_name = input("name of assignment")
    student_name = input("student")
    mark = input("mark")

    assignments[assignment_name]["marks"][student_name] = [mark]


def student_avg(student_name: str):

    a = 0 
    x = 0
    for i in assignments:
        b = int(assignments[i]["points"]) * int(assignments[i]["marks"][student_name])
        y = int(assignments[i]["points"])

        a += b
        x += y 

    return a/x

