from manim import *

# [-1,0,1,2,-1,-4]

class Problem15Anim1(Scene):
    def construct(self):
        FONT="Consolas for Powerline"
        nums = [-4, -1, -1, 0, 1, 2]

        # 数组
        array = VGroup()
        for num in nums:
            square = Square(side_length=1.0) 
            ch_text = Text(str(num), font_size=36, font=FONT) 
            ele = VGroup(square, ch_text)
            array.add(ele)

        array.arrange(RIGHT, buff=0).shift(UP * 2) 

        # 索引
        indices = VGroup() 
        for i in range(len(nums)):
            idx_text = Text(str(i), font_size=36, font=FONT) 
            idx_text.next_to(array[i], DOWN, buff=0.3) 
            indices.add(idx_text)

        # i指针
        arrow_i = Arrow(UP, DOWN).scale(0.5)
        arrow_i.tip.scale(0.5)
        arrow_i_text = Text("i", font_size=25, font=FONT).next_to(arrow_i, UP, buff=0.2)
        ptr_i = VGroup(arrow_i, arrow_i_text)
        ptr_i.next_to(array[0], UP, buff=0.2)

        results_text = Text("results:", font_size=20, font=FONT).shift(LEFT*6)

        self.play(Create(array), Create(indices), Create(ptr_i), Create(results_text))
        self.wait(1)

        # step1
        desc_text = Text("i=0,以-4为定点,left指针指向索引1,right指针指向索引5", font_size=20, font=FONT).shift(DOWN*3)
        
        # 左指针
        arrow_left = Arrow(UP, DOWN).scale(0.5)
        arrow_left.tip.scale(0.5)
        arrow_left_text = Text("left", font_size=25, font=FONT).next_to(arrow_left, UP, buff=0.2)
        ptr_left = VGroup(arrow_left, arrow_left_text)
        ptr_left.next_to(array[1], UP, buff=0.2)

        # 右指针
        arrow_right = Arrow(DOWN, UP).scale(0.5)
        arrow_right.tip.scale(0.5)
        arrow_right_text = Text("right", font_size=25, font=FONT).next_to(arrow_right, DOWN, buff=0.2)
        ptr_right = VGroup(arrow_right, arrow_right_text)
        ptr_right.next_to(indices[5], DOWN, buff=0.2)

        self.play(Create(desc_text), Create(ptr_left), Create(ptr_right))
        self.wait(0.5)
        self.play(FadeOut(desc_text))
        desc_text = Text("-4-1+2<0,left指针向右移动,并且略过重复的元素-1", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_left.animate.next_to(array[2], UP, buff=0.2))
        self.play(ptr_left.animate.next_to(array[3], UP, buff=0.2))
        self.wait(1)

        # step2
        self.play(FadeOut(desc_text))
        desc_text = Text("i=0,left指针指向索引3,right指针指向索引5", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("-4+0+2<0,left指针向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_left.animate.next_to(array[4], UP, buff=0.2))
        self.wait(1)

        # step3
        self.play(FadeOut(desc_text))
        desc_text = Text("i=0,left指针指向索引4,right指针指向索引5", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("-4+1+2<0,left指针向右移动与right指针会合,结束此次查找,i指针向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_left.animate.next_to(array[5], UP, buff=0.2))
        self.play(ptr_i.animate.next_to(array[1], UP, buff=0.2))        
        self.wait(1)

        # step4
        self.play(FadeOut(desc_text))
        desc_text = Text("i=1,以-1为定点,left指针指向索引2,right指针指向索引5", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_left.animate.next_to(array[2], UP, buff=0.2), ptr_right.animate.next_to(indices[5], DOWN, buff=0.2))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("-1-1+2=0,找到一个结果并保存,之后left指针右移,right指针左移", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        result1_text = Text("[-1, -1, 2]", font_size=20, font=FONT).shift(LEFT*6, DOWN*0.5)
        self.play(Create(result1_text))
        self.play(ptr_left.animate.next_to(array[3], UP, buff=0.2), ptr_right.animate.next_to(indices[4], DOWN, buff=0.2))
        self.wait(1)

        # step5
        self.play(FadeOut(desc_text))
        desc_text = Text("i=1,left指针指向索引3,right指针指向索引4", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(0.5)
        
        self.play(FadeOut(desc_text))
        desc_text = Text("-1+0+1=0,找到一个结果并保存,之后left指针右移,right指针左移", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        result2_text = Text("[-1, 0, 1]", font_size=20, font=FONT).shift(LEFT*6, DOWN*1)
        self.play(Create(result2_text))
        self.play(ptr_left.animate.next_to(array[4], UP, buff=0.2), ptr_right.animate.next_to(indices[3], DOWN, buff=0.2))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("left和right指针移动之后,left在right的右边,结束此次查找,i指针向右移动并略过相同元素", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_i.animate.next_to(array[2], UP, buff=0.2))        
        self.play(ptr_i.animate.next_to(array[3], UP, buff=0.2))        
        self.wait(1)

        # step6
        self.play(FadeOut(desc_text))
        desc_text = Text("i=3,以0为定点,left指针指向索引4,right指针指向索引5", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_left.animate.next_to(array[4], UP, buff=0.2), ptr_right.animate.next_to(indices[5], DOWN, buff=0.2))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("0+1+2>0,right指针向左移动与left指针会合,结束此次查找,i指针向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[4], DOWN, buff=0.2))
        self.play(ptr_i.animate.next_to(array[4], UP, buff=0.2))  
        self.play(FadeOut(ptr_left))
        self.wait(1)

        # step7
        self.play(FadeOut(desc_text))
        desc_text = Text("i=4,以1为定点,由于数组是升序排列,之后的任意数字再加上1都不可能等于0,结束遍历,返回结果", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(1)

        # manim -pql test.py SquareToCircle
