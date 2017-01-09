# Enter your code here. Read input from STDIN. Print output to STDOUT

test_case = int(raw_input())
input_strings = []
for i in range(0, test_case):
    newest_string = raw_input()
    input_strings.append(newest_string)

odd_strings = []
even_strings = []
for j in range(0, len(input_strings)):
    temp_odd_string = []
    temp_even_string = []
    for k in range(0, len(input_strings[j])):
        if (k % 2 == 0):
            temp_even_string.append(input_strings[j][k])
        else:
            temp_odd_string.append(input_strings[j][k])
            
    odd_strings.append(temp_odd_string)
    even_strings.append(temp_even_string)
    
for l in range(0, len(odd_strings)):
    print ''.join(even_strings[l]), ''.join(odd_strings[l])
            
            
        
    
    

