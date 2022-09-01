a = '0.56'
total = 0
for c in a:
    if c.isdigit() == False:
       continue
    else:
        total += int(c)

print(total)