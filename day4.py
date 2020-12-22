def main():
    input = open("day4_input.txt")
    lines = ""
    validPassports = 0
    i = input.read()
    while i:
        lines = lines + i 
        i = input.readline()
    split_line = lines.split("\n\n")
    result = []
    for j in range(len(split_line)):
        result.append(split_line[j].replace("\n", " ").split(" ")) #replace newlines with spaces and split on spaces
    for k in range(len(split_line)):
        field = []
        data = []
        for l in range(len(result[k])):
            field.append(result[k][l].split(":")[0])
            data.append(result[k][l].split(":")[1])
            
        if("byr" in field and "iyr" in field and "eyr" in field and 
        "hgt" in field and "hcl" in field and "ecl" in field and "pid" in field): #very ugly but works
            validPassports += 1
    

    return validPassports



if __name__ == '__main__':
	returnVal = main()
	print(returnVal)