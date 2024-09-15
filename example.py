# Example usage
br = BinaryRegister(3)
print("1,None,None")
br.set_bit(0,1)
bre = br.enumerate_states()
for each in bre:
    print(str(each))

print("1,1,None")
br.set_bit(1,1)
bre = br.enumerate_states()
for each in bre:
    print(str(each))

print("None,None,None")
br.set_bit(0,None)
br.set_bit(1,None)
bre = br.enumerate_states()
for each in bre:
    print(str(each))








