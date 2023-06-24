import openai
print("all questions asking mood should be inputed as a score 1-100")

what1 =input("what is the system's relationship to you? (short 1-3 words)")
Arating =input("how angry?")
Hrating =input("how happy?")
Anxrating =input("how anxious?")

def generate_text(messages, temperature =0, max_tokens=100):
    openai.api_key = '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'
    models = openai.Model.list()
    print("gpt-3.5-turbo")
    Chat_Completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=  messages,
        temperature = temperature,
        max_tokens= max_tokens
    )
    print("messages=",messages)
    print("response = ", Chat_Completion.choices[0].message.content)
    return str(Chat_Completion.choices[0].message.content)
 

def generate_context(what):
   return {"role": "system","content": "pretend you are my" + what +" and give an appropriate informal greeting referencing my mood"}
   
def generatemood(anger, happy,anx):
    if (anger>66):
       Amood ="furious"
    if(66>anger>33):
       Amood="irked"
    if(anger<33):
        Amood="calm"
    if(happy>66):
        Hmood ="ecstatic"
    if(happy<33):
        Hmood="deppresed"
    if(33<happy<66):
        Hmood="content"
    if(anx>66):
        AXmood="extremly nervous"
    if(33<anx<66):
        AXmood="nervous"
    if(anx<33):
        AXmood="not nervous"
    mood ="I feel " + " and ".join([Amood,Hmood,AXmood]) 
    return {"role": "user","content": mood}

def complexityScore(anger,happy,anxiety):
   comp=2
   if(anger<30):
        comp+=0
   
   if(30<anger<66):
         comp +=1
         comp +=1
      
   if(anger>66):
       comp +=1
   if(happy>66):
       comp+=0
   
   if(33<happy<66):
         comp+=1
         comp+=1
     
   if(happy<33):
            comp+=1
   if(anxiety<33):
      comp+=0
   if(66>anxiety>33):
         comp+=1
         comp+=1
   if(anxiety>66):
       comp+=1
   
   return int(comp)*25
   


def generate_response(anger,happy,anxiety,what):
   random =complexityScore(int(anger),int(happy),int(anxiety)) *(0.01)
   print(random)
   print("complexity score = "+str((complexityScore(int(anger),int(happy),int(anxiety)))/25))
   rmessage= [generatemood(int(anger),int(happy),int(anxiety)),generate_context(what)]
   generate_text(rmessage,temperature =random, max_tokens=complexityScore(int(anger),int(happy),int(anxiety)))
    
generate_response(Arating,Hrating,Anxrating,what1,)




