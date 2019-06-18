# Ball game

## 1. Read buttons
Read BTN_UP_PIN, BTN_DOWN_PIN, BTN_LEFT_PIN and BTN_RIGHT_PIN in https://github.com/bytebarista/iot_workshop/blob/master/src/pins.py and print them.

## 2. Write buttons to screen
Write some text that only shows when each of the buttons are pressed.

You can find example display code in https://github.com/bytebarista/iot_workshop/blob/master/components.ipynb.

## 3. Move ball on screen using the buttons

Draw a ball (circle) on the screen that moves to the left when you press the left button.

Pseudocode:
```
import and initialize screen
import buttons

ball_x = 100
ball_y = 100

while True:
    if left button is pressed:
        ball_x -= 5
        
    clear screen
    draw circle at ball_x, ball_y
```

## 4. Make it work in all directions
Extend the code to work with other buttons as well so that the ball can move in all directions

## 5. Collision with the edges
Make it so the ball can collide with the edges.

Hint: Clamp ball_x and ball_y in every iteration of the loop

## 6. Acceleration
Right now the ball only moves when you press the buttons.

Make it so the ball instead accelerates in the direction of the buttons you press.

Hint: Introduce a new speed variable which you add to your ball position at each iteration.

## 7. Bouncing ball at edges
Depending on how you did things in the previous point, the ball may be behaving a bit strangely at the edges.

Make it so the ball instead bounces when it hits the edge.

Hint: When a ball bounces, the speed component normal to the wall gets inverted. Feel free to ask for help.

## 8. Candies
Make some small candies on the board which the ball can collect. When the ball hits them, they should disappear and a new one should appear.

## 9. Score
Draw a score on the screen. Every time you collect a candy the score should increase.

## Optional: Tilt steering
Use the accelerometer to steer the ball instead of the buttons
