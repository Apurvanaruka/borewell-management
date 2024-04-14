from datetime import datetime
from .models import *
import streamlit as st
from .utils import total_time

def add_data():    
    st.subheader('Add Data')
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    date = st.date_input('Enter date')
    col1, col2 = st.columns(2)
    start_hour = col1.slider('Starting Hour',1,12,step=1)
    start_min = col2.slider('Starting Minutes',0,59,step=1)
    col1, col2 = st.columns(2)
    end_hour = col1.slider('Ending Hour',1,12,step=1)
    end_min = col2.slider('Ending Minutes',0,59,step=1)
   # st.subheader(f'Total Time {end_hour-start_hour}:{end_min-start_min} hours')
    st.subheader(total_time(start_hour, start_min, end_hour, end_min))
    start_datetime = datetime.combine(date,datetime.strptime(f"{start_hour}:{start_min}", "%H:%M").time() )
    end_datetime = datetime.combine(date, datetime.strptime(f"{end_hour}:{end_min}", "%H:%M").time())
    if st.button('Add Data'):
        user_id = session.query(User.id).filter(User.full_name == selected_user).first()[0]
        data = UserData(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime)
        session.add(data)
        session.commit()
        st.success('Data added successfully!')


