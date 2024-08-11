import math

def get_distance(point1, point2):
    """Calculate the distance between two points."""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_angle(p1, p2, p3):
    """Calculate the angle between three points p1, p2, and p3."""
    def vector(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])
    
    def dot_product(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]
    
    def magnitude(v):
        return math.sqrt(v[0] ** 2 + v[1] ** 2)
    
    v1 = vector(p2, p1)
    v2 = vector(p2, p3)
    
    cos_theta = dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))
    angle = math.degrees(math.acos(cos_theta))
    
    return angle
