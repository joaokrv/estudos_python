import tkinter as tk
from tkinter import ttk
from experta import *
import webbrowser

# -------------------------------
# Definição dos fatos
# -------------------------------
class Tempo(Fact):
    pouco = False
    medio = False
    muito = False

class Ingrediente(Fact):
    frango = False
    carne = False
    macarrao = False

# -------------------------------
# Motor de inferência
# -------------------------------
class Sugestao(KnowledgeEngine):
    resultados = []

    # -------------------------------
    # Pouco tempo
    # -------------------------------
    @Rule(Tempo(pouco=True), Ingrediente(frango=True, carne=False, macarrao=False))
    def frango_pouco(self):
        self.resultados.append("Bife de frango grelhado")

    @Rule(Tempo(pouco=True), Ingrediente(frango=False, carne=True, macarrao=False))
    def carne_pouco(self):
        self.resultados.append("Bife de carne")

    @Rule(Tempo(pouco=True), Ingrediente(frango=False, carne=False, macarrao=True))
    def macarrao_pouco(self):
        self.resultados.append("Macarrão ao alho e óleo")

    @Rule(Tempo(pouco=True), Ingrediente(frango=True, carne=True, macarrao=False))
    def frango_carne_pouco(self):
        self.resultados.extend([
            "Bife de frango grelhado",
            "Bife de carne"
        ])

    @Rule(Tempo(pouco=True), Ingrediente(frango=True, carne=False, macarrao=True))
    def frango_macarrao_pouco(self):
        self.resultados.extend([
            "Frango grelhado com macarrão simples",
            "Macarrão com peito de frango e creme de leite",
            "Macarrão ao alho e óleo"
        ])

    @Rule(Tempo(pouco=True), Ingrediente(frango=False, carne=True, macarrao=True))
    def carne_macarrao_pouco(self):
        self.resultados.extend([
            "Macarrão com picadinho de carne",
            "Macarrão com carne assada",
            "Macarrão com carne moída"
        ])


    @Rule(Tempo(pouco=True), Ingrediente(frango=True, carne=True, macarrao=True))
    def frango_carne_macarrao_pouco(self):
        self.resultados.extend([
            "Frango grelhado com macarrão simples",
            "Macarrão com peito de frango e creme de leite",
            "Macarrão com picadinho de carne",
            "Macarrão com carne assada",
            "Macarrão com carne moída",
            "Bife de frango grelhado",
            "Bife de carne"
        ])

    # -------------------------------
    # Médio tempo
    # -------------------------------
    @Rule(Tempo(medio=True), Ingrediente(frango=True, carne=False, macarrao=False))
    def frango_medio(self):
        self.resultados.extend([
            "Strogonoff de frango",
            "Frango grelhado com macarrão simples"
        ])

    @Rule(Tempo(medio=True), Ingrediente(frango=False, carne=True, macarrao=False))
    def carne_medio(self):
        self.resultados.extend([
            "Carne assada ou ensopado rápido",
            "Bife de carne"
        ])

    @Rule(Tempo(medio=True), Ingrediente(frango=True, carne=True, macarrao=False))
    def carne_frango_medio(self):
        self.resultados.extend([
            "Carne assada ou ensopado rápido",
            "Bife de carne",
            "Strogonoff de frango",
            "Frango grelhado com macarrão simples"
        ])        

    @Rule(Tempo(medio=True), Ingrediente(frango=False, carne=False, macarrao=True))
    def macarrao_medio(self):
        self.resultados.extend([
            "Macarrão ao creme de leite",
            "Macarrão ao alho e óleo"
        ])

    @Rule(Tempo(medio=True), Ingrediente(frango=True, carne=False, macarrao=True))
    def frango_macarrao_medio(self):
        self.resultados.extend([
            "Macarrão com peito de frango e creme de leite",
            "Macarrão com frango e molho branco",
            "Macarrão com frango cremoso"
        ])

    @Rule(Tempo(medio=True), Ingrediente(frango=False, carne=True, macarrao=True))
    def carne_macarrao_medio(self):
        self.resultados.extend([
            "Macarrão com picadinho de carne",
            "Macarrão com carne assada",
            "Macarrão com carne moída"
        ])

    @Rule(Tempo(medio=True), Ingrediente(frango=True, carne=True, macarrao=True))
    def frango_carne_macarrao_medio(self):
        self.resultados.extend([
            "Macarrão com picadinho de carne",
            "Macarrão com carne assada",
            "Macarrão com carne moída",
            "Macarrão com peito de frango e creme de leite",
            "Macarrão com frango e molho branco",
            "Macarrão com frango cremoso",
            "Strogonoff de frango",
            "Frango grelhado com macarrão simples",
            "Carne assada ou ensopado rápido",
            "Bife de carne",
            "Macarrão ao creme de leite",
            "Macarrão ao alho e óleo"
        ])

    # -------------------------------
    # Muito tempo
    # -------------------------------
    @Rule(Tempo(muito=True), Ingrediente(frango=True, carne=False, macarrao=False))
    def frango_muito(self):
        self.resultados.append("Frango assado ou Frango recheado")

    @Rule(Tempo(muito=True), Ingrediente(frango=False, carne=True, macarrao=False))
    def carne_muito(self):
        self.resultados.append("Carne assada elaborada")

    @Rule(Tempo(muito=True), Ingrediente(frango=True, carne=True, macarrao=False))
    def carne_frango_muito(self):
        self.resultados.extend([
            "Frango assado ou Frango recheado",
            "Carne assada elaborada",
        ])

    @Rule(Tempo(muito=True), Ingrediente(frango=False, carne=True, macarrao=True))
    def carne_macarrao_muito(self):
        self.resultados.extend([
            "Carne assada elaborada",
            "Macarrão especial com molho elaborado"
        ])

    @Rule(Tempo(muito=True), Ingrediente(frango=True, carne=False, macarrao=True))
    def macarrao_frango_muito(self):
        self.resultados.extend(
            ["Macarrão especial com molho elaborado",
            "Frango assado ou Frango recheado"
        ])

    @Rule(Tempo(muito=True), Ingrediente(frango=False, carne=False, macarrao=True))
    def macarrao_muito(self):
        self.resultados.append("Macarrão especial com molho elaborado")

    @Rule(Tempo(muito=True), Ingrediente(frango=True, carne=True, macarrao=True))
    def frango_carne_macarrao_muito(self):
        self.resultados.extend([
            "Prato único: frango, carne, vegetais e macarrão",
            "Frango assado ou Frango recheado",
            "Carne assada elaborada",
            "Macarrão especial com molho elaborado"
        ])

# -------------------------------
# Links das receitas
# -------------------------------
links_receitas = {
    # Frango
    "Bife de frango grelhado": "https://www.tudogostoso.com.br/receita/107124-file-de-frango-grelhado-com-limao.html",
    "Frango grelhado com macarrão simples": "https://www.tudogostoso.com.br/receita/69646-macarrao-alho-e-oleo-com-frango.html",
    "Strogonoff de frango": "https://www.tudogostoso.com.br/receita/2462-strogonoff-de-frango.html",
    "Frango assado ou Frango recheado": "https://www.tudogostoso.com.br/receita/6303-frango-assado-inteiro-e-descomplicado.html",
    # Frango + Macarrão
    "Macarrão com peito de frango e creme de leite": "https://www.tudogostoso.com.br/receita/142362-macarrao-com-peito-de-frango-e-creme-de-leite.html",
    "Macarrão com frango e molho branco": "https://www.receiteria.com.br/receitas-de-macarrao-com-frango/",
    "Macarrão com frango cremoso": "https://www.receiteria.com.br/receitas-de-macarrao-com-frango/",
    # Carne
    "Bife de carne": "https://www.tudogostoso.com.br/receita/24524-bife-acebolado.html",
    "Carne assada ou ensopado rápido": "https://www.tudogostoso.com.br/receita/66573-carne-assada-na-panela-de-pressao.html",
    "Carne assada elaborada": "https://receitas.globo.com/tipos-de-prato/carnes/carne-assada-facil-539083404d38857fed000043.ghtml",
    # Carne + Macarrão
    "Macarrão com picadinho de carne": "https://receitasgalo.com.br/receita/macarrao-com-picadinho-de-carne-sudeste",
    "Macarrão com carne assada": "https://todeschinialimentos.com.br/receita/macarrao-com-carne-assada",
    "Macarrão com carne moída": "https://www.tudogostoso.com.br/receita/136790-macarrao-com-molho-de-carne-moida-de-frango.html",
    # Frango + Carne + Macarrão
    "Prato único: frango, carne, vegetais e macarrão": "https://www.saboresabergastronomia.com.br/post/prato-%C3%BAnico-frango-carne-vegetais-e-macarr%C3%A3o",
    # Macarrão simples
    "Macarrão ao alho e óleo": "https://www.tudogostoso.com.br/receita/57710-macarrao-ao-alho-e-oleo-simples.html",
    "Macarrão ao creme de leite": "https://www.tudogostoso.com.br/receita/19679-macarrao-ao-creme-de-leite.html",
    "Macarrão especial com molho elaborado": "https://www.receitasgratis.net/macarrao-especial"
}

# -------------------------------
# Função para abrir links
# -------------------------------
def abrir_link(url):
    webbrowser.open(url)

# -------------------------------
# Interface Tkinter
# -------------------------------
DAVYS_GRAY = "#595959"
SILVER = "#a5a5a5"
SILVER2 = "#cccccc"
WHITE_SMOKE = "#f2f2f2"

janela = tk.Tk()
janela.title("SE Refeição")

# 🔹 Removido tamanho fixo
# janela.geometry("450x520")  
janela.configure(bg=WHITE_SMOKE)

# Permite redimensionar manualmente também
janela.resizable(True, True)
janela.minsize(400, 400)

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background=WHITE_SMOKE)
style.configure('TLabel', background=WHITE_SMOKE, foreground=DAVYS_GRAY, font=('Arial', 11))
style.configure('TButton', background=SILVER2, foreground=DAVYS_GRAY, font=('Arial', 11, 'bold'), borderwidth=0, padding=6)
style.map('TButton', background=[('active', SILVER)], foreground=[('pressed', WHITE_SMOKE)])
style.configure('TCheckbutton', background=WHITE_SMOKE, foreground=DAVYS_GRAY, font=('Arial', 10))
style.configure('TRadiobutton', background=WHITE_SMOKE, foreground=DAVYS_GRAY, font=('Arial', 10))

frame = ttk.Frame(janela)
frame.pack(padx=20, pady=20, fill='both', expand=True)

# Ingredientes
ttk.Label(frame, text="Selecione os ingredientes:").pack(anchor='w', pady=(0,5))
var_frango = tk.BooleanVar()
var_carne = tk.BooleanVar()
var_macarrao = tk.BooleanVar()
ttk.Checkbutton(frame, text="Frango", variable=var_frango).pack(anchor='w')
ttk.Checkbutton(frame, text="Carne", variable=var_carne).pack(anchor='w')
ttk.Checkbutton(frame, text="Macarrão", variable=var_macarrao).pack(anchor='w')

# Tempo
ttk.Label(frame, text="Escolha o tempo:").pack(anchor='w', pady=(15,5))
tempo = tk.StringVar()
ttk.Radiobutton(frame, text="Curto (15-30 min)", variable=tempo, value="Curto").pack(anchor='w')
ttk.Radiobutton(frame, text="Médio (30min - 1h30min)", variable=tempo, value="Médio").pack(anchor='w')
ttk.Radiobutton(frame, text="Muito (+1h30min)", variable=tempo, value="Muito").pack(anchor='w')

# Frame de resultados
resultado_frame = ttk.Frame(frame)
resultado_frame.pack(pady=10, fill='x')

def atualizar_janela():
    resultado_frame.update_idletasks()
    janela.geometry("") 

# -------------------------------
# Mostrar seleção e abrir links
# -------------------------------
def mostrar_selecao():
    for widget in resultado_frame.winfo_children():
        widget.destroy()

    ingr = {
        "frango": var_frango.get(),
        "carne": var_carne.get(),
        "macarrao": var_macarrao.get()
    }

    tempo_dict = {"pouco": False, "medio": False, "muito": False}
    if tempo.get() == "Curto":
        tempo_dict["pouco"] = True
    elif tempo.get() == "Médio":
        tempo_dict["medio"] = True
    elif tempo.get() == "Muito":
        tempo_dict["muito"] = True

    engine = Sugestao()
    engine.reset()
    engine.declare(Tempo(**tempo_dict))
    engine.declare(Ingrediente(**ingr))
    engine.resultados = []
    engine.run()

    if engine.resultados:
        ttk.Label(resultado_frame, text="Sugestões de refeição:", font=('Arial', 11, 'bold')).pack(anchor='w')
        for receita in engine.resultados:
            url = links_receitas.get(receita, "#")
        
            if url == "#":
                ttk.Label(resultado_frame, text=receita, font=("Arial", 11)).pack(anchor='w')
            else:
                link = tk.Label(resultado_frame, text=receita, fg="blue", cursor="hand2", 
                font=("Arial", 11, "underline"), bg=WHITE_SMOKE)
                link.pack(anchor='w')
                link.bind("<Button-1>", lambda e, u=url: abrir_link(u))
    else:
        ttk.Label(resultado_frame, text="Nenhuma sugestão encontrada.").pack(anchor='w')

    atualizar_janela()

ttk.Button(frame, text="Verificar seleção", command=mostrar_selecao).pack(pady=15)

janela.mainloop()