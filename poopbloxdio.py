import random
import sys
print("poop.bloxd.io")
games = ["testmode", "creative", "survival", "oneblock"]
print("games: ", games)

#GAMEMODES HERE

#TESTMODE

def testmode():
    actionwant = int(input("how many actions do you want?> "))
    thingvar = 0
    for i in range(actionwant):
        if actionwant <= 0:
            print("you have no actions left, exiting...")
            sys.exit()
        print(f"{actionwant} actions left...")
        actions = ["test1action", "test2action", "test3action", "exit"]
        print(actions)
        wantdo = input("do your buissness here> ")
        if wantdo in actions:
            print("check stage 1... complete.")
            if wantdo == "test1action":
                print("test1action works")
                print("thingvar +1")
                thingvar += 1
            elif wantdo == "test2action":
                print("test2action works")
                print("thingvar - 1")
                thingvar -= 1
            elif wantdo == "test3action":
                print("test3action works")
                print(thingvar)
            elif wantdo == "exit":
                print("exiting...")
                sys.exit()
            else:
                print("how did you get here?")
        else:
            print("it dosnt work, womp womp.")
        actionwant -= 1

#CREATIVE
def place_block(world):
    print("\n--- PLACE A BLOCK ---")
    
    # 1. Use try/except so typing letters instead of numbers won't crash the game
    try:
        col_input = input("Enter column (0-9): ")
        row_input = input("Enter row (0-9): ")
        
        target_col = int(col_input)
        target_row = int(row_input)
        
        # 2. Check if the numbers are actually on your 10x10 map
        if not (0 <= target_row < 10 and 0 <= target_col < 10):
            print("Error: Coordinates are outside the 10x10 map!")
            return  # Stops the function and goes back
            
    except ValueError:
        print("Error: Please type actual numbers for coordinates!")
        return

    # 3. Ask for the block type
    block_choice = input("Enter block type (#, X, M, or `): ")
    
    # 4. Check if it's one of your official blocks before placing it
    if block_choice in ["#", "X", "M", "`"]:
        world[target_row][target_col] = block_choice
        print("block placed successfully")
    else:
        print("error: invalid block")

def creative():
    # 1. Set the grid size
    ROWS = 10
    COLS = 10
    CENTER_ROW = 5  # Row 5 is the grass line

    # 2. Build the starting grid array
    world = []
    for r in range(ROWS):
        row_data = []
        for c in range(COLS):
            if r < CENTER_ROW:
                row_data.append("`")  # ` for Air
            elif r == CENTER_ROW:
                row_data.append("#")  # # for Grass
            else:
                row_data.append("X")  # X for Stone
        world.append(row_data)

    # 3. Print the starting grid cleanly
    print("starter grid")
    print("blocks: [#] grass  [X] stone  [M] wood  [`] air\n")

    # Print the top coordinate column numbers (0 to 9)
    print("   ", end="")
    for c in range(COLS):
        print(f"{c} ", end="")
    print("\n   " + "--" * COLS)

    # Print the clean map rows without brackets or quotes
    for r in range(ROWS):
        print(f"{r} |", end=" ")  # Print row number on the left side
        for c in range(COLS):
            print(world[r][c], end=" ")  # Print the block and a space
        print()  # Move to the next line
    while True:
        wantleave = input("do you want to leave (y/n)> ")
        if wantleave == "y":
            break
        place_block(world)
        # Print the updated grid after placing a block
        print("\nupdated grid")
        print("blocks: [#] grass  [X] stone  [M] wood  [`] air\n")
        print("   ", end="")
        for c in range(COLS):
            print(f"{c} ", end="")
        print("\n   " + "--" * COLS)
        for r in range(ROWS):
            print(f"{r} |", end=" ")
            for c in range(COLS):
                print(world[r][c], end=" ")
            print()  # Move to the next line

#SURVIVAL
def survival():
    wood = 0
    iron = 0
    gold = 0
    diamond = 0
    pickaxe = 1
    thingtodo = ["chop", "mine", "craft", "inven", "exit"]
    while True:
        print("what do you want to do?")
        print(thingtodo)
        wanttodo = input("> ")
        #chopping
        if wanttodo == "chop":
            print("you chopped some wood")
            wood += 4
        #mining
        elif wanttodo == "mine":
            if pickaxe >= 1:
                print("you mined some iron")
                iron += 7
            if pickaxe >= 2:
                print("you mined some gold")
                gold += 5
            if pickaxe >= 3:
                print("you mined some diamonds")
                diamond += 2
        #crafting
        elif wanttodo == "craft":
            if pickaxe == 1:
                if wood >= 1 and iron >= 3:
                    print("you crafted an iron pickaxe")
                    pickaxe = 2
            elif pickaxe == 2:
                if wood >= 2 and gold >= 3:
                    print("you crafted a gold pickaxe")
                    pickaxe = 3
            elif pickaxe == 3:
                if wood >= 3 and diamond >= 3:
                    print("you crafted a diamond pickaxe")
                    pickaxe = 4
        #inven
        elif wanttodo == "inven":
            print(f"you have {wood} wood")
            print(f"you have {iron} iron")
            print(f"you have {gold} gold")
            print(f"you have {diamond} diamonds")
            print(f"you have a level {pickaxe} pickaxe")
        elif wanttodo == "exit":
            print("exiting...")
            break
        else:
            print("invalid action")

#ONE BLOCK
def oneblock():
    oneblock = 0
    buildlayers = 0
    needblockforbuild = 8
    plains = ["grass", "dirt", "stone"]
    caves = ["stone", "iron", "gold", "diamonds"]
    while True:
        print(f"you have mined {oneblock} blocks")
        commands = ["mine", "craft", "inven", "build", "exit"]
        print(f"possible commands: {commands}")
        wanttodo = input("> ")
        if wanttodo == "mine":
            minedblock = random.choice(plains + caves)
            print(f"you mined a {minedblock} block")
            oneblock += 1
        elif wanttodo == "craft":
            print("nothing, yet")
        elif wanttodo == "inven":
            print(f"you mined {oneblock} blocks")
        elif wanttodo == "build":
            if oneblock >= needblockforbuild:
                buildlayers += 1
                oneblock -= needblockforbuild
                print(f"you built a layer, you have built {buildlayers} layers!")
                needblockforbuild *= 2
            else:
                print(f"you need {needblockforbuild} blocks to build a layer, you only have {oneblock}")

while True:
    wantgame = input("what game do you want to play?> ")
    if wantgame == "testmode":
        testmode()
        break
    elif wantgame == "creative":
        creative()
        break
    elif wantgame == "survival":
        survival()
        break
    elif wantgame == "oneblock":
        print("oneblock is not finished yet, but you can still play it!")
        wantoneblock = input("do you want to play oneblock (y/n)> ")
        if wantoneblock == "y":
            oneblock()
            break
        else:
            print("ok, choose a different game!")