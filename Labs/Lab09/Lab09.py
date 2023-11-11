import Sort
import Handler
import Tester
# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      Sorts lists of unsorted numbers in to ascending order.
# 4. What was the hardest part? Be as specific as possible.
#      When pretty good because I had made most of the pudeocode before hand sp all I had to do was convert it to python.
# 5. How long did it take for you to complete the assignment?
#      3hrs
# 6. Youtube Link: https://www.youtube.com/watch?v=IKbr_wI8nzI&ab_channel=school

def main():
    print("Would you like to sort a list from a file or use a test list?")
    print("1. File")
    print("2. Test List")
    print("3. Quit")
    choice = input("> ")
    if choice == "1":
        filename = Handler.get_filename()
        unsorted_list = Handler.load_file(filename)
        sorted_list = Sort.custom_sort(unsorted_list)
        print(f"Sorted list: {sorted_list}")
    elif choice == "2": # This would be removed before going to client
        Tester.test_cases()
    elif choice == "3":
        print("Goodbye!")
        return
    else:
        print("Invalid input. Please try again.")
    
    main()

if __name__ == "__main__":
    print("Welcome to the Sub-List Sort Program!")
    main()
