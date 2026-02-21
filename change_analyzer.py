class ChangeAnalyzer:
    def __init__(self, graph):
        self.graph = graph

    def analyze(self, target):
        direct = []
        indirect = []

        # Direct: functions that call target
        for node in self.graph.nodes:
            if self.graph.has_edge(node, target):
                direct.append(node)

        # Indirect: callers of direct
        for d in direct:
            for node in self.graph.nodes:
                if self.graph.has_edge(node, d):
                    indirect.append(node)

        return list(set(direct)), list(set(indirect))