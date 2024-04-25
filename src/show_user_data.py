from src.models import *
from src.utils import *
import streamlit as st 
import pandas as pd

def show_user_data():
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    user = session.query(User).filter(User.full_name == selected_user).first()
    if user:
        st.write('User Details')
        col1, col2 = st.columns(2)
        col1.subheader(f'{user.full_name}')
        col1.write(f'Mobile Number: {user.mobile_number}')
        col2.selectbox('Crop Type',[user.crop_type])
        user_data = session.query(UserData).filter(UserData.user_id == user.id).all()
        date = []
        start_time = []
        end_time = []
        for data in user_data:
            date.append(data.start_datetime.strftime("%d:%m:%Y"))
            start_time.append(data.start_datetime.strftime("%H:%M"))
            end_time.append(data.end_datetime.strftime("%H:%M"))

        date_options = []
        date_options += set(date)
        date_options.sort()
        date_options.insert(0,'All')
        selected_date = st.selectbox('Select a date',date_options)
        df = pd.DataFrame({'Date':[], 'StartTime':[],'EndTime':[],'hours':[]})
        for i in range(len(date)):
            if selected_date == 'All':
                df = df._append({'Date':date[i], 'StartTime':start_time[i],'EndTime':end_time[i],'hours':get_hour(start_time[i],end_time[i])},ignore_index=True)
            elif date[i] == selected_date:
                df = df._append({'Date':date[i], 'StartTime':start_time[i],'EndTime':end_time[i],'hours':get_hour(start_time[i],end_time[i])},ignore_index=True)
        st.write(df)
        st.write(total_hour(df.hours))
    else:
        st.warning("User not found.")


