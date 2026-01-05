from manim import *

class Problem3Anim1(Scene):
    def construct(self):
        FONT="Consolas for Powerline"
        chars = ['t', 'm', 'm', 'z', 'u', 'x', 't'] # 数组元素

        array = VGroup() # 数组
        for ch in chars:
            square = Square(side_length=1.0) # 方块
            ch_text = Text(str(ch), font_size=36, font=FONT) # 方块中的文本
            ele = VGroup(square, ch_text) # 成一组
            array.add(ele) # 添加到数组中

        array.arrange(RIGHT, buff=0).shift(UP * 2) # 数组水平排放，间距为0

        indices = VGroup() # 下标
        for i in range(len(chars)):
            idx_text = Text(str(i), font_size=36, font=FONT) # 索引文本
            idx_text.next_to(array[i], DOWN, buff=0.3) # 索引放在方块下方
            indices.add(idx_text)

        # 左指针
        arrow1 = Arrow(UP, DOWN).scale(0.5)
        arrow1.tip.scale(0.5)
        arrow1_text = Text("idx", font_size=25, font=FONT).next_to(arrow1, UP, buff=0.2)
        ptr_left = VGroup(arrow1, arrow1_text)
        ptr_left.next_to(array[0], UP, buff=0.2)

        # 右指针
        arrow2 = Arrow(DOWN, UP).scale(0.5)
        arrow2.tip.scale(0.5)
        arrow2_text = Text("i", font_size=25, font=FONT).next_to(arrow2, DOWN, buff=0.2)
        ptr_right = VGroup(arrow2, arrow2_text)        
        ptr_right.next_to(indices[0], DOWN, buff=0.2)

        hash_text = Text("hash_map", font_size=25, font=FONT).shift(LEFT*5.7)
        len_text = Text("max_len: 0", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)

        self.play(Create(array), Create(indices))
        self.play(Create(ptr_left), Create(ptr_right), Create(hash_text), Create(len_text))
        self.wait()

        # step1
        desc_text = Text("i=0,字符t第一次出现,记录t的索引位置0,更新长度为1,右指针i继续向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(1)

        t_text = Text("t", font_size=25, font=FONT)
        t_arrow = Arrow(LEFT, RIGHT).next_to(t_text, RIGHT, buff=0).scale(0.5)
        t_arrow.tip.scale(0.5)
        t_idx = Text("0", font_size=25, font=FONT).next_to(t_arrow, RIGHT, buff=0.3)
        t_hash = VGroup(t_text, t_arrow, t_idx).shift(LEFT*6.5, DOWN*0.5)
        self.play(Create(t_hash))
        new_len_text = Text("max_len: 1", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)
        self.play(Transform(len_text, new_len_text))
        self.play(ptr_right.animate.next_to(indices[1], DOWN, buff=0.2))
        self.wait(1)

        # step2
        self.play(FadeOut(desc_text))
        desc_text = Text("i=1,字符m第一次出现,记录m的索引位置1,更新长度为2,右指针i继续向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(1)

        m_text = Text("m", font_size=25, font=FONT)
        m_arrow = Arrow(LEFT, RIGHT).next_to(m_text, RIGHT, buff=0).scale(0.5)
        m_arrow.tip.scale(0.5)
        m_idx = Text("1", font_size=25, font=FONT).next_to(m_arrow, RIGHT, buff=0.3)
        m_hash = VGroup(m_text, m_arrow, m_idx).next_to(t_hash, DOWN, buff=0.2)
        self.play(Create(m_hash))
        new_len_text = Text("max_len: 2", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)
        self.play(Transform(len_text, new_len_text))
        self.play(ptr_right.animate.next_to(indices[2], DOWN, buff=0.2))
        self.wait(1)

        # step3
        self.play(FadeOut(desc_text))
        desc_text = Text("i=2,字符m在滑动窗口内已出现过一次,左指针idx定位到m上次出现位置的右侧,即索引2", font_size=20, font=FONT).shift(DOWN*3)
        ext_desc_text = Text("更新m的索引位置为2,右指针i继续向右移动", font_size=20, font=FONT).next_to(desc_text, DOWN, buff=0.05)
        self.play(Create(desc_text), Create(ext_desc_text))
        self.wait(1)

        self.play(ptr_left.animate.next_to(array[2], UP, buff=0.2))
        new_m_text = Text("m", font_size=25, font=FONT)
        new_m_arrow = Arrow(LEFT, RIGHT).next_to(new_m_text, RIGHT, buff=0).scale(0.5)
        new_m_arrow.tip.scale(0.5)
        new_m_idx = Text("2", font_size=25, font=FONT).next_to(new_m_arrow, RIGHT, buff=0.3)
        new_m_hash = VGroup(new_m_text, new_m_arrow, new_m_idx).next_to(t_hash, DOWN, buff=0.2)
        self.play(Transform(m_hash, new_m_hash))
        self.play(ptr_right.animate.next_to(indices[3], DOWN, buff=0.2))
        self.wait(1)

        # step4
        self.play(FadeOut(desc_text), FadeOut(ext_desc_text))
        desc_text = Text("i=3,字符z第一次出现,记录z的索引位置3,右指针i继续向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(1)

        z_text = Text("z", font_size=25, font=FONT)
        z_arrow = Arrow(LEFT, RIGHT).next_to(z_text, RIGHT, buff=0).scale(0.5)
        z_arrow.tip.scale(0.5)
        z_idx = Text("3", font_size=25, font=FONT).next_to(z_arrow, RIGHT, buff=0.3)
        z_hash = VGroup(z_text, z_arrow, z_idx).next_to(new_m_hash, DOWN, buff=0.2)
        self.play(Create(z_hash))
        self.play(ptr_right.animate.next_to(indices[4], DOWN, buff=0.2))
        self.wait(1)

        # step5
        self.play(FadeOut(desc_text))
        desc_text = Text("i=4,字符u第一次出现,记录u的索引位置4,更新长度为3,右指针i继续向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(1)

        u_text = Text("u", font_size=25, font=FONT)
        u_arrow = Arrow(LEFT, RIGHT).next_to(u_text, RIGHT, buff=0).scale(0.5)
        u_arrow.tip.scale(0.5)
        u_idx = Text("4", font_size=25, font=FONT).next_to(u_arrow, RIGHT, buff=0.3)
        u_hash = VGroup(u_text, u_arrow, u_idx).next_to(z_hash, DOWN, buff=0.2)
        self.play(Create(u_hash))
        new_len_text = Text("max_len: 3", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)
        self.play(Transform(len_text, new_len_text))
        self.play(ptr_right.animate.next_to(indices[5], DOWN, buff=0.2))
        self.wait(1)

        # step6
        self.play(FadeOut(desc_text))
        desc_text = Text("i=5,字符x第一次出现,记录x的索引位置4,更新长度为4,右指针i继续向右移动", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.wait(1)

        x_text = Text("x", font_size=25, font=FONT)
        x_arrow = Arrow(LEFT, RIGHT).next_to(x_text, RIGHT, buff=0).scale(0.5)
        x_arrow.tip.scale(0.5)
        x_idx = Text("5", font_size=25, font=FONT).next_to(x_arrow, RIGHT, buff=0.3)
        x_hash = VGroup(x_text, x_arrow, x_idx).next_to(u_hash, DOWN, buff=0.2)
        self.play(Create(x_hash))
        new_len_text = Text("max_len: 4", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)
        self.play(Transform(len_text, new_len_text))
        self.play(ptr_right.animate.next_to(indices[6], DOWN, buff=0.2))
        self.wait(1)

        # step7
        self.play(FadeOut(desc_text))
        desc_text = Text("i=6,字符t虽然已经出现过一次,不过上次出现的位置不在滑动窗口内,所以不视为重复元素", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        self.play(FadeOut(desc_text))
        desc_text = Text("更新长度为5,右指针i到达字符串末尾,遍历结束,获得结果最大长度为5", font_size=20, font=FONT).shift(DOWN*3)
        self.play(Create(desc_text))
        new_len_text = Text("max_len: 5", font_size=25, font=FONT).shift(LEFT*5.5, UP*2)
        self.play(Transform(len_text, new_len_text))
        self.wait(1)