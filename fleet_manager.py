def main():

    def init_database():
        names = ["Janeway", "Sisko", "Spock", "Uhura", "Scotty"]
        ranks = ["Captain", "Captain", "Commander", "Lieutenant", "Lieutenant Commander"]
        divs = ["Command", "Command", "Sciences", "Operations", "Operations"]
        id = ["1","2","3","4","5"]

        return names, ranks, divs, id
    
    def display_menu():

        print("=== Menu ===")
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