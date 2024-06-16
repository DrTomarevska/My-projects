from graphics import Canvas

RECTANGLE_SIZE = 200   
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
x = 400
y = 200

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!
    rect1 = canvas.create_rectangle(0, 400, 400, 0, "#F3D3F5")
    time.sleep(1)
    obj1 = canvas.create_text(45, 25, text = 'Please perform breathing exercises', font = 'Arial', font_size = 20, color = 'blue')
    time.sleep(2)
    top_x = x / 4
    top_y = 300
    base_x = x / 4
    base_y = 400
    rect2 = canvas.create_rectangle(base_x, base_y, base_x + RECTANGLE_SIZE, base_y - RECTANGLE_SIZE, "#79DCFF")
    time.sleep(2) 
    obj2 = canvas.create_text(5, 100, text = 'Your breathing movements must match the rhythm of the sky blue square fun animation!', font = 'Arial', font_size = 10, color ='blue')
    time.sleep(4)
    dx_top, dy_top = 0, -90
    obj3 = canvas.create_text(100, 200, text = 'Please, deep inhalation', font = 'Arial', font_size = 15, color ='blue')
    time.sleep(1)
    for i in range(5):
        canvas.change_text(obj3, new_text = 'Please, deep inhalation')
        canvas.move(rect2, dx_top, dy_top)
        time.sleep(5)
        
        while canvas.get_top_y(rect2) < (CANVAS_WIDTH / 2 - RECTANGLE_SIZE / 2):
            canvas.move(rect3, 1, 0)
            time.sleep(5)
        canvas.change_text(obj3, new_text = 'Please, deep exhalation')
        canvas.moveto(rect2, base_x, base_y)
        time.sleep(8)

    canvas.set_color(rect1, "#A499E3")
    time.sleep(2)
    canvas.set_color(rect2, "#A499E3")
    canvas.set_color(obj1, "#A499E3")
    canvas.set_color(obj2, "A499E3")
    canvas.change_text(obj3, "Thank's a lot for your good folowing!")
    time.sleep(5)
    canvas.change_text(obj3, "HAVE A GOOD HEALTH :)")


if __name__ == '__main__':
    main()