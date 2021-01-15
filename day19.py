import time
import re
def main():
    input = open("day19_input.txt")
    i = input.readline()   
    lines = ""
    while i:
        lines += i
        i = input.readline()
    
    rules = lines.split("\n\n")[0].split("\n")
    messages = lines.split("\n\n")[1]
    #print(rules)
    rule_dict = {}
    char_rule = []
    for rule in rules:
        if(re.match(r"[a-z]", rule.split(":")[1][1:])):
            char_rule.append(rule.split(":")[1][1:])
            break
        try:
            either_rule = rule.split(" | ")
            either_rule[0] = either_rule[0].split(":")[1][1:]
            try: 
                rule_dict[rule[0:2]] = [either_rule[0], either_rule[1]]
            except IndexError:
                rule_dict[rule[0:2]] = [either_rule[0]]
            #sub_rules = either_rule.split(" ")
        except IndentationError:
            pass
    valid_messages = 0
    for message in messages:
        for rule in rule_dict.keys():
            find_rules(rule, message, rule_dict)            
    

def find_rules(rule, message, rule_dict):
    if re.match(r"[a-z]", rule_dict[rule]) == None:
        list_of_rules = rule_dict[rule].split(", ")
        for ind_rule in list_of_rules:
            spl_rule = ind_rule.split(" ")
            if(find_rules(spl_rule[0], message, rule_dict)) == True and find_rules(spl_rule[1], message, rule_dict) == True:
                return True
            else: 
                return False
    else: #we hopefully reached the rule with the terminal in it, i.e "a" or "b" or similar
        if message[0] == rule_dict[rule]:
            message = message[1:]
            return True
        else:
            return False

    print(rule_dict)
    return None
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =