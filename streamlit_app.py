import streamlit as st

st.title("🍸 Mix & Shake")

st.write("What is your fav flav profile for cocktails")

import streamlit as st

option = st.radio(
    "Pick one:",
    ["Fruity", "Floral", "Herbal", "Creamy", "Spicy"]
)
if option == "Fruity":
    st.success("🍓")
elif option == "Floral":
    st.success("🌸")
elif option == "Herbal":
    st.success("🍀")
elif option == "Spicy":
    st.success("🌶")
elif option == "Creamy":
    st.success("🍦")

if st.button("Let's start with this"):
    st.success("🥂")
