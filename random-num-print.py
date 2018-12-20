import time,random,os


print "Enter a word\n"
word=raw_input()
os.system('clear')
print "got it LEt the games begin\n"
wordn = len(word)
reallength = wordn-1
os.system('clear')

while 1:
    g=random.randint(0,reallength)
    out = word[g]
    gg=word.split(out)
    gx= ''.join(gg)
    print gx.upper()
    time.sleep(1)
    os.system('clear')


