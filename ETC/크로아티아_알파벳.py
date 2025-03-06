import sys 

input = str(sys.stdin.readline())

org_num = len(input) - 1
if 'c=' in input:
    org_num -= input.count('c=')
if 'c-' in input:
    org_num -= input.count('c-')
if 'dz=' in input:
    org_num -= input.count('dz=')
if 'd-' in input:
    org_num -= input.count('d-')
if 'lj' in input:
    org_num -= input.count('lj')
if 'nj' in input:
    org_num -= input.count('nj')
if "s=" in input:
    org_num -= input.count('s=')
if "z=" in input:
    org_num -= input.count('z=')


print(org_num)