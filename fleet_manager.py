def main():

    student = [""]

    def init_database():
        names = ["janeway", "Sisko", "Spock", "Uhura", "Scotty"]
        ranks = ["Captain", "Captain", "Commander", "Lieutenant", "Lieutenant Commander"]
        divisions = ["command", "Command", "Science", "Operations", "Engineering"]
        ids = [1, 2, 3, 4, 5]

        return names, ranks, divisions, ids


    def display_menu():
        student[0] = input("Name: ").strip()

        while True:
            print("=== Menu ===")
            print("Logged in: " + student[0])
            print("1")
            print("2")
            print("3")
            print("4")
            print("5")
            print("6")
            print("7")
            print("8")
            print("9")
            print("10")

            option = input("Choose an option: ").strip()

            if option in ["1","2","3","4","5","6","7","8","9","10"]:
                return option
            
            else:
                print("Invalid")

            


