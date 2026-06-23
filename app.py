from flask import Flask, render_template, request

app = Flask(__name__)

PRODUTOS = [
  # Eletrônicos
  {"id":1,"nome":"Fone Bluetooth","categoria":"Eletrônicos","preco":89.90,"imagem":"https://cdn.pixabay.com/photo/2015/08/07/20/21/earphones-879922_1280.jpg","descricao":"Fone sem fio com bateria de 8h"},
  {"id":2,"nome":"Mouse Gamer","categoria":"Eletrônicos","preco":129.90,"imagem":"https://cdn.pixabay.com/photo/2016/11/29/13/09/mouse-1869896_1280.jpg","descricao":"Mouse RGB com 6 botões"},
  {"id":3,"nome":"Teclado Mecânico","categoria":"Eletrônicos","preco":199.90,"imagem":"https://cdn.pixabay.com/photo/2015/05/31/10/54/computer-790130_1280.jpg","descricao":"Teclado mecânico switch azul"},
  {"id":4,"nome":"Carregador USB-C","categoria":"Eletrônicos","preco":39.90,"imagem":"https://cdn.pixabay.com/photo/2017/06/17/23/31/charge-2413844_1280.jpg","descricao":"Carregador rápido 30W"},
  {"id":5,"nome":"Caixa de Som","categoria":"Eletrônicos","preco":149.90,"imagem":"https://cdn.pixabay.com/photo/2018/01/21/21/10/speaker-3097301_1280.jpg","descricao":"Caixa de som portátil à prova d'água"},
  {"id":6,"nome":"Smartwatch","categoria":"Eletrônicos","preco":299.90,"imagem":"https://cdn.pixabay.com/photo/2017/03/10/18/07/smartwatch-2133131_1280.jpg","descricao":"Relógio inteligente com monitor cardíaco"},
  {"id":7,"nome":"Webcam HD","categoria":"Eletrônicos","preco":179.90,"imagem":"https://cdn.pixabay.com/photo/2016/11/13/06/51/web-cam-1820529_1280.jpg","descricao":"Webcam 1080p com microfone integrado"},
  {"id":8,"nome":"Monitor 24\"","categoria":"Eletrônicos","preco":899.90,"imagem":"https://cdn.pixabay.com/photo/2016/11/29/08/41/apple-847182_1280.jpg","descricao":"Monitor Full HD IPS 75Hz"},
  
  # Roupas
  {"id":9,"nome":"Camiseta Preta","categoria":"Roupas","preco":49.90,"imagem":"https://cdn.pixabay.com/photo/2017/01/31/17/04/tshirt-2025553_1280.png","descricao":"Camiseta 100% algodão"},
  {"id":10,"nome":"Jaqueta Jeans","categoria":"Roupas","preco":159.90,"imagem":"https://cdn.pixabay.com/photo/2016/12/06/09/30/blank-1886008_1280.png","descricao":"Jaqueta jeans masculina"},
  {"id":11,"nome":"Vestido Floral","categoria":"Roupas","preco":89.90,"imagem":"https://cdn.pixabay.com/photo/2016/09/23/23/24/dress-1690804_1280.jpg","descricao":"Vestido leve e confortável"},
  {"id":12,"nome":"Moletom","categoria":"Roupas","preco":119.90,"imagem":"https://cdn.pixabay.com/photo/2017/09/14/19/31/sweatshirt-2750105_1280.jpg","descricao":"Moletom com capuz e bolsos"},
  {"id":13,"nome":"Calça Jeans","categoria":"Roupas","preco":99.90,"imagem":"https://cdn.pixabay.com/photo/2015/07/17/12/30/jeans-849550_1280.jpg","descricao":"Calça jeans tradicional"},
  {"id":14,"nome":"Blazer","categoria":"Roupas","preco":199.90,"imagem":"https://cdn.pixabay.com/photo/2016/10/25/12/28/blazer-1768715_1280.jpg","descricao":"Blazer social slim fit"},
  
  # Calçados
  {"id":15,"nome":"Tênis Esportivo","categoria":"Calçados","preco":249.90,"imagem":"https://cdn.pixabay.com/photo/2015/07/02/10/22/sport-828950_1280.jpg","descricao":"Tênis confortável para corrida"},
  {"id":16,"nome":"Sapato Social","categoria":"Calçados","preco":189.90,"imagem":"https://cdn.pixabay.com/photo/2015/11/07/11/15/leather-1031428_1280.jpg","descricao":"Sapato social em couro legítimo"},
  {"id":17,"nome":"Sandália","categoria":"Calçados","preco":69.90,"imagem":"https://cdn.pixabay.com/photo/2018/09/28/22/08/shoes-3710150_1280.jpg","descricao":"Sandália casual confortável"},
  {"id":18,"nome":"Botas","categoria":"Calçados","preco":299.90,"imagem":"https://cdn.pixabay.com/photo/2014/04/22/07/28/boots-329320_1280.jpg","descricao":"Bota cano curto em couro"},
  {"id":19,"nome":"Chinelo","categoria":"Calçados","preco":29.90,"imagem":"https://cdn.pixabay.com/photo/2018/09/28/22/09/shoes-3710153_1280.jpg","descricao":"Chinelo confortável para praia"},
  
  # Acessórios
  {"id":20,"nome":"Mochila Notebook","categoria":"Acessórios","preco":159.90,"imagem":"https://cdn.pixabay.com/photo/2015/10/12/15/18/bags-984215_1280.jpg","descricao":"Proteção para notebook 15.6"},
  {"id":21,"nome":"Bolsa Feminina","categoria":"Acessórios","preco":129.90,"imagem":"https://cdn.pixabay.com/photo/2015/05/26/21/50/purse-785662_1280.jpg","descricao":"Bolsa transversal em couro sintético"},
  {"id":22,"nome":"Óculos de Sol","categoria":"Acessórios","preco":79.90,"imagem":"https://cdn.pixabay.com/photo/2017/05/13/06/40/sunglasses-2308824_1280.jpg","descricao":"Óculos com proteção UV400"},
  {"id":23,"nome":"Relógio","categoria":"Acessórios","preco":149.90,"imagem":"https://cdn.pixabay.com/photo/2017/04/12/07/21/watch-2223552_1280.jpg","descricao":"Relógio analógico em aço inox"},
  {"id":24,"nome":"Carteira","categoria":"Acessórios","preco":59.90,"imagem":"https://cdn.pixabay.com/photo/2015/07/31/18/27/wallet-869558_1280.jpg","descricao":"Carteira em couro com 12 compartimentos"},
  {"id":25,"nome":"Cinto","categoria":"Acessórios","preco":49.90,"imagem":"https://cdn.pixabay.com/photo/2018/07/17/19/13/belt-3544786_1280.jpg","descricao":"Cinto couro fivela niquelada"},
  
  # Casa
  {"id":26,"nome":"Abajur","categoria":"Casa","preco":89.90,"imagem":"https://cdn.pixabay.com/photo/2017/08/01/14/19/lamp-2565538_1280.jpg","descricao":"Abajur de mesa com luz amarela"},
  {"id":27,"nome":"Almofada","categoria":"Casa","preco":39.90,"imagem":"https://cdn.pixabay.com/photo/2017/08/07/19/19/cushion-2606305_1280.jpg","descricao":"Almofada decorativa 45cm"},
  {"id":28,"nome":"Caneca","categoria":"Casa","preco":29.90,"imagem":"https://cdn.pixabay.com/photo/2017/08/05/11/38/mug-2583591_1280.jpg","descricao":"Caneca térmica 350ml"},
  {"id":29,"nome":"Vaso","categoria":"Casa","preco":69.90,"imagem":"https://cdn.pixabay.com/photo/2018/12/16/17/41/succulent-3879319_1280.jpg","descricao":"Vaso decorativo médio"},
  
  # Papelaria
  {"id":30,"nome":"Caderno","categoria":"Papelaria","preco":29.90,"imagem":"https://cdn.pixabay.com/photo/2018/11/15/14/13/notepad-3817760_1280.jpg","descricao":"Caderno 10 matérias 200 folhas"},
  {"id":31,"nome":"Caneta Colorida","categoria":"Papelaria","preco":19.90,"imagem":"https://cdn.pixabay.com/photo/2013/11/04/21/39/writing-205599_1280.jpg","descricao":"Kit 12 canetas coloridas"},
  {"id":32,"nome":"Agenda 2026","categoria":"Papelaria","preco":49.90,"imagem":"https://cdn.pixabay.com/photo/2017/08/30/07/52/calendar-2696254_1280.jpg","descricao":"Agenda anual capa dura"},
  {"id":33,"nome":"Post-it","categoria":"Papelaria","preco":12.90,"imagem":"https://cdn.pixabay.com/photo/2017/08/08/21/58/post-it-2612865_1280.jpg","descricao":"Bloco de notas adesivas 100un"},
  {"id":34,"nome":"Marca Texto","categoria":"Papelaria","preco":15.90,"imagem":"https://cdn.pixabay.com/photo/2017/11/21/11/33/highlighter-2968000_1280.jpg","descricao":"Kit 6 marca-textos fluorescência"},
  {"id":35,"nome":"Estojo","categoria":"Papelaria","preco":34.90,"imagem":"https://cdn.pixabay.com/photo/2017/09/15/21/44/pencil-case-2753502_1280.jpg","descricao":"Estojo escolar com zíper"}
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
