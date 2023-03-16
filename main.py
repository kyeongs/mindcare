import streamlit as st
import pymysql

db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
cursor = db.cursor()

name = st.text_input('면담자 이름을 입력하세요', max_chars=10, key='name')

date = st.date_input('면담 날짜')

time = st.time_input('면담 시간')

story = st.text_area('면담 내용')

# mySQL에 데이터 저장
if st.button('저장'):


    query = """insert into tasks (user_name, start_date, start_time, story) values (%s, %s, %s, %s);"""
    param = (name, date, time, story)
    cursor.execute('USE users;')
    cursor.execute(query, param)

    cursor.execute('select * from tasks;')
    result = cursor.fetchall()
    for record in result:
        print(record)

    db.commit()
    db.close()
