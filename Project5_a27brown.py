import Project5Helpers
data = Project5Helpers.get_job_data()
for game in data:
    print(game)
input("Press enter to continue...")
desired_job = []
def load_data():
    data = desired_job
    return data

def print_menu():
    print("[1] Quit")
    print("[2] Software Security")
    print("[3] Penetration Tester")
    print("[4] Digital Forensics")
    print("[5] Software Developer")
    print("[6] Software Testing SDET")
    print("[7] Database Professional")
    print("[8] Web Developer")

def main():
    game_data = load_data()
    while True:
        print_menu()
        choice = input("Please enter your choice:")
        if choice == "1":
            break
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        else:
            print("Please enter a valid choice")
main()



