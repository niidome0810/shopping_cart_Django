# INSERT文を実行しよう
import sqlite3
sqlite_path = 'db/sql_training.sqlite'
connection = sqlite3.connect(sqlite_path)
cursor = connection.cursor()

try:
    # セットアップ
    cursor.execute("DROP TABLE IF EXISTS sample")
    cursor.execute("CREATE TABLE IF NOT EXISTS sample (id INTEGER PRIMARY KEY, name TEXT)")

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

# 動作確認
cursor.execute('SELECT * FROM sample')
print(cursor.fetchall())

connection.close()
