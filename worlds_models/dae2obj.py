import os
import glob
import bpy

def delete_all_objects():
    for item in bpy.data.objects:
        bpy.data.objects.remove(item)
    # 全メッシュデータを削除
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)
    # 全マテリアルデータを削除
    for item in bpy.data.materials:
        bpy.data.materials.remove(item)
    return


obj_list = glob.glob("C:\\Users\\ryoku\\tmc_wrs_gazebo\\tmc_wrs_gazebo_worlds\\models\\*\\meshes\\*.dae")


# obj_listの文字列をループし、ファイルをシーンに追加
for item in obj_list:
    delete_all_objects()
    bpy.ops.wm.collada_import(filepath=item)
    name = item.split("models\\")[-1].split(".dae")[0].replace("\\","_")
    filepath='C:\\Users\\ryoku\\tmc_wrs_gazebo\\out\\{0}.obj'.format(name)
    print("名前")
    print(item)
    print(filepath)
    bpy.ops.export_scene.obj(filepath = filepath)


        



