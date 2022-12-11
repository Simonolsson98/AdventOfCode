input = open("day04_input.txt")
i = input.readline()

fully_contained = 0
any_overlap = 0

while i:
	sub_range = i.split(",")
	first_elf_sections = sub_range[0].split("-")
	second_elf_sections = sub_range[1].split("-")

	first_elf_range = range(int(first_elf_sections[0]), int(first_elf_sections[1]))
	second_elf_range = range(int(second_elf_sections[0]), int(second_elf_sections[1]))

	if((first_elf_range.start <= second_elf_range.start and second_elf_range.stop <= first_elf_range.stop) or 
		(second_elf_range.start <= first_elf_range.start and first_elf_range.stop <= second_elf_range.stop)):
		fully_contained += 1

	if((first_elf_range.start <= second_elf_range.start and second_elf_range.start <= first_elf_range.stop) or
	(second_elf_range.start <= first_elf_range.start and first_elf_range.start <= second_elf_range.stop)):
		any_overlap += 1

	i = input.readline()


# part 1: 
print("day4: solution for part 1: " + str(fully_contained))

# part 2:  
print("day4: solution for part 2: " + str(any_overlap))