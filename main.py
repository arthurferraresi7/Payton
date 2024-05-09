from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado='')

@app.route('/verificar', methods = ["POST"])
def verificar():
    idade = int(request.form["numero"])
    resultado = ""
    if idade >= 0 and idade <= 5:
        resultado = 'Bebê'
    if idade >= 6 and idade <= 15:
        resultado = 'Criança'
    if idade >= 16 and idade <= 18:
       resultado = 'Marmanjos hora de trabalhar'
    elif idade >= 19 and idade < 60:
        resultado = 'Acorda pra vida, que você tem boleto pra pagar'
    elif idade >= 60:
       resultado = 'Daqui pra frente e só pra traz'
    return render_template('index.html',resultado = resultado )

if __name__ == '__main__':
    app.run(debug=True)

