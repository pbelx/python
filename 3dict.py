users = {
 'john':{
     'first':'jj','second':'didi','loc':'ktb'
 },
 'jane':{
     'first':'kiki','second':'jean','loc':'usa'
 }   
}

for k , v in sorted(users.items()):
    print k
    print v
