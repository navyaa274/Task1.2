Flag = True
helpline = {'National Emergency Number':112, 'Police':100, 'Ambulance':102,
            'Fire':101, 'Disaster Management Services':108, 'Women Helpline':1091,
            'Women Abuse - Domestic':181, 'Senior Citizen Helpline':14567}

print("HELPLINE", "\t ----> \t CODE")
print()
for x in helpline.keys():
  print(x, end = "\t ----> \t ")
  c = ''
  c += x[0]
  c += x[-1]
  print('(',c.upper(),')')

while Flag:
  req = input("\n \nPlease enter the helpline code from the above list:  ")
  req = req.upper()
  for x in helpline.keys():
    c = ''
    c += x[0]
    c += x[-1]
    c = c.upper()
    if c == req:
      print("\nHelpline number for", x.upper(), "is", helpline[x])
      
  n = input("\nNeed another number? (Y/N): ")
  n = n.upper()
  if n == 'N':
    Flag = False
    print("\nThank you for trusting us! Be safe!")
