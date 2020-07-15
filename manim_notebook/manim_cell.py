from IPython.core.magic import register_cell_magic
from IPython.utils import io
import sys
import os
from .parse_args import parse_args
from .fetch_output import get_image, get_video
from IPython.display import display, HTML
from .split import split_screen

import manimlib
from . import es

@register_cell_magic
def manim(line, cell):

    #Include manimlib imports if the user forgot to include them.
    if 'from manimlib.imports import *' not in cell:
        cell = 'from manimlib.imports import *\n' + cell
    
    #A temporary file to store current cell's code
    #This file and thus it's output media files 
    #will be overwritten each time you execute the
    #cell. So, if you want to save a file use the 
    #-o option.
    file_name = '__temp__.py'

    #parse the specified arguments. "parse_args" is
    #slightly modified manim function "manimlib.config.parse_cli()".
    #It takes an additional argument -v or --verbose.
    args = parse_args(line.strip().split())

    #if file name is provided using --file option then use
    #that name instead.
    if not args.file:
        args.file = file_name
    else:
        args.file += '.py'
    #display output cell beside input cell if args.no_split == False
    if not args.no_split:
        split_screen()

    #write to the file
    with open(args.file, 'w') as new_file:
        new_file.write(cell)

    #io.capture_output() suppress output until its 
    #closed. So if args.verbose == true, then suppress
    #the output.
    if not args.verbose:
        capture_output = io.capture_output(stderr=args.quiet)
        capture_output.__enter__()

    #manim functions
    config = manimlib.config.get_configuration(args)
    manimlib.constants.initialize_directories(config)

    #end io.capture_output() if it was opened
    if not args.verbose:
        capture_output.__exit__(None, None, None)

    #es.main is a modified version of manimlib.extract_scene.main()
    #It takes the usual argument "config", plus an additional
    #argument arg.verbose. It is explicitly given args.verbose
    #because we don't want to suppress the list of scene class 
    #which is displayed on the output when multiple classes are
    #present in the code.
    all_scene_objects = es.main(config, verbose=args.verbose, quiet=args.quiet)

    #this contain the html attributes to render, like the video
    #and images of the output file
    html_to_render = ''

    #default height and width of output screen
    height = 300
    width = 480

    #if resolution is explicitly provided then use provided values instead
    if args.frame_size:
        try:
            height, width = [int(x) for x in args.frame_size.strip().split(',')]
        except Exception as e:
            print(e,'\nFrame size should have a format, height,width', file=sys.stderr)
            sys.exit(1)

    #loop through all the scene class objects to find the 
    #location of their respective output media files.
    #Use their location to generate appropriate html code
    #and append it to "html_to_render".
    for x in all_scene_objects:
        dictionary = x.__dict__['file_writer'].__dict__
        if args.save_last_frame:
            html_to_render += get_image(dictionary['image_file_path'], width=width, height=height)
        if dictionary['write_to_movie']:
            html_to_render += get_video(dictionary['movie_file_path'], width=width, height=height)

    #finally display rendered HTML   
    return HTML(html_to_render)