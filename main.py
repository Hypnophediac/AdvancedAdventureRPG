from adventurelib import *
from colorama import init, Fore, Back, Style

# Initialize colorama for colored text
init()

# Game state
current_room = None
inventory = Bag()

# Basic room setup
@when('look')
def look():
    """Look around the current room."""
    print(f'\n{Fore.CYAN}{current_room}{Style.RESET_ALL}')
    if current_room.items:
        print('You see:')
        for item in current_room.items:
            print(f'* {item}')

@when('inventory')
def show_inventory():
    """Show the player's inventory."""
    print('\nYou are carrying:')
    if not inventory:
        print('Nothing')
    else:
        for item in inventory:
            print(f'* {item}')

# Main game initialization
def init_game():
    """Initialize the game world and start the game."""
    global current_room
    
    # Create rooms
    start_room = Room("""
    You find yourself in a dimly lit chamber. Ancient runes glow faintly on the walls,
    pulsing with mysterious energy.
    """)
    
    # Set starting room
    current_room = start_room

def main():
    """Main game function."""
    print(f'{Fore.GREEN}Welcome to Advanced Adventure RPG!{Style.RESET_ALL}')
    print('Type "help" for a list of commands.')
    
    init_game()
    look()
    start()
