import openai
import os
import json
key = os.environ.get('API_Key')
openai.api_key_path="C:/Users/ccace/VSAI/KEY"

openai.api_key = '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'
mytraining=[("hello","how are you"),
            ("I am Sad","thats sad"),]
outitems=[]
for item in mytraining:
    out=repr({"prompt":item[0],"response":item[1]})
    outitems.append(out)
outstring="\n".join(outitems)
f2=open("C:/Users/ccace/VSAI/FineT2")
f2.write(mytraining)
f2.close()
create_args = {
	"training_file": "C:/Users/ccace/VSAI/FineT1",
	"validation_file": "C:/Users/ccace/VSAI/KEY",
	"model": "davinci",
	"n_epochs": 15,
	"batch_size": 3,
	"learning_rate_multiplier": 0.3
}

response = openai.FineTune.create(create_args)
job_id = response["id"]
status = response["status"]

print(f'Fine-tunning model with jobID: {job_id}.')
print(f"Training Response: {response}")
print(f"Training Status: {status}")


f=open("C:/Users/ccace/VSAI/FineT1","w+")
f.write(outstring)
f.close()
f1=open("C:/Users/ccace/VSAI/KEY","w+")
f1.write('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')
f1.close()





