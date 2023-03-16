import streamlit as st
import pymysql
from openpyxl import load_workbook

wb = load_workbook('mindcare.xlsx')
ws = wb.active

db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
cursor = db.cursor()

name = st.text_input('면담자 이름을 입력하세요', max_chars=10, key='name')

date = st.date_input('면담 날짜')

time = st.time_input('면담 시간')

story = st.text_area('면담 내용')

#버튼 클릭 시 엑셀 파일에 저장
if st.button('저장'):
    ws.title = 'mindcare'
    ws.append([name, date, time, story])
    wb.save('mindcare.xlsx')