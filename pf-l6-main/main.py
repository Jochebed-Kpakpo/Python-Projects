 #Function to fetch a response from the numbersapi based on a request
import json
import requests

def trivia_fetch(num):
  
  response = requests.get(f"http://numbersapi.com/{num}?json")

  return json.loads(response.content)



# Function to interact with user
def main():
  print("Hello learners!")

  num = int(input("Enter a number"))

  trivia = trivia_fetch(num)

  print(trivia)

if __name__=="__main__":
  main()