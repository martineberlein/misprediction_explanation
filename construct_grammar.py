import sys
import os
import pandas as pd

#help prints
def usage():
	print(f"Usage: {sys.argv[0]} -g <grammar_name>")
	print("  -g grammar_name  specify the grammar name by giving black box name")
	print("  -h, --help       print help")

args = sys.argv[1:]
grammar_name = None

#read arguments
while args:
	arg = args.pop(0)
	if arg in ["-h", "--help"]:
		usage()
		sys.exit(0)
	elif arg == "-g":
		if not args:
			print(f"Error: {arg} requires grammar name")
			usage()
			sys.exit(1)
		grammar_name = args.pop(0)
	else:
		print(f"Error: wrong argument {arg}")
		usage()
		sys.exit(1)
		
#check if -g was read
if grammar_name is None:
	print("Error: missing required argument -g <grammar_name>")
	usage()
	sys.exit(1)

#build path for .csv file
tesdata = f"blackboxes/testdata/{grammar_name}rfcXtest1.csv"

#check if file exists
if not os.path.exists(tesdata):
	print(f"Error: {teastdata} does not exist")
	usage()
	sys.exit(1)

#read .csv and exctract feature names for start symbol
df = pd.read_csv(tesdata)
columns = ' '.join(f"<{col}>" for col in df.columns)

#construct start symbol
grammar = {
	"<start>": [f"{columns}"],
}

#construct expansions
for col in df.columns:
	grammar[f"<{col}>"] = ["0", "<onenine><maybe_digits>"]

#add digit creation
grammar.update({
	"<onenine>": 'srange("123456789")',
	"<maybe_digits>": ["", "<digits>"],
	"<digits>": ["<digit>", "<digit><digits>"],
	"<digit>": 'list(string.digits)'
})

#creat .py file defining grammar
with open(f"grammars/{grammar_name}.py", "w") as f:
	f.write(f"import string\n")
	f.write(f"from fuzzingbook.Grammars import srange, Grammar\n\n")
	f.write(f"#{grammar_name} Grammar(after normalization and multiplication to remove negative and float values)\n")
	f.write(f"{grammar_name.upper()}: Grammar = {{\n")
	for i, (key, value) in enumerate(grammar.items()):
		replace = str(value).replace("'", '"')
		comma = "," if i < len(grammar) - 1 else ""
		f.write(f"{' ' * 4}\"{key}\": {replace}{comma}\n")
	f.write("}\n")

print(f"Grammar written to grammars/{grammar_name}.py")
