import pytest
from src.notificador.logic import NotificadorEmail, NotificadorSMS, difundir_alerta

def test_difundir_alerta_exito():
    """Prueba que el conteo de éxitos sea correcto."""
    servicios = [
        NotificadorEmail("profe@u.edu.co"),
        NotificadorSMS("3001234567")
    ]
    resultado = difundir_alerta("Clase de Código Limpio", servicios)
    assert resultado == 2

def test_notificador_email_invalido():
    """Prueba el fallo de validación de un email."""
    email_fail = NotificadorEmail("correo_sin_arroba")
    assert email_fail.enviar("test") is False

def test_notificador_sms_invalido():
    """Prueba el fallo de validación de un número (no numérico)."""
    sms_fail = NotificadorSMS("ABC123")
    assert sms_fail.enviar("test") is False