import graphviz

from odins_spear.store import broadwork_entities as bre
from .report_entities import external_number

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
        'start' : {
            'shape': 'record',
            'style': 'filled',
            'margin': '0.2',
            'color': '#020300',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'exit': {
            'shape': 'record',
            'style': 'filled',
            'margin': '0.2',
            'color': '#020300',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'auto_attendant': {
            'shape': 'circle',
            'style': 'filled',
            'margin': '0.2',
            'color': '#5E1008',
            'fillcolor': '#FF0000',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'call_centre': {
            'shape': 'Mrecord',
            'style': 'filled',
            'margin': '0.2',
            'color': '#68272E',
            'fillcolor': '#FFC0CB',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'hunt_group': {
            'shape': 'Mrecord',
            'style': 'filled',
            'margin': '0.2',
            'color': '#3D4066',
            'fillcolor': '#9C1FE9',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'user': {
            'shape': 'Mrecord',
            'style': 'filled',
            'margin': '0.2',
            'color': '#B87700',
            'fillcolor': '#FBA200',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        
    }
    EDGE_STYLYING = {
        "fontname": "Arial"
    }
    
    def __init__(self, output_directory: str =None):
        
        self.dot = graphviz.Digraph()
        self.output_directory = output_directory
        
   
    def generate_call_flow_graph(self, nodes: list, number: str):
        self.dot.attr(name=f"calls_to_{number}", label=number, fontname='Arial',
                      fontcolor='white', rankdir="LR")
        
        # build nodes
        self.dot.node("Start", "Start", GraphvizModule.NODE_STYLING["start"])
        for n in nodes:
            if isinstance(n, bre.User):
                self.dot.node(n.id, n.extension, GraphvizModule.NODE_STYLING["user"])
            elif isinstance(n, bre.CallCenter):
                self.dot.node(n.service_user_id, n.extension, GraphvizModule.NODE_STYLING["call_centre"])
            elif isinstance(n, bre.HuntGroup):
                self.dot.node(n.service_user_id, n.extension, GraphvizModule.NODE_STYLING["hunt_group"])
            elif isinstance(n, bre.AutoAttendant):
                self.dot.node(n.service_user_id, n.extension, GraphvizModule.NODE_STYLING["auto_attendant"])
            
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
                    self._format_edge(n, n.bounced_calls_transfer_to_phone_number, "BCT")
                if n.overflow_calls_action:
                    self._format_edge(n, n.overflow_calls_transfer_to_phone_number, "OF")
                if n.stranded_calls_action:
                    self._format_edge(n, n.stranded_calls_transfer_to_phone_number, "SCF")
                if n.stranded_call_unavailable_action:
                    self._format_edge(n, n.stranded_call_unavailable_transfer_to_phone_number, "USCF")
                        
            elif isinstance(n, bre.HuntGroup):
                if n.forward_after_timeout_enabled:
                    self._format_edge(n, n.no_answer_forward_to_phone_number, "NACF")
                if n.call_forward_not_reachable_enabled:
                    self._format_edge(n, n.call_forward_not_reachable_transfer_to_phone_number, "CFNR")
                        
            elif isinstance(n, bre.AutoAttendant):
                for key in n.business_hours_menu.keys:
                    if "Transfer" in key.action:
                        self._format_edge(n, key.phone_number, key.number)
                        
    
    def _format_edge(self, node_a: str, node_b: str, label: str):
        try:
            self.dot.edge(node_a.id, node_b.id, label, GraphvizModule.EDGE_STYLYING)
        except AttributeError:
            try:
                self.dot.edge(node_a.id, node_b.service_user_id, label, GraphvizModule.EDGE_STYLYING)
            except AttributeError:
                try:
                    self.dot.edge(node_a.service_user_id, node_b.service_user_id, label, GraphvizModule.EDGE_STYLYING)
                except AttributeError:
                    self.dot.edge(node_a.service_user_id, node_b.id, label, GraphvizModule.EDGE_STYLYING)

            
    def _save_graph(self, filename: str):
        self.dot.render(directory=self.output_directory, filename=filename,
                        format="svg", cleanup=True).replace('\\', '/')
    
        