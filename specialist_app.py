import streamlit as st

def display_specialists():
    # Define a list of specialists with details
    specialists = [
        {"Name": "John Smith", "Gender": "Male", "Age": "25", "Phone Number": "08126259023", "Status": "Available"},
        {"Name": "Cheryl Wilson", "Gender": "Female", "Age": "58", "Phone Number": "08127299093", "Status": "Unavailable"},
        {"Name": "Jackie Chan", "Gender": "Male", "Age": "82", "Phone Number": "08099876530", "Status": "Available"},
        {"Name": "Aderibigbe Samuel", "Gender": "Male", "Age": "53", "Phone Number": "08121819026", "Status": "Unavailable"},
        {"Name": "MaryAnne Gabriella", "Gender": "Female", "Age": "27", "Phone Number": "08145659473", "Status": "Available"}
    ]

    # Display specialists when checkbox is checked
    if st.checkbox("View Available Specialists"):
        st.write("**Available Specialists**")
        
        for idx, specialist in enumerate(specialists):
            if specialist["Status"] == "Available":
                with st.expander(f"Specialist {idx + 1}: {specialist['Name']}"):
                    st.write(f"**Name**: {specialist['Name']}")
                    st.write(f"**Gender**: {specialist['Gender']}")
                    st.write(f"**Age**: {specialist['Age']}")
                    st.write(f"**Phone Number**: {specialist['Phone Number']}")
                    st.write(f"**Status**: {specialist['Status']}")

# Main code to run the Streamlit app
if __name__ == "__main__":
    st.title("Specialist Information")
    
    # Calling the function to display specialists
    display_specialists()
