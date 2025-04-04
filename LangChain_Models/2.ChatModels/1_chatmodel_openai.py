from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0 , max_completion_tokens=40) 
#try temperature values between 0 to 1.5 
#max_completion_tokens=10 is roughly howmany words
#  

result = model.invoke("who is virat kohli") 
#result = model.invoke("give me python code for printing a reverse string")  
#you can change this text any time to ask any question 
# #Write a 5 line poem on datascientist

print(result.content) # print(result) (this will show everything)