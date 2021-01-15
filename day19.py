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
        if(re.match(r"[a-z]", rule[4:])):
            char_rule.append(rule)
        try:
            either_rule = rule.split(" | ")
            either_rule[0] = either_rule[0].split(":")[1][1:]
            rule_dict[rule[0:2]] = either_rule
            #sub_rules = either_rule.split(" ")
        except IndentationError:
            pass
    valid_messages = 0
    for message in messages:
        for rule in rule_dict.keys():
            pass
    print(rule_dict)
    return None
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =