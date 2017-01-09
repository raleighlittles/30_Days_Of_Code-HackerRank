# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

phonebook = {}
for i in range(0, n):
    user_input = raw_input()
    user_input = user_input.split(" ")
    
    name = user_input[0] 
    number = user_input[1]
    
    phonebook[name] = number
    
# Once input is read in, perform checks
query = raw_input()
while (query != ""):
    if (phonebook.has_key(query) == False):
        print "Not found"
    else:
        print query + "=" + phonebook[query]
        
    try: 
        query = raw_input()
    except:
        break
        

    
    
    
    
    