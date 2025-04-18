from flask import Flask
from src.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def welocom():
    logging.info('App is going to start')
    return "Welcome to Flask"


if __name__=="__main__":
    app.run(debug=True)