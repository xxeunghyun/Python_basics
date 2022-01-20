# turtle이라는 모듈 가져오기 
import turtle

#그림을 그리기 위해서 캔버스를 띄어준다. 
t = turtle.Pen()

#캔버스에 거북이 모양으로 마우스 모양 바꿈 
t.shape("turtle")

#캔버스 색을 파란색으로 설정 
t.pencolor("blue")

#100 pixel 만큼 이동 (직선으로)
t.forward(100)

#거북이의 방향을 90도만큼 rotate
t.right(90)

#거북이가 90도 회전되어있는 상태에서 100만큼 이동 
t.forward(100)
