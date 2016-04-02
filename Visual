import bpy

rows = 5 
columns = 5

r = 0 
c = 0 

for i in range (0, rows*columns):
    
    if c == columns:
        r += 1
        c = 0 
    bpy.ops.mesh.primitive_cube_add(location = (r, c, 0))
    bpy.context.scene.cursor_location = bpy.context.active_object.location
    bpy.context.scene.cursor_location.z -= 1
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    ######
    bpy.context.active_object.scale.x = 0.5
    bpy.context.active_object.scale.y = 0.5
    bpy.context.active_object.scale.z = 5.0
    #bpy.ops.object.scale_apply()
    bpy.ops.anim.keyframe_insert_menu(type='Scaling')
    bpy.context.active_object.animation_data.action.fcurves[0].lock = True
    bpy.context.active_object.animation_data.action.fcurves[1].lock = True
    
    bpy.context.area.type = 'GRAPH_EDITOR'
    
    step = 20000/(rows*columns)

    bpy.ops.graph.sound_bake(filepath="/Users/AaronJaramillo/Music/Imported Music/Kanye West - 808s & Heartbreak (2008)/05 Love Lockdown.mp3", low=(i*step), high=(i*step)+step)
    
    bpy.context.active_object.animation_data.action.fcurves[2].lock = True
    
    c += 1
