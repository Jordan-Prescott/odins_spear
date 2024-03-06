""" Graphviz formatting for standardisation in reports.
"""
    
class GraphvizFormatter:
    
    """
    Colours:
    - Black: 020300
    - Orange: FFA400 - Darker: B87700
    - Red: 95190C - Darker: 5E1008
    - Purple: 5B5F97 - Darker: 3D4066
    - Redish: A23E48 - Darker: 68272E
    """
    
    def __init__(self):
        self.start = {
            'shape': 'oval',
            'style': 'filled',
            'margin': '0.2',
            'color': '#020300',
            'fillcolor': 'white',
            'fontname': 'Arial',
            'fontcolor': 'white'
        }
        self.auto_attendant = {
            'shape': 'circle',
            'style': 'filled',
            'margin': '0.2',
            'color': '#95190C',
            'fillcolor': 'white',
            'fontname': 'Arial',
            'fontcolor': 'white'
        }
        self.call_centre = {
            'shape': 'parallelogram',
            'style': 'filled',
            'margin': '0.2',
            'color': '#A23E48',
            'fillcolor': 'white',
            'fontname': 'Arial',
            'fontcolor': 'white'
        }
        self.hunt_group = {
            'shape': 'parallelogram',
            'style': 'filled',
            'margin': '0.2',
            'color': '#5B5F97',
            'fillcolor': 'white',
            'fontname': 'Arial',
            'fontcolor': 'white'
        }
        self.user = {
            'shape': 'diamond',
            'style': 'filled',
            'margin': '0.2',
            'color': '#FFA400',
            'fillcolor': 'white',
            'fontname': 'Arial',
            'fontcolor': 'white'
        }