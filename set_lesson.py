set_1 = set()
set_1.add("hello")
set_1.update([2,4,5,"out of sight, out of mind"])
set_1.remove(2)
set_2 = set_1.copy
print(set_2 is set_1)

print(set_1)
a = (4,6)
print(a[1])