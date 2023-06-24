import openai
import time
openai.api_key = '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'



with open("C:/Users/ccace/VSAI/T3Edited_prepared (1).jsonl") as f:
  response1 = openai.File.create(file=f, purpose='fine-tune')
  print(response1)
fileid = response1["id"]
print("fileid =" ,fileid)

  
create_args = {
  
	"training_file": fileid,
	"validation_file": "",
	"model": "davinci",
	"n_epochs": 15,
	"batch_size": 3,
	"learning_rate_multiplier": 0.3
}

#response = openai.FineTune.create(training_file="<response_file_id>", model='babbage')

response2 = openai.FineTune.create(training_file=fileid, model ="davinci", batch_size=6, n_epochs =12,)
print(response2)
id =response2["id"]
status =None
while status != "completed":
  time.sleep(5)
  response3 = openai.FineTune.retrieve(id=id)
  status =response3["status"]
  print(".")
print(response3 , status )




#response = openai.FineTune.create( training_file="C:/Users/ccace/VSAI/FineT3_prepared.jsonl", model='davinci')
#openai tools fine_tunes.prepare_data -f "C:/Users/ccace/VSAI/FineT3.txt"







#delete :openai --api-key "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" api models.delete -i <FINE_TUNED_MODEL>
#call list:openai api fine_tunes.list
#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
#openai --api-key "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" api fine_tunes.list 


#davinci:ft-personal-2023-06-05-21-12-15 DOESNT EXIST? (could have been already deleted)
#davinci:ft-personal-2023-06-06-19-49-44 DELETED!
#davinci:ft-personal:use1-2023-06-06-19-59-38 DELETED!
#curie:ft-personal-2023-06-06-20-28-19 DELETED!
#curie:ft-personal-2023-06-06-20-41-56 DELETED!
#davinci:ft-personal-2023-06-06-20-35-22 DELETED!
#davinci:ft-personal:c1-2023-06-06-20-46-08 DELETED!
#curie:ft-personal:c1-2023-06-06-20-43-43 DELETED!
#why dont they go away? what was and wasnt deleted?

