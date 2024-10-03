from tkinter import*
import services
def main():
    nome = nomeEntry.get()
    email = emailEntry.get()
    senha = senhaEntry.get()
    services.enviar_dados(nome, email, senha)

    nomeEntry.delete(0,END)
    emailEntry.delete(0,END)
    senhaEntry.delete(0,END)

def deletar_user(email):
    email = emailEntry
    services.recover_usuario(email)

    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de gerenciamento de usuario')


    titulo = Label(janela, text='CRUD', font=(' Arial black', 20))
    titulo.pack()


    nome = Label(janela, text="Nome:")
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, Width=20 )
    nomeEntry.place(x=50, y=100)

    email = Label(janela, text="Email" )
    email.place(x=50, y=130)

    global emailEntry
    emailEntry = Label(janela, Width=20 )
    emailEntry.place(x=100, y=130)

    senha = Label(janela, text="Senha:")
    senha.place(x=50, y=160)

    global senhaEntry
    senhaEntry = Entry(janela, Width=30, show='*')
    senhaEntry.place(x=100, y=160)

    enviar = Label(janela, text="Cadastrar", Width=10)
    enviar.place(x=100, y=200)

    listar = Button(janela, text='Listar usuario', Width=15)
    listar.place(x=200, y=200)

    remover = Button(janela, text='Remover', width=10 )
    remover.place(x=100, y=150)


    janela.mainloop()

if __name__== '__main__':
    main()