import time

def main():
    input = open("day19_input.txt")
    i = input.readline()   
    lines = ""
    while i:
        lines += i
        i = input.readline()
    
    rules = lines.split("\n\n")[0].split("\n")
    messages = lines.split("\n\n")[1]
    print(rules)
    rule_dict = {}
    for rule in rules:
        
        print(rule_dict)
        try:
            either_rule = rule[1:].split(" | ")
            rule_dict[rule[0:2]] = either_rule
            #sub_rules = either_rule.split(" ")
        except IndentationError:
            pass
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =