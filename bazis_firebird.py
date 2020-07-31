import fdb as fd

con11 = fd.connect(
    dsn='d:/Baza11.FDB',
    user='sysdba',
    password='masterkey',
    charset='UTF8'
)

con10 = fd.connect(
    dsn='d:/Baza10.FDB',
    user='sysdba',
    password='masterkey',
    charset='UTF8'
)

cur10 = con10.cursor()
cur11 = con11.cursor()

####################################################
####################################################

cur10.execute("delete from GROUP_MATERIAL")
con10.commit()
cur11.execute("select * from GROUP_MATERIAL order by ID_GRM")

for t in cur11:
    print(str(t).replace('None', 'null'))
    cur10.execute("insert into GROUP_MATERIAL values " + str(t).replace('None', 'null'))
con10.commit()

cur10.execute("delete from MEASURE")
con10.commit()
cur11.execute("select * from MEASURE")

for t in cur11:
    print(str(t).replace('None', 'null'))
    cur10.execute("insert into MEASURE values " + str(t).replace('None', 'null'))
con10.commit()

cur10.execute("delete from MATERIAL")
con10.commit()
cur11.execute("select * from MATERIAL")

for t in cur11:
    print(str(t))
    print(str(t).replace('None', 'null'))

    cur10.execute("insert into MATERIAL values " + str(t).replace('None', 'null'))
con10.commit()
