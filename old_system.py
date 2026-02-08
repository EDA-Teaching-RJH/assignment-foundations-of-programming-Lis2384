n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    
    while loading < 5:
        loading += 1 in range(5)                           #added +1 to each line and gave it a range of 5 so it stops 
        print("Loading module" + str(loading))
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = int(input("Select option: "))                  #Made it an integer input  
        
        if opt == 1:                                       #Added another equal sign
            print("Current Crew List:")
            
            for i in range(len(n)):                           #changed the range for 4 to len so that opt 2 can run
                print(n[i] + " - " + r[i]) 
                
        elif opt == 2:                                   #Removed the "" off of every opt as its an integer not a string
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")
            
        elif opt == 3:
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == 4:
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or "Commander": 
                    count = count + 1
            print("High ranking officers: " + count) 
            
        elif opt == 5:
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()                    #Added brakets
