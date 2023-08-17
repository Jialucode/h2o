from flask import Flask,render_template,request
import pymysql
app=Flask(__name__)
import openai
openai.api_key = "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"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    print(message)
    return message



@app.route("/",methods=["GET","POST"])
def add_chat():
    if request.method == "GET":
        #1.连接MySQL 
        # conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats2')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # #2.发送指令
        # sql = "select * from admin"
        conn = pymysql.connect(host="containers-us-west-120.railway.app",port=7216,user='root',passwd="dW5oxfg0GdpkESgIbkDx",charset='utf8',db='railway')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #2.发送指令
        sql = "select * from userchats2"
        cursor.execute(sql)
        datalist = cursor.fetchall()
        print(datalist)
        #3.关闭
        cursor.close()
        conn.close()
        return render_template("index.html",data_list=datalist)

    user_input = request.form.get("input")
    print(user_input)
    user_output = generate_text(user_input)
    # 连接mysql

    # #1.连接MySQL 
    # conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats2')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn = pymysql.connect(host="containers-us-west-120.railway.app",port=7216,user='root',passwd="dW5oxfg0GdpkESgIbkDx",charset='utf8',db='railway')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #2.发送指令
    sql = "insert into userchats2(input,reply) values(%s,%s)"
    #2.发送指令
    # sql = "insert into admin(input,reply) values(%s,%s)"
    cursor.execute(sql,[user_input,user_output])
    conn.commit()
    #3.关闭
    cursor.close()
    conn.close()
    #1.连接MySQL 
    # conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats2')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # #2.发送指令
    # sql = "select * from admin"
    conn = pymysql.connect(host="containers-us-west-120.railway.app",port=7216,user='root',passwd="dW5oxfg0GdpkESgIbkDx",charset='utf8',db='railway')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #2.发送指令
    sql = "select * from userchats2"
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

    # mysql -hcontainers-us-west-120.railway.app -uroot -pdW5oxfg0GdpkESgIbkDx --port 7216 --protocol=TCP railway
    #1.连接MySQL 
    # conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="123456",charset='utf8',db='userchats2')
    conn = pymysql.connect(host="containers-us-west-120.railway.app",port=7216,user='root',passwd="dW5oxfg0GdpkESgIbkDx",charset='utf8',db='railway')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #2.发送指令
    sql = "select * from userchats2"
    # sql = "select * from admin"
    cursor.execute(sql)
    datalist = cursor.fetchall()
    print(datalist)
    #3.关闭
    cursor.close()
    conn.close()
    return render_template("show_chat.html",data_list=datalist)
if __name__ =='__main__':
    app.run()