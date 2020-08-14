import math
def gradient(p1,p2):
    (x1, y1), (x2, y2) = p1, p2
    m = (y2 - y1) / (x2 - x1)
    return m

def y_int(p,m):
    (x1, y1) = p
    y = y1 - m * x1
    return y

def lines(points): #finds gradients and y-intercepts for line A, B and C
    a_points, b_points, c_points = points[0:2], points[2:4], points[4:6]
    m_a, m_b, m_c = gradient(a_points[0], a_points[1]), gradient(b_points[0], b_points[1]), gradient(c_points[0], c_points[1])
    m_ave = (m_a + m_b + m_c) / 3
    y_int_a, y_int_b, y_int_c = y_int(a_points[0], m_ave), y_int(b_points[0], m_ave), y_int(c_points[0], m_ave)
    y_ints = [y_int_a, y_int_b, y_int_c]
    return m_ave, y_ints

def point_to_line(point, m, y_int):
    (x1, y1) = point
    d = abs(-m * x1 + y1 - y_int) / math.sqrt(m ** 2 + 1)
    return d

def distances(points, m, y_ints): # finds perpendicular distance between lines and ball to line c
    (x_b, y_b) = points[6]
    ab = point_to_line((0, y_ints[1]), m, y_ints[0])
    bc = point_to_line((0, y_ints[2]), m, y_ints[1])
    cd = point_to_line((x_b, y_b), m, y_ints[2])
    return ab, bc, cd

def cross_ratio(ab, bc, cd):
    #ab is goal-line to 6-yard-box
    #bc is 6-yard-box to penalty box
    #cd is penalty box to ball
    c = ((ab + bc) * (bc + cd)) / (bc * (ab + bc + cd))
    return c

def get_dist(c):
    x = (181.5 - 181.5 * c)/(11 * c - 16.5) #values derived from real distances on field #real length from ball to penalty box
    d = x + 16.5  #16.5m is the length of the box
    return d