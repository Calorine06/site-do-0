from flask import Flask, render_template

# 1. O app DEVE ser criado aqui no escopo principal:
app = Flask(__name__)

LISTA_PRODUTOS = [...] # suas rotas e produtos aqui

@app.route('/')
def home():
    return render_template('login.html', produtos=LISTA_PRODUTOS)

# 2. Apenas o app.run fica no final:
if __name__ == '__main__':
    app.run(port=3000, debug=True)