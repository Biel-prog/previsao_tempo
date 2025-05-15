from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "317d78fc643660020081af1689af1147"
@app.route('/', methods=['GET', 'POST'])
def index():
    clima = None

    if request.method == 'POST':
        cidade = request.form['cidade']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            clima = {
                'cidade': dados['name'],
                'temperatura': dados['main']['temp'],
                'descricao': dados['weather'][0]['description'],
                'icone': dados['weather'][0]['icon']
            }
        else:
            clima = {'erro': 'Cidade não encontrada!'}

    return render_template('index.html', clima=clima)
if __name__ == '__main__':
    app.run(debug=True)