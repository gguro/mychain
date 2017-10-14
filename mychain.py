
from app import *
from app import key, communicator, transaction


communicator.start()
initiate_node(3000)


# menu 1 : send_tx()
def send_tx():
    print("Input a message \n")
    print("9. Back")
    print("0. Quit")

    choice = input(" >> ")
    print(choice)

    if choice != '9' or choice != '0':
        message = choice
        pri_key, pub_key = key.get_key()
        tx = transaction.create_tx(pub_key, pri_key, message)
        transaction.send_tx(tx)
        back()
    else:
        exec_menu(choice)

    return


# menu 2 : create a block
def create_block_menu():
    create_block()
    back()

# menu 3 : show node list
def show_node_list():
    print("\nNode List\n")

    #list_all_node()
    back()

#menu 4 : show transaction list
def show_transaction_list():
    print("\nTransaction List\n")

    #list_all_transaction()
    back()

# menu 5
def show_block_list():
    print("\nBlock list\n")

    #list_all_block()
    back()


def exec_menu(choice):
    ch = choice.lower()

    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()

    return


# Back to main menu
def back():
    menu_actions['main_menu']()

# Terminate program
def terminate():
    import os
    os._exit(-1)

def main_menu():
    print("\nPlease choose the menu you want to start:")
    print("1. Send a transaction")
    print("2. Create a block")
    print("3. Show node list")
    print("4. Show transactionlist")
    print("5. Show block list")

    print("\n0. Quit\n")
    choice = input(" >> ")
    exec_menu(choice)

    return

#Menu definition
menu_actions = {
    'main_menu' : main_menu,
    '1' : send_tx,
    '2' : create_block_menu,
    '3' : show_node_list,
    '4' : show_transaction_list,
    '5' : show_block_list,
    '6' : back,
    '0' : terminate
}

if __name__ == '__main__':
    main_menu()
