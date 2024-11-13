#FUNCION QUE ENCIERRA A LOS OBJETOS EN UN ROMBO PARA DETECTAR COLISIONES

def rombo_colision(PosObj2_X,PosObj2_Y,PosObj2_Z,Obj2_width, Obj2_height, Obj2_depth,PosXob1,PosYob1,PosZob1,Obj1_height):

    obj2_rombo = (
        (PosObj2_X - Obj2_width / 2, PosObj2_Y, PosObj2_Z),
        (PosObj2_X, PosObj2_Y, PosObj2_Z - Obj2_depth / 2),
        (PosObj2_X + Obj2_width / 2, PosObj2_Y, PosObj2_Z),
        (PosObj2_X, PosObj2_Y + Obj2_height, PosObj2_Z)
    )

    Obj1_rombo = (
        (PosXob1 - 0.5, PosYob1, PosZob1),
        (PosXob1, PosYob1, PosZob1 - 0.5),
        (PosXob1 + 0.5, PosYob1, PosZob1),
        (PosXob1, PosYob1 + Obj1_height, PosZob1)
    )

    for p1 in obj2_rombo:
        for p2 in Obj1_rombo:
            if abs(p1[0]-p2[0]) + abs(p1[1] - p2[1]) <= 1.0:
                return True     
    return False

def AABB_intersection(AABB1, AABB2):
    # AABB1 y AABB2 son tuplas que representan las cajas delimitadoras
    # AABB = (min_x, max_x, min_y, max_y) en 2D, (min_x, max_x, min_y, max_y, min_z, max_z) en 3D
    
    if (AABB1[1] < AABB2[0] or AABB1[0] > AABB2[1]):
        return False
    if (AABB1[3] < AABB2[2] or AABB1[2] > AABB2[3]):
        return False
    
    return True

def sphere_intersection(sphere1, sphere2):
    # sphere1 y sphere2 son tuplas que representan las esferas
    # sphere = (x, y, z, radius)
    
    distance_squared = (sphere1[0] - sphere2[0])**2 + (sphere1[1] - sphere2[1])**2 + (sphere1[2] - sphere2[2])**2
    radii_sum_squared = (sphere1[3] + sphere2[3])**2
    
    return distance_squared <= radii_sum_squared

def SAT_collision(obj1, obj2):
    axes = obj1.get_axes() + obj2.get_axes()  # Obtener ejes de separación potenciales
    
    for axis in axes:
        projection1 = obj1.project(axis)
        projection2 = obj2.project(axis)
        
        if not overlap(projection1, projection2):
            return False
    
    return True

def overlap(projection1, projection2):
    return not (projection1[1] < projection2[0] or projection2[1] < projection1[0])

