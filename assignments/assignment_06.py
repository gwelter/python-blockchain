import json
import pickle

user_input_list = []

def get_user_choice():
    """ Get the user choice """
    return input("Your choice: ")


def save_simple_data_to_file(content):
    with open('common_data.txt', mode='a') as fo:
        fo.write(content + '\n')


def read_simple_data_from_file():
    with open('common_data.txt', mode='r') as fo:
        for line in fo:
            print(line, end='')


def save_list_data_to_file(content):
    global user_input_list
    user_input_list.append(content)
    with open('common_data.json', mode='w') as fo:
        fo.write(json.dumps(user_input_list))

    with open('common_data.b', mode='wb') as fo:
        fo.write(pickle.dumps(user_input_list))


def read_json_data_from_file():
    global user_input_list
    with open('common_data.json', mode='r') as fo:
        user_input_list = json.load(fo)
        print(user_input_list)


def read_pickle_data_from_file():
    global user_input_list
    with open('common_data.b', mode='rb') as fo:
        file_content = fo.read()
        user_input_list = pickle.loads(file_content)
        print(user_input_list)


waiting_for_input = True

while waiting_for_input:
    print("\nPlease choose one option")
    print("1: Say something")
    print("2: List what you've said")
    print("3: List what you've said (json)")
    print("4: List what you've said (pickle)")
    print("q: Quit")

    user_choice = get_user_choice()
    if user_choice == "1":
        content = input("- ")
        save_simple_data_to_file(content)
        save_list_data_to_file(content)
    if user_choice == "2":
        read_simple_data_from_file()
    if user_choice == "3":
        read_json_data_from_file()
    if user_choice == "4":
        read_pickle_data_from_file()
    if user_choice == "q":
        waiting_for_input = False