raw = """
0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0 1
1 1 1 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 1 0 1
1 1 1 0 0 1 0 1 0 0 1 1 1 1 0 1 1 1 0 1 0
1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0 0 1 0 0
1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 1 0
1 1 1 1 0 0 1 0 1 1 0 1 1 1 1 0 1 1 1 0 1
0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0 0 1 1
0 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 1
0 1 1 1 1 0 0 1 0 1 0 0 1 1 1 1 0 1 1 1 0
1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0 0 1
0 0 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0
1 0 1 1 1 1 0 0 1 0 1 0 0 1 1 1 1 0 1 1 1
0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0 0
1 1 0 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 0 0 1
0 1 0 1 1 1 1 0 0 1 0 1 1 0 1 1 1 1 0 1 1
1 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0
0 1 0 0 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 0 0
1 0 1 0 1 1 1 1 0 0 1 0 1 1 0 1 1 1 1 0 1
1 1 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0
0 0 1 0 0 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 0
0 1 0 1 0 1 1 1 1 0 0 1 0 1 0 0 1 1 1 1 0
1 1 1 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1
0 0 0 1 0 0 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1
"""
lines = raw.replace(' ','').strip('\n').split('\n')
string = ''.join(lines)