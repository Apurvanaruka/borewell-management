from src.models import *
from src.number_verify import * 
import streamlit as st

def register_user():
    st.subheader('Register User')
    full_name = st.text_input('Full Name')
    mobile_number = st.text_input('Mobile Number')[-10:]
    generated_otp=0000
    if st.button('Send OTP'):
        generated_otp=send_otp('+91'+mobile_number)
    entered_otp=st.text_input('Enter your OTP')
    crop_type = st.selectbox('Crop Type', ['Wheat', 'Rice', 'Corn'])
    if st.button('Register user'):
        if not verify_otp(int(entered_otp),generated_otp): 
            user = User(full_name=full_name, mobile_number=mobile_number, crop_type=crop_type)
            session.add(user)
            session.commit()
            st.success('User registered successfully!')
        else:
            st.warning('Invalid OTP!')


