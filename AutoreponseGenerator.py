import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")
st.header("Auto response generator for any reviews")
reviews = st.text_area("Copy and Paste any review")
button = st.button("Autogenrate Response")


def generate_auto_reponse(reviews):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Auto Response Generator \n\n Review: {reviews} \n\n Reply: ",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text

if reviews and button:
  with st.spinner(".......Generating Autoresponse to your review........"):
    reply = generate_auto_reponse(reviews)
    st.write(reply)
