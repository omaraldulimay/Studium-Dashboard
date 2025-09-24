import streamlit as st
import pandas as pd
from services.storage import load_student, save_student
from models.module import Module

st.set_page_config(page_title="Studienfortschritt", page_icon="📊", layout="wide")
st.title("📊 Studienfortschritt Dashboard")

student = load_student()

# --- KPIs ---
kpi1, kpi2 = st.columns(2)
kpi1.metric("ECTS erreicht", student.ects_total)
kpi2.metric("Durchschnittsnote", student.average_grade)

# --- Sidebar: Filter + Neues Modul ---
st.sidebar.header("Aktionen")
status_filter = st.sidebar.selectbox("Status filtern", ["Alle", "Bestanden", "Offen"])

with st.sidebar.form("add_module"):
    st.subheader("Neues Modul hinzufügen")
    name = st.text_input("Name")
    ects = st.number_input("ECTS", min_value=1, max_value=30, step=1, value=5)
    grade_str = st.text_input("Note (leer lassen = offen)", value="")
    submitted = st.form_submit_button("Hinzufügen")
    if submitted:
        grade = float(grade_str.replace(",", ".")) if grade_str.strip() else None
        student.modules.append(Module(name=name, ects=int(ects), grade=grade))
        save_student(student)
        st.success(f"Modul '{name}' hinzugefügt.")
        st.rerun()

# --- Tabelle + Inline-Edit für Noten ---
data = [{"Name": m.name, "ECTS": m.ects, "Note": m.grade, "Bestanden": m.passed} for m in student.modules]
df = pd.DataFrame(data)

if status_filter == "Bestanden":
    df = df[df["Bestanden"] == True]
elif status_filter == "Offen":
    df = df[df["Bestanden"] == False]

st.subheader("Module")
edited = st.data_editor(
    df,
    num_rows="dynamic",
    column_config={
        "Bestanden": st.column_config.CheckboxColumn(disabled=True),
        "Note": st.column_config.NumberColumn(format="%.1f"),
    },
    use_container_width=True,
    key="editor"
)

# Änderungen übernehmen
if st.button("Änderungen speichern"):
    # Map von Name -> (ECTS, Note) zurück ins Domain-Modell
    name_to_row = {row["Name"]: row for _, row in edited.iterrows()}
    for m in student.modules:
        row = name_to_row.get(m.name)
        if row is not None:
            m.ects = int(row["ECTS"])
            # leere Note bleibt None
            m.grade = float(row["Note"]) if pd.notna(row["Note"]) else None
    save_student(student)
    st.success("Gespeichert.")
    st.rerun()

# --- Charts ---
st.subheader("ECTS je Modul")
if not edited.empty:
    st.bar_chart(edited.set_index("Name")["ECTS"])

# --- Export ---
st.download_button(
    "📥 Export als CSV",
    data=edited.to_csv(index=False).encode("utf-8"),
    file_name="studium_module.csv",
    mime="text/csv",
)
