import requests
import streamlit as st

def get_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()['content']
    else:
        return "Failed to retrieve quote."

st.title("InspireQuote Generator")
if st.button('Generate Quote'):
    quote = get_random_quote()
    st.write(quote)
