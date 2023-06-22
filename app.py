import streamlit as st

st.title("Incoming Data")

# List to store received data
received_data = []

# Display received data on the web page
for data in received_data:
    st.write(data)

# Streamlit form to receive new data
new_data = st.text_input("Enter new data:")
if st.button("Submit"):
    received_data.append(new_data)
