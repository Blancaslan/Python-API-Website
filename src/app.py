from flask import Flask

data = {
    "firstname": ["Dennis", "Leroy", "Calum"],
    "lastname": ["Ceker", "D'eath", "Murrel"]
}

app = Flask(__name__)

@app.route('/Get')
def Get():
    return data