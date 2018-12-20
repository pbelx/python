import sys
aa=sys.argv[1]
bb=sys.argv[2]
def talk(a):
    print a

def delete(a):
    print "system is deleting file " + a

if aa=="say":
    talk(bb)
if aa=="del":
    delete(bb)
#talk(aa)

