import pytest
from modelo_base import CajaAhorro, CuentaCorriente

def test_deposito_caja_ahorro():
    cuenta = CajaAhorro("001", "Ana Carod", 1000.0)
    cuenta.depositar(500.0)
    assert cuenta.get_saldo() == 1500.0

def test_retiro_exitoso():
    cuenta = CajaAhorro ("001", "Ana Carod", 1000.0)
    cuenta.retirar(400.0)
    assert cuenta.get_saldo() == 600.0

def test_retiro_con_error():
    cuenta = CajaAhorro("001", "Ana Carod", 500.0)
    with pytest.raises(ValueError):
        cuenta.retirar(1000.0)