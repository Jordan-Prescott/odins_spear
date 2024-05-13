class call_flow:
    def __init__(
            self, name, nodes: list) -> None:
        """Usually a call flow to a number and how calls to this number flows through the system.

        :param name: Flow name.
        :param nodes: List of the nodes that make up the flow.
        """

        self.name = name
        self.nodes = nodes