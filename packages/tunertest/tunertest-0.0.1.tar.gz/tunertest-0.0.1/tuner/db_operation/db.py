import pugsql
testdata = pugsql.module('testdata/')
testdata.connect('mysql+pymysql://root:Aa112233!@116.63.68.174:3306/autho')
r = testdata.test()
print(r)