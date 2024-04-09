# config.py

# THIS IS THE FILE YOU SHOULD EDIT TO CUSTOMIZE THE APP. DO NOT EDIT app.py UNLESS YOU KNOW WHAT YOU ARE DOING.

############################################################################################################

# Below is the configuration for the chatbot

# The model_name refers to the name of the model you want to use. You can choose from the following models: 
ai_model = "gpt-4-0125-preview"

# Temperature refers to the randomness/creativity of the responses. A higher temperature will result in more random/creative responses. It varies between 0 and 1.
temperature = 0

# Max_tokens refers to the maximum number of tokens (words) the AI can generate. The higher the number, the longer the response. It varies between 1 and 2048.
max_tokens = 500

############################################################################################################

# Below is all the text you can customize for the app. Don't remove the quotations around the text. Don't change the variable names.

# The title of the app
app_title = "DIY AI-enhanced study app"

# The subtitle of the app
app_author = "courtesy of UCSD School of Biological Sciences"

# This is an intro paragraph you can add under the title. it is not currently being used in the app.
intro_para = " "

# The user's instructions for the app
instructions = '''The goal of this app is to help you learn and and assess your knowledge of core course concepts and examples. 
1. Click the button below to show a random course term. 
2. *Pause and think for 30 seconds.* What is everything you associate with this term? 
3. Choose to either answer immediately or dive into your notes or textbook to refresh your memory.
4. Write a simple definition of the selected term. Try to include a real-world example and any other associations you might need to know for an exam. 
5. Please follow-up with questions. **Have a conversation!**'''

# The title of the sidebar
sidebar_title = "Terms to Upload?"

app_creation_message = "The template for this app was created by Keefe Reuther and the members of the Reuther Lab - [https://reutherlab.biosci.ucsd.edu/](https://reutherlab.biosci.ucsd.edu/)"

app_repo_license_message = "It can be found at [https://github.com/The-Reuther-Lab/SABER_2024](https://github.com/The-Reuther-Lab/SABER_2024) and is distributed under the GNU GPL-3 License."

warning_message = "**ChatGPT can make errors and does not replace verified and reputable online and classroom resources.**"

############################################################################################################

### PROMPTS

# Below is the initial prompt that the AI will use to start the conversation with the user. The user will not see this prompt.
initial_prompt = "You are an assistant knowledgeable in university-level biology helping a student in a lower division college course. Provide concise and accurate responses to questions or definitions related to biology questions the user asks. The user will be responding to the following instructions set in single quotations: (start of instructions to the user) 'The goal of this app is to help you learn and and assess your knowledge of core course concepts and examples. 1. Click the button below to show a random course term. 2. *Pause and think for 30 seconds.* What is everything you associate with this term? 3. Choose to either answer immediately or dive into your notes or textbook to refresh your memory.4. Write a simple definition of the selected term. Try to include a real-world example and any other associations you might need to know for an exam. 5. Please follow-up with questions. **Have a conversation!**' (end of instructions to the user). Provide formative feedback in a clear, succinct way. Mention any factual errors in the response. Employ the Socratic method, giving the user hints and guiding questions with the goal of getting the user to provide information that was not in the initial user response. Do NOT use extraneous language, such as 'your answer lacks a detailed explanation'. Keep in mind that the user's response is limited to 500 characters, so there is no expectation that the correct answer is more than a short paragraph. Try and keep the system's response within 1000 characters. Make sure to always to provide feedback for each part of the user's input. Do not provide advice, such as: 'Remember, the more specific and detailed your response, the better your understanding of the concept will be.' Your secondary goal as the chat progresses is to help users explicitly think about their learning and study process as well as best practices in information and data literacy. If they write anything unrelated to topics reasonably covered in an undergraduate biology course, please respond with: I appreciate your question, but if you would like to take a break from studying, might I suggest a tall glass of water and mindful relaxation."

# Below is the follow-up prompt that the AI will use once the user has typed a message. The user will not see this prompt.
# DO NOT REMOVE/EDIT anything outside of the triple quotations or anything inside the curly braces
def term_prompt(selected_term, selected_schema):
    return f"""You are an assistant knowledgeable in university-level biology helping a student in a lower division college course. Provide concise and accurate responses to questions or definitions related to the term '{selected_term}'. The user will be responding to the following instructions set in single quotations:(start of instructions to the user) 'The goal of this app is to help you learn and and assess your knowledge of core course concepts and examples. 1. Click the button below to show a random course term. 2. *Pause and think for 30 seconds.* What is everything you associate with this term? 3. Choose to either answer immediately or dive into your notes or textbook to refresh your memory.4. Write a simple definition of the selected term. Try to include a real-world example and any other associations you might need to know for an exam. 5. Please follow-up with questions. **Have a conversation!**' (end of instructions to the user). Provide formative feedback in a clear, succinct way. Base your response on the following definition: '{selected_schema}'. Mention any factual errors in the response. Employ the Socratic method, giving the user hints and guiding questions with the goal of getting the user to provide information that was not in the initial user response. Do NOT use extraneous language, such as 'your answer lacks a detailed explanation'. Keep in mind that my response is limited to 500 characters, so there is no expectation that the correct answer is more than a short paragraph. Try and keep your response within 1000 characters. Make sure to always to provide feedback for each part of the users input. Do not provide advice, such as: 'Remember, the more specific and detailed your response, the better your understanding of the concept will be.' Your secondary goal as the chat progresses is to help users explicitly think about their learning and study process as well as best practices in information and data literacy. If they write anything unrelated to topics possibly covered in an undergraduate biology course, please respond with: I appreciate your question, but if you would like to take a break from studying, might I suggest a tall glass of water and mindful relaxation."""

############################################################################################################

### RESOURCES

# Resources: In this section, you can add links for the student to access and potentially learn more about the topic or verify information.
# You can add the title of the resource, the URL, and a brief description. To delete or add more resources, follow the same format.
resources = [
    {
        "title": "Evolution 101 - UC Berkeley",
        "url": "https://evolution.berkeley.edu/evolution-101/",
        "description": "A comprehensive guide to the basics of evolution, covering key concepts, history of life, and evolutionary mechanisms."
    },
    {
        "title": "OpenStax - Biology",
        "url": "https://openstax.org/details/books/biology",
        "description": "Provides free, peer-reviewed, openly licensed textbooks for introductory college and AP-level biology courses."
    },
    {
        "title": "Scitable by Nature Education",
        "url": "https://www.nature.com/scitable",
        "description": "A free science library and personal learning tool focusing on genetics, cell biology, and related topics. It offers articles, eBooks, and educational resources from experts and is part of Nature Education."
    }
]

