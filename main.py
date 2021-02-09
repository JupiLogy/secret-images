import sys
from utils import write_to_file, read_from_file

if __name__ == "__main__":
    while True:
        print("\nJames, Rhiannon and Jeff's secret image messaging service")
        print("----------------------------*----------------------------")
        print("               How can we help you today?                ")
        print("               --------------------------                ")
        print("Service                                         |  Select")
        print("------------------------------------------------|--------")
        print("Encrypt message into image                      |    1   ")
        print("Decrypt message stored in image                 |    2   ")
        print("Exit                                            |    3   ")
        selected_option = False
        while not selected_option:
            opt = input("\nEnter your selection now: ")
            if opt == "1":
                write_to_file()
                selected_option = True
            elif opt == "2":
                read_from_file()
                selected_option = True
            elif opt == "3":
                sys.exit("See ya!")
                selected_option = True
            else:
                print("\nSorry, selection not recognised.\nPlease type a number then press enter.")
