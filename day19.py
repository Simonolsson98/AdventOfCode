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
        either_rule = rule.split(" | ")
        key = either_rule[0].split(":")[0]
        either_rule[0] = either_rule[0].split(":")[1][1:]
        to_add = []
        for rule_asd in either_rule:
            to_add.append(rule_asd)
        rule_dict[key] = to_add
   
    valid_messages = 0
    global message
    message = ""
    print(rule_dict)
    for asd in messages:
        message = asd
        should_break = False
        rule = '0' #only need to check rule 0 according to spec

        for val in rule_dict[rule]:
            sub_rule = val.split(" ")
            for each_sub_rule in sub_rule:
                print(f"SUB_RULE: {sub_rule}")
                print(f"CHECKING: {each_sub_rule}")
                if not find_rules(each_sub_rule, message, rule_dict):
                    print("rule didnt work, break! (reset message pls)") #should break to next message here...
                    should_break = True
                    break
            if should_break == True:
                break
        if len(message) == 0:
            valid_messages += 1

    return valid_messages 

def find_rules(each_sub_rule, message, rule_dict):
    global asd
    asd = message
    print(rule_dict[each_sub_rule].count("\""))
    print(f"for rule {each_sub_rule}: {rule_dict[each_sub_rule][0]}")
    if rule_dict[each_sub_rule][0].count("\"") > 0: #we hopefully reached the rule with the terminal in it, i.e "a" or "b" or similar
        print(f"message[0]: {message[0]} for rule: {each_sub_rule}")
        if message[0] == rule_dict[each_sub_rule][0][1]:
            print(f"message changed from {message}")
            message = message[1:]
            print(f"to {message}")
            return True
        else:
            return False
    else:
        for either_rule in rule_dict[each_sub_rule]:
            if isinstance(either_rule, str) and len(either_rule) == 1:
                if not find_rules(rule_dict[each_sub_rule], message, rule_dict):
                    return False
            else:
                print(either_rule)
                seq_of_rules = either_rule.split(", ")
                print(seq_of_rules)
                for sequence in seq_of_rules:
                    list_of_rules = sequence.split(" ")
                    print(list_of_rules)
                    for indiviual_rule in list_of_rules:
                        if not find_rules(indiviual_rule, message, rule_dict):
                            break
                        
                    return True
        return False

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =