from manim import *

class Problem167AnimBianrySearch(Scene):
    def construct(self):
        FONT="Consolas for Powerline"
        nums = [2, 7, 11, 15]

        # 数组
        array = VGroup()
        for n in nums:
            square = Square(side_length=1.0)
            num_text = Text(str(n), font_size=36, font=FONT)
            ele = VGroup(square, num_text)
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

        # target
        target_text = Text("target: 9", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)

        self.play(Create(array), Create(indices), Create(ptr_i), Create(target_text))
        self.wait(1)

        # step1
        desc_text = Text("i=0,定位数字为2,在索引[1,3]的范围内进行二分查找", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        # 左指针
        arrow_left = Arrow(DOWN, UP).scale(0.5)
        arrow_left.tip.scale(0.5)
        arrow_left_text = Text("left", font_size=25, font=FONT).next_to(arrow_left, DOWN, buff=0.2)
        ptr_left = VGroup(arrow_left, arrow_left_text)
        ptr_left.next_to(indices[1], DOWN, buff=0.2)
        
        # 右指针
        arrow_right = Arrow(DOWN, UP).scale(0.5)
        arrow_right.tip.scale(0.5)
        arrow_right_text = Text("right", font_size=25, font=FONT).next_to(arrow_right, DOWN, buff=0.2)
        ptr_right = VGroup(arrow_right, arrow_right_text)
        ptr_right.next_to(indices[3], DOWN, buff=0.2)

        self.play(Create(ptr_left), Create(ptr_right))

        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=3,mid=2,nums[mid]为11", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(0.5)
        self.play(FadeOut(desc_text))
        desc_text = Text("2+11>9,需要在左区间寻找更小的值,right移动到mid左边", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        self.play(ptr_right.animate.next_to(indices[2], DOWN, buff=0.2))
        self.wait(1)

        # step2
        self.play(FadeOut(desc_text))
        desc_text = Text("left=1,right=2,mid=1,nums[mid]为7", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(0.5)
        self.play(FadeOut(desc_text))
        desc_text = Text("2+7=9,找到答案,返回结果", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)        

class Problem167AnimTwoPointers(Scene):
    def construct(self):
        FONT="Consolas for Powerline"
        nums = [2, 7, 11, 15]

         # 数组
        array = VGroup()
        for n in nums:
            square = Square(side_length=1.0)
            num_text = Text(str(n), font_size=36, font=FONT)
            ele = VGroup(square, num_text)
            array.add(ele)

        array.arrange(RIGHT, buff=0).shift(UP * 2)

        # 索引
        indices = VGroup()
        for i in range(len(nums)):
            idx_text = Text(str(i), font_size=36, font=FONT)
            idx_text.next_to(array[i], DOWN, buff=0.3)
            indices.add(idx_text)

        # 左指针
        arrow_left = Arrow(UP, DOWN).scale(0.5)
        arrow_left.tip.scale(0.5)
        arrow_left_text = Text("left", font_size=25, font=FONT).next_to(arrow_left, UP, buff=0.2)
        ptr_left = VGroup(arrow_left, arrow_left_text)
        ptr_left.next_to(array[0], UP, buff=0.2)

        # 右指针
        arrow_right = Arrow(UP, DOWN).scale(0.5)
        arrow_right.tip.scale(0.5)
        arrow_right_text = Text("right", font_size=25, font=FONT).next_to(arrow_right, UP, buff=0.2)
        ptr_right = VGroup(arrow_right, arrow_right_text)
        ptr_right.next_to(array[3], UP, buff=0.2)

        # target
        target_text = Text("target: 9", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)

        self.play(Create(array), Create(indices), Create(ptr_left), Create(ptr_right), Create(target_text))
        self.wait(1)

        # step1
        desc_text = Text("left=0,right=3,分别指向数字2和15", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        self.play(FadeOut(desc_text))
        desc_text = Text("2+15>9,需要更小的数字,所以右指针向左移动", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        self.play(ptr_right.animate.next_to(array[2], UP, buff=0.2))
        self.wait(1)

        # step2
        self.play(FadeOut(desc_text))
        desc_text = Text("left=0,right=2,分别指向数字2和11", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        self.play(FadeOut(desc_text))
        desc_text = Text("2+11>9,需要更小的数字,所以右指针向左移动", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        self.play(ptr_right.animate.next_to(array[1], UP, buff=0.2))
        self.wait(1)

        # step3
        self.play(FadeOut(desc_text))
        desc_text = Text("left=0,right=1,分别指向数字2和7", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)

        self.play(FadeOut(desc_text))
        desc_text = Text("2+7=9,找到答案,返回结果", font_size=30, font=FONT).shift(DOWN * 2)
        self.play(Create(desc_text))
        self.wait(1)
