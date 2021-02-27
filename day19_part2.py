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
    global message #has to be global, since we are doing recursion
    for message in messages:
        should_break = False
        rule = '0' #only need to check rule 0 according to spec

        for val in rule_dict[rule]:
            print(val)
            sub_rule = val.split(" ")
            for each_sub_rule in sub_rule:
                if not find_rules(each_sub_rule, message, rule_dict):
                    should_break = True #should break to next message here...
                    break
            if should_break == True: #scuffed way to break out of nested for loop
                break
        if len(message) == 0: #if entire message was parsed, it is a successful message!
            valid_messages += 1

    return valid_messages 

def find_rules(each_sub_rule, msg, rule_dict):
    global message
    message = msg
    temp_message = message

    if rule_dict[each_sub_rule][0].count("\"") > 0: #we hopefully reached the rule with the terminal in it, i.e "a" or "b" or similar
        try:
            if message[0] == rule_dict[each_sub_rule][0][1]: #if first char in message matches the rule, it passes parsing!
                message = message[1:] #so we remove this char and end this recursive branch
                return True
            else:
                return False
        except IndexError:
            return False
    else:
        length = -1
        counter = 0 #used to check if we passed all the rules in a sequence of rules
        if each_sub_rule == 8:
            rule_dict[each_sub_rule] = "42 | 42 8"
        elif each_sub_rule == 11:
            rule_dict[each_sub_rule] = "42 31 | 42 11 31"
        #print(f"{each_sub_rule}, : {rule_dict[each_sub_rule]}")
        for either_rule in rule_dict[each_sub_rule]:
            
            if isinstance(either_rule, str) and len(either_rule) == 1: #if 2: 5 for example 
                if not find_rules(rule_dict[each_sub_rule], message, rule_dict):
                    return False
            else: #either_rule is ex: 10 8
                split_rules = either_rule.split(" ")
                length = len(split_rules)
                for indiviual_rule in split_rules:
                    if not find_rules(indiviual_rule, message, rule_dict): #if either of the rules fail to parse, break
                        message = temp_message #reset message
                        break
                    counter += 1
                if counter == length: #if this is true, we passed all the rules in a sequence (either of the rule sequences split with a "|")
                    return True #sequence hopefully finished here
                counter = 0

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 311
