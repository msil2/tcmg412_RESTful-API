from flask import Flask, jsonify, escape
import hashlib
import slack
from slackeventsapi import SlackEventAdapter

# Create the main Flask app object
app = Flask(__name__)

# Set '/md5/<string>' app route
@app.route('/md5/<string>')
# Pass value of '<string>' to 'string' in 'md5_encode' function
def md5_encode(string):  
  # Encode default_string as md5
  string_to_md5 = hashlib.md5(escape(string).encode('utf-8')).hexdigest()
 
  # Return JSON payload consisting of input value and output value
  #change to jsonify
  return {"input": string, "output": string_to_md5}


  # Set '/factorial' app route
@app.route('/factorial')
# Set '/factorial/' app route
@app.route('/factorial/')
# Build function 
def factorial():
    factorialOutput = 1

    while True:
        try:
            # get the input
            factorialInput = int(input("What number do you want the factorial of?: "))
            #calculate the factorial
            if (factorialInput > 0):
                for i in range(1, factorialInput + 1):
                    factorialOutput = factorialOutput * i
            # Return JSON payload consisting of input value and output value
                return jsonify(input = factorialInput, output = factorialOutput)
            else:
                return jsonify(input = factorialInput, output = "That's not a valid number!")
            break
        except:
            return jsonify(input = factorialInput, output = "That's not a valid number!")

# Set '/factorial/<num>' app route
@app.route('/factorial/<num>')
# Pass value of '<num>' to 'num' in 'factorial_made' function
def factorial_made(num):
    factorialOutput = 1
    
    while True:
        try:
            num1 = int(num)
            if num1 < 0:
                return jsonify(input = num, output = "That's not a valid number!")
            #calculate the factorial
            
            for i in range(1, num1 + 1):
                factorialOutput = factorialOutput * i
            # Return JSON payload consisting of input value and output value
            return jsonify(input = num, output = factorialOutput)
        except:
            return "Page not found", 404

@app.route('/fibonacci/<int:number>')
def fibonacci(number=1):
  #remove while true and try catch and defalut value (line above this) input needs to be *number* and output should be fib(number)
    while True:
        try:
            n1 = int(number)
            if int(n1) < 0:
                return "Error: not a valid number"
            return jsonify(input = "fib(" + str(number) + "): ", output = str(fib(number)))
        except:
            return jsonify(input = n1, output = "not a valid number")
        
    #return "Howdy!!<hr>fib("+ str(number) + "): " + str(fib(number))

#def fib(n):
   # while True:
       # try:
         #   n1 = int(n)
         #   if int(n1) < 1:
          #      return "Error: not a valid number"
         #   if n1 == 0:
          #      return 0
         #   elif n1 == 1:
          #      return 1
         #   else:
          #      return fib(n1 - 1) + fib(n1 - 2)
      #  except:
          #  return jsonify(input = n1, output = "not a valid number")

#slack alert
import requests
url = "https://hooks.slack.com/services/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"
 slack_data = {'text': 'message here'}
  
  # use the `requests` module to POST to Slack
  r = requests.post(url, json=slack_data)
  
  # you can check the status code of the response from Slack
  if r.status_code == 200:
    # do something if Slack worked
  else:
    # do something else if Slack didn't work

@app.route('/is-prime/<n>')
def is_prime(n): 
  try:
    n = int(n) 

    if n == 1:
        return jsonify(input=n, output=False)

    solve_prime = int(n / 2)
    for i in range(2, solve_prime):
        if n % i == 0:
            return jsonify(input=n, output=False)

    return jsonify(input=n, output=True)

  except:
    return "Error not a number", 404
        
  
    

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
 
