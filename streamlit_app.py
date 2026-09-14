import streamlit as st
import numpy as np
import pandas as pd

st.title("😸 All the kitties in the cartoon world ")

q1 = "Guess which cartoon cat charater is my favourite 😻"
q2 = "What attitude do you think this 😺 has?"
q3 = "When did this 🐱 become famous"

list_cat = ["Garfield","Hello Kitty","Puss in Boots", "Cheshire Cat", "Doraemon", "Marie"]

guess = st.selectbox(q1, options=list_cat, index=None)
submitted = st.button("Is that's it?")

if (guess and submitted):
    if guess=="Cheshire Cat":
        st.success("😻")
    else:
        st.error("Meope 😼 Take another pick")


cat_df = pd.DataFrame ({"cat": list_cat,
                    "year_fam": [1987, 1974, 2004, 1865, 1969, 1970],
                    "attitude": ["Sarcastic","Cute", "Adventurous", "Mysterious", "Intelligent", "Spolied"]
                    })

with st.expander("open kitties data"):
    st.dataframe(cat_df)

num_cat = len(cat_df["cat"].unique().tolist())
if "rand_id" not in st.session_state:
    st.session_state.rand_id = np.random.randint(0,num_cat)
rand_id = st.session_state.rand_id
st.write(rand_id)

rand_att = cat_df["attitude"].iloc[rand_id]
q_att = f"which 🐱 is {rand_att}?"
st.write(q_att)
ans_att = st.selectbox("",cat_df["cat"])

if ans_att ==cat_df["cat"].iloc[rand_id]:
    st.success("😻 Gemau")
else:
    st.error("Meope 😼 Take another pick")

rand_year = cat_df["year_fam"].iloc[rand_id]
q_year = f"when did this 🐱 got famous?"
st.write(q_year)
ans_year = st.select_slider("Select the year:", options=sorted(cat_df["year_fam"]))
submit = st.button("Is that it?")

if submit == True:
    if ans_year == rand_year:
        st.success("😻 You're a cartoon kitty expert")
    else:
        st.error("Meope 😼 Take another pick")





