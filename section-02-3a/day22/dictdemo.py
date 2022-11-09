# Create a raw dictionary
# in code, usually add from data instead
onecard = {'dmusicant': 4.32, 'abyerly': 0.67, 'wshakesp': 14.00}





print(onecard['dmusicant'])
print(onecard['wshakesp'])
onecard['jondich'] = 99
print(onecard['jondich'])
onecard[23.4] = 100   # really bad style
print(onecard[23.4]) # again terrible
#onecard[ [1,2,3,4,5] ] = 98     error
onecard[('ryan', 'son')] = 1000
