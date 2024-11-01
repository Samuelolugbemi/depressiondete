from secrets import choice
from charset_normalizer import detect
from numpy import result_type
import streamlit as st
import joblib
from stream import detect


import sqlite3
file_name = "finalized_model.sav"
loaded_model = joblib.load(file_name)
conn = sqlite3.connect("data.db")
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username= ? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data



def main():
    st.title("Depression Detection System")

    menu = ["Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)
    

    if choice == "Login":
        st.subheader("Home")

        st.info("Kindly login or signup if you don't have an account")

        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type= "password")
        if st.sidebar.checkbox("Log In"):
            create_usertable()
            result = login_user(username, password)
            if result:
                st.success("Logged In as {}".format(username))
                detect.main()
                
                
            else:
                st.error("User not found or Incorrect Password")
                
              
                

         
    
    elif choice == "SignUp":
        st.subheader("Sign Up")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup") :
            create_usertable()
            add_userdata(new_user, new_password)
            st.success("You now have an account, Proceed to log in")



if __name__ == '__main__':
    main()