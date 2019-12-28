from manimlib.imports import *
import os
import pyclbr
import random
import math
from manimlib.scene.zoomed_scene import *

# load a picture

class Images(ZoomedScene):
    CONFIG={
        "plane_kwargs" : {
        "color" : RED
        },
        "camera_config":{"background_color":BLACK},
        "zoom_factor": 0.1,
        "zoomed_display_height": 1.5,
        "zoomed_display_width": 1.5,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
            "background_color":LIGHT_GRAY,
        },
    }
    def construct(self):
        img = ImageMobject('./media/designs/svg_images/map2.png')
        img.scale(4)  # Resize to be twice as big
        img.shift(2.1 * LEFT)  # Move the image

        self.play(ShowCreation(img))  # Display the image

        # zoom the map
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

     
        frame.set_color(RED)

        zoomed_display_frame.set_color(BLUE)
        zoomed_display.shift(2.5*DOWN+0.2*RIGHT)
        

        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        tex = TextMobject("\\che{当前观测}")
        tex.next_to(zoomed_display,UP)
        tex.set_color(BLUE)
        tex.scale(0.8)


        self.play(
            ShowCreation(frame),
            ShowCreation(tex),
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        self.play(frame.shift,0.1*DOWN)
        self.play(frame.shift,0.1*LEFT)
        self.play(frame.shift,0.1*LEFT)
        self.play(frame.shift,0.1*LEFT)
        self.play(frame.shift,0.1*LEFT)
        self.play(frame.shift,0.1*LEFT)
        self.play(frame.shift,0.1*UP)
        self.play(frame.shift,0.1*LEFT)


        self.wait(2)
      
 
class gradient_of_map(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    "camera_config":{"background_color": LIGHT_GRAY},
    }
    def construct(self):
       
        squarelist = []
        resultlist = []
        resultlist2= []

        points1 = [x*0.5*RIGHT+y*0.5*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,-4,1)
            ]     #List of vectors pointing to each grid point
        points2 = [x*0.5*RIGHT+y*0.5*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(4,5,1)
            ]     #List of vectors pointing to each grid point
        points3 = [0.5*x*RIGHT+0.5*y*UP
            for y in np.arange(-4,4,1)
            for x in np.arange(-5,-4,1)
            ]     #List of vectors pointing to each grid point
        points4 = [0.5*x*RIGHT+0.5*y*UP
            for y in np.arange(-4,4,1)
            for x in np.arange(4,5,1)
            ]     #List of vectors pointing to each grid point

        for point in points1:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=0.8)
            result = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)
        for point in points2:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=0.8)
            result = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)
        for point in points3:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=0.8)
            result = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)
        for point in points4:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=0.8)
            result = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=RED_D, fill_opacity=1, color=RED_D)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)

        draw_field = VGroup(*squarelist)
        draw_field.shift(0.25*(UP+RIGHT)+RIGHT)  

        draw_field2 = VGroup(*resultlist)
        draw_field2.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        draw_field2.shift(0.25*(UP+RIGHT)+RIGHT)

        draw_field3 = VGroup(*resultlist2)
        draw_field3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        draw_field3.shift(0.25*(UP+RIGHT)+RIGHT)

        tex_breif = TextMobject("\\che{地图的梯度?}")
        tex_breif.scale(1.5)
        tex_breif.to_edge(UP+LEFT)
        tex_breif.set_color(GREEN)

        self.play(Write(tex_breif),rate=10)
        self.play(GrowFromCenter(draw_field2),rate = 5) 
        self.play(Transform(draw_field2,draw_field),rate = 0.2)
        draw_field3.rotate((-4)*TAU/60)
        self.play(ShowCreation(draw_field3),rate=5)

        #正式进入图像梯度
        all_direction = VGroup(*[Vector(UP),Vector(DOWN),Vector(RIGHT),Vector(LEFT)])
        all_direction.scale(0.5)
        all_direction.move_to(draw_field3[0])
        all_direction.set_color(ORANGE)

        all_direction_tex = VGroup(*[
            TextMobject("0").move_to(all_direction[0].get_start()+0.8*UP),
            TextMobject("0").move_to(all_direction[0].get_start()+0.8*DOWN),
            TextMobject("1").move_to(all_direction[0].get_start()+0.8*RIGHT),
            TextMobject("0").move_to(all_direction[0].get_start()+0.8*LEFT),
        ]
        )
        all_direction_tex.set_color(ORANGE)


        self.play(GrowFromCenter(all_direction),GrowFromCenter(all_direction_tex))
        self.wait(1.4)
        self.play(FadeOut(all_direction_tex),ApplyMethod(all_direction.move_to,draw_field3[1]))
        for i in range (8):
            self.play(ApplyMethod(all_direction.move_to,draw_field3[i+2]),rate=20)
            if i==3:
                all_direction_tex2 = VGroup(*[
                    TextMobject("-1").move_to(all_direction[0].get_start()+0.7*UP),
                    TextMobject("-1").move_to(all_direction[0].get_start()+0.7*DOWN),
                    TextMobject("0").move_to(all_direction[0].get_start()+0.7*RIGHT),
                    TextMobject("0").move_to(all_direction[0].get_start()+0.7*LEFT),
                ]
                )
                all_direction_tex2.set_color(ORANGE)
                self.wait(0.7)
                self.play(GrowFromCenter(all_direction_tex2))
                self.wait(1.7)
                self.play(FadeOut(all_direction_tex2))
                        


class derivation(ZoomedScene):
    CONFIG={
        "plane_kwargs" : {
        "color" : RED
        },
        "camera_config":{"background_color":LIGHT_GRAY},
        "zoom_factor": 0.7,
        "zoomed_display_height": 2,
        "zoomed_display_width": 13,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
            "background_color":LIGHT_GRAY,
        },
    }
    def construct(self):
        equation1 = TexMobject(
           "\\mathbf{\\xi}^*","=\\mathop{\\arg\\min}","_{\\mathbf{\\xi}}","\\sum_i","[1-","M","(","\\mathbf{S}_i","(","\\mathbf{\\xi}","))]^2"
            )
        equation1.set_color(DARK_GRAY)
        equation1.set_color_by_tex_to_color_map(
                {
                    "*": BLUE,
                    "\\mathbf{\\xi}": BLUE,
                    "M": GREEN,
                    "\\mathbf{S}_i": RED,
                })
        equation1.to_edge(UP)

        texd2 = VGroup(*[TextMobject(
            "\\che{给定初始估计}"," ","$\\mathbf{\\xi}$",
             )
            ,
            TextMobject(
                ", ","\\che{通过}"
            ),
            TextMobject(
                "\\che{梯度下降}"
            ),
            TextMobject(
                "\\che{找出最优变换 $\\mathbf{\\xi}^*$}",
                tex_to_color_map={
                "$\\mathbf{\\xi}^*$": BLUE,
            }
            )]

         ).arrange(RIGHT)
        texd2.set_color(DARK_GRAY)
        texd2[0].set_color_by_tex_to_color_map({
                "$\\mathbf{\\xi}$": BLUE,
             })
        texd2[2].set_color(YELLOW)
        texd2[3].set_color_by_tex_to_color_map({
                "$\\mathbf{\\xi}^*$": BLUE,
             })


        equation2 = VGroup(
            *[
                TexMobject(
           "\\sum [1-M(\\mathbf{S}_i(\\mathbf{\\xi} +",
            tex_to_color_map={
                "\\mathbf{\\xi}": BLUE,
                "M": GREEN,
                "\\mathbf{S}_i": RED,
            }
            ),
            TexMobject(
            "\\Delta\\mathbf{\\xi}",
            tex_to_color_map={
                "\\Delta\\mathbf{\\xi}": YELLOW,
            }
            ),
            TexMobject("))]^2 \\rightarrow 0")]
        ).arrange(RIGHT)
        equation2.set_color(DARK_GRAY)
        for mob in equation2:
            mob.set_color_by_tex_to_color_map({
                "\\mathbf{\\xi}": BLUE,
                "M": GREEN,
                "\\mathbf{S}_i": RED,
                "\\Delta\\mathbf{\\xi}": YELLOW,
            })
        

        #线性化公式
        equation3 = VGroup(*[
            TexMobject(
           "\\sum[1-M(\\mathbf{S}_i \\left( \\mathbf{\\xi} \\right))-",
            tex_to_color_map={
                "\\mathbf{\\xi}": BLUE,
                "M": GREEN,
                "\\mathbf{S}_i": RED,
            }
            ),

            TexMobject(
            "\\nabla M","(","\\mathbf{S}_i","(","\\mathbf{\\xi}","))",        
            ).set_color(GREEN),

            TexMobject(
            "\\frac{\\partial \\mathbf{S}_i (\\mathbf{\\xi})}{\\partial \\mathbf{\\xi}}",   
            ),

            TexMobject(
                "\\Delta\\mathbf{\\xi}"
            ).set_color(YELLOW),

            TexMobject("]^2")

        ]).arrange(1.5*RIGHT)
        equation3.set_color(DARK_GRAY)
        for mob in equation3:
            mob.set_color_by_tex_to_color_map({
                "\\mathbf{\\xi}": BLUE,
                "M": GREEN,
                "\\mathbf{S}_i": RED,
                "\\Delta\\mathbf{\\xi}": YELLOW,
            })
        equation3[2].set_color(DARK_GRAY)
        
        


        texd2.to_edge(LEFT)
        texd2.shift(1.5*UP+1.2*RIGHT)
        texd2.scale(1.2)

        braces1 = Brace(equation3[1],DOWN)
        eq_nabla = braces1.get_text("\\che{地图的梯度}")
        braces1.set_color(GREEN)
        eq_nabla.set_color(GREEN)

        braces2 = Brace(equation3[2],DOWN)
        tex_nabla = TexMobject("\\begin{bmatrix} 1 & 0 &-sin(\\psi)s_{i,x}-cos(\\psi)s_{i,y}\\\\0 & 1 & cos(\\psi)s_{i,x}-sin(\\psi)s_{i,y}\\end{bmatrix}")
        tex_nabla.next_to(braces2,3*DOWN)
        tex_nabla.set_color(DARK_GRAY)
        braces2.set_color(DARK_GRAY)
 

        texd2_copy = texd2[2].copy()

        tex_eq3_guodu = TextMobject(
            "\\che{线性化}","$M$","$(\\cdot)$",
            tex_to_color_map={
                "$M$": GREEN,
             }
             )
        tex_eq3_guodu.set_color(DARK_GRAY)
        tex_eq3_guodu.set_color_by_tex_to_color_map({
            "$M$": GREEN,
        })

        tex_qitashuoming = VGroup(*[TextMobject(
            "\\che{1.$\\quad$线性化后为凸函数, 求 }","$\\Delta\\mathbf{\\xi}^*$","\\che{, 使得}","$\\frac{\\partial f}{\\partial{\\Delta\\mathbf{\\xi}}^*}=0$\\\\",
        ),
            TextMobject(
                "2.","$\\quad \\mathbf{\\xi}$","$\\leftarrow$","$\\mathbf{\\xi}$","+","$\\Delta{\\mathbf{\\xi}^*}$\\\\",
            ),
        ]
        ).arrange(DOWN)
        tex_qitashuoming.to_edge(DOWN)
        tex_qitashuoming.shift(0.5*UP)
        tex_qitashuoming.scale(1.2)
        tex_qitashuoming.bg=SurroundingRectangle(tex_qitashuoming,color=DARK_GRAY)
        tex_qitashuoming.set_color(DARK_GRAY)
        tex_qitashuoming[0].set_color_by_tex_to_color_map({
            "$\\Delta\\mathbf{\\xi}^*$": YELLOW,
        })
        tex_qitashuoming[1].set_color_by_tex_to_color_map({
            "$\\Delta{\\mathbf{\\xi}^*}$\\\\": YELLOW,
            "$\\mathbf{\\xi}$": BLUE,
            "$\\quad \\mathbf{\\xi}$": BLUE
        })

        

        self.add(equation1)
        self.wait(1.8)
        self.play(FadeIn(texd2))
        self.wait(2.4)
        self.play(Write(equation2))
        self.add(texd2_copy)
        self.wait(0.5)
        self.play(Transform(texd2[2],equation2[1]))
        self.wait(1)
        self.play(FadeOut(texd2[2]),Transform(equation2,tex_eq3_guodu))
        self.wait(1.1)
        self.play(Transform(equation2,equation3))
        self.wait(1.6)
        self.play(GrowFromCenter(braces1),Write(eq_nabla))
        self.play(GrowFromCenter(braces2),Write(tex_nabla))

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        another_scene = gradient_of_map
        another_scene.construct(self)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.add(equation1,texd2[0],texd2[1],texd2[3],texd2_copy,equation2)

        self.wait(3.7)
        self.play(ShowCreation(tex_qitashuoming.bg))
        self.wait(0.8)
        self.play(Write(tex_qitashuoming))
        self.wait(2)

        self.play(
            FadeOut(texd2[0]),FadeOut(texd2[1]),FadeOut(texd2[3]),FadeOut(tex_qitashuoming),FadeOut(texd2_copy),FadeOut(equation2),FadeOut(tex_qitashuoming.bg),ApplyMethod(equation1.shift,2.5*DOWN),
            # All mobjects in the screen are saved in self.mobjects
        )
        self.play(ApplyMethod(equation1.scale,1.5))
        self.wait(2)
        

        #zoom in图上信息
        # zoomed_camera = self.zoomed_camera
        # zoomed_display = self.zoomed_display
        # frame = zoomed_camera.frame
        # zoomed_display_frame = zoomed_display.display_frame

        # frame.move_to(equation1)
        # frame.set_color(PURPLE)

        # zoomed_display_frame.set_color(RED)
        # zoomed_display.shift(2.5*DOWN)
        
        # zd_rect = BackgroundRectangle(
        #     zoomed_display,
        #     fill_opacity=0,
        #     buff=MED_SMALL_BUFF,
        # )

        # unfold_camera = UpdateFromFunc(
        #     zd_rect,
        #     lambda rect: rect.replace(zoomed_display)
        # )


        # self.play(
        #     ShowCreation(frame),
        # )

        # # Activate zooming
        # self.activate_zooming()

        # self.play(
        #     # You have to add this line
        #     self.get_zoomed_display_pop_out_animation(),
        #     unfold_camera
        # )
        # self.wait(2)

       


class state_estimate(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },

    "rotate_kwargs":{
        "about_point": [2.63897822,2.18502734,0.],
        "about_edge": None,
    }

    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen

        field =Vector(2*UP)
        field.set_color(BLUE) 
        field.shift(0.5*(DOWN+LEFT))

        field2 =Vector(2*RIGHT)
        field2.set_color(BLUE) 
        field2.move_to(field.get_start())
        field2.shift(RIGHT)

        field3 = Circle(fill_color=BLUE, fill_opacity=1, color=BLUE);
        field3.move_to(field.get_start())
        field3.scale(0.02)

        tex3 = TextMobject("O")
        tex3.scale(1.5)
        tex3.set_color(BLUE)
        tex3.next_to(field3,2.2*(DOWN)+2.2*LEFT)

        list=[]
        list.append(field)
        list.append(field2)
        list.append(field3)

        a = VGroup(*list)
        a.scale(1.5)
        a.shift(UP+RIGHT)
        tex3.shift(UP+RIGHT)

        b=a.copy()
        b.shift(RIGHT+2*UP)
        b.rotate(TAU/6)
        b.scale(0.5)
        b.set_color(YELLOW)

        fieldx = Vector(b[0].get_start()-a[0].get_start())
        fieldx.shift(a[0].get_start())
        fieldx.set_color(YELLOW)

        print(b[0].get_start())
        c = a.copy()


        d = a.copy()
        d.shift(4*LEFT+2*DOWN)
        d.set_color(RED)
        texd = TextMobject("S")
        texd.scale(1.5)
        texd.set_color(RED)
        texd.next_to(d,0.05*DOWN+0.05*LEFT)

        fieldx2 = Vector(a[0].get_start()-d[0].get_start())
        fieldx2.shift(d[0].get_start())
        fieldx2.set_color(BLUE)
        
        texd2 = TextMobject("\\che{重定位(Re-localization)}")
        texd2.next_to(fieldx2,1.4*DOWN)
        texd2.shift(0.6*RIGHT)

        texd3 = TextMobject("\\che{运动估计}")
        texd3.next_to(fieldx,0.8*DOWN)

        self.play(ShowCreation(field3),ShowCreation(tex3),rate=0.5)
        self.play(ShowCreation(field),ShowCreation(field2),rate=0.5)
        self.add(c)
        self.play(Transform(a,b),ShowCreation(texd3))
        self.play(ShowCreation(fieldx))
        self.play(Rotate(a,-TAU/10,**self.rotate_kwargs))
        self.play(Rotate(a,-TAU/10,**self.rotate_kwargs))

        for i in range(30):
            a.shift(0.0015*i*LEFT)
            fieldx.put_start_and_end_on(fieldx.get_start(),a[0].get_start())
            self.add(fieldx,a)
            self.wait(0.02)
        for i in range(30):
            a.shift(0.045*LEFT-0.0015*i*LEFT)
            fieldx.put_start_and_end_on(fieldx.get_start(),a[0].get_start())
            self.add(fieldx,a)
            self.wait(0.02)
        


        self.play(ShowCreation(d),ShowCreation(texd))
        self.play(ShowCreation(fieldx2),ApplyMethod(tex3.shift,0.8*RIGHT),ApplyMethod(texd3.shift,0.8*RIGHT),ShowCreation(texd2))
        

        self.wait(2)

        



class scan_matching(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen

        squarelist = []
        resultlist = []
        resultlist2= []

        points1 = [x*0.5*RIGHT+y*0.5*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,-4,1)
            ]     #List of vectors pointing to each grid point
        points2 = [x*0.5*RIGHT+y*0.5*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(4,5,1)
            ]     #List of vectors pointing to each grid point
        points3 = [0.5*x*RIGHT+0.5*y*UP
            for y in np.arange(-4,4,1)
            for x in np.arange(-5,-4,1)
            ]     #List of vectors pointing to each grid point
        points4 = [0.5*x*RIGHT+0.5*y*UP
            for y in np.arange(-4,4,1)
            for x in np.arange(4,5,1)
            ]     #List of vectors pointing to each grid point

        for point in points1:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=1)
            result = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)
        for point in points2:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=1)
            result = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)
        for point in points3:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=1)
            result = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)
        for point in points4:
            square=Square(side_length=0.5,fill_color=BLUE, fill_opacity=1)
            result = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result.scale(0.04)
            result.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            result2 = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
            result2.scale(0.04)
            result2.move_to(point+0.025*random.randint(0,9)*RIGHT+0.025*random.randint(0,9)*UP)

            square.move_to(point)
            squarelist.append(square)
            resultlist.append(result)

            resultlist2.append(result2)

        draw_field = VGroup(*squarelist)
        draw_field.shift(0.25*(UP+RIGHT))

        draw_field2 = VGroup(*resultlist)
        draw_field2.shift(0.25*(UP+RIGHT))

        draw_field3 = VGroup(*resultlist2)
        draw_field3.shift(0.25*(UP+RIGHT))

        #箭头
        field =Vector(UP)
        field.set_color(BLUE) 
        field.shift(0.5*DOWN)
        field.scale(0.7)

        field2 =Vector(UP)
        field2.set_color(YELLOW) 
        field2.shift(0.5*DOWN)
        field2.scale(0.7)

        self.play(GrowFromCenter(draw_field2),rate = 5)  
        self.wait(1)
        self.play(Transform(draw_field2,draw_field),ShowCreation(field),rate = 0.2)

        # self.play(FadeIn(draw_field3))
        # self.play(FadeOut(draw_field3))
        # self.play(FadeIn(draw_field3))
        # self.play(FadeOut(draw_field3))
        # self.play(FadeIn(draw_field3))
        # self.play(FadeOut(draw_field3))

        self.add(draw_field)

        draw_field3.rotate((-4)*TAU/60)
        field2.rotate((-4)*TAU/60)
        self.play(ShowCreation(draw_field3),ShowCreation(field2),rate=5)
        self.wait(0.5)
        tex=(TextMobject("Hits:"))
        tex.to_edge(UP+LEFT)
        tex.scale(1.5)
        for i in range(8,0,-1):
            self.play(Rotate(draw_field3,(i*math.pow(-1,i))*TAU/60),Rotate(field2,(i*math.pow(-1,i))*TAU/60))  
            self.wait(0.4)
            count = 0
            for square in draw_field:
                 #square.set_color(BLUE)
                 square_center = square.get_center()
                 squarelist.remove(square)
                 square = Square(side_length=0.5,fill_color=BLUE, fill_opacity=1)
                 square.move_to(square_center)
                 squarelist.append(square)
                 draw_field = VGroup(*squarelist)
                 self.add(draw_field)
                 for circle in draw_field3:
                      diff = circle.get_center()-square_center
                   #   print(diff)
                      if abs(diff[0])<0.251 and abs(diff[1])<0.251:
                          squarelist.remove(square)
                          square = Square(side_length=0.5,fill_color=YELLOW, fill_opacity=1)
                          square.move_to(square_center)
                          squarelist.append(square)
                          draw_field = VGroup(*squarelist)
                          count = count+1
                          break
                 self.add(draw_field)
                

            if i==8:              
                tex=(TextMobject("Hits:"+str(count)))
                tex.to_edge(UP+LEFT)
                tex.scale(1.5)
                self.play(ShowCreation(tex))
            else:
                tex2=(TextMobject("Hits:"+str(count)))
                tex2.to_edge(UP+LEFT)
                tex2.scale(1.5)
                self.play(Transform(tex,tex2))

            self.wait(0.5)
            
      
        


class localGaussian(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen
        vec_field = []  #Empty list to use in for loop
        draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup

        square=Square(side_length=1,fill_color=YELLOW, fill_opacity=1)
        square.move_to(0.5*(LEFT+UP))
	
        squarelist = []

        forlist = [-1,1]		
#================================定义9个小方块=============================#
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i+0.5)*(LEFT+UP))
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i-0.5)*(RIGHT+UP)+UP)
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((0.5+i)*UP+0.5*LEFT)
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i)*RIGHT+0.5*(LEFT+UP))
            squarelist.append(square)
        square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.8)
        square.move_to(0.5*(LEFT+UP))
        squarelist.append(square)
#================================定义9个小方块=============================#
        field = 0.5*RIGHT + 0.5*UP   #Constant field up and to right
   
        #生成一个机器人
        result = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
        result.scale(0.1)
        result.move_to(0.5*(LEFT+UP))
        self.add(result)

        draw_field = VGroup(*squarelist)
     
        eq0 = TextMobject("$\\mathbf{(\\mu^*_1,\\sigma^*_1)}$")
        eq0.scale(2)
        eq0.to_edge(UP)
        eq0.shift(1*DOWN)
        eq0.set_color(BLUE)

        eq1 = TextMobject("$\\mathbf{(\\mu^*_1,\\sigma^*_1),(\\mu^*_2,\\sigma^*_2),\\cdots,(\\mu^*_9,\\sigma^*_9)}$")
        eq1.scale(2)
        eq1.to_edge(UP)
        eq1.shift(1*DOWN)
        eq1.set_color(BLUE)

        eq2 = TextMobject("$\\mathbf{(\\mu^*_s,\\sigma^*_s)}$")
        eq2.scale(2)
        eq2.shift(1.5*DOWN)
        eq2.set_color(YELLOW)
#===============================动作=============================#
        self.add_foreground_mobjects(result ) #将箭头置于上层

        self.play(GrowFromCenter(draw_field),rate = 5)
        self.play(ApplyMethod(draw_field.shift,UP),ApplyMethod(result.shift,UP+0.1*RIGHT))
        self.play(ApplyMethod(draw_field.shift,RIGHT),ApplyMethod(result.shift,RIGHT+0.1*DOWN))
        self.play(ApplyMethod(draw_field.shift,2*DOWN),ApplyMethod(result.shift,2*DOWN+0.1*DOWN))
        self.play(ApplyMethod(draw_field.shift,RIGHT),ApplyMethod(result.shift,RIGHT+0.1*LEFT))
        self.play(ApplyMethod(draw_field.shift,DOWN),ApplyMethod(result.shift,DOWN+0.05*LEFT))
        self.play(ApplyMethod(draw_field.shift,2*RIGHT),ApplyMethod(result.shift,2*RIGHT+0.1*UP))
        self.play(FadeOut(plane))
        self.play(Transform(squarelist[1],eq0))
        self.wait(2)
        self.play(Transform(squarelist[1],eq1))
        self.wait(3)
        self.play(Transform(squarelist[1],eq2)) 
        self.wait(5)
#===============================动作=============================#


	
       # self.play(ShowCreation(draw_field))   #Draw VGroup on screen


class Shapes(Scene):
    #A few simple shapes
    #Python 2.7 version runs in Python 3.7 without changes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.add(line)

class MoreShapes(Scene):
    #A few more simple shapes
    #2.7 version runs in 3.7 without any changes
    #Note: I fixed my 'play command not found' issue by installing sox
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class MovingShapes(Scene):
    #Show the difference between .shift() and .move_to
    #move_to是移动到某个地方，shift是移动多少
    def construct(self):
        circle=Circle(color=TEAL_A)
        circle.move_to(LEFT)
        square=Circle()
        square.move_to(LEFT+3*DOWN)

        self.play(GrowFromCenter(circle), GrowFromCenter(square), rate=5)
        self.play(ApplyMethod(circle.move_to,RIGHT), ApplyMethod(square.move_to,UP))
        self.play(ApplyMethod(circle.move_to,RIGHT+UP), ApplyMethod(square.shift,RIGHT+UP))
        self.play(ApplyMethod(circle.move_to,LEFT+UP), ApplyMethod(square.shift,LEFT+UP))

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))
        ###Try uncommenting the following###
        #self.play(ApplyMethod(second_line.move_to, LEFT_SIDE-2*LEFT))
        #self.play(ApplyMethod(my_first_text.next_to,second_line))


class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("\\che{高斯过程回归}").scale(1.5)
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("\\che{局部高斯过程回归}").scale(1.5)
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
 	
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))

class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label)  #Order matters
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))

class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))

class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }",r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))



class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))


class UsingBracesConcise(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]
        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        eq2_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group=VGroup(eq1,eq2)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),

    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)



        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))


    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=TOP)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()


class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : { 
        "x_line_frequency" : 2,
        "y_line_frequency" :2
        }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        #self.wait()

class SimpleField(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]     #List of vectors pointing to each grid point

        vec_field = []  #Empty list to use in for loop
        for point in points:
            field = 0.5*RIGHT + 0.5*UP   #Constant field up and to right
            result = Vector(field).shift(point)   #Create vector and shift it to grid point
            vec_field.append(result)   #Append to list

        draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup


        self.play(ShowCreation(draw_field))   #Draw VGroup on screen


class FieldWithAxes(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.play(ShowCreation(field))


    def calc_field(self,point):
        #This calculates the field at a single point.
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)  #Try one of these two fields
        #efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3  #Try one of these two fields
        return Vector(efield).shift(point)

class ExampleThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.set_camera_orientation(phi=PI/3,gamma=PI/5)
        self.play(ShowCreation(field2D))
        self.wait()
        #self.move_camera(gamma=0,run_time=1)   #Doesn't work in most recent commit
        #self.move_camera(phi=3/4*PI, theta=-PI/2)   #Doesn't work in most recent commit
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)

    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)


class EFieldInThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        field3D = VGroup(*[self.calc_field3D(x*RIGHT+y*UP+z*OUT)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            for z in np.arange(-5,5,1)])



        self.play(ShowCreation(field3D))
        self.wait()
        #self.move_camera(0.8*np.pi/2, -0.45*np.pi)   #Doesn't work in most recent commit
        self.begin_ambient_camera_rotation()
        self.wait(6)


    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def calc_field3D(self,point):
        x,y,z = point
        Rx,Ry,Rz = self.point_charge_loc
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2+(z-Rz)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)
        return Vector(efield).shift(point)


class MovingCharges(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def moving_charge(self):
        numb_charges=4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles:
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class FieldOfMovingCharge(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0))
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)

    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r<0.0000001:   #Prevent divide by zero
            efield = np.array((0,0,0))  
        else:
            efield = (observation_point - source_point)/r**3
        return efield



    def moving_charge(self):
        numb_charges=3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(self.source_charge, *[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles[1:]:
            particle.velocity = np.array((0,0,0))
        self.play(FadeIn(particles[1:]))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)


    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration

            for v in self.field:
                field_vect=np.zeros(3)
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())

            for p in self.moving_particles:
                accel = np.zeros(3)
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3


class StickMan(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "stick_man",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "height" : 3,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        self.head.set_fill(self.color, opacity = 1)
        self.body.set_fill(RED, opacity = 1)
        self.arms.set_fill(YELLOW, opacity = 1)
        self.legs.set_fill(BLUE, opacity = 1)
        return self

class Waving(Scene):
    def construct(self):
        start_man = StickMan()
        plain_man = StickMan()
        waving_man = StickMan("wave")

        self.add(start_man)
        self.wait()
        self.play(Transform(start_man,waving_man))
        self.play(Transform(start_man,plain_man))

        self.wait()

class CirclesAndSquares(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "circles_and_squares",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "height" : 3,
        "start_corner" : None,
        "circle_index" : 0,
        "line1_index" :1,
        "line2_index" : 2,
        "square1_index" : 3,
        "square2_index" : 4,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "circles_and_squares_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.circle = self.submobjects[self.circle_index]
        self.line1 = self.submobjects[self.line1_index]
        self.line2 = self.submobjects[self.line2_index]
        self.square1 = self.submobjects[self.square1_index]
        self.square2 = self.submobjects[self.square2_index]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        self.name_parts()
        self.circle.set_fill(RED, opacity = 1)
        self.line1.set_fill(self.color, opacity = 0)
        self.line2.set_fill(self.color, opacity = 0)
        self.square1.set_fill(GREEN, opacity = 1)
        self.square2.set_fill(BLUE, opacity = 1)
        return self


class SVGCircleAndSquare(Scene):
    def construct(self):
        thingy = CirclesAndSquares()

        self.add(thingy)
        self.wait()

if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'manim_tutorial_P37'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  #Does not play files
