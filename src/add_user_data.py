from datetime import datetime
from .models import *
import streamlit as st
from .utils import total_time


def add_new_entry():
    st.subheader('Add new Entry')
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    date = st.date_input('Enter date')

    #start time
    st.write('Start Time')
    col1, col2 = st.columns(2)
    start_hour = col1.slider('Starting Hour',1,12,step=1)
    start_min = col2.slider('Starting Minutes',0,59,step=1)

    #end Time
    col1, col2 = st.columns(2)
    col1.write('End Time')
    is_stop_time = col2.checkbox('To be Continue')
    end_datetime = None
    if not is_stop_time: 
        end_hour = col1.slider('Ending Hour',1,12,step=1)
        end_min = col2.slider('Ending Minutes',0,59,step=1)
        st.subheader(total_time(start_hour, start_min, end_hour, end_min))
        end_datetime = datetime.combine(date, datetime.strptime(f"{end_hour}:{end_min}", "%H:%M").time())
    start_datetime = datetime.combine(date,datetime.strptime(f"{start_hour}:{start_min}", "%H:%M").time() )
    if st.button('Add Data'):
        user_id = session.query(User.id).filter(User.full_name == selected_user).first()[0]
        data = UserData(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime)
        session.add(data)
        session.commit()
        st.success('Data added successfully!')





def update_entry():
    st.subheader('Update Entry')
    users = session.query(User).all()
    user_options = [user.full_name for user in users]
    selected_user = st.selectbox('Select User', user_options)
    # get date from previous record
    user = session.query(User).filter(User.full_name == selected_user).first()
    user_data = session.query(UserData).filter(UserData.user_id == user.id, UserData.end_datetime == None).all()
    selected_datetime = st.selectbox('Enter Date',[ data.start_datetime for data in user_data ])
    #start time
    if selected_datetime:        
        st.write('Start Time')
        col1, col2 = st.columns(2)
        start_hour = col1.slider('Starting Hour',1,12,step=1,value=int(selected_datetime.strftime("%H")),disabled=True)
        start_min = col2.slider('Starting Minutes',0,59,step=1,value=int(selected_datetime.strftime("%M")),disabled=True)

        #end Time
        st.write('End Time')
        col1,col2 = st.columns(2)
        end_hour = col1.slider('Ending Hour',1,12,step=1)
        end_min = col2.slider('Ending Minutes',0,59,step=1)
        st.subheader(total_time(start_hour, start_min, end_hour, end_min))
        end_datetime = datetime.combine(datetime.strptime(selected_datetime.strftime("%d:%m:%Y"),"%d:%m:%Y"), datetime.strptime(f"{end_hour}:{end_min}", "%H:%M").time())
        start_datetime = datetime.combine(datetime.strptime(selected_datetime.strftime("%d:%m:%Y"),"%d:%m:%Y"),datetime.strptime(f"{start_hour}:{start_min}", "%H:%M").time() )
        if st.button('Update Data'):
            id = session.query(UserData.id).filter(UserData.start_datetime == selected_datetime).first()[0]
            user_datetime = session.query(UserData).filter_by(id=id).first()
            user_datetime.end_datetime = end_datetime 
            session.commit()
            st.success('Data updated successfully!')
    else:
        st.header("All records upto date.")

    
    


def add_data():    
    entry_type = st.radio('Select one',['Add New Entry', 'update entry'],horizontal=True)
    if entry_type == 'Add New Entry':
        add_new_entry()
    elif entry_type == 'update entry':
        update_entry()
