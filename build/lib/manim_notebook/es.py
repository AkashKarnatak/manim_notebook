#this file is same as manimlib.extract_scene.main(config)
#Changes are addressed by comments
import sys

from manimlib.extract_scene import get_scene_classes_from_module, get_scenes_to_render, open_file_if_needed
from manimlib.utils.sounds import play_finish_sound
from manimlib.utils.sounds import play_error_sound
from IPython.utils import io
import traceback

def main(config, verbose, quiet):
    module = config["module"]
    all_scene_classes = get_scene_classes_from_module(module)
    scene_classes_to_render = get_scenes_to_render(all_scene_classes, config)

    #io.capture_output() suppress output until its 
    #closed. So if args.verbose == true, then suppress
    #the output. This statement wasn't placed on the top
    #because we want "get_scenes_to_render" to output a 
    #list of scene classes when, more than one scenes are
    #present in the module
    if not verbose:
        capture_output = io.capture_output(stderr=quiet)
        capture_output.__enter__()
    scene_kwargs = dict([
        (key, config[key])
        for key in [
            "camera_config",
            "file_writer_config",
            "skip_animations",
            "start_at_animation_number",
            "end_at_animation_number",
            "leave_progress_bars",
        ]
    ])

    #list to store objects of all scene classes. This
    #will be used in the main file to extract scene's 
    #output media directory
    all_scene_objects = []
    for SceneClass in scene_classes_to_render:
        try:
            # By invoking, this renders the full scene
            scene = SceneClass(**scene_kwargs)
            all_scene_objects.append(scene)
            open_file_if_needed(scene.file_writer, **config)
            if config["sound"]:
                play_finish_sound()
        except Exception:
            print("\n\n")
            traceback.print_exc()
            print("\n\n")
            if config["sound"]:
                play_error_sound()
    if not verbose:
        capture_output.__exit__(None, None, None)
    #return "all_scene_objects" list
    return all_scene_objects
