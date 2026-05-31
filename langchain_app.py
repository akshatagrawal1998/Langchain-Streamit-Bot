from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

from my_keys import open_ai_api_key as OPENAI_API_KEY

print(OPENAI_API_KEY)

def make_chain(OPENAI_API_KEY, input_text1, input_text2):
    template = (
        "You are a helpful councellor. Given the name: {input_text1} and the experience {input_text2}, recommend the right course for them."
    )
    
    # both below prompt 

    # prompt = ChatPromptTemplate.from_template(template)

    prompt = PromptTemplate(input_variables=["input_text1", "input_text2"], template=template)



    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,openai_api_key=OPENAI_API_KEY)
    chain = prompt | llm | StrOutputParser()
    
    return chain.invoke({
        "input_text1": input_text1,
        "input_text2": input_text2
    })


#print(make_chain(OPENAI_API_KEY, "Akshat", "5"))


# import os

# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# #from langchain_prompts.chat import HumanMessagePromptTemplate, SystemMessagePromptTemplate
# from langchain_core.messages import HumanMessage, AIMessage
# from langchain_openai import ChatOpenAI
# from my_keys import open_ai_api_key as OPENAI_API_KEY

# def make_chain(OPENAI_API_KEY, name, experience):
#     temperature = 0.7
#     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature, openai_api_key=OPENAI_API_KEY)
#     system_template = "You are a helpful assistant that provides recommendations based on the user's experience."
#     human_template = "My name is {name} and I have {experience} years of experience."
    
#     system_message_prompt = AIMessage.from_template(system_template)
#     human_message_prompt = HumanMessage.from_template(human_template)
    
#     chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
#     return llm, chat_prompt


# make_chain(OPENAI_API_KEY, 'Akshat', 5)