import openai

prompt = input("Enter A Number from 1-100 based on your current mood ")
def generate_text(prompt):
    openai.api_key = 'sk-(not for public)'
    models = openai.Model.list()
    print(models.data[2].id)
    Chat_Completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": ("I am " + str(prompt) + "on a scale from 1-100 where 100 is very happy and 1 is extremly depressed.")},{"role": "system", "content":("pretend you are a drill seargent")}],
        #messages= [],
        temperature =.1,
        max_tokens=80
    )
    print(Chat_Completion.choices[0].message.content)


    # Extract the generated text from the API response


# Prompt the user for input


generate_text(prompt)
