import argparse
import os
import json
import subprocess
import ast

parser = argparse.ArgumentParser(description='Calculates accuracy of generated postconditions')

parser.add_argument('--data', type=str, required=True, help='human eval jsonl file path')
parser.add_argument('--inputs', type=str, required=True, help='plus_input or base_input')
parser.add_argument('--postdir', type=str, required=True, help='directory of postconditions')

args = parser.parse_args()
assert args.inputs == "plus_input" or args.inputs == "base_input"

datafile = open(args.data)
data = [json.loads(l) for l in datafile.readlines()]
datafile.close()

for k, inst in enumerate(data):
    failed, passed, invalid = 0, 0, 0

    for pidx in range(5):
        f = open(args.postdir + f"/{k}/{pidx}.py")
        asserts = []
        for line in f.readlines():
            if("assert" in line):
                asserts.append(line.strip())
        f.close()

        test = inst['prompt'].replace(inst['entry_point'], "_canonical") + \
                inst['canonical_solution'] + \
                "return_val = None\n"+inst['prompt'] + "    " + \
                "\n    ".join(asserts)

        for inp in inst[args.inputs]:
            test += "\nreturn_val = _canonical(*" + str(inp) + ")"
            test += "\n" + inst['entry_point'] + "(*" + str(inp) + ")"
        
        tmpfile = open("/tmp/_tmpfile.py", "w")
        tmpfile.write(test)
        tmpfile.close()

        try:
            ast.parse(test)
        except:
            invalid += 1

        timedout = False
        try:
            out = subprocess.run(["python3", "/tmp/_tmpfile.py"], timeout=30, check=True)
        except subprocess.TimeoutExpired as e:
            print("timeout on {}/{}".format(k, pidx))
            timedout = True
        except Exception as e:
            out = e

        if(timedout or out.returncode): failed += 1
        else: passed += 1

    print(k, "->", passed, failed, invalid)

