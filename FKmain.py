'''
Program to determine the distance of the ball to the goal-line during a free-kick from an oriented image.
'''
import os
import matplotlib.pyplot as plt
from FKfunctions import lines, distances, cross_ratio, get_dist
from guizero import App, Combo, Drawing, PushButton, Text

#to add - switching to diff app or pasting over the app, resize the popups
dir = "images"
images_dir = [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
images_names = [(x[7:])[:-4] for x in images_dir]
image = ""
app =App(title="Free-Kick Distance Calculator", bg="beige")

def select_image():
    global image
    image = images_combo.value
    i=-1
    for x in images_names:
        i+=1
        if x == image:
            break
    image = images_dir[i]
    button_select_points.enable()

def select_points(image):
    img = plt.imread(image)
    fig, ax = plt.subplots()
    ax.imshow(img)
    points = plt.ginput(7)
    if len(points) == 7:
        plt.close()
    return points

def close():
    app.destroy()

def functions():
    points = select_points(image)
    m, y_ints = lines(points)
    ab, bc, cd = distances(points, m, y_ints)
    c = cross_ratio(ab, bc, cd)
    d = get_dist(c)
    text = "Free-Kick Distance: " + str(round(d)) + " metres or " + str(round(d * 1.094)) + " yards"
    result.value = text
    images_combo.visible = False
    button_select_points.visible = False
    text1.visible = False
    close_button.visible = True

text1 = Text(app, "Select Image: ")
images_combo = Combo(app, options=images_names, command=select_image)
button_select_points = PushButton(app, text="Select Points", command=functions, enabled=False)
result = Text(app, " ")
close_button = PushButton(app, text="   Close   ", command=close, align="bottom", visible=False)
app.display()