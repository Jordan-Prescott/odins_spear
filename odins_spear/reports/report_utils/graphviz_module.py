import graphviz

import odins_spear.logger as logger

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
            'shape': 'oval',
            'style': 'filled',
            'margin': '0.2',
            'color': '#020300',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'end': {
            'shape': 'box',
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
            'shape': 'parallelogram',
            'style': 'filled',
            'margin': '0.2',
            'color': '#68272E',
            'fillcolor': '#FFC0CB',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'hunt_group': {
            'shape': 'parallelogram',
            'style': 'filled',
            'margin': '0.2',
            'color': '#3D4066',
            'fillcolor': '#9C1FE9',
            'fontname': 'Arial',
            'fontcolor': 'white'
        },
        'user': {
            'shape': 'diamond',
            'style': 'filled',
            'margin': '0.2',
            'color': '#B87700',
            'fillcolor': '#FBA200',
            'fontname': 'Arial',
            'fontcolor': 'white'
        }
    }

    def __init__(self, output_directory: str =None):
        
        self.dot = graphviz.Digraph()
        self.output_directory = output_directory
        
   
    def generate_call_flow_graph(self, flow: object, number: str):
        self.dot.attr(name=f"calls_to_{number}", label=number, fontname='Arial',
                      fontcolor='white', rankdir="LR")
        
    
    def _save_graph(self, filename: str):
        self.dot.render(directory=self.output_directory, filename=filename,
                        format="svg", cleanup=True).replace('\\', '/')
    
        