from src.models import *
import streamlit as st 
import pandas as pd

def show_user_data():
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    user = session.query(User).filter(User.full_name == selected_user).first()
    if user:
        st.subheader('User Details')
        st.write(f'Full Name: {user.full_name}')
        st.write(f'Mobile Number: {user.mobile_number}')
        st.write(f'Crop Type: {user.crop_type}')
        user_data = session.query(UserData).filter(UserData.user_id == user.id).all()
        date = []
        start_time = []
        end_time = []
        for data in user_data:
            date.append(data.start_datetime.strftime("%d:%m:%Y"))
            start_time.append(data.start_datetime.strftime("%H:%M:%S"))
            end_time.append(data.end_datetime.strftime("%H:%M:%S"))
        df = pd.DataFrame({'Date':date, 'StartTime':start_time,'EndTime':end_time})
        st.write(df)
    else:
        st.warning("User not found.")


