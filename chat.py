import streamlit as st
from huggingface_hub import InferenceClient



# Set up the Hugging Face API token
api_key = 'INSERT_API_KEY'
model_name = 'mistralai/Mistral-7B-Instruct-v0.3'

client = InferenceClient(model=model_name, token=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")

if prompt is not None and prompt.strip() == "":
    st.warning("Vous ne pouvez pas envoyer un message vide. Veuillez entrer un texte.")
else:
    if prompt:
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        st.session_state.messages.append({"role": "user", "content": prompt})

        
        prompt_input = f"""
        <s>[INST]
        You are an AI assistant from Gnomon Digital, specialized in optimizing decision-making via AI-based solutions. 
        Always respond in the same language as the user's input, whether it's English, French, or any other language. 
        Your responses should be brief (1-2 sentences) and highly deterministic. Provide clear and concise answers without unnecessary details.
        Here is the prompt: {prompt}
        [/INST]
        """

        result = client.text_generation(
            prompt=prompt_input,
            max_new_tokens=64,  
            temperature=0.2,  # Lower temperature for more deterministic output
            top_p=0.9,  
            top_k=40    
        )

        assistant_response = result  

        
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
