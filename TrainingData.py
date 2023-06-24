import openai
import os
import json


# Amood ="furious"
     #  Amood="irked"
   #     Amood="calm"
#       Hmood ="ecstatic"
   #     Hmood="deppresed"
   #     Hmood="content"
   #     AXmood="extremly nervous"
     #   AXmood="nervous"
   #     AXmood="not nervous"
  #  mood ="I feel " + " and ".join([Amood,Hmood,AXmood]) 
   # return {"role": "user","content": mood}

Training=[("I feel irked and ecstatic and extremely nervous, give me an appropriate greeting referencing my mood", "You seem to have some conflicting emotions today, how are you?"),
          ("I feel irked and depressed and extremely nervous , give me an appropriate greeting referencing my mood","You seem to be having a bad day, its important to understand one bad day is only one day"),
          ("I feel irked and content and extremly nervous , give me an appropriate greeting referencing my mood","You seem to have some conflicting emotions, how are you?"),
          ("I feel furious and nervous, give me an appropriate greeting referencing my mood","You seem to be having a rough day why is that?"),
          ("I feel not nervous and calm and content, give me an appropriate greeting referencing my mood","You seem to be having a good day could you tell me more?"),
          ("I feel calm depressed and not nervous, give me an appropriate greeting referencing my mood","You seem depressed, its important to take care of your mental health"),
          ]
outitems=[]
for item in Training:
    out=repr({"prompt":item[0],"response":item[1]})
    outitems.append(out)
outstring="\n".join(outitems)
outstring=outstring.replace("'",'"')
f =open("C:/Users/ccace/VSAI/FineT3","w+")
f.write(outstring)
f.close()
#openai--api-key "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" api fine_tunes.create -t "C:/Users/ccace/VSAI/FineT3_prepared.jsonl" -m "davinci" 
openai.api_key = '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'






