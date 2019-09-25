print("Hello, welcome to markbook")
book.print_classrooms()
action = input("what would you like to do")

selected_class = input("What class would you like to view")
book.classrooms[selected_class].print_students()

