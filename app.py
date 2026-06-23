from flask import Flask, render_template, request

app = Flask(__name__)

PRODUTOS = [
  # Eletrônicos
  {"id":1,"nome":"Fone Bluetooth","categoria":"Eletrônicos","preco":89.90,"imagem":"https://placehold.co/400x300/667eea/ffffff?text=Fone+BT","descricao":"Fone sem fio com bateria de 8h"},
  {"id":2,"nome":"Mouse Gamer","categoria":"Eletrônicos","preco":129.90,"imagem":"https://placehold.co/400x300/764ba2/ffffff?text=Mouse","descricao":"Mouse RGB com 6 botões"},
  {"id":3,"nome":"Teclado Mecânico","categoria":"Eletrônicos","preco":199.90,"imagem":"https://placehold.co/400x300/667eea/ffffff?text=Teclado","descricao":"Teclado mecânico switch azul"},
  {"id":4,"nome":"Carregador USB-C","categoria":"Eletrônicos","preco":39.90,"imagem":"https://placehold.co/400x300/764ba2/ffffff?text=USB-C","descricao":"Carregador rápido 30W"},
  {"id":5,"nome":"Caixa de Som","categoria":"Eletrônicos","preco":149.90,"imagem":"https://placehold.co/400x300/667eea/ffffff?text=Caixa+Som","descricao":"Caixa de som portátil à prova d'água"},
  {"id":6,"nome":"Smartwatch","categoria":"Eletrônicos","preco":299.90,"imagem":"https://placehold.co/400x300/764ba2/ffffff?text=Smartwatch","descricao":"Relógio inteligente com monitor cardíaco"},
  {"id":7,"nome":"Webcam HD","categoria":"Eletrônicos","preco":179.90,"imagem":"https://placehold.co/400x300/667eea/ffffff?text=Webcam","descricao":"Webcam 1080p com microfone integrado"},
  {"id":8,"nome":"Monitor 24","categoria":"Eletrônicos","preco":899.90,"imagem":"https://placehold.co/400x300/764ba2/ffffff?text=Monitor","descricao":"Monitor Full HD IPS 75Hz"},
  
  # Roupas
  {"id":9,"nome":"Camiseta Preta","categoria":"Roupas","preco":49.90,"imagem":"https://placehold.co/400x300/e74c3c/ffffff?text=Camiseta","descricao":"Camiseta 100% algodão"},
  {"id":10,"nome":"Jaqueta Jeans","categoria":"Roupas","preco":159.90,"imagem":"https://placehold.co/400x300/3498db/ffffff?text=Jaqueta","descricao":"Jaqueta jeans masculina"},
  {"id":11,"nome":"Vestido Floral","categoria":"Roupas","preco":89.90,"imagem":"https://placehold.co/400x300/e91e63/ffffff?text=Vestido","descricao":"Vestido leve e confortável"},
  {"id":12,"nome":"Moletom","categoria":"Roupas","preco":119.90,"imagem":"https://placehold.co/400x300/2ecc71/ffffff?text=Moletom","descricao":"Moletom com capuz e bolsos"},
  {"id":13,"nome":"Calça Jeans","categoria":"Roupas","preco":99.90,"imagem":"https://placehold.co/400x300/2980b9/ffffff?text=Calca+Jeans","descricao":"Calça jeans tradicional"},
  {"id":14,"nome":"Blazer","categoria":"Roupas","preco":199.90,"imagem":"https://placehold.co/400x300/8e44ad/ffffff?text=Blazer","descricao":"Blazer social slim fit"},
  
  # Calçados
  {"id":15,"nome":"Tênis Esportivo","categoria":"Calçados","preco":249.90,"imagem":"https://placehold.co/400x300/1abc9c/ffffff?text=Tenis","descricao":"Tênis confortável para corrida"},
  {"id":16,"nome":"Sapato Social","categoria":"Calçados","preco":189.90,"imagem":"https://placehold.co/400x300/34495e/ffffff?text=Sapato","descricao":"Sapato social em couro legítimo"},
  {"id":17,"nome":"Sandália","categoria":"Calçados","preco":69.90,"imagem":"https://placehold.co/400x300/e67e22/ffffff?text=Sandalia","descricao":"Sandália casual confortável"},
  {"id":18,"nome":"Botas","categoria":"Calçados","preco":299.90,"imagem":"https://placehold.co/400x300/7f8c8d/ffffff?text=Botas","descricao":"Bota cano curto em couro"},
  {"id":19,"nome":"Chinelo","categoria":"Calçados","preco":29.90,"imagem":"https://placehold.co/400x300/f39c12/ffffff?text=Chinelo","descricao":"Chinelo confortável para praia"},
  
  # Acessórios
  {"id":20,"nome":"Mochila Notebook","categoria":"Acessórios","preco":159.90,"imagem":"https://placehold.co/400x300/2c3e50/ffffff?text=Mochila","descricao":"Proteção para notebook 15.6"},
  {"id":21,"nome":"Bolsa Feminina","categoria":"Acessórios","preco":129.90,"imagem":"https://placehold.co/400x300/c0392b/ffffff?text=Bolsa","descricao":"Bolsa transversal em couro sintético"},
  {"id":22,"nome":"Óculos de Sol","categoria":"Acessórios","preco":79.90,"imagem":"https://placehold.co/400x300/16a085/ffffff?text=Oculos","descricao":"Óculos com proteção UV400"},
  {"id":23,"nome":"Relógio","categoria":"Acessórios","preco":149.90,"imagem":"https://placehold.co/400x300/d35400/ffffff?text=Relogio","descricao":"Relógio analógico em aço inox"},
  {"id":24,"nome":"Carteira","categoria":"Acessórios","preco":59.90,"imagem":"https://placehold.co/400x300/607d8b/ffffff?text=Carteira","descricao":"Carteira em couro com 12 compartimentos"},
  {"id":25,"nome":"Cinto","categoria":"Acessórios","preco":49.90,"imagem":"https://placehold.co/400x300/795548/ffffff?text=Cinto","descricao":"Cinto couro fivela niquelada"},
  
  # Casa
  {"id":26,"nome":"Abajur","categoria":"Casa","preco":89.90,"imagem":"https://placehold.co/400x300/ff9800/ffffff?text=Abajur","descricao":"Abajur de mesa com luz amarela"},
  {"id":27,"nome":"Almofada","categoria":"Casa","preco":39.90,"imagem":"https://placehold.co/400x300/4caf50/ffffff?text=Almofada","descricao":"Almofada decorativa 45cm"},
  {"id":28,"nome":"Caneca","categoria":"Casa","preco":29.90,"imagem":"https://placehold.co/400x300/9c27b0/ffffff?text=Caneca","descricao":"Caneca térmica 350ml"},
  {"id":29,"nome":"Vaso","categoria":"Casa","preco":69.90,"imagem":"https://placehold.co/400x300/00bcd4/ffffff?text=Vaso","descricao":"Vaso decorativo médio"},
  
  # Papelaria
  {"id":30,"nome":"Caderno","categoria":"Papelaria","preco":29.90,"imagem":"https://placehold.co/400x300/3f51b5/ffffff?text=Caderno","descricao":"Caderno 10 matérias 200 folhas"},
  {"id":31,"nome":"Caneta Colorida","categoria":"Papelaria","preco":19.90,"imagem":"https://placehold.co/400x300/ff5722/ffffff?text=Caneta","descricao":"Kit 12 canetas coloridas"},
  {"id":32,"nome":"Agenda 2026","categoria":"Papelaria","preco":49.90,"imagem":"https://placehold.co/400x300/673ab7/ffffff?text=Agenda","descricao":"Agenda anual capa dura"},
  {"id":33,"nome":"Post-it","categoria":"Papelaria","preco":12.90,"imagem":"https://placehold.co/400x300/009688/ffffff?text=Post-it","descricao":"Bloco de notas adesivas 100un"},
  {"id":34,"nome":"Marca Texto","categoria":"Papelaria","preco":15.90,"imagem":"https://placehold.co/400x300/e91e63/ffffff?text=Marca+Texto","descricao":"Kit 6 marca-textos fluorescência"},
  {"id":35,"nome":"Estojo","categoria":"Papelaria","preco":34.90,"imagem":"https://placehold.co/400x300/f44336/ffffff?text=Estojo","descricao":"Estojo escolar com zíper"}
]

def get_categorias():
    return sorted(set(p['categoria'] for p in PRODUTOS))

@app.route('/')
def home():
    produtos = PRODUTOS[:]
    categorias = get_categorias()
    query = request.args.get('q', '').strip()
    categoria = request.args.get('categoria', '').strip()
    if query:
        produtos = [p for p in produtos if query.lower() in p['nome'].lower() or query.lower() in p['descricao'].lower() or query.lower() in p['categoria'].lower()]
    if categoria:
        produtos = [p for p in produtos if p['categoria'] == categoria]
    return render_template('index.html', produtos=produtos, categorias=categorias, query=query, categoria=categoria)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
