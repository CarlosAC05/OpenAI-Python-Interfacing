import openai
openai.api_key = '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'


print(openai.FineTune.retrieve("ft-VUoIhBlVPKl2yNjKuGcfA4vJ"))


while True:
  False
  p= input("prompt:")
  print(repr(p))
  if len(p) ==0:
    break
  response =openai.Completion.create(
  model="text-davinci-003",
  prompt=p,
  max_tokens =100,
  temperature =0)
  answer= response["choices"][0]["text"]
  answer.encode("ascii","ignore")
  print(answer)
#"davinci:ft-personal-2023-06-08-20-49-56"
#"davinci:ft-personal-2023-06-09-17-29-40"



