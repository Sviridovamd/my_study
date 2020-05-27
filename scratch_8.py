import sys
import subprocess
cmd = input().split()
subprocess.run(cmd)

for i in range(1,len(sys.argv)):
    print(sys.argv[i])

