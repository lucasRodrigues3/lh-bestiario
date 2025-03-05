from flask import Flask, render_template, request
from random import randint

app = Flask(__name__, static_folder='static')

tipos = ['Aquaris','Feralis','Nanktuk','Plumavel','Reptilha','Vegetuz']
levels_rand = ['Básico','Básico', 'Básico', 'Básico', 'Básico', 'Básico', 'Avançado', 'Avançado', 'Avançado', 'Superior']
levels = ['Básico', 'Avançado', 'Superior']
classes = ['Bruiser', 'Combo', 'Control', 'Nuker', 'Tank']
atividades = ['Diurna', 'Noturna', 'Indefinida']
dados = {
    'Básico': ['D6','D8'],
    'Avançado': ['D10','D12'],
    'Superior': ['D20']
}
atributos = {
    'atq_def': {
        'Básico': [20, 50],
        'Avançado': [70, 100],
        'Superior': [170, 340]
    },
    'psc': {
        'Básico': [10, 20],
        'Avançado': [25, 40],
        'Superior': [50, 50]
    },
    'ict': {
        'Básico': [10, 20],
        'Avançado': [30, 40],
        'Superior': [50, 100]
    },
    'vit': {
        'Básico': [100, 300],
        'Avançado': [500, 1000],
        'Superior': [5000, 50000]
    },
}
lista_poderes = {
    'Aquaris': {
        'Básico': ['Explosão Hídrica', 'Movimento De Ondas', 'Bolha Aquática', 'Hidro Armadura'],
        'Avançado': ['Tsunami', 'Barreira Tornado', 'Benção Do Leviathan'],
        'Superior': ['Pressão Marítima', 'Inundação Oceânica']
    },
    'Feralis': {
        'Básico': ['Garras Dilacerantes', 'Mordida Brutal', 'Rugido Ameaçador', 'Salto Devastador'],
        'Avançado': ['Fúria Primordial', 'Investida Predatória', 'Benção Do Behemort'],
        'Superior': ['Instinto Imortal', 'Golpe Selvagem']
    },
    'Nanktuk': {
        'Básico': ['Zumbido Paralisante', 'Ferrão Excruciante', 'Túnel Predatório', 'Encasular'],
        'Avançado': ['Armadura Quitinosa', 'Olhos Multifacetados', 'Veneno Corrosivo'],
        'Superior': ['Chamado Da Colônia', 'Simbiose Do Enxame']
    },
    'Plumavel': {
        'Básico': ['Retalho De Asas', 'Visão Predatória', 'Grito Estridente', 'Barreira De Penas'],
        'Avançado': ['Frenesi Aéreo', 'Cacofonia Celeste', 'Proteção Aérea'],
        'Superior': ['Soberano Alado', 'Tempestade De Plumas']
    },
    'Reptilha': {
        'Básico': ['Infectar', 'Sangue Frio', 'Olhar Hipnótico', 'Pele Maleável'],
        'Avançado': ['Escamas Primordiais', 'Veneno Corrosivo', 'Mimetismo Rèptil'],
        'Superior': ['Raio Natural', 'Sopro Abrasador']
    },
    'Vegetuz': {
        'Básico': ['Reflorescer', 'Lianas De Espinhos', 'Mutação Botânica', 'Armadilha Natural'],
        'Avançado': ['Pólen Ilusório', 'Fortaleza Arbórea', 'Jardim Da Carnificina'],
        'Superior': ['Corrupção Botânica', 'Raio Solar']
    }
}

class CriaCriatura:
    def __init__(self, tipo=None, level=None, classe=None, atividade=None, dados_atq=None, qtd_dados_atq=None,
                 dados_def=None, qtd_dados_def=None, pts_atq=None, pts_def=None, pts_psc=None, pts_ict=None,
                 pts_vit=None, poderes=None, nature=None):
        
        if tipo is None:
            tipo = self.define_tipo
        if level is None:
            level = self.define_level
        if classe is None:
            classe = self.define_classe
        if atividade is None:
            atividade = self.define_atividade
        if dados_atq is None:
            dados_atq = self.define_dados_atq(level)
        if qtd_dados_atq is None:
            qtd_dados_atq = self.define_qtd_dados_atq()
        if dados_def is None:
            dados_def = self.define_dados_def(level)
        if qtd_dados_def is None:
            qtd_dados_def = self.define_qtd_dados_def()
        if pts_atq is None:
            pts_atq = self.define_atq(level)
        if pts_def is None:
            pts_def = self.define_def(level)
        if pts_psc is None:
            pts_psc = self.define_psc(level)
        if pts_ict is None:
            pts_ict = self.define_ict(level)
        if pts_vit is None:
            pts_vit = self.define_vit(level)
        if poderes is None:
            poderes = self.define_poderes(tipo, level)
        if nature is None:
            nature = self.define_nature(level)

        self.tipo = tipo
        self.level = level
        self.classe = classe
        self.atividade = atividade
        self.dados_atq = dados_atq
        self.qtd_dados_atq = qtd_dados_atq
        self.dados_def = dados_def
        self.qtd_dados_def = qtd_dados_def
        self.pts_atq = pts_atq
        self.pts_def = pts_def
        self.pts_psc = pts_psc
        self.pts_ict = pts_ict
        self.pts_vit = pts_vit
        self.poderes = poderes
        self.nature = nature

    @property
    def define_tipo(self):
        return tipos[randint(0, len(tipos) - 1)]
    
    @property
    def define_level(self):
        return levels_rand[randint(0, len(levels_rand) - 1)]
    
    @property
    def define_classe(self):
        return classes[randint(0, len(classes) - 1)]
    
    @property
    def define_atividade(self):
        return atividades[randint(0, len(atividades) - 1)]

    def define_dados_atq(self, level):
        return dados[level][randint(0, len(dados[level]) - 1)]
    
    def define_qtd_dados_atq(self):
        return randint(10, 20)
    
    def define_dados_def(self, level):
        return dados[level][randint(0, len(dados[level]) - 1)]      
    
    def define_qtd_dados_def(self):
        return randint(10, 20)
         
    def define_atq(self, level):
        min_val = atributos['atq_def'][level][0]
        max_val = atributos['atq_def'][level][1]
        return randint(min_val, max_val)
    
    def define_def(self, level):
        min_val = atributos['atq_def'][level][0]
        max_val = atributos['atq_def'][level][1]
        return randint(min_val, max_val)
    
    def define_psc(self, level):
        min_val = atributos['psc'][level][0]
        max_val = atributos['psc'][level][1]
        return randint(min_val, max_val)
    
    def define_ict(self, level):
        min_val = atributos['ict'][level][0]
        max_val = atributos['ict'][level][1]
        return randint(min_val, max_val)
    
    def define_vit(self, level):
        min_val = atributos['vit'][level][0]
        max_val = atributos['vit'][level][1]
        return randint(min_val, max_val)    

    def define_poderes(self, tipo, level):
        if level == 'Básico':
            poder_excluir = lista_poderes[tipo][level][randint(0, 3)]
            poderes_basicos_escolhidos = [elemento for elemento in lista_poderes[tipo][level] if elemento != poder_excluir]

            poderes = poderes_basicos_escolhidos
            poderes_vertical = "'\n'".join(poderes)
            return poderes_vertical
        
        elif level == 'Avançado':
            poder_excluir = lista_poderes[tipo]['Básico'][randint(0, 3)]
            poderes_basicos_escolhidos = [elemento for elemento in lista_poderes[tipo]['Básico'] if elemento != poder_excluir]

            poder_excluir = lista_poderes[tipo][level][randint(0, 2)]
            poderes_avancados_escolhidos = [elemento for elemento in lista_poderes[tipo][level] if elemento != poder_excluir]

            poderes = poderes_basicos_escolhidos + poderes_avancados_escolhidos
            poderes_vertical = "'\n'".join(poderes)
            return poderes_vertical
        
        else:
            poder_excluir = lista_poderes[tipo]['Básico'][randint(0, 3)]
            poderes_basicos_escolhidos = [elemento for elemento in lista_poderes[tipo]['Básico'] if elemento != poder_excluir]

            poder_excluir = lista_poderes[tipo]['Avançado'][randint(0, 2)]
            poderes_avancados_escolhidos = [elemento for elemento in lista_poderes[tipo]['Avançado'] if elemento != poder_excluir]

            poder_excluir = lista_poderes[tipo][level][randint(0, 1)]
            poderes_superiores_escolhidos = [elemento for elemento in lista_poderes[tipo][level] if elemento != poder_excluir]

            poderes = poderes_basicos_escolhidos + poderes_avancados_escolhidos + poderes_superiores_escolhidos
            poderes_vertical = "'\n'".join(poderes)
            return poderes_vertical

    def define_nature(self, level):
        if level == 'Básico':
            return [randint(1, 3)]
        elif level == 'Avançado':
            excluir = randint(1, 3)
            return [n for n in [1, 2, 3] if n != excluir]
        else:
            return [1, 2, 3]

    def __str__(self):
        return f"""
Tipo: {self.tipo}
Level: {self.level}
Classe: {self.classe}
Atividade: {self.atividade}
Ataque: {self.qtd_dados_atq}{self.dados_atq} + {self.pts_atq * 2 if self.classe == 'Nuker' else self.pts_atq}
Defesa: {self.qtd_dados_def}{self.dados_def} + {self.pts_def * 2 if self.classe == 'Tank' else self.pts_def}
Precisão: {self.pts_psc * 2 if self.classe == 'Control' else self.pts_psc}
Iniciativa: {self.pts_ict * 2 if self.classe == 'Combo' else self.pts_ict}
Vitalidade: {self.pts_vit * 2 if self.classe == 'Bruiser' else self.pts_vit}
Poderes:
'{self.poderes}'
Nature: {self.nature}
        """

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        level = request.form.get('level')
        classe = request.form.get('classe')
        atividade = request.form.get('atividade')

        criatura = CriaCriatura(tipo=tipo if tipo != '' else None,
                                level=level if level != '' else None,
                                classe=classe if classe != '' else None,
                                atividade=atividade if atividade != '' else None)
        # print(criatura)
        return render_template('index.html', criatura=criatura, tipos=tipos, levels=levels, classes=classes, atividades=atividades)
    
    # Se for um GET, apenas renderiza o template com as opções
    return render_template('index.html', tipos=tipos, levels=levels, classes=classes, atividades=atividades)

if __name__ == '__main__':
    app.run(debug=True)