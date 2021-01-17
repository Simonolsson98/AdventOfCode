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
    print(rule_dict)
    for message in messages:
        should_break = False
        rule = '0' #only need to check rule 0 according to spec

        for val in rule_dict[rule]:
            sub_rule = val.split(" ")
            for each_sub_rule in sub_rule:
                print(f"SUB_RULE: {sub_rule}")
                print(f"CHECKING: {each_sub_rule} WITH MESSAGE: {message}")
                if not find_rules(each_sub_rule, message, rule_dict):
                    print("rule didnt work, break!") #should break to next message here...
                    should_break = True
                    break
            if should_break == True:
                break
        if len(message) == 0:
            valid_messages += 1
        print("next message:")

    return valid_messages 

def find_rules(each_sub_rule, msg, rule_dict):
    global message
    message = msg
    temp_message = message

    print(f"for rule {each_sub_rule}: {rule_dict[each_sub_rule]}")
    if rule_dict[each_sub_rule][0].count("\"") > 0: #we hopefully reached the rule with the terminal in it, i.e "a" or "b" or similar
        try:
            if message[0] == rule_dict[each_sub_rule][0][1]:
                print(f"message changed from {message}")
                message = message[1:]
                print(f"to {message}")
                return True
            else:
                return False
        except IndexError:
            return False
    else:
        for either_rule in rule_dict[each_sub_rule]:
            if isinstance(either_rule, str) and len(either_rule) == 1: #if 2: 5 for example 
                if not find_rules(rule_dict[each_sub_rule], message, rule_dict):
                    return False
            else:
                #either_rule is ex: 10 8
                split_rules = either_rule.split(" ")
                print(f"split_rules: {split_rules}")
                for indiviual_rule in split_rules:
                    if not find_rules(indiviual_rule, message, rule_dict): #if either of the rules fail to parse, break
                        message = temp_message #reset message
                        break
                print(f"message: {message}")
        return True

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =