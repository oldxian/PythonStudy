# coding: utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':

    # 连接数据库
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='kisstherain',
        charset = "utf8",
        db='oldxian',
    )
    cur = conn.cursor()
    print "select * from department"
    cur.execute("select * from department;")

f = open('/home/oldxian/Desktop/作业/university/department.txt', 'r')

while True:
    line = f.readline()
    if line:
            # 处理每行\n
        line = line.strip('\n')
        line = line.split(" ")
        print(line)
        line[2] =int(line[2])
        cur.execute("insert into department(dept_mane,building,budget) values('%s','%s',%d)"%(line[0],line[1],line[2]))
    else:
        break
    f.close()
print "select * from student"
cur.execute("select * from student;")

f = open('/home/oldxian/Desktop/作业/university/student.txt', 'r')

while True:
    line = f.readline()
    if line:
            # 处理每行\n
        line = line.strip('\n')
        line = line.split(" ")
        print(line)
        line[0] = int(line[0])
        line[3] = int(line[3])
        cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_mane) values(%d,'%s','%s',%d,'%s','%s')"%(line[0],line[1],line[2],line[3],line[4],line[5]))
    else:
        break
    f.close()
print "select * from exam"
cur.execute("select * from exam;")

f = open('/home/oldxian/Desktop/作业/university/exam.txt', 'r')

while True:
    line = f.readline()
    if line:
            # 处理每行\n
        line = line.strip('\n')
        line = line.split(" ")
        print(line)
        line[0] = int(line[0])
        line[2] = int(line[2])
        cur.execute("insert into exam(student_ID,exam_name,garde) values(%d,'%s',%d)"%(line[0],line[1],line[2]))
    else:
        break
f.close()
cur.close()
conn.commit()
conn.close()