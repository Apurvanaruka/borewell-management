from src.models import *
import streamlit as st 


def show_user_data(st):
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    user = session.query(User).filter(User.full_name == selected_user).first()
    if user:
        st.subheader('User Details')
        st.write(f'Full Name: {user.full_name}')
        st.write(f'Mobile Number: {user.mobile_number}')
        st.write(f'Crop Type: {user.crop_type}')
        user_data = session.query(UserData).filter(UserData.user_id == user.id).first()

        if user_data:
            st.write(f'Start Date: {user_data.start_date} End Date: {user_data.end_date}')
            st.write(f'Start time: {user_data.start_time} End Time: {user_data.end_time}')
        else:
            st.warning('User Data not found.')
    else:
        st.warning("User not found.")


