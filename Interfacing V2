import openai


anger = input("rate your anger from 1-100 ")
happiness =input("rate your happiness from 1-100")
context = "pretend"
if(int(anger)> 50):
    Arating = "very angry"
else:
    Arating ="not Angry"

if(int(happiness) > 50):
    Hrating = "very happy"
else:
    Hrating =" very depressed"
    
def generate_text(Arating,Hrating,context):
    openai.api_key = ''
    models = openai.Model.list()
    print(models.data[2].id)
    Chat_Completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
             {"role": "user", "content": ("I am "+ Arating)},
            {"role": "user", "content": ( "I am" + Hrating )},
            {"role": "system", "content":( context + "you are my friend who is just recieving this information from a friend and thinking of an appropriate response to make them go back to the default of not angry and happy, only if they are not happy or are angry, otherwise just say the word yes. ")}
                  ],
        #messages= [],
        temperature =.5,
        max_tokens=100
    )
    print(Chat_Completion.choices[0].message.content)

response = generate_text(Arating,Hrating,context)
def generate_text(response):
    openai.api_key = ''
    models = openai.Model.list()
    print(models.data[2].id)
    Chat_Completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
             {"role": "user", "content": ( )},
                  ],
        #messages= [],
        temperature =.5,
        max_tokens=100
    )
    print(Chat_Completion.choices[0].message.content)


    # Extract the generated text from the API response


# Prompt the user for input


generate_text(response)



#Goals: Create a more streamlined approach to an inpout and output given index scores
#Make sure the emotional states can vary while still mantaining relevent response
