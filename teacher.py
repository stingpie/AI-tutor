import anthropic
#import streamlit as st
#import speech_recognition as sr
#import st_utils

#st.title('Teacher')



try:
    client = anthropic.Anthropic()
except:
    client = anthropic.Anthropic(api_key=input("Please type out your anthropic API key."))




## thx:https://pythonexamples.org/python-get-list-of-all-files-in-directory-and-sub-directories/
import os

def list_files_recursive(path='.'):
    filelist=[]
    for root, dirs, files in os.walk(path):
	    for file in files:
            #append the file name to the list
    		filelist.append(os.path.join(root,file))
    return filelist

def lesson():
    #print(st.query_params)
    #params = st.query_params
    #print(params)
    #lesson = params['lesson']
#    examples = st.query_params.examples

    #use_tts = st.checkbox("Would you like the website read aloud?")
    #use_stt = st.checkbox("Would you like to speak instead of write?")
    use_tts=False
    use_stt=False

    #lesson = st_utils.read_input("What would you like to lean today? Please give me a single word topic.", value="place", use_stt = use_stt)
    lesson = input("What would you like to learn about today? please type a one word topic.")
    history=[{"role": "user", "content": "I'd like to learn about "+lesson}]

    

    examples=""
    for file in list_files_recursive("."):
        if(lesson in file):
            examples += "\n```\n"+open(file,'r').read()+"\n```\n"
    if len(examples)==0:
        examples += "\n```\n"+open("lessons/math/one_ten_hundred_place.txt",'r').read()+"\n```\n"


    i=0 
    while(1):
        i+=1
        #with st.spinner('Generating response...'):
        message = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1024,
                system = open("prompt.txt",'r').read() + "For example, these are some lessons you've done in the past: "+examples,
                messages=history
            )
        if("Student:" in message.content[0].text or "student:" in message.content[0].text):
            
            message.content[0].text = message.content[0].text[:message.content[0].text.lower().find("student:")]
        if "\n" in message.content[0].text:
            message.content[0].text = (message.content[0].text.split("\n"))[0]


        history += [{"role":"assistant","content":("Teacher: "if(not message.content[0].text.lower().startswith("teacher:"))else "") +message.content[0].text}]
    
        #st_utils.output_text(message.content[0].text, use_tts = use_tts)
        print(message.content[0].text)
        #new_response = st_utils.read_input("Your response",key=23*i+123131244, use_stt=use_stt)
        new_response = "Student: " + input()
        history += [{"role":"user","content":new_response}]




if __name__=="__main__":
    lesson()
