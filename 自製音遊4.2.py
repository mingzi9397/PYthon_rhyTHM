import pygame
import time

pygame.init()
wn = pygame.display.set_mode((1000,600))    # 建立視窗
pygame.display.set_caption("自主學習 : 自製音遊")    # 視窗名稱


# global variables 全域變數
running = True
mouse = ""
loop_start_time = 0
start_time = 0
time_pass = 0
started = False
open_menu = False
music_confirm1 = False
music_confirm2 = False
settlement1 = False
settlement2 = False
drop_before_arrive = 0.8     # 音符到達判定線前幾秒要出現
pixel_per_second = 600 / drop_before_arrive   # 音符速度
showing_array1 = []
showing_array2 = []
pointer = 0
perfect = 0
great = 0
good = 0
miss = 0


# objects 物件
    # 圖片載入
bar = pygame.image.load("bar.jpg")   # 單壓音符圖片
start_menu = pygame.image.load("start_menu.jpg")     # 起始背景圖片
start_button = pygame.image.load("start_button.png")    # 開始按鈕
back_button = pygame.image.load("back_button.png")      # 返回按鈕
skip_button = pygame.image.load("skip_button.png")      # 跳過按鈕
World_Vanquisher_jacket = pygame.image.load("World_Vanquisher-jacket.webp")   
padoru_jacket = pygame.image.load("padoru_jacket.png")

    # 大小調整
bar = pygame.transform.scale(bar, (63,20))   
start_menu = pygame.transform.scale(start_menu, (1000,600))
start_button = pygame.transform.scale(start_button, (200, 60))
back_button = pygame.transform.scale(back_button, (50,50))
skip_button = pygame.transform.scale(skip_button, (50,50))
World_Vanquisher_jacket = pygame.transform.scale(World_Vanquisher_jacket, (400,400))
padoru_jacket = pygame.transform.scale(padoru_jacket, (400,400))

    # 圖形繪畫(x位置, y位置, x長度, y長度)
back_pic = pygame.Rect(0, 0, 1000, 600)    
left_border = pygame.Rect(238, 0, 10, 600)
right_border = pygame.Rect(752, 0, 10, 600)
display_pressed1 = pygame.Rect(248, 500, 63, 30)
display_pressed2 = pygame.Rect(311, 500, 63, 30)
display_pressed3 = pygame.Rect(374, 500, 63, 30)
display_pressed4 = pygame.Rect(437, 500, 63, 30)
display_pressed5 = pygame.Rect(500, 500, 63, 30)
display_pressed6 = pygame.Rect(563, 500, 63, 30)
display_pressed7 = pygame.Rect(626, 500, 63, 30)
display_pressed8 = pygame.Rect(689, 500, 63, 30)

display_pressed1_1 = pygame.Rect(248, 0, 63, 500)
display_pressed2_1 = pygame.Rect(311, 0, 63, 500)
display_pressed3_1 = pygame.Rect(374, 0, 63, 500)
display_pressed4_1 = pygame.Rect(437, 0, 63, 500)
display_pressed5_1 = pygame.Rect(500, 0, 63, 500)
display_pressed6_1 = pygame.Rect(563, 0, 63, 500)
display_pressed7_1 = pygame.Rect(626, 0, 63, 500)
display_pressed8_1 = pygame.Rect(689, 0, 63, 500)

display_pressed1_2 = pygame.Rect(248, 530, 63, 70)
display_pressed2_2 = pygame.Rect(311, 530, 63, 70)
display_pressed3_2 = pygame.Rect(374, 530, 63, 70)
display_pressed4_2 = pygame.Rect(437, 530, 63, 70)
display_pressed5_2 = pygame.Rect(500, 530, 63, 70)
display_pressed6_2 = pygame.Rect(563, 530, 63, 70)
display_pressed7_2 = pygame.Rect(626, 530, 63, 70)
display_pressed8_2 = pygame.Rect(689, 530, 63, 70)

    # 音訊載入
track1 = pygame.mixer.Sound("World Vanquisher.mp3")
track2 = pygame.mixer.Sound("Padoru Padoru ♪(Azure Project Remix).mp3")

    # 字型載入(檔案路徑, 大小)
font1 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\worldofwater\WORLDOFW.TTF", 32)   
font2 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\worldofwater\WORLDOFW.TTF", 50)
font3 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\worldofwater\WORLDOFW.TTF", 30)
font4 = pygame.font.Font("freesansbold.ttf", 65)
font5 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\標楷體.ttc", 31)
font6 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\標楷體.ttc", 65)
font7 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\worldofwater\WORLDOFW.TTF", 60)
font8 = pygame.font.Font("C:/Users/user\Desktop\.spyder-py3\worldofwater\WORLDOFW.TTF", 40)


# files 檔案

times_arrive1 = []
times_drop1 = []
notes1 = []
times_arrive2 = []
times_drop2 = []
notes2 = []
note_dict = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7}    # 配合音符陣列(note編號:key編號)

   # World Vanquisher 譜面載入
with open(f"note_and_time\\times_world_vanquisher.txt","r") as time_f:   # 載入WV譜面對照時間
    for i in time_f:
        i = int(i)
        i /= 1000
        i = round(i, 4)  # 小數點後第四位四捨五入
        times_arrive1.append(i)

with open(f"note_and_time\\notes_world_vanquisher.txt","r") as note_f:   # 載入WV譜面對照位置
    for i in note_f:
        i = int(i)
        i = note_dict[i]
        notes1.append(i)

for i in times_arrive1:
    i -= drop_before_arrive   
    i = round(i, 4)
    times_drop1.append(i)

   # padoru 譜面載入
with open(f"note_and_time\\times_padoru.txt","r") as time_f: # 載入Padoru譜面對照時間
    for i in time_f:
        i = int(i)
        i /= 1000
        i = round(i, 4)  
        times_arrive2.append(i)

with open(f"note_and_time\\notes_padoru.txt","r") as note_f: # 載入Padoru譜面對照位置
    for i in note_f:
        i = int(i)
        i = note_dict[i]
        notes2.append(i)

for i in times_arrive2:
    i -= drop_before_arrive   # dropping rate
    i = round(i, 4)
    times_drop2.append(i)


# class 

class Note():
    def __init__(self, drop_time, arrive_time, xcor, ycor, block):
        self.drop_time = drop_time
        self.arrive_time = arrive_time
        self.xcor = xcor
        self.ycor = ycor
        self.block = block
        self.hit = False
        self.show = True
    
    def ycor_update(self, time_pass):
        p = time_pass - self.drop_time # 開始墜落後經過的時間。
        # 上面的時間 * 像素每秒 - (目前位置 + 60) = 要增加的座標 (60 是測試出來的緩衝座標)
        self.ycor += pixel_per_second * p - (self.ycor + 60) 

    def check_remove_perfect(self, time_pass):
        block_check = keys[self.block]
        time_check = abs(time_pass - self.arrive_time) <= 0.0617
        return block_check and time_check 
    
    def check_remove_great(self, time_pass):
        block_check = keys[self.block]
        time_check = 0.0617 < abs(time_pass - self.arrive_time) <= 0.1033
        return block_check and time_check
    
    def check_remove_good(self, time_pass):
        block_check = keys[self.block]
        time_check = 0.1033 < abs(time_pass - self.arrive_time) <= 0.1283
        return block_check and time_check
    
    def check_remove_miss(self, time_pass):
           block_check = keys[self.block]
           time_check = 0.1283 < abs(time_pass - self.arrive_time) <= 0.14
           return block_check and time_check 


def showingArray_appending(time_pass):
    global showing_array1
    global showing_array2
    global pointer
    coresponding_location = [248, 311, 374, 437, 500, 563, 626, 689, 752] # xcor 定位用
    coresponding_key = {0: pygame.K_s, 1: pygame.K_d, 2: pygame.K_f, 3: pygame.K_g, 4: pygame.K_h, 5: pygame.K_j, 6: pygame.K_k, 7: pygame.K_l} # block 定位用
    
    if music_confirm1:   #如果確認 World Vanquisher，載入 World Vanquisher 的譜面
       while pointer < len(times_drop1) and abs(time_pass - times_drop1[pointer]) <= 0.1:
           # Note(drop_time, arrive_time, xcor, ycor, block)
           one_note = Note(times_drop1[pointer], times_arrive1[pointer], coresponding_location[notes1[pointer]], -100, coresponding_key[notes1[pointer]])
           showing_array1.append(one_note)
           pointer += 1
           
    if music_confirm2:   #如果確認 padoru，載入 padoru 的譜面
       while pointer < len(times_drop2) and abs(time_pass - times_drop2[pointer]) <= 0.1:
           one_note = Note(times_drop2[pointer], times_arrive2[pointer], coresponding_location[notes2[pointer]], -100, coresponding_key[notes2[pointer]])
           showing_array2.append(one_note)
           pointer += 1


def note_displaying(time_pass):
    global showing_array1
    global showing_array2
    global miss
    for one_note in showing_array1:
        if one_note.show: 
            one_note.ycor_update(time_pass)              # 更新自己的 y 座標
            wn.blit(bar, (one_note.xcor, one_note.ycor)) # blit 到螢幕上
        if one_note.ycor >= 768:
            if one_note.show:
                miss += 1
                one_note.show = False
            
    for one_note in showing_array2:
        if one_note.show: 
            one_note.ycor_update(time_pass) 
            wn.blit(bar, (one_note.xcor, one_note.ycor)) 
        if one_note.ycor >= 768:
            if one_note.show:
                miss += 1
                one_note.show = False
        
        
def note_remove(time_pass):
    global showing_array1
    global showing_array2
    global perfect
    global great
    global good
    global miss
    for one_note in showing_array1:
       if one_note.show:
          if one_note.check_remove_perfect(time_pass):
              one_note.hit = True
              one_note.show = False
              perfect += 1
          if one_note.check_remove_great(time_pass):
              one_note.hit = True
              one_note.show = False
              great += 1
          if one_note.check_remove_good(time_pass):
              one_note.hit = False
              one_note.show = False
              good += 1  
          if one_note.check_remove_miss(time_pass):
              one_note.hit = False
              one_note.show = False
              miss += 1

    for one_note in showing_array2:
        if one_note.show:
           if one_note.check_remove_perfect(time_pass):
               one_note.hit = True
               one_note.show = False
               perfect += 1
           if one_note.check_remove_great(time_pass):
               one_note.hit = True
               one_note.show = False
               great += 1
           if one_note.check_remove_good(time_pass):
               one_note.hit = False
               one_note.show = False
               good += 1   
           if one_note.check_remove_miss(time_pass):
               one_note.hit = False
               one_note.show = False
               miss += 1


def combo_showing():   # combo 顯示
    # count combo
    combo = 0
    note_died_count = 0  # 已經有幾個不再顯示
    if music_confirm1:
       for one_note in showing_array1:
           if one_note.arrive_time + 0.14 < time_pass: # 判斷不再顯示的條件
               note_died_count += 1
       for i in range(note_died_count): # 在這些不顯示的音符裡面，有被打到 combo 就加一，否則歸零
           if showing_array1[i].hit:
               combo += 1
           else:
               combo = 0
            
    if music_confirm2:
       for one_note in showing_array2:
           if one_note.arrive_time + 0.14 < time_pass: # 判斷不再顯示的條件
               note_died_count += 1
       for i in range(note_died_count): # 在這些不顯示的音符裡面，有被打到 combo 就加一，否則歸零
           if showing_array2[i].hit:
               combo += 1
           else:
               combo = 0 
    
    # show combo
    if started:
       combo_show_word = font3.render(f'combo', True, (216,186,255))
       combo_show_combo = font4.render(f'{combo}', True, (216,186,255))
                                      # ^(顯示的字, 是否用滑順字體, 顏色)
       wn.blit(combo_show_word, (835, 270))
       wn.blit(combo_show_combo, (815, 200))

# functions 程式
def pre_time_handle():
    global loop_start_time   # loop 開始時間
    global start_time   # 遊戲開始時間
    global time_pass   # 遊戲開始後經過多少時間(秒)
    loop_start_time = time.time()
    if not started:
        start_time = loop_start_time
    time_pass = float(loop_start_time-start_time)   # 遊戲進行時間
    time_pass = round(time_pass,4) 

def post_time_handle(loop_start_time):
    now_end_time = time.time()
    now_end_time = round(now_end_time,4)
    loop_time = now_end_time-loop_start_time   # loop執行時間
    if loop_time < 0.001:
        time.sleep(0.001-loop_time)

def pygame_events(): # pygame 控制
    global running
    global mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = "up"
        if event.type != pygame.MOUSEBUTTONUP:
            mouse = ""
            
def draw_start():
    wn.blit(start_menu, (0,0))   # (開始畫面 ,位置)
    wn.blit(start_button, (400,360))   # (開始按鈕, 位置)
    text10 = font7.render(" PYthon rhyTHM ", True, (0,0,0), (216,186,255))                       
    wn.blit(text10, (300,200))

def draw_menu1():     # 選歌畫面繪製
    wn.blit(start_menu, (0,0))   
    wn.blit(back_button, (26,26))
    text1 = font1.render(" World Vanquisher ", True, (0,0,0), (222,43,182))                       
    wn.blit(text1, (130,150)) 
    text2 = font1.render(" Padoru Padoru~(Azure Project Remix) ", True, (0,0,0), (222,43,182))                       
    wn.blit(text2, (130,200))
    text7 = font2.render("                      MUSIC SELECT                     ", True, (0,0,0), (94,24,216))                       
    wn.blit(text7, (100,25))
    
def draw_confirm1():   # 確認畫面1繪製
    wn.blit(start_menu, (0,0))
    wn.blit(back_button, (26,26))
    text2 = font2.render(" World Vanquisher ", True, (0,0,0), (94,24,216))
    wn.blit(text2, (295,25))
    wn.blit(World_Vanquisher_jacket, (295,100)) #登登登圖片位置
    wn.blit(start_button, (395,520))  # 開始按鈕位置game

def draw_confirm2():   # 確認畫面2繪製
    wn.blit(start_menu, (0,0))
    wn.blit(back_button, (26,26))
    text6 = font2.render(" Padoru Padoru~(Azure Project Remix) ", True, (0,0,0), (94,24,216))
    wn.blit(text6, (115,25))
    wn.blit(padoru_jacket, (295,100)) # padoru圖片位置
    wn.blit(start_button, (395,520))  # 開始按鈕位置game

def draw_back():    # 遊戲畫面繪製
    pygame.draw.rect(wn, (106,14,159), back_pic)   # (視窗, 顏色, 物件)
    pygame.draw.rect(wn, (154,1,195), left_border)
    pygame.draw.rect(wn, (154,1,195), right_border)
    wn.blit(skip_button, (900,26))

def draw_judgementline(): # 判定線繪製
    # 垂直線判定區劃分線
    pygame.draw.line(wn, (172,142,207), (311,0), (311,600))   # (視窗, 顏色, 起點, 終點)
    pygame.draw.line(wn, (172,142,207), (374,0), (374,600))
    pygame.draw.line(wn, (172,142,207), (437,0), (437,600))
    pygame.draw.line(wn, (172,142,207), (500,0), (500,600))
    pygame.draw.line(wn, (172,142,207), (563,0), (563,600))
    pygame.draw.line(wn, (172,142,207), (626,0), (626,600))
    pygame.draw.line(wn, (172,142,207), (689,0), (689,600))
    # 水平判定區劃分線
    pygame.draw.line(wn, (180,176,186), (250,500), (750,500))
    pygame.draw.line(wn, (180,176,186), (250,530), (750,530))

def draw_press():   # 按鈕回饋
    if keys[pygame.K_s]:
        pygame.draw.rect(wn, (216,186,255), display_pressed1)   # (視窗, 顏色, 物件)
        pygame.draw.rect(wn, (184,100,210), display_pressed1_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed1_2)
    if keys[pygame.K_d]:
        pygame.draw.rect(wn, (216,186,255), display_pressed2)
        pygame.draw.rect(wn, (184,100,210), display_pressed2_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed2_2)
    if keys[pygame.K_f]:
        pygame.draw.rect(wn, (216,186,255), display_pressed3)
        pygame.draw.rect(wn, (184,100,210), display_pressed3_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed3_2)
    if keys[pygame.K_g]:
        pygame.draw.rect(wn, (216,186,255), display_pressed4)
        pygame.draw.rect(wn, (184,100,210), display_pressed4_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed4_2)
    if keys[pygame.K_h]:
        pygame.draw.rect(wn, (216,186,255), display_pressed5)
        pygame.draw.rect(wn, (184,100,210), display_pressed5_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed5_2)
    if keys[pygame.K_j]:
        pygame.draw.rect(wn, (216,186,255), display_pressed6)
        pygame.draw.rect(wn, (184,100,210), display_pressed6_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed6_2)
    if keys[pygame.K_k]:
        pygame.draw.rect(wn, (216,186,255), display_pressed7)
        pygame.draw.rect(wn, (184,100,210), display_pressed7_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed7_2)
    if keys[pygame.K_l]:
        pygame.draw.rect(wn, (216,186,255), display_pressed8)
        pygame.draw.rect(wn, (184,100,210), display_pressed8_1)
        pygame.draw.rect(wn, (184,100,210), display_pressed8_2)

              
def draw_settlement1(): # 結算畫面1繪製
    wn.blit(start_menu, (0,0))
    wn.blit(back_button, (26,26))
    text8 = font2.render("                      GAME RESULT                         ", True, (0,0,0), (94,24,216))
    wn.blit(text8,(85,25))
    text9 = font8.render(" World Vanquisher ", True, (0,0,0), (222,43,182))
    wn.blit(text9,(340,78))
    perfect_count = font7.render(f'perfect : {perfect}', True, (216,186,255))
    wn.blit(perfect_count,(365,200))
    great_count = font7.render(f'great : {great}', True, (240,69,202))
    wn.blit(great_count,(365,270))
    good_count = font7.render(f'good : {good}', True, (1,195,13))
    wn.blit(good_count,(365,340))
    miss_count = font7.render(f'miss : {miss}', True, (108,108,108))
    wn.blit(miss_count,(365,410))
    
def draw_settlement2(): # 結算畫面2繪製
    wn.blit(start_menu, (0,0))
    wn.blit(back_button, (26,26))
    text8 = font2.render("                      GAME RESULT                         ", True, (0,0,0), (94,24,216))
    wn.blit(text8,(85,25))
    text9 = font8.render(" Padoru Padoru~(Azure Project Remix) ", True, (0,0,0), (222,43,182))
    wn.blit(text9,(140,78))
    perfect_count = font7.render(f'perfect : {perfect}', True, (216,186,255))
    wn.blit(perfect_count,(365,200))
    great_count = font7.render(f'great : {great}', True, (240,69,202))
    wn.blit(great_count,(365,270))
    good_count = font7.render(f'good : {good}', True, (1,195,13))
    wn.blit(good_count,(365,340))
    miss_count = font7.render(f'miss : {miss}', True, (108,108,108))
    wn.blit(miss_count,(365,410))
    
def judgementline_display():  #判定線演出
    global started
    if started:
        draw_judgementline()

def game_display(mouse_pos): # 負責遊戲畫面
    global open_menu
    global music_confirm1
    global music_confirm2
    global started
    global started_time
    global time_pass
    global settlement1
    global settlement2
    
    if open_menu:
        draw_menu1()
    else:
        draw_start()
        if mouse == "up":
           if 600 > mouse_pos[0] > 400 and 420 > mouse_pos[1] > 360:
                   open_menu = True
       
    if music_confirm1:
        draw_confirm1()
    else:
        if mouse == "up":
            if 383 > mouse_pos[0] > 130 and 184 > mouse_pos[1] > 150:
                music_confirm1 = True
            if 76 > mouse_pos[0] > 26 and 76 > mouse_pos[1] > 26:
                open_menu = False
                
    if music_confirm2:
        draw_confirm2()
    else:
        if mouse == "up":
            if 668 > mouse_pos[0] > 130 and 234 > mouse_pos[1] > 200:
                music_confirm2 = True  
            if 76 > mouse_pos[0] > 26 and 76 > mouse_pos[1] > 26:
                open_menu = False

    if started == True:
        if music_confirm1:
            track1.set_volume(0.1)  # 音樂音量
            track1.play()
        elif music_confirm2: 
            track2.set_volume(0.1)  # 音樂音量
            track2.play()   # 開始放音樂
    else:
        if music_confirm1:
            track1.stop()
        elif music_confirm2:
            track2.stop()
                
    if started:
         draw_back()   # 開始就畫遊戲畫面
         draw_press()
    else:
        if music_confirm1:
          if mouse == "up":
              if 600 > mouse_pos[0] > 400 and 580 > mouse_pos[1] > 520:
                   started = True    # 遊戲開始
              if 76 > mouse_pos[0] > 26 and 76 > mouse_pos[1] > 26:
                  music_confirm1 = False

    if settlement1:
        draw_settlement1()
        if mouse == "up":
            if 76 > mouse_pos[0] > 26 and 76 > mouse_pos[1] > 26:
                settlement1 = False
    else:
        if music_confirm1:
           if started:
              if mouse == "up":
                  if 950 > mouse_pos[0] > 900 and 76 > mouse_pos[1] > 26:
                      started = False
                      settlement1 = True
                  
    if started:
         draw_back()   # 開始就畫上面的那些圖
         draw_press()
    else:                 
        if music_confirm2:
          if mouse == "up":
              if 600 > mouse_pos[0] > 400 and 580 > mouse_pos[1] > 520:
                   
                   started = True    # 遊戲開始
              if 76 > mouse_pos[0] > 26 and 76 > mouse_pos[1] > 26:
                  music_confirm2 = False
                  
    if settlement2:
        draw_settlement2()
        if mouse == "up":
            if 76 > mouse_pos[0] > 26 and 76 > mouse_pos[1] > 26:
                settlement2 = False
    else:
        if music_confirm2:
           if started:
              if mouse == "up":
                  if 950 > mouse_pos[0] > 900 and 76 > mouse_pos[1] > 26:
                      started = False
                      settlement2 = True  
                      
# game loop 遊戲迴圈
while running:
    pre_time_handle()
    
    mouse_pos = pygame.mouse.get_pos()   # 取得滑鼠座標
    keys = pygame.key.get_pressed()   # 取得鍵盤輸入
    pygame_events()
    
    game_display(mouse_pos)
    judgementline_display()
    
    showingArray_appending(time_pass)
    note_displaying(time_pass)
    note_remove(time_pass)
    combo_showing()
    
    
    pygame.display.update()   # 更新視窗
    post_time_handle(loop_start_time)
    
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


