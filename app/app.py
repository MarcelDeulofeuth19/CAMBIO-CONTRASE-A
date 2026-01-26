from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'cambio_contraseña_secret_key'

API_URL = "http://98.91.0.246:3000/reports/journey-notification"  # Endpoint base

@app.route('/', methods=['GET', 'POST'])
def change_password():
    message = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            payload = {
                "variable1": email,
                "variable2": "2"
            }
            try:
                response = requests.post(API_URL, json=payload, timeout=10)
                # Mostrar respuesta y status para depuración
                print(f"[DEBUG] URL: {API_URL}")
                print(f"[DEBUG] Payload: {payload}")
                print(f"[DEBUG] Status code: {response.status_code}")
                print(f"[DEBUG] Response text: {response.text}")
                if response.status_code == 200:
                    try:
                        data = response.json()
                        if data.get('status') == 'error':
                            message = "No se pudo enviar el correo. Por favor valida que el correo sea correcto y esté registrado."
                        else:
                            # Si el mensaje es de éxito, mostrarlo, si no, pedir validar correo
                            msg = data.get('message', '').lower()
                            if 'exitosamente' in msg or 'enviado' in msg:
                                message = data.get('message', 'Se ha enviado el correo para cambio de contraseña.')
                            else:
                                message = "No se pudo enviar el correo. Por favor valida que el correo sea correcto y esté registrado."
                    except Exception:
                        message = 'Se ha enviado el correo para cambio de contraseña.'
                else:
                    message = "No se pudo enviar el correo. Por favor valida que el correo sea correcto y esté registrado."
            except Exception as e:
                message = f'Error de conexión o formato: {str(e)}'
        else:
            message = 'Por favor ingresa tu correo.'
        session['message'] = message
        return redirect(url_for('change_password'))
    # GET
    if 'message' in session:
        message = session.pop('message')
        show_message = True
    else:
        message = None
        show_message = False
    return render_template('index.html', message=message, show_message=show_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
