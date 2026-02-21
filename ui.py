import streamlit as st
from parser import CodeParser
from graph_builder import GraphBuilder
from change_analyzer import ChangeAnalyzer
from report_generator import generate_report

st.set_page_config(page_title="Impact Trace", layout="wide")

st.title("🚀 Impact Trace – Blast Radius Analyzer")

# Input Section
st.header("🔍 Change Intent")

change_type = st.selectbox(
    "Select Change Type",
    ["MODIFY_FUNCTION", "API_CHANGE", "LOGIC_CHANGE"]
)

target = st.text_input("Enter Target Function Name")

if st.button("Analyze Blast Radius"):

    parser = CodeParser("sample_code")
    functions, calls = parser.parse()

    graph_builder = GraphBuilder(functions, calls)
    graph = graph_builder.build()

    analyzer = ChangeAnalyzer(graph)
    direct, indirect = analyzer.analyze(target)

    report = generate_report(target, direct, indirect)

    st.header("📊 Blast Radius Report")

    st.write("### Changed Component")
    st.write(report["changed_component"])

    st.write("### Direct Impacts")
    st.write(report["direct_impacts"])

    st.write("### Indirect Impacts")
    st.write(report["indirect_impacts"])

    st.write("### Risk Level")
    st.write(report["risk_level"])