import streamlit as st
import pandas as pd
from actividad_loader import obtener_actividades
from empresas_loader import obtener_empresas
from utils.visualizaciones import mostrar_dashboard_financiero
from utils.login import login_form
from utils.macroeconomia import mostrar_macro
from utils.aduanas import mostrar_importaciones
from utils.sercop import mostrar_contratacion_publica

st.set_page_config(page_title="Business360", layout="wide")

if not login_form():
    st.stop()

st.title("📊 Business360 - Inteligencia de Negocio 360°")

# Filtros
st.sidebar.header("🔎 Filtros")
actividades = obtener_actividades()
actividad = st.sidebar.selectbox("Actividad económica", [a["descripcion"] for a in actividades])

empresas = obtener_empresas()
empresas_filtradas = [e for e in empresas if actividad in e["razon_social"]]
empresa = st.sidebar.selectbox("Empresa", [e["razon_social"] for e in empresas_filtradas])

st.markdown("## 🧾 Información General")
st.write(f"**Actividad:** {actividad}")
st.write(f"**Empresa:** {empresa}")

st.markdown("## 💰 Análisis Financiero")
mostrar_dashboard_financiero()

st.markdown("## 📦 Importaciones Aduaneras")
mostrar_importaciones()

st.markdown("## 🏛️ Contratación Pública")
mostrar_contratacion_publica()

st.markdown("## 🌐 Indicadores Macroeconómicos")
mostrar_macro()
