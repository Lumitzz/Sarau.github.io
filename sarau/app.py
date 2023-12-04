from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    topics = [
        {
            'title': 'Tereza de Benguela',
            'text': 'Tereza de Benguela, também conhecida como Rainha Tereza, foi uma líder quilombola que viveu na região de Cuiabá (MT) durante o século 18. Chefiou entre 1750 a 1770 o Quilombo do Quariterê, abrigando mais de 100 pessoas negras e indígenas. Sob sua liderança, a comunidade negra e indígena resistiu à escravidão por duas décadas. A Lei 12.987 estipulou o dia 25 de julho, o Dia da Mulher Negra, Latino-Americana e Caribenha, como o Dia de Tereza Bengela.',
        },
        {
            'title': 'Hilária Batista de Almeida (Tia Ciata)',
            'text': 'Hilária Batista de Almeida, conhecida como Tia Ciata, nasceu em 1854 em Santo Amaro (BA). Iniciada no candomblé, foi perseguida por sua religião e teve que se mudar para o Rio de Janeiro aos 22 anos. Tia Ciata foi sambista e mãe de santo brasileira, considerada por muitos como uma das figuras mais influentes para o surgimento do samba carioca.',
        },
        # Adicione mais tópicos conforme necessário
    ]

    authors_info = {
        'activity_code': '2601',
        'authors': 'Yara Ferreira, Maria Eduarda, Kethelen Cristine 3A',
        'professor': 'Soraia',
        'school': 'Cemi Cruzeiro',
        'publication_year': '2023'
    }

    introduction = "A nossa apresentação é dedicada às mulheres negras mais importantes do mundo. Conheça as histórias inspiradoras e impactantes dessas mulheres que deixaram uma marca significativa na sociedade."

    conclusion = "O nosso objetivo com esse trabalho é mostrar a importância das mulheres negras no mundo."

    # Lista de caminhos das imagens
    images = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'image4.jpg',
        'image5.jpg',
    ]

    return render_template('index.html', topics=topics, authors_info=authors_info, introduction=introduction, conclusion=conclusion, images=images)

if __name__ == '__main__':
    app.run(debug=True)
