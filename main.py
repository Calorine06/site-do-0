from flask import Flask, render_template

# 1. O app DEVE ser criado aqui no escopo principal:
app = Flask(__name__)

LISTA_PRODUTOS = [
    {"nome": "Cone Trufado", "preco": 12.00},
    {"nome": "Palha Italiana", "preco": 15.49}, 
    {"nome": "Tortinha", "preco": 16.00  },
    {"nome": "Bombom de Morango", "preco": 18.00},
    {"nome": "Bombom de Uva", "preco": 18.00},
] # suas rotas e produtos aqui

@app.route('/')
def home():
    return render_template('login.html', produtos=LISTA_PRODUTOS)

# 2. Apenas o app.run fica no final:
if __name__ == '__main__':
    app.run(port=3000, debug=True)