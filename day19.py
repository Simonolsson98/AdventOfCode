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
    messages = messages.split("\n")

    rule_dict = {}
    char_rule = []
    for rule in rules:
        if(re.match(r"[a-z]", rule.split(":")[1][1:])):
            char_rule.append(rule.split(":")[1][1:])
            break
        try:
            either_rule = rule.split(" | ")
            key = either_rule[0].split(":")[0]
            either_rule[0] = either_rule[0].split(":")[1][1:]
            try: 
                rule_dict[key] = either_rule[0], either_rule[1]
            except IndexError:
                rule_dict[key] = either_rule[0]
        except IndentationError:
            pass
    valid_messages = 0

    print(rule_dict)
    global message
    for message in messages:
        for rule in rule_dict.keys():
            for val in rule_dict[rule]:
                sub_rule = val.split(" ")
                for each_sub_rule in sub_rule:
                    print(each_sub_rule)
                    if find_rules(each_sub_rule, message, rule_dict) == False:
                        break
                    if message == "":
                        valid_messages += 1
                        break
                        

def find_rules(each_sub_rule, message, rule_dict):
    print(rule_dict[each_sub_rule])
    if len(re.findall("\"[a-z]\"", rule_dict[each_sub_rule])) == 0:
        rule_or_rule = rule_dict[each_sub_rule].split(", ")
        #print(rule_or_rule)
        for ind_rule in rule_or_rule:
            spl_rule = ind_rule.split(" ")
            if find_rules(spl_rule[0], message, rule_dict) == True and find_rules(spl_rule[1], message, rule_dict) == True:
                return True
            else: 
                return False
    else: #we hopefully reached the rule with the terminal in it, i.e "a" or "b" or similar
        print(f"message[0]: {message[0]}")
        if message[0] == rule_dict[each_sub_rule][1]:
            print(f"message changed from {message} \n")
            message = message[1:]
            print(f"to {message}")
            return True
        else:
            return False

    print(rule_dict)
    return None
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =