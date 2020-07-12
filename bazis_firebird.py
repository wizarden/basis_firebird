import fdb as fd

con11 = fd.connect(
    dsn='d:/my11.FDB',
    user='sysdba',
    password='masterkey',
    charset='UTF8'
)

con10 = fd.connect(
    dsn='d:/my10.FDB',
    user='sysdba',
    password='masterkey',
    charset='UTF8'
)

cur10 = con10.cursor()
cur11 = con11.cursor()

cur10.execute("delete from GROUP_MATERIAL")
con10.commit()
cur11.execute("select * from GROUP_MATERIAL order by ID_GRM")

for t in cur11:
    print(str(t).replace('None', 'null'))
    cur10.execute("insert into GROUP_MATERIAL values " + str(t).replace('None', 'null'))

#cur10.execute("insert into GROUP_MATERIAL values (1, 'Направляющие', 1, 4, '') ")
#cur10.execute("insert into GROUP_MATERIAL values (1, 'База материалов', null, 1, '') ")


con10.commit()
