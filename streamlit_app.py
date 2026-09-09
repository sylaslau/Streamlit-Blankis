import streamlit as st
import pandas as pd

st.title("😸 All the kitties in the cartoon world 😸")

st.write("Guess my favourite cartoon cat charater")

import streamlit as st

list_cat = ["Garfield","Hello Kitty","Puss in Boots", "Cheshire Cat", "Doraemon", "Marie"]

cat_df = pd.DataFrame ({"sth": list_cat,
                    "year_fam": [1987, 1974, 2004, 1865, 1969, 1970],
                    "attitude": ["Sarcastic","Cute", "Adventurous", "Mysterious", "Intelligent", "Spolied"]
                    })


with st.expander("open for df"):
    st.dataframe(cat_df)

#q1 = "What attitude style do you think this cat has?"

#q2 = "When did this cat become famous"