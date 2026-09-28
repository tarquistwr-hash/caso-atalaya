"""Cobertura por dominios aplicables; no acredita aceptación del riesgo residual."""
from datetime import datetime
import argparse
import csv
import json
import re
import sys

APLICABLES = {"Fisico": {"FISICO"}, "Digital": {"DIGITAL"}, "Ambos": {"FISICO", "DIGITAL"}, "Pendiente": None}
ESTADOS = {"PLANIFICADO", "PARCIAL", "IMPLEMENTADO"}
ESCALAS = ("i_personas", "i_patrimonio", "i_privacidad", "i_legal", "probabilidad")
RIESGO_CAMPOS = {"codigo", "titulo", "dominios", "justificacion_dominios", "propietario", *ESCALAS}
CONTROL_CAMPOS = {"id_control", "id_riesgo", "descripcion", "dominio", "estado", "evidencia", "periodicidad_dias", "fecha_ultima_verificacion", "alcance_cobertura", "condicion"}


def clasificacion(i_personas, i_patrimonio, i_privacidad, i_legal, probabilidad):
    valores = (i_personas, i_patrimonio, i_privacidad, i_legal, probabilidad)
    if any(type(v) is not int or not 1 <= v <= 4 for v in valores):
        raise ValueError("Impactos y probabilidad deben ser enteros entre 1 y 4")
    nivel = max(valores[:4]) * probabilidad
    return "Crítico" if nivel >= 12 else "Alto" if nivel >= 6 else "Moderado" if nivel >= 3 else "Bajo"


def es_grave(categoria):
    return categoria in ("Alto", "Crítico")


def fecha(texto):
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", texto):
        raise ValueError(f"Fecha no válida: {texto!r}; use DD/MM/AAAA")
    return datetime.strptime(texto, "%d/%m/%Y")


def esta_cubierto(estado, evidencia, fecha_verificacion, periodicidad_dias, hoy):
    if estado != "IMPLEMENTADO" or not evidencia.strip() or not fecha_verificacion:
        return False
    return 0 <= (hoy - fecha(fecha_verificacion)).days <= periodicidad_dias


def motivo_control(c, hoy):
    if c["alcance_cobertura"] == "PENDIENTE":
        return "justificación de cobertura pendiente"
    if c["estado"] != "IMPLEMENTADO":
        return "implantación pendiente"
    if not c["evidencia"].strip():
        return "sin evidencia"
    if not c["fecha_ultima_verificacion"]:
        return "sin verificación"
    edad = (hoy - fecha(c["fecha_ultima_verificacion"])).days
    if edad < 0:
        return "verificación posterior al corte"
    if edad > c["periodicidad_dias"]:
        return "verificación vencida"
    if c["alcance_cobertura"] == "CONDICIONADO":
        return "cobertura condicionada: " + c["condicion"]
    if c["dominio"] == "ORGANIZATIVO":
        return "medida organizativa verificada según datos; no suma cobertura física o digital"
    return "cobertura acreditada según datos"


def dominios_cubiertos(controles, hoy):
    efectivos = {c["dominio"] for c in controles if c["alcance_cobertura"] == "GENERAL"
                 and esta_cubierto(c["estado"], c["evidencia"], c["fecha_ultima_verificacion"], c["periodicidad_dias"], hoy)}
    return "FISICO" in efectivos, "DIGITAL" in efectivos


def tiene_convergencia(controles, hoy, dominios):
    return diagnostico(controles, hoy, dominios).startswith("Cumple")


def diagnostico(controles, hoy, dominios):
    requeridos = APLICABLES[dominios]
    if requeridos is None:
        return "Evaluación pendiente de dominios"
    fisico, digital = dominios_cubiertos(controles, hoy)
    faltan = requeridos - ({"FISICO"} if fisico else set()) - ({"DIGITAL"} if digital else set())
    if not faltan:
        return "Cumple cobertura de los dominios aplicables"
    if faltan == {"FISICO", "DIGITAL"}:
        return "Sin cobertura en los dominios aplicables"
    return "Falta cobertura física" if "FISICO" in faltan else "Falta cobertura digital"


def leer_csv(ruta, requeridos):
    with open(ruta, encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        cabecera = lector.fieldnames or []
        if len(set(cabecera)) != len(cabecera) or not requeridos <= set(cabecera):
            raise ValueError(f"{ruta}: cabecera duplicada o faltan columnas: {sorted(requeridos-set(cabecera))}")
        filas = list(lector)
    if not filas:
        raise ValueError(f"{ruta}: no contiene registros")
    if any(None in fila or any(v is None for v in fila.values()) for fila in filas):
        raise ValueError(f"{ruta}: fila con número incorrecto de columnas")
    return filas


def cargar(riesgos_path, controles_path):
    riesgos = leer_csv(riesgos_path, RIESGO_CAMPOS)
    controles = leer_csv(controles_path, CONTROL_CAMPOS)
    for filas, clave, patron in [(riesgos, "codigo", r"RSC-\d{3}"), (controles, "id_control", r"C-\d{3}")]:
        ids = [r[clave] for r in filas]
        if len(set(ids)) != len(ids) or any(not re.fullmatch(patron, x) for x in ids):
            raise ValueError(f"Identificador duplicado o no válido en {clave}")
    riesgos_ids = {r["codigo"] for r in riesgos}
    for r in riesgos:
        if r["dominios"] not in APLICABLES or not r["justificacion_dominios"].strip():
            raise ValueError(f"{r['codigo']}: dominios no válidos o sin justificación")
        for k in ESCALAS:
            r[k] = int(r[k])
        clasificacion(*(r[k] for k in ESCALAS))
    for c in controles:
        if c["id_riesgo"] not in riesgos_ids:
            raise ValueError(f"{c['id_control']}: riesgo inexistente {c['id_riesgo']}")
        if c["dominio"] not in {"FISICO", "DIGITAL", "ORGANIZATIVO"} or c["estado"] not in ESTADOS:
            raise ValueError(f"{c['id_control']}: dominio o estado no válido")
        if c["alcance_cobertura"] not in {"GENERAL", "CONDICIONADO", "PENDIENTE"}:
            raise ValueError(f"{c['id_control']}: alcance de cobertura no válido")
        if c["alcance_cobertura"] != "GENERAL" and not c["condicion"].strip():
            raise ValueError(f"{c['id_control']}: falta explicar la condición o pendiente")
        c["periodicidad_dias"] = int(c["periodicidad_dias"])
        if c["periodicidad_dias"] not in {90, 180, 365}:
            raise ValueError(f"{c['id_control']}: periodicidad fuera de DOC-004 (90, 180, 365)")
        if c["fecha_ultima_verificacion"]:
            fecha(c["fecha_ultima_verificacion"])
    return riesgos, controles


def evaluar(riesgos, controles, hoy):
    resultados = []
    for r in riesgos:
        if not es_grave(clasificacion(*(r[k] for k in ESCALAS))):
            continue
        propios = [c for c in controles if c["id_riesgo"] == r["codigo"]]
        resultados.append({"codigo": r["codigo"], "dominios": r["dominios"], "diagnostico": diagnostico(propios, hoy, r["dominios"]),
                           "controles": [{"id": c["id_control"], "dominio": c["dominio"], "motivo": motivo_control(c, hoy), "condicion": c["condicion"]} for c in propios]})
    return resultados


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("riesgos")
    parser.add_argument("controles")
    parser.add_argument("corte", help="DD/MM/AAAA")
    parser.add_argument("--json", action="store_true", help="Salida estructurada con motivos")
    parser.add_argument("--detalle", action="store_true", help="Estado de cada control")
    parser.add_argument("--exigir-cobertura", action="store_true", help="Código 1 si falta cobertura o evaluación")
    args = parser.parse_args(argv)
    try:
        riesgos, controles = cargar(args.riesgos, args.controles)
        resultados = evaluar(riesgos, controles, fecha(args.corte))
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Error de entrada: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            print(r["codigo"], r["diagnostico"])
            if args.detalle:
                if not r["controles"]:
                    print("  Sin controles diseñados")
                for c in r["controles"]:
                    print(f"  {c['id']} ({c['dominio']}): {c['motivo']}")
    return int(args.exigir_cobertura and any(not r["diagnostico"].startswith("Cumple") for r in resultados))


if __name__ == "__main__":
    sys.exit(main())
