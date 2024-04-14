import streamlit as st
from datetime import datetime
from src.number_verify import send_otp,verify_otp
from src.add_user_data import *
from src.show_user_data import *
from src.register_user import *


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

