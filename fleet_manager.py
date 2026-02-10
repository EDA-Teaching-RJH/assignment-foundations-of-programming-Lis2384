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
        valid_divs = ["Command", "Sciences", "Operations"]
        name = input("Name: ").strip().title()

        while True:
            rank = input("Rank: ").strip().title()

            if rank in valid_ranks:
                break

            else:
                print("Invalid rank")
                print("Valid rank:" + valid_ranks)


        while True:
            div = input("Division: ").strip().title()

            if div in valid_divs:
                break

            else:
                print("Invalid division")
                print("Valid division: " + valid_divs)
        

        while True:
            new_id = input("ID: ").strip()

            if new_id in id:
                print("ID exists, choose another")
                continue

            else:
                break



        names.append(name)
        ranks.append(rank)
        divs.append(div)
        id.append(new_id)

        print("Member added")

    while True:
        option = display_menu()

        if option == "1":
            names, ranks, divs, id = init_database()
            print("Database loaded")
        
        elif option == "2":
            add_member(names, ranks, divs, id)
        
        else:
            break



main()