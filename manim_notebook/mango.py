from IPython.core.magic import register_cell_magic
import argparse
from .manim_cell import manim
import sys

#global verialbes
TAB = '    '
SETTINGS = {
    'configs': '',
    'super_class': 'Scene',
    'class_name': 'Foo',
    'header': ''
}

def get_code(header='', class_name='Foo', super_class='Scene', configs='', body='pass'):
    #refactor code and stitch everything together
    header = header + '\n'
    configs = TAB + configs.strip().replace('\n', f'\n{TAB}') + '\n'
    body = TAB*2 + body.strip().replace('\n', f'\n{TAB*2}') + '\n'
    code = (header +
            f'class {class_name}({super_class}):\n'
                    + configs
            + TAB + 'def construct(self):\n'
                        + body)
    return code

def parse_args(args_to_parse):
    parser = argparse.ArgumentParser(description='Configure manim')
    parser.add_argument('-s', '--super-class', action = 'store', metavar = 'SUPER_CLASS', default='Scene', help = 'Super class name. Default super class is \"Scene\"')
    parser.add_argument('-c', '--class-name', action = 'store', metavar = 'CLASS_NAME', default='Foo', help = 'Class name. Default class name is \"Foo\"')
    return parser.parse_args(args_to_parse)

#use this cell magic to configure class name, super class name
#and CONFIG dictionary
@register_cell_magic
def _config(line, cell):
    args = parse_args(line.split())
    SETTINGS['super_class'] = args.super_class 
    SETTINGS['class_name'] = args.class_name
    SETTINGS['configs'] = cell

#use this cell_magic if you want to include imports and functions
@register_cell_magic
def header(line, cell):
    SETTINGS['header'] = cell

#cell_magic to run manim code snippets
@register_cell_magic
def mango(line, cell):
    code = get_code(SETTINGS['header'], SETTINGS['class_name'], SETTINGS['super_class'], SETTINGS['configs'], body=cell)
    return manim(line, code)