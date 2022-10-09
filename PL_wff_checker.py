#Helper Functions
def ConvertToList(string):
    str_list = []
    str_list[:0] = string    
    return str_list

#User Input 
wff = input('WFF: ')# gets user input, converts to upper case, returns string
user_list = ConvertToList(wff) #converts user input to list

# Merge items on list to form -> and <->
def merge_conditional(list):
    for i in list:
        if i == '>':
            r = list.index(i)
            if r != 0:
                if list[r-1] == '-':
                    list[r-1:r+1] = [''.join(list[r-1:r+1])]                    
                    print(list)
            else:                
                break
    return list

def merge_biconditional(list):
    for i in list:
        if i == '->':
            r = list.index(i)
            if r != 0:
                if list[r-1] == '<':
                    list[r-1:r+1] = [''.join(list[r-1:r+1])]                    
                    print(list)
            else:                
                break
    return list

merge_conditional(user_list)
merge_biconditional(user_list)

user_list_index = [] # list of the indices of all characters
user_list_enumerated = list(enumerate(user_list))#list of characters of user input with its index number

# Error List
error_list = [] # list that we append strings of error statements.

# Logical Operators and Symbols
letters = "ABCDEFGQHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz" #exclude v
accept_letters= ConvertToList(letters) #List from propositional operators
accept_symbols = ['->','~', 'v','^','<->']
connectives = ['->','v','^','<->']
parentheses = ['(',')']
accept_char = [*accept_letters, *accept_symbols, *parentheses] # unpacks lists into one list

# CHECK FOR ACCEPTABLE CHARACTERS:
def check_characters():
    char_value = True
    for i in user_list:
        if i in accept_char:
            char_value = True
        else:
            error_list.append(f"{i} is not a symbol in propositional logic.")
            char_value = False
            break
    return char_value

# CHECK FOR DOUBLE LETTERS:
def check_propositional_letters():
    for x, y in user_list_enumerated:
        print(x,y)
        if y in accept_letters:
            x+=1        
            y = user_list_enumerated[x][0]
            if x < len(user_list_enumerated):
                if y in accept_letters:
                    error_list.append(f"There is a problem with your use of propositional letters. You likely have two letters next to each other.")
                    return False
                else:
                    return True
        else:
            return True

# CHECK PARENTHESES - STEP 1. Compare the sizes of parentheses
def check_paren_size():        
    left_par = []
    right_par = []
    for i in user_list:
        if i == '(':
            left_par.append(i)
        elif i == ')':
            right_par.append(i)
    if len(left_par) == len(right_par):
        return True
    else: 
        error_list.append('You are missing a parenthesis')

# CHECK PARENTHESES - STEP 2. Check LEFT AND RIGHT ORDER
#No idea how to get NEC and SUF conditions if paren are always correct. So, let's just throw a bunch of necessary conditions:

# UPDATE: This needs to be revised. I'm only checking the char to the right. I should also check to the left. In the case of the right paren, I'm only checking to the left. (()) will pass as wff

def check_left_paren():
    for x, y in user_list_enumerated:
        if y == '(':
            x+=1        
            y = user_list_enumerated[x][1]
            if y in accept_letters or y == '(' or y == '~':
                return True
            else:
                error_list.append(f"There is a problem with your use of the left parenthesis.")
                return False
        else:
            return True

def check_right_paren():
    for x, y in user_list_enumerated:
        if y == ')':
            x-=1        
            y = user_list_enumerated[x][1]
            if y in accept_letters or y == ')' or y in connectives:
                return True
            else:
                error_list.append(f"There is a problem with your use of the right parenthesis.")
                return False
        else:
            return True

###############
# OPERATORS
############

def check_negation():
    wff_status = True
    for x, y in user_list_enumerated:
        if y == '~':
            if x == len(user_list_enumerated)-1:
                wff_status = False 
                error_list.append(f"There is a problem with your use of negation.")   
            elif x <= len(user_list_enumerated)-1:
                x+=1        
                y = user_list_enumerated[x][1]
                if y in accept_letters or y == '(' or y == '~':
                    pass
                else:
                    error_list.append(f"There is a problem with your use of negation.")
                    wff_status = False
        else:
            pass
    return wff_status

# Update: Loop not correct. Need to check all instances, not just the first. See code in negation for example

def check_operators():
    wff_status = True
    for x, y in user_list_enumerated:
        if y == '^' or y == 'v' or y == '->' or y == '<->':            
            if x == len(user_list_enumerated)-1 or x == 0: #check if last char
                wff_status = False 
                error_list.append(f"There is a problem with your use of the operators. Connectives (^, v, ->, <->) cannot occur at the end or the beginning of a wff.")
                break
            elif x <= len(user_list_enumerated)-1 and x != 0:
                x+=1 # gets the next index
                r_char= user_list_enumerated[x][1] # char to the right
                x-=2
                l_char=user_list_enumerated[x][1]
                if (l_char in accept_letters or l_char == ')') and (r_char in accept_letters or r_char == '(' or r_char == '~'):
                    return wff_status
                else:
                    error_list.append('Something is wrong with your use of operators.')
                    wff_status = False
                    break       
            else:                
                error_list.append('Something is wrong with your use of operators.')
                wff_status = False
                break
        else:
            pass
    return wff_status

check_list = [check_characters(), check_propositional_letters(), check_paren_size(), check_left_paren(), check_right_paren(), check_negation(),check_operators()]

#print(check_list) # Used for testing

def check_wff():
    if all(check_list):
        print("Your formula is a wff.")
    else:
        for i in error_list:
            print("This is not a wff.", i)

check_wff()

#1. NEXT, need to link all of the above together to output a clear statement "This is a wff or This is not a wff because reasons X, Y, Z"
#2. Put in GUI
