def astar(startnode,stopnode):
    os=set(startnode)
    cs=set()
    g={}
    parents={}
    g[startnode]=0
    parents[startnode]=startnode
    while len(os)>0:
        n=None
        for v in os:
            if n==None or g[v]+heu[v]<g[n]+heu[n]:
                n=v
        if n==stopnode or Graphnode[n]==None:
            pass
        else:
            for (m,wei) in get_nei(n):
                if m not in os and m not in cs:
                    os.add(m)
                    parents[m]=n
                    g[m]=g[n]+wei
                else:
                    if g[m]>g[n]+wei:
                        g[m]=g[n]+wei
                        parents[m]=n
                        if m in cs:
                            cs.remove(m)
                            os.add(m)
        if n==None:
            print("path not found")
            return None
        if n==stopnode:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(startnode)
            path.reverse()
            print("path found:{}".format(path))
            return path
        os.remove(m)
        cs.add(m)
    print("Path not exists")
    return None
def get_nei(v):
    if v in Graphnode[v]:
        return Graphnode[v]
    else:
        return None
def heu(n):
    h_dist={
        'A':11,
        'B':6,
        'C':99,
        'D':1,
        'E':0,
        'G':7
    }
    return h_dist[n]
Graphnode={
    'A':[('B',2),('C',3)],
    'B':[('C',1),('G',9)],
    'C':None,
    'E':[('D',6)],
    'D':[('G',1)]
}
astar('A','G')
