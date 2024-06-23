from turtle import * 



speed(15)
#დიდი მართკუთხედი

width(5)
color("brown")

forward(700)
right(90)

forward(350)
right(90)

forward(400)
right(90)

left(90)
forward(200)

forward(350)
right(90)

forward(350)
right(90)

forward(350)
right(90)

left(90)
forward(400)

#ერთი კუბიკი

color("green")


penup()
left(180)
forward(650)
pendown()

right(110)
forward(140)

right(70)
forward(150)

right(80)
forward(135)

#მეორე კუბიკი

penup()
left(80)
forward(30)
pendown()

left(70)
forward(145)

right(70)
forward(150)

right(70)
forward(145)


#მესამე კუბიკი

penup()
left(75)
forward(30)
pendown()

left(70)
forward(135)

right(75)
forward(150)

right(70)
forward(140)



#ერთი სამკუთხედი

penup()
right(180)
forward(140)
left(70)
forward(30)
pendown()

color("green")
begin_fill()

right(65)
forward(100)

left(130)
forward(100)

end_fill()
#მეორე სამკუთხედი

penup()
right(65)
forward(35)
left(70)
forward(140)
right(70)
forward(30)
right(70)
forward(145)
left(70)
forward(30)
pendown()

begin_fill()

right(65)
forward(90)

left(130)
forward(90)

end_fill()
#მესამე სამკუთხედი

penup()
right(60)
forward(37)
left(70)
forward(140)
right(75)
forward(30)
right(70)
forward(145)
left(70)
forward(30)
pendown()

begin_fill()

right(65)
forward(100)

left(130)
forward(100)

end_fill()

#ფაჯარა ერთი

penup()
right(50)
forward(20)
left(70)
forward(135)
left(100)
forward(130)
left(90)
forward(60)
pendown()

color("orange")
begin_fill()


circle(40)

end_fill()

#ფანჯარა მეორე

penup()
right(107)
forward(210)
pendown()

begin_fill()

circle(40)

end_fill()

#ფანჯარა მესამე

penup()
right(349)
forward(290)
pendown()

begin_fill()

circle(40)

end_fill()

#კარები

color("purple")

penup()
right(90)
forward(370)
right(90)
forward(150)
pendown()

begin_fill()

right(90)
forward(180)

left(90)
forward(300)

left(90)
forward(180)

end_fill()

penup()
left(90)
forward(300)
left(90)
forward(150)
pendown()

begin_fill()

circle(150)

end_fill()

#სახურავი

color("purple")

penup()
right(90)
forward(350)
left(90)
forward(207)
pendown()

left(40)
forward(410)

left(50)
forward(450)

left(54)
forward(400)

#მეფე

penup()
left(37)
forward(350)
pendown()

#მეფე(ფეხები)

color("red")

penup()
right(90)
forward(80)
pendown()

right(90)
forward(200)

left(90)
forward(80)

left(90)
forward(200)

left(90)
forward(30)

left(90)
forward(180)

right(90)
forward(20)

right(90)
forward(180)

left(90)
forward(30)

#მეფე(ტანი)

penup()
left(90)
forward(200)
pendown()

color("sky blue")

right(90)
forward(20)

left(90)
forward(150)

left(90)
forward(120)

left(90)
forward(150)

left(90)
forward(20)

penup()
forward(45)
left(90)
forward(60)
pendown()

begin_fill()

circle(7)

end_fill()

penup()
forward(40)
pendown()

begin_fill()

circle(7)

end_fill()



#მეფის ერთი ხელი

penup()
forward(20)
left(90)
forward(70)
pendown()

left(50)
forward(80)

left(90)
forward(10)

left(90)
forward(75)

#მეფის მეორე ხელი

penup()
right(50)
forward(125)
pendown()

left(50)
forward(80)

#დროშა
penup()
right(150)
forward(60)
pendown()

color("black")


left(180)
forward(370)

left(90)
forward(300)

left(90)
forward(180)

left(90)
forward(300)

#მეფის მეორე ხელი

penup()
right(90)
forward(110)
left(180)
pendown()

color("sky blue")

left(150)
forward(85)


#მეფის თავი

penup()
right(45)
forward(15)
right(90)
forward(100)
pendown()

color("pink")

circle(40)

#მეფის კისერი

penup()
left(180)
forward(70)
right(90)
forward(20)
right(90)
pendown()

forward(35)

penup()
left(90)
forward(40)
left(80)
pendown()

forward(30)

#სახე

penup()
left(180)
forward(50)
right(110)
pendown()

width(3)

forward(15)
left(90)

right(30)
forward(15)


penup()
left(30)
forward(20)
pendown()

circle(5)

penup()
left(105)
forward(35)
pendown()

circle(5)

#გვირგვინი

penup()
right(80)
forward(30)
left(90)
forward(30)
right(180)
pendown()

color("yellow")

forward(90)

left(65)
forward(50)

left(160)
forward(30)

right(120)
forward(30)

left(75)
forward(55)

left(70)
forward(30)

right(120)
forward(30)

left(145)
forward(50)

#დედოფალი

penup()
left(355)
forward(460)
right(90)
forward(155)
pendown()

color("pink")

right(90)
forward(200)

left(90)
forward(80)

left(90)
forward(200)

left(90)
forward(30)

left(90)
forward(180)

right(90)
forward(20)

right(90)
forward(180)

left(90)
forward(30)

#დედოფლის კაბა

penup()
left(90)
forward(100)
right(90)
forward(30)
pendown()

color("orange")
begin_fill()

left(105)
forward(105)

left(75)
forward(85)

left(75)
forward(105)

left(105)
forward(10)

end_fill()

#დედოფლის ტაანი

penup()
forward(100)
left(90)
forward(100)
pendown()

color("red")

right(90)
forward(20)

left(90)
forward(150)

left(90)
forward(120)

left(90)
forward(150)

left(90)
forward(20)

penup()
forward(55)
left(90)
forward(90)
pendown()

color("pink")
begin_fill()

circle(12)

end_fill()

penup()
forward(60)
pendown()

begin_fill()

#თავი

penup()
right(90)
forward(25)
left(90)
forward(70)
pendown()

circle(40)

penup()
left(90)
forward(20)
left(90)
forward(35)
pendown()

forward(35)

penup()
right(90)
forward(40)
right(90)
pendown()

forward(35)

#სახე

penup()
forward(20)
pendown()

right(120)

width(3)

forward(15)
left(90)

right(30)
forward(20)

penup()
left(30)
forward(20)
pendown()

circle(5)

penup()
left(105)
forward(35)
pendown()

circle(5)

#გვირგვინი

penup()
right(80)
forward(30)
left(90)
forward(30)
right(180)
pendown()

color("yellow")

forward(90)

left(65)
forward(50)

left(160)
forward(30)

right(120)
forward(30)

left(75)
forward(55)

left(70)
forward(30)

right(120)
forward(30)

left(145)
forward(50)

#ხელები

color("pink")

penup()
forward(150)
right(90)
forward(25)
pendown()

left(50)
forward(80)

left(90)
forward(10)

left(90)
forward(75)

penup()
left(70)
forward(20)
right(123)
forward(135)
pendown()

right(60)
forward(80)

right(90)
forward(10)

right(90)
forward(80)

#დროშის წარწერა
#G
penup()
right(40)
forward(370)
right(90)
forward(65)
pendown()

color("green")

left(180)
forward(50)

left(90)
forward(80)

left(90)
forward(50)

left(90)
forward(40)

left(90)
forward(30)

#O
penup()
left(180)
forward(50)
right(90)
pendown()

circle(40)
#A

penup()
forward(40)
left(90)
forward(80)
left(70)
pendown()

forward(90)
right(140)
forward(80)


left(180)
forward(30)

left(70)
forward(30)











exitonclick()