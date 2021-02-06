string = '***********\tGreetings from '+str(input())+'\t***********\n'
message = '"The greatest compassion is the prevention of human'
message1 = 'suffering through patience,'
message2 = 'alertness, courage and kindness"'
x = string+message.center(len(string), ' ') + '\n' + message1.center(len(string), ' ') + '\n' + message2.center(len(string), ' ')
print(x)