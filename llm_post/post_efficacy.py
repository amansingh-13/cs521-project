import argparse
import os
import json
import subprocess

parser = argparse.ArgumentParser(description='Calculates accuracy of generated postconditions')

parser.add_argument('--data', type=str, required=True, help='human eval jsonl file path')
parser.add_argument('--inputs', type=str, required=True, help='plus_input or base_input')
parser.add_argument('--postdir', type=str, required=True, help='directory of postconditions')
parser.add_argument('--codedir', type=str, required=True, help='directory of buggy code')

args = parser.parse_args()
assert args.inputs == "plus_input" or args.inputs == "base_input"

datafile = open(args.data)
data = [json.loads(l) for l in datafile.readlines()]
datafile.close()

def check_efficacy(k, pidx, asserts):
    inst = data[k]
    falsified, invalid = 0, 0

    for cname in os.listdir(args.codedir + f"/{k}/"):
        f = open(args.codedir + f"/{k}/{cname}")
        code = f.read()
        f.close()
        
        test = "from typing import List\n" + \
                code.replace(inst['entry_point'], "_canonical") + \
                "\nreturn_val = None\n"+inst['prompt'] + "    " + \
                "\n    ".join(asserts)

        for inp in inst[args.inputs]:
            test += "\nreturn_val = _canonical(*" + str(inp) + ")"
            test += "\n" + inst['entry_point'] + "(*" + str(inp) + ")"
        
        tmpfile = open("/tmp/_tmpfile.py", "w")
        tmpfile.write(test)
        tmpfile.close()

        try:
            out = subprocess.run(["python3", "/tmp/_tmpfile.py"],
                    capture_output=True, timeout=15, check=True)
        except Exception as e:
            out = e

        output = out.stderr.decode('utf-8') if out.stderr else ""

        if("AssertionError" in output):
            falsified += 1

    return falsified


for k, inst in enumerate(data):
    good, okay = 0, 0

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

        timedout = False
        try:
            out = subprocess.run(["python3", "/tmp/_tmpfile.py"], timeout=30, check=True)
        except subprocess.TimeoutExpired as e:
            timedout = True
        except Exception as e:
            out = e

        if(not timedout and not out.returncode):
            falsified = check_efficacy(k, pidx, asserts)
            if(falsified > 0):
                good += 1
            okay += 1
    
    print(k, "->", good, okay)
