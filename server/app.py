from flask import Flask

app = Flask(__name__) 

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def home ():
    return "<p>Welcome to Flatiron Cars<p>"

@app.route ('/<models>')
def models(model):
    if model in existing_models:
        return f"<p>Flatiron {model} is in our fleet!<p>"
    return f"<p>No models called {model} exists in our catalog<p>"

if __name__ == '__main__':
    app.run(debug=True)