import streamlit as st
from langchain_app import make_chain
from my_keys import open_ai_api_key as OPENAI_API_KEY



st.title("choose the right course for you")
st.subheader("Provide the follwing inputs for the right recommendations!")
input_text1 = st.text_input("What is your name")
input_text2 = st.text_input("What is your experience")

if st.button("generate recommendations."):
  if input_text1 and input_text2:
    result = make_chain(OPENAI_API_KEY, input_text1, input_text2)
    st.write(result)
  else:
    st.write("Please provide both inputs to get recommendations.")





# import streamlit as st
# from langchain_app import make_chain

# st.title("Langchain App!")
# st.write("This is a simple Streamlit app.")

# name = st.text_input("What is your name?:", key="input_text")

# experience = st.text_input("What is your experience in years?", key="input_text2")

# if st.button("Generate Recommendations\n"):
#     st.write(f"Hello, {name}! Your experience is: {experience}")
#     st.write("Here are some recommendations based on your experience:")
#     if name and experience:
#         st.write("- Recommendation 1: Learn more about Streamlit.")
#         st.write("- Recommendation 2: Explore Langchain for building applications.")
#         st.write("- Recommendation 3: Practice coding regularly.")
#         llm, chat_prompt = make_chain(OPENAI_API_KEY, name, experience)