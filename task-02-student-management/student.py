class Student:

    def __init__(self, name, email, phone, course, student_id=None):
        self.id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.course = course

    def display_details(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Course:", self.course)

    def update_details(self, name, email, phone, course):
        self.name = name
        self.email = email
        self.phone = phone
        self.course = course