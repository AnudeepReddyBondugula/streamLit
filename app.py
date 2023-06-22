import streamlit as st

st.title("Post Request Receiver")

# List to store received data
received_data = []

# Display received data on the web page
for data in received_data:
    st.write(data)

# Streamlit form to receive new data
new_data = st.text_input("Enter new data:")
if st.button("Submit"):
    received_data.append(new_data)

# Streamlit loop to continuously check for new data via POST requests
while True:
    try:
        request_data = st.experimental_get_query_params()
        if request_data:
            received_data.append(request_data)
    except KeyboardInterrupt:
        break
