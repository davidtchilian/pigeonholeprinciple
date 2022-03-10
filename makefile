install:
	pip3 install python-sat[pblib,aiger]
	chmod 777 cnf.sh
	chmod 777 dimacs.sh

exemple:
	python3 pigeon.py -u -m 3 3