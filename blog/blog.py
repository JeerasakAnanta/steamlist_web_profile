import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


import seaborn as sns

# Define the data

# Set up the Streamlit app
st.title("Dog Lovers' Blog")
st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate")

# Sections of the blog
menu = ["Home", "Dog Breeds", "Gallery", "Contact"]
choice = st.sidebar.selectbox("Choose a section", menu)

if choice == "Home":
    st.header("Welcome to Dog Lovers' Blog")
    st.write(
        "This blog is all about our furry friends. Explore different breeds, enjoy pictures, and share your love for dogs!"
    )

elif choice == "Dog Breeds":
    st.header("Explore Dog Breeds")
    breeds = {
        "Labrador Retriever": {"Origin": "Canada", "Weight": "25-36 kg"},
        "German Shepherd": {"Origin": "Germany", "Weight": "22-40 kg"},
        "Golden Retriever": {"Origin": "Scotland", "Weight": "25-34 kg"},
    }
    df_breeds = pd.DataFrame(breeds).T
    st.write(df_breeds)

elif choice == "Gallery":
    st.header("Dog Gallery")
    st.image("./image/labradorRetriever.jpg", caption="Labrador Retriever")
    st.image("./image/germanShepherd", caption="German Shepherd")
    st.image("./image/goldenRetriever", caption="Golden Retriever")

elif choice == "Contact":
    st.header("Contact Us")
    st.write("For more information, reach out to us at info@dogloversblog.com")

# Footer
st.sidebar.markdown("Created by a Dog Lover")
