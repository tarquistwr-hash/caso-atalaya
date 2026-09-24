from project import clasificacion, es_grave, esta_cubierto, dominios_cubiertos, tiene_convergencia, diagnostico
from datetime import datetime


def test_clasificacion():
    assert clasificacion(4, 3, 3, 2, 4) == "Crítico"
    assert clasificacion(2, 1, 1, 1, 4) == "Alto"
    assert clasificacion(1, 1, 1, 1, 1) == "Bajo"
    assert clasificacion(2, 2, 2, 2, 2) == "Moderado"


def test_es_grave():
    assert es_grave("Crítico")
    assert es_grave("Alto")
    assert not es_grave("Bajo")
    assert not es_grave("Moderado")


def test_esta_cubierto():
    hoy = datetime(2026, 7, 31)
    assert not esta_cubierto("IMPLEMENTADO", "EV-2026-001", "15/01/2026", 90, hoy)
    assert not esta_cubierto("PLANIFICADO", "EV-2026-001", "15/07/2026", 90, hoy)
    assert not esta_cubierto("IMPLEMENTADO", "EV-2026-001", "", 90, hoy)
    assert not esta_cubierto("IMPLEMENTADO", "", "15/07/2026", 90, hoy)
    assert esta_cubierto("IMPLEMENTADO", "EV-2026-001", "02/05/2026", 90, hoy)
    assert esta_cubierto("IMPLEMENTADO", "EV-2026-001", "15/07/2026", 90, hoy)


def test_tiene_convergencia():
    hoy = datetime(2026, 7, 31)
    control_fisico = {"dominio": "FISICO", "estado": "IMPLEMENTADO", "evidencia": "EV-1", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    control_digital = {"dominio": "DIGITAL", "estado": "IMPLEMENTADO", "evidencia": "EV-2", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    control_digital_caducado = {"dominio": "DIGITAL", "estado": "IMPLEMENTADO", "evidencia": "EV-2", "fecha_ultima_verificacion": "15/01/2026", "periodicidad_dias": 90}
    control_organizativo = {"dominio": "ORGANIZATIVO", "estado": "IMPLEMENTADO", "evidencia": "EV-1", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    assert tiene_convergencia([control_fisico, control_digital], hoy)
    assert not tiene_convergencia([control_fisico], hoy)
    assert not tiene_convergencia([control_fisico, control_digital_caducado], hoy)
    assert not tiene_convergencia([control_fisico, control_organizativo], hoy)


def test_verificacion_no_admite_futuro_ni_evidencia_en_blanco():
    hoy = datetime(2026, 7, 31)
    assert not esta_cubierto("IMPLEMENTADO", "EV-1", "01/08/2026", 90, hoy)
    assert not esta_cubierto("IMPLEMENTADO", " \t ", "31/07/2026", 90, hoy)
    assert not esta_cubierto("IMPLEMENTADO", "EV-1", "31/07/2026", -1, hoy)
    assert esta_cubierto("IMPLEMENTADO", "EV-1", "31/07/2026", 0, hoy)
    assert not esta_cubierto("IMPLEMENTADO", "EV-1", "30/07/2026", 0, hoy)


def test_verificacion_vence_al_dia_siguiente_del_plazo():
    assert esta_cubierto("IMPLEMENTADO", "EV-1", "02/05/2026", 90, datetime(2026, 7, 31))
    assert not esta_cubierto("IMPLEMENTADO", "EV-1", "02/05/2026", 90, datetime(2026, 8, 1))


def test_diagnostico():
    hoy = datetime(2026, 7, 31)
    control_fisico = {"dominio": "FISICO", "estado": "IMPLEMENTADO", "evidencia": "EV-1", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    control_digital = {"dominio": "DIGITAL", "estado": "IMPLEMENTADO", "evidencia": "EV-2", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    assert diagnostico([control_fisico, control_digital], hoy) == "Cobertura convergente"
    assert diagnostico([control_digital], hoy) == "Falta cobertura física"
    assert diagnostico([control_fisico], hoy) == "Falta cobertura digital"
    assert diagnostico([], hoy) == "Sin cobertura"


def test_dominios_cubiertos():
    hoy = datetime(2026, 7, 31)
    control_fisico = {"dominio": "FISICO", "estado": "IMPLEMENTADO", "evidencia": "EV-1", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    control_organizativo = {"dominio": "ORGANIZATIVO", "estado": "IMPLEMENTADO", "evidencia": "EV-3", "fecha_ultima_verificacion": "15/07/2026", "periodicidad_dias": 90}
    assert dominios_cubiertos([control_fisico], hoy) == (True, False)
    assert dominios_cubiertos([control_organizativo], hoy) == (False, False)
    assert dominios_cubiertos([], hoy) == (False, False)
