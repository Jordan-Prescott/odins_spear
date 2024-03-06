""" Graphviz formatting for standardisation in reports.
"""
    
    
class GraphvizFormatter():
    
    def __init__(self):
        self.flow_node = {
                'shape': 'box',
                'style': 'filled',
                'margin': '0.2',
                'color': '#01162a',
                'fontname': 'Arial',
                'fontcolor': 'white'}
        self.interactive_node = {
            'shape': 'Mrecord',
            'penwidth': '2',
            'style': 'filled',
            'fontname': 'Helvetica',
            'fontcolor': 'white',
            'fillcolor': '#594d6b',
            'color': '#292037'}
        self.info_node = {
            'shape': 'Mrecord',
            'penwidth': '2',
            'width': '2',
            'style': 'filled',
            'fontname': 'Helvetica',
            'fontcolor': 'white',
            'fillcolor': '#9d6fb8',
            'color': '#6E4E81',
        }
        self.script_node = {
            'shape': 'Mrecord',
            'penwidth': '2',
            'width': '2',
            'style': 'filled',
            'fontname': 'Helvetica',
            'fontcolor': 'white',
            'fillcolor': '#b37196',
            'color': '#7B4F68'
        }
        self.transfer_node = {
            'shape': 'Mrecord',
            'penwidth': '2',
            'width': '2',
            'style': 'filled',
            'fontname': 'Helvetica',
            'fontcolor': 'white',
            'fillcolor': '#c87273',
            'color': '#c87273'
        }
        self.sms_node = {
            'shape': 'Mrecord',
            'penwidth': '2',
            'width': '2',
            'style': 'filled',
            'fontname': 'Helvetica',
            'fontcolor': 'white',
            'fillcolor': '#c87273',
            'color': '#844B4C'
        }