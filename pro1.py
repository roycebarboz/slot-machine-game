import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROW= 3
COLUMN=3

symbols={
    "A":3,
    "B":4,
    "C":2,
    "D":4
}

symbols_value={
    "A":4,
    "B":2,
    "C":4,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings , winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column= []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
    
        print()

def deposit():
    while True:
        amount = input("Enter amount you want to transfer: ")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("please enter valid amount")

        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet from 1-"+(str(MAX_LINES))+": ")
        if lines.isdigit():
            lines= int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print("please enter valid number of lines")
        else:
            print("please enter a number")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter amount between ${MIN_BET} - ${MAX_BET} which you want bet on each line: ")
        if amount.isdigit():
            amount= int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else:
                print("please enter valid amount")
        else:
            print("please enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f"insufficent balance,your current balance is {balance}")
        else:
            break
    print(f"you are bet is {bet} and number of lines are {lines} , your total bet is {total_bet}")

    slot= get_slot_machine_spin(ROW,COLUMN,symbols)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot,lines,bet,symbols_value)
    print(f"you won ${winnings}.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer= input("press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print("you left with ${balance}")

main()

