import sqlite3
import simplejson as json
import datetime

conn = sqlite3.connect('g:/python/section2/python_practice/files/sqlite3.db' , isolation_level=None)


now = datetime.datetime.now()

# print('now', now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime',nowDatetime)

c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, username text, email text, phone text, website text, regdate text)")
#
# #데이터 삽입
# c.execute("INSERT INTO users VALUES (1 ,'kim','kim@naver.com', '010-0000-0000', 'kim.com', ?)", (nowDatetime,))
# # c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'park', 'park@naver.com', '010-1111-1111', 'park.com', nowDatetime))

# userList = (
#     (3 ,'lee','lee@naver.com', '010-2222-2222', 'lee.com', nowDatetime),
#     (4 ,'cho','cho@naver.com', '010-3333-3333', 'cho.com', nowDatetime),
#     (5 ,'noh','noh@naver.com', '010-4444-4444', 'noh.com', nowDatetime)
# )
# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)


#JSON to Sqlite 삽입2
with open('g:/python/section2/python_practice/files/users.json','r') as infile:
    r = json.load(infile)
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        userData.append(t)
    #c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userData)
    c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", tuple(userData))


# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")
# conn.commit()
print(c.execute("SELECT * from users"))
print(c.fetchmany(size=10))
