import re

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
            checkConditions = 0
            for m in range(len(field)):
                fieldName = field[m]
                dataToCheck = str(data[m])
                if fieldName == "byr":
                    if re.match(r'\b[0-9]{4}\b', dataToCheck) and int(dataToCheck) >= 1920 and int(dataToCheck) <= 2002:
                        checkConditions += 1
                elif fieldName == "iyr":
                    if re.match(r'\b[0-9]{4}\b', dataToCheck) and int(dataToCheck) >= 2010 and int(dataToCheck) <= 2020:
                        checkConditions += 1
                elif fieldName == "eyr":
                    if re.match(r'\b[0-9]{4}\b', dataToCheck) and int(dataToCheck) >= 2020 and int(dataToCheck) <= 2030:
                        checkConditions += 1
                elif fieldName == "hgt":
                    metricOrNot = dataToCheck[len(dataToCheck)-2:]
                    number = dataToCheck[:len(dataToCheck)-2]
                    if re.match(r'\b[0-9]{3}cm\b', dataToCheck) and int(number) >= 150 and int(number) <= 193:
                        checkConditions += 1
                    elif re.match(r'\b[0-9]{2}in\b', dataToCheck) and int(number) >= 59 and int(number) <= 76:
                        checkConditions += 1
                elif fieldName == "hcl":
                    if re.match(r'^#[0-9a-f]{6}\b', dataToCheck):
                        checkConditions += 1
                elif fieldName == "ecl":
                    if re.match(r'\bamb\b|\bblu\b|\bbrn\b|\bgry\b|\bgrn\b|\bhzl\b|\both\b', dataToCheck):
                        checkConditions += 1
                elif fieldName == "pid":
                    if re.match(r'\b[0-9]{9}\b', dataToCheck):
                        checkConditions += 1
            if checkConditions == 7:
                validPassports += 1
    return validPassports

if __name__ == '__main__':
	returnVal = main()
	print(returnVal)