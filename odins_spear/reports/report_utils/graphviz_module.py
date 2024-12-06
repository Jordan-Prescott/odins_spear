import graphviz

from ...store import broadwork_entities as bre


class GraphvizModule:
    """
    Colours:
    - Black: 020300
    - Orange: FFA400 - Darker: B87700
    - Red: 95190C - Darker: 5E1008
    - Purple: 5B5F97 - Darker: 3D4066
    - Redish: A23E48 - Darker: 68272E
    """

    NODE_STYLING = {
        "start": {
            "shape": "record",
            "style": "filled",
            "margin": "0.2",
            "color": "#020300",
            "fontname": "Arial",
            "fontcolor": "white",
        },
        "exit": {
            "shape": "record",
            "style": "filled",
            "margin": "0.2",
            "color": "#020300",
            "fontname": "Arial",
            "fontcolor": "white",
        },
        "auto_attendant": {
            "shape": "record",
            "style": "filled",
            "margin": "0.2",
            "color": "#1C3A3A",
            "fillcolor": "#356969",
            "fontname": "Arial",
            "fontcolor": "white",
        },
        "call_centre": {
            "shape": "record",
            "style": "filled",
            "margin": "0.2",
            "color": "#CCCCCC",
            "fillcolor": "#D9D9D9",
            "fontname": "Arial",
            "fontcolor": "black",
        },
        "hunt_group": {
            "shape": "record",
            "style": "filled",
            "margin": "0.2",
            "color": "#4773EB",
            "fillcolor": "#5E85ED",
            "fontname": "Arial",
            "fontcolor": "black",
        },
        "user": {
            "shape": "record",
            "style": "filled",
            "margin": "0.2",
            "color": "#CAE188",
            "fillcolor": "#E3FE97",
            "fontname": "Arial",
            "fontcolor": "black",
        },
    }
    EDGE_STYLYING = {"fontname": "Arial"}

    def __init__(self, output_directory: str = None):
        self.dot = graphviz.Digraph()
        self.output_directory = output_directory

    def generate_call_flow_graph(self, nodes: list, number: str):
        self.dot.attr(
            name=f"calls_to_{number}",
            label=number,
            fontname="Arial",
            fontcolor="white",
            rankdir="LR",
        )

        # build nodes
        self.dot.node("Start", "Start", GraphvizModule.NODE_STYLING["start"])
        for n in nodes:
            try:
                node_config = f"<extension> Extension: {n.extension} "
            except AttributeError:
                node_config = ""

            if isinstance(n, bre.User):
                node_config += f"| <name> Name: {n.first_name} {n.last_name}"
                self.dot.node(n.id, node_config, GraphvizModule.NODE_STYLING["user"])

            elif isinstance(n, bre.CallCenter) or isinstance(n, bre.HuntGroup):
                node_config += f"| <name> Name: {n.name} | <policy> Policy: {n.policy}"
                for i, a in enumerate(n.agents):
                    node_config += f"| <{a.id}> Agent {i+1}: {a.extension}"
                self.dot.node(
                    n.service_user_id,
                    node_config,
                    GraphvizModule.NODE_STYLING["call_centre"]
                    if isinstance(n, bre.CallCenter)
                    else GraphvizModule.NODE_STYLING["hunt_group"],
                )

            elif isinstance(n, bre.AutoAttendant):
                node_config += f"| <name> Name: {n.name}"
                for k in n.business_hours_menu.keys:
                    node_config += f"| <key{k.number}> Option {k.number}: {k.action}"
                    k.id = f"{n.service_user_id}:<key{k.number}>"
                self.dot.node(
                    n.service_user_id,
                    node_config,
                    GraphvizModule.NODE_STYLING["auto_attendant"],
                )

        # build edges
        for n in nodes:
            try:
                if n._start_node:
                    try:
                        self.dot.edge("Start", n.id)
                    except Exception:
                        self.dot.edge("Start", n.service_user_id)
            except AttributeError:
                # node is note the start node
                pass

            if isinstance(n, bre.User):
                if n.call_forwarding_always:
                    self._format_edge(n, n.call_forwarding_always, "CFA")
                if n.call_forwarding_busy:
                    self._format_edge(n, n.call_forwarding_busy, "CFB")
                if n.call_forwarding_not_reachable:
                    self._format_edge(n, n.call_forwarding_not_reachable, "CFNR")

            elif isinstance(n, bre.CallCenter):
                if n.bounced_calls_enabled:
                    self._format_edge(
                        n, n.bounced_calls_transfer_to_phone_number, "BCT"
                    )
                if n.overflow_calls_action:
                    self._format_edge(
                        n, n.overflow_calls_transfer_to_phone_number, "OF"
                    )
                if n.stranded_calls_action:
                    self._format_edge(
                        n, n.stranded_calls_transfer_to_phone_number, "SCF"
                    )
                if n.stranded_call_unavailable_action:
                    self._format_edge(
                        n, n.stranded_call_unavailable_transfer_to_phone_number, "USCF"
                    )

            elif isinstance(n, bre.HuntGroup):
                if n.forward_after_timeout_enabled:
                    self._format_edge(n, n.no_answer_forward_to_phone_number, "NACF")
                if n.call_forward_not_reachable_enabled:
                    self._format_edge(
                        n, n.call_forward_not_reachable_transfer_to_phone_number, "CFNR"
                    )

            elif isinstance(n, bre.AutoAttendant):
                for key in n.business_hours_menu.keys:
                    if "Transfer" in key.action:
                        self._format_edge(key, key.phone_number, key.number)

    def _format_edge(self, node_a: str, node_b: str, label: str):
        if node_b is None:
            return None

        node_a_id = node_a.id if hasattr(node_a, "id") else node_a.service_user_id
        node_b_id = node_b.id if hasattr(node_b, "id") else node_b.service_user_id

        self.dot.edge(node_a_id, node_b_id, label, GraphvizModule.EDGE_STYLYING)

    def _save_graph(self, filename: str):
        self.dot.render(
            directory=self.output_directory,
            filename=filename,
            format="svg",
            cleanup=True,
        ).replace("\\", "/")
