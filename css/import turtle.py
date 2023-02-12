import turtle
t = turtle.Turtle()
for i in range (180) :
	t.speed(0)
	t.color('#BF00FF');
	t.circle(190 - i, 90);
	t.left(90);
	t.color('#ffc200');
	t.circle(190 - i, 90);
	t.left(18);