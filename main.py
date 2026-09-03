from flask import Flask, render_template
from produtos import LISTA_PRODUTOS  # Importa a lista dos seus doces

app = Flask(__name__)

@app.route('/')
def home():
    # Envia a lista dos doces para a página HTML automaticamente
    return render_template('login.html', produtos=LISTA_PRODUTOS)

if __name__ == '__main__':
    app.run(port=3000, debug=True)