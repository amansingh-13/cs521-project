import argparse
import os
import json
import subprocess
import ast

parser = argparse.ArgumentParser(description='Introduces bugs ;)')

parser.add_argument('--codedir', type=str, required=True, help='directory of code')
parser.add_argument('--buggydir', type=str, required=True, help='directory of buggy code')

args = parser.parse_args()

for k in range(45):
    os.makedirs(args.buggydir + f"/{k}/", exist_ok=True)

    for cidx in range(10):
        f = open(args.codedir + f"/{k}/{cidx}.py")
        code = f.read()
        f.close()

        bugs = {
                code,
                code.replace(">=", ">"),
                code.replace("<=", "<"),
                code.replace("and", "or"),
                code.replace("==", "!="),
                code.replace("!=", "=="),
                code.replace("not", ""),
                code.replace("+", "-"),
        }

        for j, bug in enumerate(bugs):
            f = open(args.buggydir + f"/{k}/{cidx}_{j}.py", "w")
            f.write(bug)
            f.close()

