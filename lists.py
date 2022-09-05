""" hacker rank- lists  """
if __name__ == '__main__':
    N = int(input())
    #n = input()
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)
