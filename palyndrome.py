
wd = " Ma dam    iM    adam "
reswd = "".join(wd.split()).lower()
rs = ""
for w in reversed(reswd):
    rs = rs + w
wd2 = "maDamimadam".lower()
if rs == wd2:
    print(True)
print(rs)