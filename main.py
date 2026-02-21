from parser import CodeParser
from graph_builder import GraphBuilder
from change_analyzer import ChangeAnalyzer
from report_generator import generate_report

def main():
    parser = CodeParser("sample_code")
    functions, calls = parser.parse()

    graph_builder = GraphBuilder(functions, calls)
    graph = graph_builder.build()

    change = {
        "change_type": "MODIFY_FUNCTION",
        "target": "validate_user"
    }

    analyzer = ChangeAnalyzer(graph)
    direct, indirect = analyzer.analyze(change["target"])

    report = generate_report(change["target"], direct, indirect)

    print("\n===== BLAST RADIUS REPORT =====")
    print(report)

if __name__ == "__main__":
    main()