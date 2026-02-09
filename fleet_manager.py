def main():

    student = [""]


    def init_database():
        names = ["Janeway", "Sisko", "Spock", "Uhura", "Scotty"]
        ranks = ["Captain", "Captain", "Commander", "Lieutenant", "Lieutenant Commander"]
        divs = ["Command", "Command", "Sciences", "Operations", "Operations"]
        id = ["1","2","3","4","5"]

        return names, ranks, divs, id
    
    
    def display_menu():

        student_name = input("Full name: ").strip()

        if student_name:
            student[0] = student_name

        print("=== Menu ===")
        print("Logged in: " + student[0])
        print("1) Database")
        print("2) Add member")
        print("3) Remove member")
        print("4) Update rank")
        print("5) Display roster")
        print("6) Search crew")
        print("7) Filter by division")
        print("8) Calculate payroll")
        print("9) Count officers")
        print("10) Exit")

        option = input("Choose an option: ").strip()
        return option
    

    def add_member(names, ranks, divs, id):

        valid_ranks = ["Ensign", "Lieutenant", "Lieutenant Junior Grade", "Lieutenant Commander", "Commander", "Captain", "Admiral"]

        name = input("Name: ").strip().title()

        while True:
            rank = input("Rank: ").strip().title()

        


        names.append(name)

    
main()