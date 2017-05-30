# -*- coding: utf-8 -*-

s = 'Tecent Technology Company Limited'
with open('companies.txt', 'a+') as f:
    f.writelines('\n')
    f.writelines(s)
    cNames = f.readlines()
    print(cNames)