# Jason Gonzalez
rooms = {
'Home': {"North": 'Abandoned Library', 'Item': 'Shoes'},
'Abandoned Library': {"East": 'Town Market', 'Item': 'A Scroll'},
'Town Market': {"North": 'Blacksmith', 'Item': 'Garlic'},
'Blacksmith': {"West": 'Forge', 'Item': 'Armor'},
'Forge': {"South": 'Stables', 'Item': 'A Sword'},
'Stables': {"West": 'The Woods', 'Item': 'A Horse'},
'The Woods': {"South": 'Draculas Castle', 'Item': 'Dracula!'}

}
state = 'Home'


# function
def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state
    return new_state  # return


# function
def get_item(state):
    return rooms[state]['Item']  # returning Item value


# function
def show_instructions():
    # print a main menu and the commands
    print("Vampire Text Adventure Game")
    print("Collect 6 items to win the game, or be killed by Dracula.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


show_instructions()  # calling function
inventory = []
while (1):  # gameplay loop
    print('You are in ', state)  # printing state
    print('Inventory:', inventory)  # printing inventory
    item = get_item(state)  # calling get_item function
    print('You see', item)  # print
    print('------------------------------')
    if item == 'Dracula':  # if
        print('GAME OVER!')
        print('Thanks for playing!')
        exit(0)
    direction = input('Enter your move: ')  # asking user
    if (direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South'):  # if
        direction = direction[3:]
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('The room has wall in that direction enter other direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    elif direction == str('get '+item):  # if
        if item in inventory:  # if item already present in inventory
            print('Item already taken go to another room!!')
        else:
            inventory.append(item)  # appending
    else:
        print('Invalid direction!!')  # print
    if len(inventory) == 6:
        # print
        print('Congratulations! You have collected all items and saved your hometown!')
        print('Thanks for playing!')
        exit(0)