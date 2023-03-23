from collections import defaultdict
dd=defaultdict(float)
income=[('books',1250.00),
        ('books',1300.00),
        ('books',1420.00),
        ('tutorials',560.00),
        ('tutorials',630.00),
        ('tutorials',750.00),
        ('courses',2500.00),
        ('courses',2430.00),
        ('courses',2750.00)]
# for key,values in income.items():
# if type(values) == tuple:
#     for value in values:
#         print(value)
for d,s in income:
    dd[d] += s
print(dd)
