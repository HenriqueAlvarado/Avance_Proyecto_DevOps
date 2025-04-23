import os
import subprocess

def run(cmd):
    print(f"Ejecutando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def instalar_dependencias():
    run("sudo apt update")
    run("sudo apt install -y python3-pip")
    run("pip3 install flask boto3")

def crear_app_flask():
    app_code = '''
from flask import Flask, render_template_string, request, redirect
import boto3

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla_usuarios = dynamodb.Table('usuarios')

# Templates HTML
login_html = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh;">
    <div>
        <h2>Iniciar Sesión</h2>
        <form method="post" action="/login">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Entrar">
        </form>
        <br>
        <h2>Registrar</h2>
        <form method="post" action="/register">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Registrar">
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(login_html)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = tabla_usuarios.get_item(Key={'username': username})
    user = response.get('Item')

    if user and user['password'] == password:
        return f"<h1 style='text-align:center;margin-top:20%'>Bienvenido a Sellphones, {username}!</h1>"
    else:
        return "<h3>Credenciales incorrectas</h3><a href='/'>Volver</a>"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    try:
        tabla_usuarios.put_item(Item={'username': username, 'password': password})
        return "<h3>Usuario registrado correctamente</h3><a href='/'>Volver al login</a>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
'''
    os.makedirs("/home/ubuntu/app", exist_ok=True)
    with open("/home/ubuntu/app/app.py", "w") as f:
        f.write(app_code)
    run("sudo nohup python3 /home/ubuntu/app/app.py &")

if __name__ == "__main__":
    instalar_dependencias()
    crear_app_flask()
    