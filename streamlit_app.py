import streamlit as st

st.title("🎈 My new app")

st.write("Guess my fav direction of flav for cocktails")

import streamlit as st

option = st.selectbox(
    "Choose a flavor profile:",
    ["Smokey", "Fruity", "Floral", "Bitter", "Woody"]
)
if st.button("Submit Guess"):
    if option == "Woody":
        st.success("Bingo!")
    else:
        st.error("Nope")

