from flask import Flask, render_template, request

app = Flask(__name__)

PRODUTOS = [
  # Eletrônicos
  {"id":1,"nome":"Fone Bluetooth","categoria":"Eletrônicos","preco":89.90,"imagem":"https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=300&fit=crop","descricao":"Fone sem fio com bateria de 8h"},
  {"id":2,"nome":"Mouse Gamer","categoria":"Eletrônicos","preco":129.90,"imagem":"https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400&h=300&fit=crop","descricao":"Mouse RGB com 6 botões"},
  {"id":3,"nome":"Teclado Mecânico","categoria":"Eletrônicos","preco":199.90,"imagem":"https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400&h=300&fit=crop","descricao":"Teclado mecânico switch azul"},
  {"id":4,"nome":"Carregador USB-C","categoria":"Eletrônicos","preco":39.90,"imagem":"https://images.unsplash.com/photo-1640955014212-63b86e6d3c17?w=400&h=300&fit=crop","descricao":"Carregador rápido 30W"},
  {"id":5,"nome":"Caixa de Som","categoria":"Eletrônicos","preco":149.90,"imagem":"https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400&h=300&fit=crop","descricao":"Caixa de som portátil à prova d'água"},
  {"id":6,"nome":"Smartwatch","categoria":"Eletrônicos","preco":299.90,"imagem":"https://images.unsplash.com/photo-1546868871-af0de0ae72f5?w=400&h=300&fit=crop","descricao":"Relógio inteligente com monitor cardíaco"},
  {"id":7,"nome":"Webcam HD","categoria":"Eletrônicos","preco":179.90,"imagem":"https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400&h=300&fit=crop","descricao":"Webcam 1080p com microfone integrado"},
  {"id":8,"nome":"Monitor 24\"","categoria":"Eletrônicos","preco":899.90,"imagem":"https://images.unsplash.com/photo-1586210579192-33b45d38d99e?w=400&h=300&fit=crop","descricao":"Monitor Full HD IPS 75Hz"},
  
  # Roupas
  {"id":9,"nome":"Camiseta Preta","categoria":"Roupas","preco":49.90,"imagem":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=300&fit=crop","descricao":"Camiseta 100% algodão"},
  {"id":10,"nome":"Jaqueta Jeans","categoria":"Roupas","preco":159.90,"imagem":"https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=300&fit=crop","descricao":"Jaqueta jeans masculina"},
  {"id":11,"nome":"Vestido Floral","categoria":"Roupas","preco":89.90,"imagem":"https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400&h=300&fit=crop","descricao":"Vestido leve e confortável"},
  {"id":12,"nome":"Moletom","categoria":"Roupas","preco":119.90,"imagem":"https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400&h=300&fit=crop","descricao":"Moletom com capuz e bolsos"},
  {"id":13,"nome":"Calça Jeans","categoria":"Roupas","preco":99.90,"imagem":"https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=400&h=300&fit=crop","descricao":"Calça jeans tradicional"},
  {"id":14,"nome":"Blazer","categoria":"Roupas","preco":199.90,"imagem":"https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=400&h=300&fit=crop","descricao":"Blazer social slim fit"},
  
  # Calçados
  {"id":15,"nome":"Tênis Esportivo","categoria":"Calçados","preco":249.90,"imagem":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=300&fit=crop","descricao":"Tênis confortável para corrida"},
  {"id":16,"nome":"Sapato Social","categoria":"Calçados","preco":189.90,"imagem":"https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400&h=300&fit=crop","descricao":"Sapato social em couro legítimo"},
  {"id":17,"nome":"Sandália","categoria":"Calçados","preco":69.90,"imagem":"https://images.unsplash.com/photo-1603487742131-4160ec999306?w=400&h=300&fit=crop","descricao":"Sandália casual confortável"},
  {"id":18,"nome":"Botas","categoria":"Calçados","preco":299.90,"imagem":"https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=400&h=300&fit=crop","descricao":"Bota cano curto em couro"},
  {"id":19,"nome":"Chinelo","categoria":"Calçados","preco":29.90,"imagem":"https://images.unsplash.com/photo-1603487742131-4160ec999306?w=400&h=300&fit=crop","descricao":"Chinelo confortável para praia"},
  
  # Acessórios
  {"id":20,"nome":"Mochila Notebook","categoria":"Acessórios","preco":159.90,"imagem":"https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=300&fit=crop","descricao":"Proteção para notebook 15.6"},
  {"id":21,"nome":"Bolsa Feminina","categoria":"Acessórios","preco":129.90,"imagem":"https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400&h=300&fit=crop","descricao":"Bolsa transversal em couro sintético"},
  {"id":22,"nome":"Óculos de Sol","categoria":"Acessórios","preco":79.90,"imagem":"https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400&h=300&fit=crop","descricao":"Óculos com proteção UV400"},
  {"id":23,"nome":"Relógio","categoria":"Acessórios","preco":149.90,"imagem":"https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=400&h=300&fit=crop","descricao":"Relógio analógico em aço inox"},
  {"id":24,"nome":"Carteira","categoria":"Acessórios","preco":59.90,"imagem":"https://images.unsplash.com/photo-1627123424574-724758594e93?w=400&h=300&fit=crop","descricao":"Carteira em couro com 12 compartimentos"},
  {"id":25,"nome":"Cinto","categoria":"Acessórios","preco":49.90,"imagem":"https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=300&fit=crop","descricao":"Cinto couro fivela niquelada"},
  
  # Casa
  {"id":26,"nome":"Abajur","categoria":"Casa","preco":89.90,"imagem":"https://images.unsplash.com/photo-1507473885765-e6ed057ab6fe?w=400&h=300&fit=crop","descricao":"Abajur de mesa com luz amarela"},
  {"id":27,"nome":"Almofada","categoria":"Casa","preco":39.90,"imagem":"https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?w=400&h=300&fit=crop","descricao":"Almofada decorativa 45cm"},
  {"id":28,"nome":"Caneca","categoria":"Casa","preco":29.90,"imagem":"https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=400&h=300&fit=crop","descricao":"Caneca térmica 350ml"},
  {"id":29,"nome":"Vaso","categoria":"Casa","preco":69.90,"imagem":"https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400&h=300&fit=crop","descricao":"Vaso decorativo médio"},
  
  # Papelaria
  {"id":30,"nome":"Caderno","categoria":"Papelaria","preco":29.90,"imagem":"https://images.unsplash.com/photo-1531346878377-a5be20888e57?w=400&h=300&fit=crop","descricao":"Caderno 10 matérias 200 folhas"},
  {"id":31,"nome":"Caneta Colorida","categoria":"Papelaria","preco":19.90,"imagem":"https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=400&h=300&fit=crop","descricao":"Kit 12 canetas coloridas"},
  {"id":32,"nome":"Agenda 2026","categoria":"Papelaria","preco":49.90,"imagem":"https://images.unsplash.com/photo-1531346878377-a5be20888e57?w=400&h=300&fit=crop","descricao":"Agenda anual capa dura"},
  {"id":33,"nome":"Post-it","categoria":"Papelaria","preco":12.90,"imagem":"https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=400&h=300&fit=crop","descricao":"Bloco de notas adesivas 100un"},
  {"id":34,"nome":"Marca Texto","categoria":"Papelaria","preco":15.90,"imagem":"https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=400&h=300&fit=crop","descricao":"Kit 6 marca-textos fluorescência"},
  {"id":35,"nome":"Estojo","categoria":"Papelaria","preco":34.90,"imagem":"https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=400&h=300&fit=crop","descricao":"Estojo escolar com zíper"}
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
