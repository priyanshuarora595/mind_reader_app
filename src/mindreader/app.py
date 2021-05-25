"""
its a fun game
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random


class MindReader(toga.App):

    def clear_all(self,widget=None):
        self.bot_score.value = 0
        self.player_score.value = 0
        self.elem=['h','t']
        init=random.choice(self.elem)
        self.data=[]
        self.data.append(init)

    def check_4(self,widget):
        lt=self.data[-5:-2]
        ch=lt.count('h')
        ct=lt.count('t')
        res1=self.check_3(lt)
        if res1==self.data[-2]:
            return res1
        elif ch>ct:
            return 'h'
        elif ct>ch:
            return 't'

    def check_2(self,widget):
        ch=self.data.count('h')
        ct=self.data.count('t')
        if ch==ct:
            return self.data[-2]
        elif ch>ct:
            return 'h'
        else:
            return 't'

    def check_3(self,widget):
        res1=self.check_2(self.data)
        ch=self.data.count('h')
        ct=self.data.count('t')
        if res1==self.data[-2]:
            return res1
        elif ch>ct:
            return 'h'
        else:
            return 't'

    def score(self,x,y):
        if x==y:
            temp=int(self.bot_score.value)
            temp+=1
            self.bot_score.value=temp

        else:
            temp=int(self.player_score.value)
            temp+=1
            self.player_score.value=temp

    def call_h(self,widget):
        self.user_input='h'
        self.check()

    def call_t(self,widget):
        self.user_input='t'
        self.check()

    def check(self):
        self.data.append(self.user_input)
        l=len(self.data)
        if l==2:
            res=self.check_2(self.data)
            self.score(x=res,y=self.data[-1])
        elif l==3:
            res=self.check_3(self.data)
            self.score(x=res,y=self.data[-1])
        elif l>=4:
            res=self.check_4(self.data)
            self.score(x=res,y=self.data[-1])
            if int(self.bot_score.value)>=int(10):
                self.main_window.info_dialog(title="winner",message="Bot is the winner!!")
                self.clear_all()
            if int(self.player_score.value)>=int(10):
                self.main_window.info_dialog(title='winner',message="Player is the winner!!")
                self.clear_all()

    def startup(self):
        
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        main_box = toga.Box(style=Pack(direction=COLUMN,background_color='yellow'))

        label_box=toga.Box(style=Pack(direction=ROW,flex=2))
        score_box=toga.Box(style=Pack(direction=ROW,flex=2))
        choice_box=toga.Box(style=Pack(direction=ROW,flex=2))


        bot_label=toga.Label('BOT',style=Pack(flex=1,direction=COLUMN,padding_left=20,padding_right=10,padding_bottom=40,padding_top=20,font_size=40,color='green'))
        player_label=toga.Label('PLAYER',style=Pack(flex=1,direction=COLUMN,padding_right=80,padding_bottom=40,padding_top=20,font_size=40,color='red'))

        self.data=[] 

        self.bot_score = toga.TextInput(id='bot_score',style=Pack(flex=1,alignment='center',padding_left=60,padding_right=80,padding_bottom=40,padding_top=20,text_align='center',color='yellow',font_size=40),readonly=True)
        self.player_score = toga.TextInput(id='player_score',style=Pack(flex=1,alignment='center',padding_left=110,padding_right=40,padding_bottom=40,padding_top=20,text_align='center',color='yellow',font_size=40),readonly=True,)
        self.bot_score.value = int(0)
        self.player_score.value= int(0)

        heads_button = toga.Button("Heads",style=Pack(flex=1,alignment='center',text_align='center',padding_left=30,padding_right=70,padding_bottom=40,padding_top=20,font_size=40),on_press=self.call_h)
        tails_button = toga.Button("Tails",style=Pack(flex=1,alignment='center',text_align='center',padding_left=70,padding_right=40,padding_bottom=40,padding_top=20,font_size=40),on_press=self.call_t)
        clear_button = toga.Button("CLEAR",style=Pack(flex=1,alignment='center',text_align='center',padding=(0,5),font_size=40),on_press=self.clear_all)
        info_label1 = toga.Label("Start playing by choosing head or tails",style=Pack(flex=1,alignment='center',text_align='center',padding=(20,20,20,20),padding_right=30,font_size=20))
        info_label2 = toga.Label("Reach the score of 10 to win ",style=Pack(flex=1,alignment='center',text_align='center',padding=(20,20,20,20),padding_right=30,font_size=20))
        info_label3 = toga.Label("All the best",style=Pack(flex=1,alignment='center',text_align='center',padding=(20,20,20,20),padding_right=30,font_size=20))
        label_box.add(bot_label)
        label_box.add(player_label)
        score_box.add(self.bot_score)
        choice_box.add(heads_button)

        
        score_box.add(self.player_score)
        choice_box.add(tails_button)

        main_box.add(label_box)
        main_box.add(score_box)
        main_box.add(choice_box)
        main_box.add(clear_button)
        main_box.add(info_label1)
        main_box.add(info_label2)
        main_box.add(info_label3)

        self.main_window.content = main_box
        self.main_window.show()


def main():
    return MindReader("MindReader")