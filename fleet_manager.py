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
    
    def remove_member(names, ranks, divs, id):

        remove = input("whats the ID you want to remove: ").strip()
        
        if remove in id:
            remove_id = id.index(remove)

            names.pop(remove_id)
            ranks.pop(remove_id)
            divs.pop(remove_id)
            id.pop(remove_id)

            print("Removed member")
        
        else:
            print("ID not found")
    
    def update_rank(names, ranks, id):

        valid_ranks = ["Ensign", "Lieutenant", "Lieutenant Junior Grade", "Commander", "Captain", "Admiral"]
        print("Valid ranks are: " + ", " .join(valid_ranks))

        mem_id = input("ID to update: ").strip()

        if mem_id in id:
            up_id = id.index(mem_id)

            while True:
                new_rank = input("New rank: ").strip().title()

                if new_rank in valid_ranks:
                    ranks[up_id] = new_rank
                    print("Rank updated for " + names[up_id])
                    break

                else:
                    print("Invalid rank")
        
        else:
            print("ID not found")

    def display_roster(names, ranks, divs, id):

        print("=== Roster ===")

        for roster in range(min(len(names), len(ranks), len(divs), len(id))):
            print(id[roster] + " " + names[roster] + " " + ranks[roster] + " " + divs[roster])

    def search_crew(names, ranks, divs, id):

        term = input("Search term: ").strip().lower()

        found = False

        for search in range(len(names)):
            if term in names[search].lower():
                print(id[search] + " " + names[search] + " " + ranks[search] + " " + divs[search])
                found = True

        if found == False:
                print("No matches")

    def filter_by_division(names, divs):

        choice = input("Division: ").strip().title()

        if choice == "Command":
            target = "Command"
        
        elif choice == "Operations":
            target = "Operations"

        elif choice == "Sciences":
            target = "Sciences"
        
        else:
            print("Invalid division")
            return
        
        found = False

        for division in range(len(names)):
            if divs[division] == target:
                print(names[division])
                found = True
        
        if found == False:
            print("No crew in that divion")

    def calculate_payroll(ranks):

        total = 0

        for rank in ranks

            if rank == "Captain":
                total = total + 1000
            
            elif rank == "Commander":
                total = total + 800
            
            elif rank == "Lieutenant Commander":
                total = total + 600
            
            elif rank == "Lieutenant":
                total = total + 400

            elif rank == "Lieutenant Junior Grade":
                total = total + 300
            
            else rank == "Ensign":
                total = total + 200

            else total + total + 0

        return total

        






    names, ranks, divs, id = init_database()






    student[0] = input("Full name: ").strip()

    while True:
        option = display_menu()

        if option == "1":
            add_member(names, ranks, divs, id)
        
        elif option == "2":
            remove_member(names, ranks, divs, id)
        
        elif option == "3":
            update_rank(names, ranks, id)
        
        elif option == "4":
            display_roster(names, ranks, divs, id)
        
        elif option == "5":
            search_crew(names, ranks, divs, id)

        elif option == "6":
            filter_by_division(names, divs)
        
        elif option == "7":
            calculate_payroll(ranks)
        
        elif option == "9":
            print("Exiting")
            break
            



main()