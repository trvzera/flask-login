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
        <style>
  * {
    padding: 0px;
    margin: 0px;
    box-sizing: border-box;
    transition: 0.3s ease-in-out;
  }

  section {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #1c1c1e;
  }

  div {
    font-family: Arial, Helvetica, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: max-content;
    height: max-content;
    background-color: #dfdfdf;
    padding: 20px 60px;
    border-radius: 15px;
    border: 3px solid #fff;
    box-shadow: inset 3px 3px 7px rgba(0, 0, 0, 0.3), inset 3px 3px 7px rgba(255, 255, 255, 1);
  }

  h1 {
    font-size: 3rem;
    color: #1c1c1e;
    margin-bottom: 40px;
  }

  form {
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  input {
    height: 40px;
    width: 250px;
    border-radius: 6px;
    outline: none;
    border: 2px solid #bababe;
    padding: 5px 10px;
    background-color: #dfdfdf;
  }

  input::placeholder {
    color: #bababe;
    font-size: 0.8rem;
    font-weight: 500;
    transition: 0.3s ease-in-out;
  }

  input:focus {
    border: 2px solid #2f67ff;
    box-shadow: 0 0 10px rgba(0, 38, 255, 0.432);
  }

  input:focus::placeholder {
    color: #2f67ff;
    font-size: 0.8rem;
    font-weight: 500;
  }

  input:not(:placeholder-shown) {
    border: 2px solid #2f67ff;
  }

  button {
    width: 100%;
    height: 40px;
    border-radius: 10px;
    outline: none;
    border: 1px solid #fff;
    background: linear-gradient(to right, #2f67ff, #0071e3);
    cursor: pointer;
    transition: 0.3s ease-in-out;
    font-size: 1rem;
    font-weight: 500;
    color: #fff;
  }

  button:hover {
    background: linear-gradient(to right, #2f67ff, #0071e3);
    color: #fff;
    transform: scale(1.02);
    box-shadow: 0 10px 20px rgba(0, 38, 255, 0.432);
  }

  button:active {
    transform: scale(0.98);
    background: linear-gradient(to right, #2f67ff, #0071e3);
    color: #fff;
  }
</style>

<body>
  <section>
    <div>
      <h1>Login</h1>
      <form method="POST">
        <input type="text" name="user" placeholder="Usuário"><br><br>
        <input type="password" name="senha" placeholder="Senha"><br><br>
        <button type="submit">Entrar</button>
      </form>
    </div>
  </section>
</body>
        """)
  
def validarUser():
  user = request.form.get('user')
  for usuario in logins.keys():
    if user == usuario:
      return validarSenha(user)
    else:
      continue
  return """<style>
 * {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  transition: 0.3s ease-in-out;
  font-family: Arial, Helvetica, sans-serif;
 }
 section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1c1c1e;
 }
 h1 {
  font-size: 3rem;
  color: #ad0000;
  background-color: #e5e5ea;
  padding: 20px 60px;
  border-radius: 15px;
  border:3px solid #fff;
  box-shadow:inset 3px 3px 7px rgba(0, 0, 0, 0.3), inset 3px 3px 7px rgba(255, 255, 255, 1);
 }
</style>

<body>
  <section>
    <h1>Usuário não encontrado!</h1>
  </section>
</body>"""
      
def validarSenha(user):
  senha = request.form.get('senha')
  if senha == logins[user]:
    return f"<h1>Bem-vindo, {user}!</h1>"
  else: 
    return """<style>
 * {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  transition: 0.3s ease-in-out;
  font-family: Arial, Helvetica, sans-serif;
 }
 section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1c1c1e;
 }
 h1 {
  font-size: 3rem;
  color: #ad0000;
  background-color: #e5e5ea;
  padding: 20px 60px;
  border-radius: 15px;
  border:3px solid #fff;
  box-shadow:inset 3px 3px 7px rgba(0, 0, 0, 0.3), inset 3px 3px 7px rgba(255, 255, 255, 1);
 }
</style>

<body>
  <section>
    <h1>Senha inválida!</h1>
  </section>
</body>
"""


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return validarUser()
    else:
        return mostrarTela()

if __name__ == "__main__":
    app.run(debug=True)