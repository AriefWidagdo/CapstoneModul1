[Program outline can be checked here](https://imgur.com/a/9Ovd8Xu)

This program simulates the front-end of a Fantasy RPG Shop. This program was written as requirement for Capstone Project Module 1. It allows user to manage shop inventories through Shop Management and allow user to buy and sell item as Player. The program implement CRUD (Create, Read, Update, Delete) operations to achieve this effect. The secondary objective of this program is to have an immersive and pleasing experience running the program, this mainly done by using Typewriter function and putting strategic delay in some functions.

## Features

### Via Shop Management, user can:
*   View all items in the Shop's inventory
*   Add new item to the Shop's inventory
*   Modify any item and any parameters(except Item's name) in the Shop's inventory
*   Delete item from the shop's stock
*   Restore deleted item

### As Player, user can:
*   Buy any item (as long as money permits) from the shop
*   Sell any item from Player's invetory
*   See the player's inventory
*   Fast Forward a day to increase Player's money

## How to use
Run the script from your Terminal, make sure Python is installed.

## Structure
This code can be organized into several functions:

### General Support Function
*   `typewriter()`: To simulate a typewriter machine
*   `find_item_in_shop()`: To find name in shop's inventory

### Shop Management
*   `create_item()`: Add new item to the shop's inventory
*   `read_data()`: Display the shop's inventory, additional functionality including searching item by name, sorting it by price (ascending and descending), filter it by item type
*   `update_item()`: Change any parameters as desired(except name)
*   `delete_item()`: Delete an item
*   `view_deleted_items()`: Display items that has been deleted by user (by default its empty)
*   `restore_item()`: Returned the deleted item to the shop's inventory

### Player Interaction
*   `beli_barang()`: buy item from shop's inventory and added it to the player's inventory
*   `jual_barang()`: sell the choosen item from player's inventory to the shops at half the original price
*   `view_player_inventory()`: see the player's currrent possessed item(s)
*   `next_day()`: Fast forward the day ahead as money gaining mechanism
