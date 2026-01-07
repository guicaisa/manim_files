from manim import *

# [1,8,6,2,5,4,8,3,7]

class Problem11Anim1(Scene):
    def construct(self):
        FONT="Consolas for Powerline"
        nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]

        # 数组
        rects = VGroup()
        for n in nums:
            half = n / 4
            rect = Rectangle(width=0.5, height=half)
            rects.add(rect)

        rects.arrange(RIGHT, buff=0.5, aligned_edge=DOWN).shift(UP*2.5)

        array = VGroup()
        for i in range(len(nums)):
            n = nums[i]
            square = Square(side_length=1.0)
            num_text = Text(str(n), font_size=36, font=FONT)
            ele = VGroup(square, num_text).next_to(rects[i], DOWN, buff=0.1)
            array.add(ele)

        # 索引
        indices = VGroup()
        for i in range(len(nums)):
            idx_text = Text(str(i), font_size=36, font=FONT)
            idx_text.next_to(array[i], DOWN, buff=0.3)
            indices.add(idx_text)

        # max_area
        max_area_text = Text("max_area: 0", font_size=25, font=FONT).shift(LEFT*5.7, DOWN * 1.5)

        # 左指针
        arrow_left = Arrow(DOWN, UP).scale(0.5)
        arrow_left.tip.scale(0.5)
        arrow_left_text = Text("left", font_size=25, font=FONT).next_to(arrow_left, DOWN, buff=0.2)
        ptr_left = VGroup(arrow_left, arrow_left_text)
        ptr_left.next_to(indices[0], DOWN, buff=0.2)

        # 右指针
        arrow_right = Arrow(DOWN, UP).scale(0.5)
        arrow_right.tip.scale(0.5)
        arrow_right_text = Text("right", font_size=25, font=FONT).next_to(arrow_right, DOWN, buff=0.2)
        ptr_right = VGroup(arrow_right, arrow_right_text)
        ptr_right.next_to(indices[8], DOWN, buff=0.2)

        self.play(Create(rects), Create(array), Create(indices), Create(max_area_text), Create(ptr_left), Create(ptr_right))
        self.wait(1)

        # step1
        desc_text = Text("left=0,right=8,高为1,宽为8,面积为8,更新max_area为8", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        new_max_area_text = Text("max_area: 8", font_size=25, font=FONT).shift(LEFT*5.7, DOWN * 1.5)
        self.play(Transform(max_area_text, new_max_area_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,left指针右移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_left.animate.next_to(indices[1], DOWN, buff=0.2))
        self.wait(1)

        # step2
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=8,高为7,宽为7,面积为49,更新max_area为49", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        new_max_area_text = Text("max_area: 49", font_size=25, font=FONT).shift(LEFT*5.7, DOWN * 1.5)
        self.play(Transform(max_area_text, new_max_area_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[7], DOWN, buff=0.2))
        self.wait(1)

        # step3
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=7,高为3,宽为6,面积为18,无需更新max_area", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[6], DOWN, buff=0.2))
        self.wait(1)

        # step4
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=6,高为8,宽为5,面积为40,无需更新max_area", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[5], DOWN, buff=0.2))
        self.wait(1)

        # step5
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=5,高为4,宽为4,面积为16,无需更新max_area", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[4], DOWN, buff=0.2))
        self.wait(1)

        # step6
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=4,高为5,宽为3,面积为15,无需更新max_area", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[3], DOWN, buff=0.2))
        self.wait(1)

        # step7
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=3,高为2,宽为2,面积为4,无需更新max_area", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(ptr_right.animate.next_to(indices[2], DOWN, buff=0.2))
        self.wait(1)

        # step8
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=2,高为6,宽为1,面积为6,无需更新max_area", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(0.5)

        self.play(FadeOut(desc_text))
        desc_text = Text("移动短边,right指针左移", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.play(FadeOut(desc_text))
        desc_text = Text("right继续左移后与left指针相等,宽为0,面积为0,结束遍历,获得结果max_area为49", font_size=20, font=FONT).shift(DOWN * 3)
        self.play(Create(desc_text))
        self.wait(1)

