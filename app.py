from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    '<div> i am at the home page</div>'

if __name__ == '__main__':
    app.run(debug=True)