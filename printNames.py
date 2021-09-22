def printName():
	file_name = input("Input the .txt file containing the roster: ")
	my_file = open(file_name, "r")
	
	list_names = []
	#source: kite.com
	for line in my_file:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		list_names.append(line_list)
		
	my_file.close()
	
	print(list_names)
	
	
printName();
