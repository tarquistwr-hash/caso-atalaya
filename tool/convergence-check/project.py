from datetime import datetime
import csv
import sys


def clasificacion(i_personas, i_patrimonio, i_privacidad, i_legal, probabilidad):
    impacto = max(i_personas, i_patrimonio, i_privacidad, i_legal)
    nivel = impacto * probabilidad
    if nivel >= 12:
        return "Crítico"
    elif nivel >= 6:
        return "Alto"
    elif nivel >= 3:
        return "Moderado"
    else:
        return "Bajo"


def es_grave(categoria):
    return categoria in ("Alto", "Crítico")


def esta_cubierto(estado, evidencia, fecha_verificacion, periodicidad_dias, hoy):
    if estado != "IMPLEMENTADO":
        return False
    if not evidencia.strip():
        return False
    if fecha_verificacion == "":
        return False
    resultado_fecha = datetime.strptime(fecha_verificacion, "%d/%m/%Y")
    transcurridos = (hoy - resultado_fecha).days
    return 0 <= transcurridos <= periodicidad_dias


def dominios_cubiertos(controles, hoy):
    fisico_cubierto = False
    digital_cubierto = False
    for control in controles:
        if not esta_cubierto(control["estado"], control["evidencia"], control["fecha_ultima_verificacion"], control["periodicidad_dias"], hoy):
            continue
        if control["dominio"] == "FISICO":
            fisico_cubierto = True
        if control["dominio"] == "DIGITAL":
            digital_cubierto = True
    return fisico_cubierto, digital_cubierto


def tiene_convergencia(controles, hoy):
    fisico_cubierto, digital_cubierto = dominios_cubiertos(controles, hoy)
    return fisico_cubierto and digital_cubierto


def diagnostico(controles, hoy):
    fisico_cubierto, digital_cubierto = dominios_cubiertos(controles, hoy)
    if fisico_cubierto and digital_cubierto:
        return "Cobertura convergente"
    elif fisico_cubierto:
        return "Falta cobertura digital"
    elif digital_cubierto:
        return "Falta cobertura física"
    else:
        return "Sin cobertura"


def main():
    if len(sys.argv) != 4:
        sys.exit("Uso: python project.py riesgos.csv controles.csv DD/MM/AAAA")
    with open(sys.argv[1], encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        riesgos = list(lector)
    with open(sys.argv[2], encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        controles = list(lector)
    hoy = datetime.strptime(sys.argv[3], "%d/%m/%Y")
    for riesgo in riesgos:
        categoria = clasificacion(int(riesgo["i_personas"]), int(riesgo["i_patrimonio"]), int(riesgo["i_privacidad"]), int(riesgo["i_legal"]), int(riesgo["probabilidad"]))
        if not es_grave(categoria):
            continue
        controles_del_riesgo = []
        for control in controles:
            if control["id_riesgo"] == riesgo["codigo"]:
                control["periodicidad_dias"] = int(control["periodicidad_dias"])
                controles_del_riesgo.append(control)
        resultado = diagnostico(controles_del_riesgo, hoy)
        print(riesgo["codigo"], resultado)


if __name__ == "__main__":
    main()
