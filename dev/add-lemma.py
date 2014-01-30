import sys;

main = False;

for line in sys.stdin.readlines(): #{


	if line.count('"main"') > 0 and line.count('<sec') > 0: #{
		main = True;
	#}


	if line.count('</sec') and main == True: #{
		main = False;
	#}

	if main: #{

		if line.count('<r>') > 0 and line.count('lm=') < 1: #{
			lema = line.replace('<b/>', ' ').split('<r>')[1].split('<')[0];
			line = line.replace('<e', '<e lm="'+lema+'"');
			print(line.strip('\n'));
		else: #{
			print(line.strip('\n'));
		#}
	else: #{

		print(line.strip('\n'));
	#}
#}
