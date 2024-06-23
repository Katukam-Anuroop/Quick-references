import google.generativeai as genai



def send_prompt(prompt):
    genai.configure(api_key='')
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(prompt)
    return response.text

# https://www.gemini.com/user_authentication/api_key=''?
# 500, 200,405
#
# https://www.gemini.com/give_a_prompt/Model/prompt?
# list_of_prompts = ["Write a poem about a cat chasing a butterfly.",
#                    "capital of india",
#                    "how are you doing today."]
#
# # check_prompt_1 = send_prompt("Write a poem about a cat chasing a butterfly.")
# # print(check_prompt_1)
#
# for prompt in list_of_prompts:
#     prompt_output = send_prompt(prompt)
#     print(prompt_output)









# import genai
#
# # Replace with your own API key
# API_KEY = "AIzaSyBWzyoRsIyJm6_GuCo9PzzeEO7IzTTtz0g"
#
# # Configure API client
# genai.configure(api_key=API_KEY)
#
# # Define your prompt or instructions
# prompt = "Write a poem about a cat chasing a butterfly."
#
# # Send request to Gemini API (text-only prompt)
# response = genai.text.generate(prompt=prompt)
#
# # Access and print the generated text
# generated_text = response.text
# print(generated_text)

# from google.generativeai import models, Auth
#
# # Set your API key (replace with your actual key)
# API_KEY = "AIzaSyBWzyoRsIyJm6_GuCo9PzzeEO7IzTTtz0g"
#
# # Authenticate with the API key
# credentials = Auth.from_api_key(API_KEY)
#
# # Create a generative models client
# client_options = {"api_endpoint": "https://generativelanguage.googleapis.com"}
# client = models.GenerativeModelsClient(credentials=credentials, client_options=client_options)
#
# # Define your prompt or instructions
# prompt = "Write a poem about a cat chasing a butterfly."
#
# # Send request to Gemini API (text-only prompt)
# response = client.generate_content(prompt=prompt)
#
# # Access and print the generated text
# generated_text = response.text
# print(generated_text)


# Import necessary libraries
# from google.generativeai import models
#
# # Set the environment variable for application default credentials (optional)
# # export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
#
# # Create a generative models client
# client = models.GenerativeModelsClient()
#
# # Define your prompt or instructions
# prompt = "Write a poem about a cat chasing a butterfly."
#
# # Send request to Gemini API (text-only prompt)
# response = client.generate_content(prompt=prompt)
#
# # Access and print the generated text
# generated_text = response.text
# print(generated_text)
# #
# cl = "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"
#
# import os
# import anthropic
#
# client = anthropic.Anthropic(
#     api_key=cl,
# )
#
# from IPython.display import Markdown, display
# from anthropic import HUMAN_PROMPT, AI_PROMPT
#
# completion = client.completions.create(
#     model="claude-3-opus-20240229",
#     max_tokens_to_sample=300,
#     prompt=f"{HUMAN_PROMPT} What is Matthew effect? {AI_PROMPT}",
# )
# Markdown(completion.completion)