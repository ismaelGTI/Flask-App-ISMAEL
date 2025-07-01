def test_contacto_post_valido(tmp_path, monkeypatch):
    # Usar un archivo temporal para no modificar mensajes.txt real
    test_file = tmp_path / "mensajes.txt"
    import builtins
    real_open = builtins.open
    def fake_open(f, m='r', *args, **kwargs):
        if f == "mensajes.txt":
            return real_open(test_file, m, *args, **kwargs)
        return real_open(f, m, *args, **kwargs)
    monkeypatch.setattr(builtins, "open", fake_open)
    tester = app.test_client()
    data = dict(nombre='Test User', email='test@example.com', mensaje='Mensaje de prueba')
    response = tester.post('/contacto', data=data, follow_redirects=True)
    assert b'Mensaje enviado correctamente!' in response.data
    # Verifica que el mensaje se guardó en el archivo temporal
    contenido = test_file.read_text(encoding='utf-8')
    assert 'Test User' in contenido
    assert 'test@example.com' in contenido
    assert 'Mensaje de prueba' in contenido
import pytest
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Bienvenido' in response.data

def test_about():
    tester = app.test_client()
    response = tester.get('/about')
    assert response.status_code == 200
    assert b'Sobre' in response.data

def test_contacto_get():
    tester = app.test_client()
    response = tester.get('/contacto')
    assert response.status_code == 200
    assert b'Contacto' in response.data

def test_contacto_post_incompleto():
    tester = app.test_client()
    response = tester.post('/contacto', data=dict(nombre='', email='', mensaje=''), follow_redirects=True)
    assert b'Por favor, completa todos los campos.' in response.data

def test_sorpresa():
    tester = app.test_client()
    response = tester.get('/sorpresa')
    assert response.status_code == 200
    assert b'Sorpresa' in response.data
