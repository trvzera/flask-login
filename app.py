from flask import Flask, request, render_template_string

app = Flask(__name__)

logins = {
  "dolga": "cotemig123",
  "janaina": "python321",
  "antonio": "monitor456",
  "giovanni": "1011"
}

def mostrarTela():
  return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="user" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
        """)
  
def validarUser():
  user = request.form.get('user')
  for usuario in logins.keys():
    if user == usuario:
      return validarSenha(user)
    else:
      continue
  return "<h1>Usuário não encontrado</h1>"
      
def validarSenha(user):
  senha = request.form.get('senha')
  if senha == logins[user]:
    return f"<h1>Bem-vindo, {user}!</h1>"
  else: 
    return "<h1>Senha inválida!</h1>"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return validarUser()
    else:
        return mostrarTela()

if __name__ == "__main__":
    app.run(debug=True)