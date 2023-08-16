from flask import Flask,render_template,request
import pymysql
from openai_test import generate_text
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def add_chat():
    if request.method == "GET":
        #1.连接MySQL 
        conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #2.发送指令
        sql = "select * from admin"
        cursor.execute(sql)
        datalist = cursor.fetchall()
        print(datalist)
        #3.关闭
        cursor.close()
        conn.close()
        return render_template("index.html",data_list=datalist)

    user_input = request.form.get("input")
    user_output = generate_text(user_input)
    print(user_input)
    # 连接mysql

    #1.连接MySQL 
    conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #2.发送指令
    sql = "insert into admin(input,reply) values(%s,%s)"
    cursor.execute(sql,[user_input,user_output])
    conn.commit()
    #3.关闭
    cursor.close()
    conn.close()
    #1.连接MySQL 
    conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #2.发送指令
    sql = "select * from admin"
    cursor.execute(sql)
    datalist = cursor.fetchall()
    print(datalist)
    #3.关闭
    cursor.close()
    conn.close()
    # 执行sql

    # 关闭连接

    return render_template("index.html",data_list=datalist)

@app.route("/show/chat/",methods=["GET","POST"])
def show_caht():

    
    #1.连接MySQL 
    conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #2.发送指令
    sql = "select * from admin"
    cursor.execute(sql)
    datalist = cursor.fetchall()
    print(datalist)
    #3.关闭
    cursor.close()
    conn.close()
    return render_template("show_chat.html",data_list=datalist)
if __name__ =='__main__':
    app.run()