import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.number_verify import send_otp,verify_otp

# Database setup
engine = create_engine('sqlite:///user_database.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    mobile_number = Column(String)
    crop_type = Column(String)

class UserData(Base):
    __tablename__ = 'user_data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    start_date = Column(DateTime)
    start_time = Column(DateTime)
    end_date = Column(DateTime)
    end_time = Column(DateTime)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Streamlit UI
def register_user():
    st.subheader('Register User')
    full_name = st.text_input('Full Name')
    mobile_number = st.text_input('Mobile Number')
    generated_otp=0000
    if st.button('Send OTP'):
        generated_otp=send_otp(mobile_number)
    entered_otp=st.text_input('Enter your OTP')
    if st.button('Verify OTP'):
        verify_otp(int(entered_otp),generated_otp)
    crop_type = st.selectbox('Crop Type', ['Wheat', 'Rice', 'Corn'])
    if st.button('Register user') and verify_otp(int(entered_otp),generated_otp):
        user = User(full_name=full_name, mobile_number=mobile_number, crop_type=crop_type)
        session.add(user)
        session.commit()
        st.success('User registered successfully!')
    else:
        st.warning('Invalid OTP!')

def add_data():
    st.subheader('Add Data')
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    today_date = datetime.today().date()
    start_date = st.date_input('Starting Date', value=today_date)
    start_time = st.time_input('Starting Time', value=datetime.now().time())
    end_date = st.date_input('Ending Date', value=today_date)
    end_time = st.time_input('Ending Time', value=datetime.now().time())
    start_datetime = datetime.combine(today_date, start_time)
    end_datetime = datetime.combine(today_date, end_time)
    if st.button('Add Data'):
        user_id = session.query(User.id).filter(User.full_name == selected_user).first()[0]
        data = UserData(user_id=user_id, start_date=start_date, start_time=start_datetime,end_date=end_date, end_time=end_datetime)
        session.add(data)
        session.commit()
        st.success('Data added successfully!')

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
        user_data = session.query(UserData).filter(UserData.user_id == user.id).first()

        if user_data:
            st.write(f'Start Date: {user_data.start_date} End Date: {user_data.end_date}')
            st.write(f'Start time: {user_data.start_time} End Time: {user_data.end_time}')
        else:
            st.warning('User Data not found.')
    else:
        st.warning("User not found.")

# Main UI
def main():
    st.title('User Registration and Data Addition')
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Register User', 'Add Data','Show user Data'])
    
    if page == 'Register User':
        register_user()
    elif page == 'Add Data':
        add_data()
    elif page == 'Show user Data':
        show_user_data()
if __name__ == '__main__':
    main()

