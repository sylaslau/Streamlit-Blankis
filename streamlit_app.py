import streamlit as st

st.title("🍸 Mix & Shake")

st.write("Guess what is my fav flav profile for cocktails")

import streamlit as st

profile = st.radio(
    "Pick one:",
    ["Fruity", "Floral", "Herbal", "Creamy", "Spicy"]
)
if profile == "Fruity":
    st.success("🍓")
elif profile == "Floral":
    st.error("🌸")
elif profile == "Herbal":
    st.error("🍀")
elif profile == "Spicy":
    st.error("🌶")
elif profile == "Creamy":
    st.error("🍦")


sweet = st.select_slider(
    "On a scale of 1 to 5, how sweet do you like your cocktail?",
    options=[1, 2, 3, 4, 5]
)

strength = st.select_slider(
    "And how boozy do you want it to be?",
    options=[0, 1, 2, 3, 4, 5]
)

if st.button("Let's start with this"):
    st.success("🥂")



#cate = ["a", "b", "c", "d","e"]
#cate_df = pd.DataFrame({
#    "profile": 
#})


