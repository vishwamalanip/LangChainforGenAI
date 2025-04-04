from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.5 , max_completion_tokens=40) 
#try temperature values between 0 to 2 
# (which indicate that if value is 0 thn it will give you same output again and again
#  but if you change it to 0.5 it will change a bit of output but if you give maximun 2 value if will change the output more creatively and mostly completely)
#max_completion_tokens=10 is roughly howmany words
#  

result = model.invoke("who is virat kohli") 
#result = model.invoke("give me python code for printing a reverse string")  
#you can change this text any time to ask any question 
# #Write a 5 line poem on datascientist

print(result.content) # print(result) (this will show everything)
