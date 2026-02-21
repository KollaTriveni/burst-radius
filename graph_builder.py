import networkx as nx

class GraphBuilder:
    def __init__(self, functions, calls):
        self.graph = nx.DiGraph()
        self.functions = functions
        self.calls = calls

    def build(self):
        # Add nodes
        for func in self.functions:
            self.graph.add_node(func, type="function")

        # Add edges
        for caller, callee in self.calls:
            if callee in self.functions:
                self.graph.add_edge(caller, callee, type="calls")

        return self.graph