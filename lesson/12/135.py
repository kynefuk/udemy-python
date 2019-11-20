import sqlite3

#conn = sqlite3.connect('test_sqlite.db')
# 実行する事にメモリ上にデータベースを作成・削除する
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("MIKE")'
)
conn.commit()

curs.execute(
    'UPDATE persons set name = "MICHAEL" WHERE name = "MIKE"'
)
conn.commit()

curs.execute(
    'DELETE FROM persons WHERE name = "MICHAEL"'
)
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.close()
conn.close()