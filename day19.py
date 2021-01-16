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
        rule = '0' #only need to check rule 0 according to spec
        temp_message = message
        for val in rule_dict[rule]:
            sub_rule = val.split(" ")
            print(sub_rule)
            for each_sub_rule in sub_rule:
                print(f"CHECKING: {each_sub_rule}")
                if find_rules(each_sub_rule, message, rule_dict) == False:
                    print("rule didnt work, break! (reset message pls)")
                    break
            message = temp_message
        if len(message) == 0:
            valid_messages += 1

def find_rules(each_sub_rule, message, rule_dict):
    print(rule_dict[each_sub_rule].count("\""))
    print(f"for rule {each_sub_rule}")
    if rule_dict[each_sub_rule].count("\"") > 0: #we hopefully reached the rule with the terminal in it, i.e "a" or "b" or similar
        print(f"message[0]: {message[0]} for rule: {each_sub_rule}")
        if message[0] == rule_dict[each_sub_rule][1]:
            print(f"message changed from {message}")
            message = message[1:]
            print(f"to {message}")
            return True
        else:
            return False
    else:
        for either_rule in rule_dict[each_sub_rule]:
            if isinstance(either_rule, str) and len(either_rule) == 1:
                if not find_rules(rule_dict[either_rule], message, rule_dict):
                    return False
            else:
                print(either_rule)
                seq_of_rules = either_rule.split(", ")
                print(seq_of_rules)
                for sequence in seq_of_rules:
                    list_of_rules = sequence.split(" ")
                    for indiviual_rule in list_of_rules:
                        if not find_rules(indiviual_rule, message, rule_dict):
                            return False
        return True

    print(rule_dict)
    return None
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =