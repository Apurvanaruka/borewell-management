from datetime import datetime
from .models import *

def add_data(st):    
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


