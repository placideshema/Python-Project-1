  # RwandaAir animation flying and its history
  
  # draw a plane
Rect(0,0,400,400)
# background of plane.
backgroundb=Rect(0,0,400,400,fill=gradient('cornflowerBlue','white',start='top'))
 
# clouds fucntions with almost same characters but with tremendously different "X".


# clouds Groups
Moveclouds=Group(
    Oval(400,330,100,70,fill=gradient('white','gray',start='top')),
    Oval(350,320,100,70,fill=gradient('white','gray',start='top')),
    Oval(60,250,100,70,fill=gradient('white',"gray",start='top')),
    Oval(310,330,100,70,fill=gradient('white','gray',start='top')),
    Oval(80,220,100,70,fill=gradient('white','gray',start='top')),
    Oval(340,300,100,70,fill=gradient('white','gray',start='top')),
    Oval(20,230,100,70,fill=gradient('white','gray',start='top')),
    Oval(330,320,100,70,fill=gradient('white','gray',start='top')),
    Oval(200,330,100,70,fill=gradient('white','gray',start='top')),
    Oval(193,300,100,70,fill=gradient('white','gray',start='top')),
    Oval(223,350,110,70,fill=gradient('white','gray',start='top')),
    Oval(120,270,110,70,fill=gradient('white','gray',start='top')),
    Oval(129,330,110,70,fill=gradient('white','gray',start='top')),
    Oval(250,305,100,70,fill=gradient('white','gray',start='top')),
    Oval(100,280,90,70,fill=gradient('white','gray',start='top')),
    Oval(70,330,100,70,fill=gradient('white','gray',start='top')),
    Oval(380,330,100,70,fill=gradient('white','gray',start='top')),
    Oval(360,340,120,70,fill=gradient('white','gray',start='top')),
    Oval(350,120,130,70,fill=gradient('white','gray',start='top')),
    Oval(340,130,140,70,fill=gradient('white','gray',start='top')),
    Oval(340,160,120,70,fill=gradient('white','gray',start='top')),
    Oval(310,130,110,70,fill=gradient('white','gray',start='top')),
    Oval(320,110,120,70,fill=gradient('white','gray',start='top')),
    Oval(260,160,100,70,fill=gradient('white','gray',start='top')),
    Oval(340,110,90,70,fill=gradient('white','gray',start='top')),
    Oval(200,100,110,70,fill=gradient('white','gray',start='top')),
    Oval(193,100,100,70,fill=gradient('white','gray',start='top')),
    Oval(193,100,130,70,fill=gradient('white','gray',start='top')),
    Oval(139,130,120,70,fill=gradient('white','gray',start='top')),
    Oval(220,130,100,70,fill=gradient('white','gray',start='top')),
    Oval(193,160,100,70,fill=gradient('white','gray',start='top')),
    Oval(125,100,100,70,fill=gradient('white','gray',start='top')),
    Oval(100,140,100,70,fill=gradient('white','gray',start='top')),
    Oval(140,200,100,70,fill=gradient('white','gray',start='top')),
    Oval(100,170,100,70,fill=gradient('white','gray',start='top')),
    Oval(130,130,100,70,fill=gradient('white','gray',start='top')),
    Oval(179,125,100,70,fill=gradient('white','gray',start='top'))
    
    )


# draw a plane
    


plane=Group(

# draw a plane
# draw rudder,tail and elevator
Polygon(53,128,70,127,100,150,80,153,fill='darkblue',border='black',borderWidth=1),
Polygon(20,150,53,128,66,127,26,150,fill='white',border='black',borderWidth=1),
Polygon(66,127,53,128,63,110,69,110,70,127,fill='White',border='black',borderWidth=1),
Polygon(80,153,87,159,92,160,120,158,118,140,fill='blue',border='black',borderWidth=1),
Line(81,153,106,146,fill='darkBlue'),
Line(96,147,106,144,fill='darkBlue',lineWidth=4),
# body
Polygon(118,140,260,120,260,158,126,166,fill=gradient('gray','white',start='bottom')),
Oval(118,150,6,20,fill=gradient('gray','white',start='bottom')),
# nose of plane
Polygon(260,120,310,140,309,142,280,154,260,158,fill=gradient('gray','white',start='bottom')),
Label('Rwand Air',182,145,size=12,fill=rgb(10,60,250),rotateAngle=-3),
# draw engines
# bottom engine

Polygon(106,160,113,153,113,168,106,166,108,168,fill='dimgray'),
Line(106,160,113,160,fill='White'),
Polygon(113,153,113,168,126,167,126,150,fill=gradient('gray','white',start='bottom')),
Oval(125,159,10,17,fill=gradient('black',rgb(60,60,60),start='left'),border='black',borderWidth=1),
Oval(114,160,6,17,fill=gradient('gray','white',start='bottom')),

# top engine

Polygon(118,139,116,134,126,131,126,139,fill='dimgray'),
Line(117,138,126,137,fill='White'),
Polygon(126,139,126,131,139,128,139,137,fill=gradient('gray','white',start='bottom')),
Oval(139,134,6,12,fill=gradient('black',rgb(60,60,60),start='left'),border='black',borderWidth=1),
Line(136,139,144,139,fill='white'),
Oval(127,134,4,8,fill=gradient('gray','white',start='bottom')),

# draw wings
# bottom wing
Oval(172,161,71,6,fill='darkBlue',rotateAngle=-4),
Polygon(150,161,200,160,150,190,135,191,fill='white'),
Polygon(150,190,135,191,80,240,91,239,fill='white'),
Polygon(91,239,80,240,93,241,82,242,80,223,fill='blue'),
Line(168,170,178,170,lineWidth=6,rotateAngle=-7),
Line(172,164,180,164,lineWidth=6,rotateAngle=-7,opacity=50),
Line(181,165,185,164,lineWidth=6,rotateAngle=7,opacity=50),
# top wing
Polygon(171,135,195,132,205,100,190,100,fill='white'),
Polygon(190,100,205,100,205,98,180,90,182,90,fill='blue'),

# declate the plane by drawing windows and 
# putting color on it and also yellow (sun) and its rays
# start from windows
Line(137,155,221,150,dashes=(4,3),opacity=60,lineWidth=4),
# 2nd is sun and its ray on the tail of the plane

Oval(80,142,15,10,fill='yellow',rotateAngle=28),
Oval(80,142,15,8,fill='blue',rotateAngle=28),
Star(80,142,4,8,fill='yellow'),
# 3rd declate colors

Oval(251,153,98,10,fill='darkblue',rotateAngle=-7),
Line(290,150,305,142,fill='darkblue',lineWidth=4),
# draw cockpit where the pilot look through
Oval(267,128,30,15,fill=gradient('gray','white',start='right-top'),rotateAngle=13),
Oval(290,136,23,8,fill=gradient('gray','white',start='top'),rotateAngle=14),
Oval(269,136,12,30,fill='black',opacity=50,rotateAngle=65),
Oval(264,133,13,33,fill=gradient('gray','white',start='right-top'),rotateAngle=66),
# draw door
Rect(240,150,10,10,fill=None,border='White',opacity=60,rotateAngle=-30),
Rect(237,142,10,10,fill=None,border='White',opacity=70,rotateAngle=-10),
Line(245,155,242,150,fill='darkBlue',lineWidth=6),
Line(242,146,242,149,fill='black',opacity=80)
)
# plane 2
check=Rect(34,344,30,40,opacity=0)

# background of introduction of where the plane come from
background=Rect(0,0,400,400,fill=gradient("blue","yellow","green",start="top"),opacity=0)
# rwandairlogo star.
# its background

starbackground=Rect(0,100,400,200,fill="blue",opacity=0)
# star group
rwandairlogostar=Group(
    
    Oval(39,194,50,90,fill=rgb(20,190,250),rotateAngle=50),
    Oval(59,205,60,90,fill="greenYellow",rotateAngle=65),
    Oval(52,195,60,90,fill=rgb(20,80,250),rotateAngle=48.5),
    Rect(76,160,40,45,fill=rgb(20,80,250)),
    Rect(0,196,30,35,fill=rgb(20,80,250)),
   
    Star(50,200,30,24,fill="Yellow",roundness=50),
    Oval(50,200,28,40,fill="yellow",rotateAngle=60),
    Oval(50,200,20,30,fill=None,border="white",rotateAngle=55))

# centerise a logo and plane.
rwandairlogostar.centerX=-60
rwandairlogostar.centerY=200
check.centerX=0
check.centerY=300

# drawing of "rwandair" words group.
rwandair=Group(
    Label("Rwand",200,101,size=50,fill="white"),
    Label("Air",310,101,size=50,fill="yellow")
    )

rwandair.dx=4
rwandair.dy=5
rwandair.visible=False
# last label on rwandair logo fly the dream of Africa
flyword=Group(
    Label("Fly the dream of Africa",270,450,size=15,fill="yellow")
    )
# backgound of plane 3
backgroundc=Rect(0,0,400,400,fill="lightblue",opacity=0)
# its road pass
road=Rect(0,300,400,100,fill=rgb(76,76,76),opacity=0)

besidebushes=Rect(0,200,400,100,fill= gradient("lightgreen","green",start="left"),opacity=0)

roadline1=Line(0,350,400,350,fill="white",dashes=(10,5),lineWidth=0.5,opacity=0)
roadline2black=Line(0,300,400,300,lineWidth=4,dashes=(5,7),opacity=0)
roadline2awhite=Line(6,300,400,300,fill="white",lineWidth=4,dashes=(5,7),opacity=0)

# house of controler
House=Group(Rect(0,150,300,50,fill="burlywood"),
Rect(350,150,50,50,fill="burlywood"),
Line(0,165,300,165,fill="darkgray",dashes=(12,4),lineWidth=16),
Line(0,190,300,190,fill="darkgray",dashes=(12,4),lineWidth=16),
Line(350,165,400,165,fill="darkgray",dashes=(12,4),lineWidth=16),
Line(350,190,400,190,fill="darkgray",dashes=(12,4),lineWidth=16),
Rect(100,80,90,70,fill="burlywood"),
Line(105,80,105,150,fill="gray",dashes=(2,3),lineWidth=2),
Line(113,80,113,150,fill="gray",dashes=(2,3),lineWidth=4),
Line(122,80,122,150,fill="gray",dashes=(6,2),lineWidth=4),
Line(130,80,130,150,fill="gray",dashes=(6,2),lineWidth=4),
Line(145,80,145,150,fill="gray",dashes=(12,5),lineWidth=8),
Line(160,80,160,150,fill="gray",dashes=(12,5),lineWidth=8),
Line(175,80,175,150,fill="gray",dashes=(2,3),lineWidth=2),
Line(183,80,183,150,fill="gray",dashes=(2,3),lineWidth=4),
Polygon(96,65,100,80,190,80,198,62,92,62,fill="burlywood",border="gray"),
Line(98,68,194,68,fill="gray",dashes=(7,4),lineWidth=6),
Polygon(92,62,198,62,210,40,78,40,fill="burlywood",border="gray"),
Line(92,50,175,50,dashes=(12,5),lineWidth=10,rotateAngle=-2),
Polygon(110,40,180,40,192,20,98,20,fill="burlywood",border="gray",),
Line(110,30,180,30,dashes=(12,5),lineWidth=10,rotateAngle=-2))
House.opacity=0
    # plane 3
plane3=Group(

# draw a plane
# draw rudder,tail and elevator
Polygon(53,128,77,127,100,150,80,153,fill='darkblue',border='black',borderWidth=1),
Polygon(30,135,53,128,76,129,46,135,fill='white',border='black',borderWidth=1),
Polygon(80,153,82,159,92,160,120,158,118,140,fill='blue',border='black',borderWidth=1),
Line(81,153,106,146,fill='darkBlue'),
Line(96,147,106,144,fill='darkBlue',lineWidth=4),
Polygon(80,153,82,159,74,156,fill=gradient("gray","black",start="top")),

# body
Polygon(118,140,260,120,260,158,126,166,fill=gradient('gray','white',start='bottom')),
Oval(118,150,6,20,fill=gradient('gray','white',start='bottom')),
# nose of plane
Polygon(260,120,310,140,309,142,280,154,260,158,fill=gradient('gray','white',start='bottom')),
Label('Rwand Air',196,139,size=12,fill=rgb(10,60,250),rotateAngle=-6),
Label('rwandair.com',145,149,size=4,fill=rgb(10,60,250),rotateAngle=-6),
# draw engines
# bottom engine
Oval(116,160,50,8,fill="darkBlue",rotateAngle=5),
Polygon(106,150,113,143,113,158,106,156,108,158,fill='dimgray'),
Line(106,150,113,150,fill='White'),
Polygon(113,143,113,158,126,157,126,140,fill=gradient('gray','white',start='bottom')),
Oval(125,149,10,17,fill=gradient('black',rgb(60,60,60),start='left'),border='black',borderWidth=1),
Oval(114,150,6,17,fill=gradient('gray','white',start='bottom')),

# draw wings
# bottom wing or right wing
Oval(174,160,69,10,fill=gradient("black","white",start="bottom"),rotateAngle=-5,opacity=63),
Polygon(160,169,150,169,143,155,146,155,fill='blue',rotateAngle=-19),
Line(150,169,203,159,lineWidth=0.8),
Line(160,169,154,168,fill="blue"),
Line(156,169,166,167,fill="blue"),
Line(203,160,196,163),
Line(166,168,196,163,opacity=65),
Oval(154,165,6,6,fill='yellow',rotateAngle=-70),
Oval(154,165,6,4,fill='blue',rotateAngle=-70),
Star(154,165,2,4,fill='yellow'),
 
# draw landing gear
Oval(169,172,10,8,opacity=90),
Oval(169,172,6,4,fill="white"),
Oval(166,173,10,8,opacity=90),
Oval(166,173,6,4,fill="white"),
Oval(166,173,4,2,opacity=90),
Oval(284,156,7,5,opacity=90),
Oval(284,156,4,2,fill="white"),
Line(284,156,284,152,lineWidth=2),
# declate the plane by drawing windows and 
# putting color on it and also yellow (sun) and its rays
# start from windows
Line(134,152,250,144,dashes=(4,3),opacity=60,lineWidth=4,rotateAngle=-3),
# 2nd is sun and its ray on the tail of the plane

Oval(80,142,15,10,fill='yellow',rotateAngle=-70),
Oval(80,142,15,8,fill='blue',rotateAngle=-70),
Star(80,142,4,8,fill='yellow'),

# 3rd declate colors.

Oval(251,153,98,10,fill='darkblue',rotateAngle=-7),
Line(290,150,305,142,fill='darkblue',lineWidth=4),
# draw cockpit where the pilot look through
Oval(267,128,30,15,fill=gradient('gray','white',start='right-top'),rotateAngle=13),
Oval(290,136,23,8,fill=gradient('gray','white',start='top'),rotateAngle=14),
Oval(274,134,12,20,fill=rgb(67,67,67),rotateAngle=65),
Oval(270,130,12,20,fill=gradient('gray','white',start='right-top'),rotateAngle=66),
Line(279,128,284,133,opacity=60),
Line(270,137,275,141,opacity=50),
# draw door
Rect(243,137,10,20,fill=None,border='White',opacity=70,rotateAngle=-10))
# its rotation and visibility.
plane3.rotateAngle=10
plane3.centerY=310
plane3.visible=False
plane3.opacity=0
app.stepsPerSecond=15
# final essay of many pragraph which determine the rwandair

woardspragraphs=Group(
    Label("HISTORY",100,-10,fill="blue"),
    Label("Incorporation",200,2,size=20),
    Label("After the",30,22,size=13),
    Label("1994 genocide",100,22,size=13,fill="blue"),
    Label("the government took several attempts ",256,22,size=13),
    Label("to revive the farmer national career ",110,36,size=13),
    Label("Air Rwanda",245,36,size=13,fill="blue"),
    Label("that ceased  ",320,36,size=13),
    Label("operations during the genocide. Various private companies showed  ",206,50,size=13),
    Label(" interest in partnering with the government and Uganda-based  ",190,64,size=13),
    Label(" SA alliance Air  ",50,78,size=13 ,fill="blue"),
    Label(" ran the company from 1997 to 2000. After SAAlliance ",245,78,size=13 ),
    Label("ceased operations,the government of Rwanda took over the ",185,91,size=13 ),
    Label("Rwandan operations on 1st December 2002 as the new national",197,104,size=13 ),
    Label("carrier for Rwanda under name",100,117,size=13 ),
    Label("Rwandair Express",260,117,size=16 ,font="Arial Black"),
    Label("( with pass- ",360,117,size=13),
    Label("enger air transportation as the core activity). in 2016 , RwandAir",195,130,size=13),
    Label("received ",40,143,size=13),
    Label("International Air Transport Association's ",180,143,fill="blue",size=13),
    Label("Safety Audit for ",339,143,size=13),
    Label("Ground operations (ISAGO).",97,156,size=13),
    Label("about bombardier RwandAirs, ",200,190,size=15,fill="blue"),
    Label("Bombarier Aerospace had the first of two crj900 NextGen regional, ",200,210,size=13),
    Label("jets ordered by RwandaAir of Kigali Rwanda.RwandaAir'firm, ",185,223,size=13),
    Label("ordered for the crj900 NextGen aircraft,along with options of two, ",197,236,size=13),
    Label("additional crj900 NextGen aircraft,was announced on march 19,2012,",200,249,size=13),
    Label(" RwandaAir took delivery of its first crj900 NextGen Airliner from Bombarier,",200,270,size=11),
    Label("October 22,2012-Montreal",200,283,size=11)
    
    )
woardspragraphs.centerY=560
# plane and clouds opacity
plane.opacity=0
Moveclouds.opacity=0
def onStep():
    check.centerX+=1
 
        # condition that will increase background opacity.
        # and rotation of rwandair logo.
    if(check.centerX>0)and(check.centerX<98):
        backgroundb.opacity-=1
        background.opacity+=1
        starbackground.opacity+=0.5
        # rwandair words condition of movement 
        rwandair.visible=True
        rwandair.centerX+=rwandair.dx
        rwandair.centerY+=rwandair.dy
        rwandair.rotateAngle+=0.0001
    if ((rwandair.left <= 0) or (rwandair.right >= 400)):
        rwandair.dx = -rwandair.dx

    
    if ((rwandair.top <= 0) or (rwandair.bottom >= 400)):
        rwandair.dy = -rwandair.dy
    # condition of fly dream of Africa
    if(check.centerX>=99)and (check.centerX<=109):
        flyword.centerY-=20
        
        # condition of star
    if(check.centerX>=99)and (check.centerX<=140):
        if(check.centerX<=110):
            rwandairlogostar.centerX+=50
        if(check.centerX>110):
            if(rwandairlogostar.left>0):
                rwandairlogostar.centerX-=50
        # star condition
        if(rwandairlogostar.centerY<200):
            rwandairlogostar.visible=True
            rwandairlogostar.centerX-=3
            rwandairlogostar.centerY+=3
            
        # folmulae that will make rwandair logo come true 
    if(check.centerX>=98):
        starbackground.fill=rgb(20,80,250)
        starbackground.opacity=100
# condition which will restart the plane from the ground
    # condition of opacity
    if(check.centerX>140)and (check.centerX<240):
        backgroundc.opacity+=1
        plane3.visible=True
    
        # condition that will increase the visiblity of plane3 to restart on the ground even roadlines and house.
    if(check.centerX>140)and (check.centerX<341):
        plane3.opacity+=0.5
        road.opacity+=0.5
        besidebushes.opacity+=0.5
        roadline1.opacity+=0.5
        roadline2black.opacity+=0.5
        roadline2awhite.opacity+=0.5
        House.opacity+=0.5
    # move the lines of the road to start the planes from the grounds
    if(check.centerX>140):
        roadline1.x1-=2
        roadline2black.x1-=2
        roadline2awhite.x1-=2
        House.centerX-=1
    # condition that will refly the plane from the ground
    if(check.centerX>300)and(check.centerX<600):
        
        # condition that will move the plane upward and road downward
        if(plane3.centerY>=150):
            plane3.centerY-=0.4
            road.centerY+=0.8
            besidebushes.centerY+=0.8
            roadline1.centerY+=0.8
            roadline2black.centerY+=0.8
            roadline2awhite.centerY+=0.8
            House.centerY+=0.8
        # condition that will rotate when it is standing up 
        if(plane3.centerY>=250):
            plane3.rotateAngle-=0.1
            
        # condition that will reput the angle,it had before it stand up
        else:
            if(plane3.rotateAngle<=3):
                plane3.rotateAngle+=0.1
    # condition that will invisible third plane and it's background
    # and then make the first background called backgroundb to front.
    if(check.centerX>520)and (check.centerX<601):
        
        backgroundb.toFront()
        if(plane.opacity>2):
            plane3.opacity-=2
        
        if backgroundb.opacity<98:
            backgroundb.opacity+=2
    # plane in the clouds
    if(check.centerX>570) and check.centerY <800:
        if plane.opacity<97:
            Moveclouds.toFront()
            plane.toFront()
            
            plane.opacity+=3
            Moveclouds.opacity+=3
        plane.centerX+=2
        Moveclouds.centerX-=3
        Moveclouds.centerY-=3
        
    # condition that  will move down the plane at the end of fly
    if(check.centerX> 745):
        plane.centerY=100
        plane.centerX=100
        if(woardspragraphs.centerY>235):
            woardspragraphs.centerY-=2
            woardspragraphs.toFront()
