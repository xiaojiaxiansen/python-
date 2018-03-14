users = []
'''
for user in users:
    if user == 'admin':
        print("Hello admin,would you like to see status report?")
    else:
        print("Hello Eric,thank you for loggin in again.")
'''

if users:
    for user in users:
        print("Hello Eric,thank you for to loggin in again.")
else:
    print("We need to find some users!")
