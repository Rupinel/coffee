import pymysql

#Open database connection
db = pymysql.connect(host='coffee.cae2ccwief0j.ap-northeast-2.rds.amazonaws.com', port=3306, user='rupinel', passwd='qwer1234',db='coffee',charset='utf8')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database
CATEGORY_CD = 'RPG'
GAME_CD = 'lineagerk'
GAME_NM = '리니지 레드나이츠'

# make sql
sql = "INSERT INTO GAME_TB(CATEGORY_CD, GAME_CD, GAME_NM) VALUES (%s, %s, %s)" % ("'"+CATEGORY_CD+"'","'"+GAME_CD+"'","'"+GAME_NM+"'")

try :
    # Execute the SQL command
    cursor.execute(sql)

    # Commit 명령으로 DB에 데이터 insert
    db.commit()

    # SELECT 한 내용을 fetchall로 객체에 담아 print
    # cursor.execute("SELECT CATEGORY_CD, GAME_CD, GAME_NM FROM GAME_TB")
    # print(cursor.fetchall())

except Exception as e :
    print(str(e))
    # Rollback in case there is any error
    db.rollback()

# Disconnect from database
db.close()
