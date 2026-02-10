def main():

    student = [""]


    def init_database():
        names = ["Janeway", "Sisko", "Spock", "Uhura", "Scotty"]
        ranks = ["Captain", "Captain", "Commander", "Lieutenant", "Lieutenant Commander"]
        divs = ["Command", "Command", "Sciences", "Operations", "Operations"]
        id = ["1","2","3","4","5"]

        return names, ranks, divs, id
    
    
    def display_menu():
        

        print("=== Menu ===")
        print("Logged in: " + student[0])
        print("1) Add member")
        print("2) Remove member")
        print("3) Update rank")
        print("4) Display roster")
        print("5) Search crew")
        print("6) Filter by division")
        print("7) Calculate payroll")
        print("8) Count officers")
        print("9) Exit")

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
                print("Valid rank:", valid_ranks)


        while True:
            div = input("Division: ").strip().title()

            if div in valid_divs:
                break

            else:
                print("Invalid division")
                print("Valid division: ", valid_divs)
        

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
    
    names, ranks, divs, id = init_database()

    student[0] = input("Full name: ").strip()

    while True:
        option = display_menu()

        if option == "1":
            add_member(names, ranks, divs, id)
        
        elif option == "9":
            print("Exiting")
            break
            



main()