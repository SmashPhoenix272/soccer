import sys,re
from collections import defaultdict

def process_results(lines):
    t=defaultdict(int)
    for l in filter(str.strip,lines):
        m=re.match(r'^([\w\s]+) (\d+), ([\w\s]+) (\d+)$',l.strip())
        if m:
            a,b,c,d=m.groups()
            p=lambda x,y:(3,0)if x>y else(0,3)if x<y else(1,1)
            t[a.strip()]+=p(int(b),int(d))[0]
            t[c.strip()]+=p(int(b),int(d))[1]
    return sorted(t.items(),key=lambda x:(-x[1],x[0]))

def main(input_lines=None):
    if input_lines is None:
        input_lines = sys.stdin.readlines() if len(sys.argv)==1 else open(sys.argv[1]).readlines()
    r=process_results(input_lines)
    rank=1
    prev_points=None
    for i,(t,p) in enumerate(r):
        if prev_points!=p:
            rank=i+1
        print(f"{rank}. {t}, {p} {'pt' if p==1 else 'pts'}")
        prev_points=p

if __name__=="__main__":main()