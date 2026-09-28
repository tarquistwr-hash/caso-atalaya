from datetime import datetime
from pathlib import Path
import csv
import json
import pytest
from project import (clasificacion, es_grave, esta_cubierto, dominios_cubiertos,
                     tiene_convergencia, diagnostico, cargar, evaluar, main, motivo_control)
from check_corpus import ejecutar
import check_corpus

HERE=Path(__file__).resolve().parent
HOY=datetime(2026,7,31)


def control(dominio="DIGITAL",**cambios):
    c={"id_control":"C-001","dominio":dominio,"estado":"IMPLEMENTADO","evidencia":"EV-1",
       "fecha_ultima_verificacion":"15/07/2026","periodicidad_dias":90,"alcance_cobertura":"GENERAL","condicion":""}
    return c | cambios


@pytest.mark.parametrize("impacto,prob,categoria",[(1,1,"Bajo"),(1,2,"Bajo"),(1,3,"Moderado"),(2,2,"Moderado"),(2,3,"Alto"),(3,3,"Alto"),(3,4,"Crítico"),(4,4,"Crítico")])
def test_umbral_riesgo(impacto,prob,categoria):
    assert clasificacion(1,impacto,1,1,prob)==categoria
    assert es_grave(categoria)==(categoria in {"Alto","Crítico"})


@pytest.mark.parametrize("mal",[0,5,-1,1.5,True])
def test_escala_invalida(mal):
    with pytest.raises(ValueError):clasificacion(mal,1,1,1,1)


@pytest.mark.parametrize("estado,evidencia,fecha,esperado",[
    ("IMPLEMENTADO","EV","02/05/2026",True),("IMPLEMENTADO","EV","01/05/2026",False),
    ("IMPLEMENTADO","EV","01/08/2026",False),("IMPLEMENTADO"," \t ","15/07/2026",False),
    ("IMPLEMENTADO","EV","",False),("PARCIAL","EV","15/07/2026",False)])
def test_vigencia(estado,evidencia,fecha,esperado):
    assert esta_cubierto(estado,evidencia,fecha,90,HOY)==esperado


@pytest.mark.parametrize("dominios,controles,esperado",[
    ("Digital",[control()],"Cumple"),("Fisico",[control("FISICO")],"Cumple"),
    ("Ambos",[control()],"Falta cobertura física"),("Ambos",[control("FISICO")],"Falta cobertura digital"),
    ("Ambos",[control(),control("FISICO")],"Cumple"),
    ("Pendiente",[control(),control("FISICO")],"Evaluación pendiente"),
    ("Ambos",[control("ORGANIZATIVO")],"Sin cobertura"),
    ("Digital",[],"Falta cobertura digital")])
def test_dominios_aplicables(dominios,controles,esperado):
    assert diagnostico(controles,HOY,dominios).startswith(esperado)
    assert tiene_convergencia(controles,HOY,dominios)==(esperado=="Cumple")


@pytest.mark.parametrize("alcance",["CONDICIONADO","PENDIENTE"])
def test_alcance_no_se_convierte_en_cobertura_general(alcance):
    c=control(alcance_cobertura=alcance,condicion="Solo órdenes desde 50.000 euros")
    assert dominios_cubiertos([c],HOY)==(False,False)
    assert diagnostico([c],HOY,"Digital")=="Falta cobertura digital"


def test_motivos_distintos():
    assert motivo_control(control(evidencia=""),HOY)=="sin evidencia"
    assert motivo_control(control(fecha_ultima_verificacion="01/01/2026"),HOY)=="verificación vencida"
    assert motivo_control(control(estado="PLANIFICADO"),HOY)=="implantación pendiente"
    assert "no suma cobertura" in motivo_control(control("ORGANIZATIVO"),HOY)


def test_ejemplos_publicados_coinciden_con_ejecucion(capsys):
    for controles,corte,ejemplo in [("controles.csv","24/07/2026","ejemplo_corte.txt"),
                                    ("controles_junio.csv","30/06/2027","ejemplo_demo.txt")]:
        assert main([str(HERE/'riesgos.csv'),str(HERE/controles),corte])==0
        salida=capsys.readouterr().out
        assert salida==(HERE/ejemplo).read_text(encoding='utf-8')
        if ejemplo=='ejemplo_demo.txt':
            assert salida in (HERE.parents[1]/'README.md').read_text(encoding='utf-8')


def test_resultados_del_corpus():
    riesgos,controles=cargar(HERE/"riesgos.csv",HERE/"controles_junio.csv")
    salidas={r['codigo']:r['diagnostico'] for r in evaluar(riesgos,controles,datetime(2027,6,30))}
    faltas={"RSC-004":"Falta cobertura física","RSC-006":"Falta cobertura digital",
            "RSC-010":"Falta cobertura digital","RSC-014":"Evaluación pendiente de dominios",
            "RSC-016":"Falta cobertura digital","RSC-018":"Sin cobertura en los dominios aplicables",
            "RSC-020":"Falta cobertura digital","RSC-022":"Falta cobertura física"}
    esperados={f"RSC-{i:03}":faltas.get(f"RSC-{i:03}","Cumple cobertura de los dominios aplicables") for i in range(1,26) if i!=17}
    assert salidas==esperados
    riesgos,controles=cargar(HERE/"riesgos.csv",HERE/"controles.csv")
    resultados=evaluar(riesgos,controles,datetime(2026,7,24))
    assert len(resultados)==24 and not any(r['diagnostico'].startswith('Cumple') for r in resultados)


def test_coherencia_excel_csv_soa():
    resultado=ejecutar()
    assert (resultado['riesgos'],resultado['controles'],resultado['soa'])==(25,64,93)
    assert len(resultado['excepciones'])==2


def test_rechaza_resumen_soa_incorrecto(monkeypatch):
    _,controles=check_corpus.extraer()
    wb=check_corpus.openpyxl.load_workbook(check_corpus.SOA,data_only=True)
    wb['Resumen']['B11']=0
    monkeypatch.setattr(check_corpus.openpyxl,'load_workbook',lambda *args,**kwargs:wb)
    with pytest.raises(ValueError,match='Resumen B11'):
        check_corpus.comprobar_soa(controles)


@pytest.fixture
def csv_temporales(tmp_path):
    for nombre in ['riesgos.csv','controles.csv']:
        (tmp_path/nombre).write_bytes((HERE/nombre).read_bytes())
    return tmp_path


@pytest.mark.parametrize("campo,valor",[("dominio","FÍSICO"),("estado","implementado"),("id_riesgo","RSC-999"),
    ("periodicidad_dias","-1"),("periodicidad_dias","0"),("fecha_ultima_verificacion","31/02/2026"),
    ("fecha_ultima_verificacion","1/7/2026"),("alcance_cobertura","")])
def test_rechaza_datos_invalidos(csv_temporales,campo,valor):
    p=csv_temporales/'controles.csv'
    with p.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    rows[0][campo]=valor
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=rows[0].keys());wr.writeheader();wr.writerows(rows)
    with pytest.raises(ValueError):cargar(csv_temporales/'riesgos.csv',p)


def test_rechaza_duplicados_y_columnas_ausentes(csv_temporales):
    p=csv_temporales/'controles.csv';text=p.read_text(encoding='utf-8')
    p.write_text(text+text.splitlines()[1]+'\n',encoding='utf-8')
    with pytest.raises(ValueError,match='duplicado'):cargar(csv_temporales/'riesgos.csv',p)
    p.write_text('id_control\nC-001\n',encoding='utf-8')
    with pytest.raises(ValueError,match='columnas'):cargar(csv_temporales/'riesgos.csv',p)


def test_cli_json_y_codigos(capsys):
    args=[str(HERE/'riesgos.csv'),str(HERE/'controles.csv'),'24/07/2026']
    assert main(args+['--json'])==0
    assert len(json.loads(capsys.readouterr().out))==24
    assert main(args+['--exigir-cobertura'])==1
    capsys.readouterr()
    assert main(['no-existe.csv',args[1],args[2]])==2
    assert 'Error de entrada' in capsys.readouterr().err
