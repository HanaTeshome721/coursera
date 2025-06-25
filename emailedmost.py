name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emaillist=[]
for line in handle:
    
    line.split() 
    print(line)
    findfrom=line.find('From')
    upto=line.find('')
   
    email=line[findfrom+1:upto]
    #print(email)
    emaillist.append(email)
   
emaildic={}
for em in emaillist:
    emaildic['em']=emaildic.get('em',0) + 1
whomost=None
howmany=None
for who,count in emaildic.items():
    if whomost is None or count>howmany:
        whomost=who
        howmany=count
print(whomost,howmany)        
        
    
       
