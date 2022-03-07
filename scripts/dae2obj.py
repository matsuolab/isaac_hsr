# simple script to batch convert collada to obj.
# run as:
# blender --background --python dae2obj.py target_dir

import os
import sys
import glob
import bpy

print(sys.argv)
if len(sys.argv) != 5:
    print('Invalid command given')
    print('blender --background --python dae2obj.py <target_dir>')
    exit -1

for infile in glob.glob(os.path.join(sys.argv[-1], '*.dae')):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.ops.wm.collada_import(filepath=infile)
    outfilename = os.path.splitext(os.path.split(infile)[1])[0] + ".obj"

    # Update scene
    bpy.context.view_layer.update()

    bpy.ops.export_scene.obj(filepath=os.path.join(sys.argv[-1], outfilename))
