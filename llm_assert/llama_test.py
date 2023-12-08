import argparse
import os
import subprocess
import re

parser = argparse.ArgumentParser(description='Tests LLM\'s efficiency in generating asserts')

parser.add_argument('--runner', type=str, required=True, help='path to model runner')
parser.add_argument('--model', type=str, required=True, help='path to model')
parser.add_argument('--abench', type=str, required=True, help='assert benchmark directory')
parser.add_argument('--timeout', type=int, required=True, help='upper bound LLM codegen time')
parser.add_argument('--temp', type=float, default=0.8, help='temperature for LLM codegen')

args = parser.parse_args()

tmpfile = "/tmp/llm_test_tmp.c"

def parse(lines):
    source, target = [], []
    asrt_lnos, cmnt_lnos = [], []

    # improve this
    for i,l in enumerate(lines):
        if re.search("assert[(].+[)]", l):
            asrt_lnos.append(i)
        elif re.search("//", l):
            cmnt_lnos.append(i)
    return asrt_lnos, cmnt_lnos


for f in os.listdir(args.abench):
    fd = open(os.path.join(args.abench, f), "r")
    
    lines = fd.readlines()
    asrt_lnos, cmnt_lnos = parse(lines)
    assert len(asrt_lnos) == len(cmnt_lnos), "Dataset formatting error : {}".format(f)

    for i, al in enumerate(asrt_lnos):
        cl = cmnt_lnos[i]
        assert al > cl

        prompt = "".join(lines[:cl+1]+["\n"])
        truth = "".join(lines[cl+1:al+1])
        
        tmpfd = open(tmpfile, "w")
        tmpfd.write(prompt)
        tmpfd.close()
        try:
            out = subprocess.run([args.runner, "-m", args.model, "-f", tmpfile,
                "-s", "42", "--temp", str(args.temp)], capture_output=True, timeout=args.timeout)
        except subprocess.TimeoutExpired as e:
            out = e

        olines = out.stdout.decode('utf-8').split('\n')
        oasrt_lnos, ocmnt_lnos = parse(olines)
        assert ocmnt_lnos[i] == cl
        if(len(oasrt_lnos) > i):
            output = "\n".join(olines[ocmnt_lnos[i]+1:oasrt_lnos[i]+1])
        else:
            output = "\n".join(olines[ocmnt_lnos[i]+1:])

        print("--FILENAME--")
        print(f)
        print("--TRUTH--")
        print(truth)
        print("--OUTPUT--")
        print(output)

    fd.close()
