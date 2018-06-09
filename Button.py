from tkinter import PhotoImage
import musicandbg as ms

script = []

file = open("./script.txt", "r", encoding = "UTF-8")
for row in file:
    row = str(row).strip('\ufeff\n\t')
    if(row != ''):
        script.append(row)
file.close()



class Event:
    s = ''
    ck = 0
    screen = 1
    music_controll = ms.Ｍusic()

    def conbined_function(a):     
        Event.next_page(a[0])    
        Event.situations(a)
        Event.person(a)

    def person(a):
                if(script[Event.ck - 1][0] == "紫"):
                    Event.refresh_image(a[2], "purpleshirts")
                elif(script[Event.ck -1][0] == "唐"):
                    Event.refresh_image(a[2], "tangsan")
                elif(script[Event.ck -1][0] == "素"):
                    Event.refresh_image(a[2], "susu")
                elif(script[Event.ck -1][0] == "金"):
                    Event.refresh_image(a[2], "dream")
                elif(script[Event.ck -1][0] == "孫"):
                    Event.refresh_image(a[2], "wookong")
                elif(script[Event.ck -1][0] == "佛"):
                    Event.refresh_image(a[2], "buddha")
                elif(script[Event.ck -1][0] == "佛"):
                    Event.refresh_image(a[2], "zeus")
                else:
                    Event.refresh_image(a[2], "")


    def next_page(txt):
        txt["state"] = "normal"
        txt.delete("1.0", "end-1c")
        txt.insert("1.0", script[Event.ck])
        txt["state"] = "disabled"
        txt.see("end")
        Event.ck += 1        

    def refresh_image(lbl, s1):
        if(s1 == ''):
            lbl["image"] = ''
        else:
            img = PhotoImage(file = "./pics/{}.gif".format(s1))
            lbl["image"] = img
            lbl.image = img

    def situations(a):        
                
                if(script[Event.ck - 1][:6] == "素：都不是啦"):
                    Event.refresh_image(a[1], "antibiotic")
                elif(script[Event.ck - 1][:6] == "唐：素素前！"):
                    Event.refresh_image(a[1], "susuforward")

                elif(script[Event.ck - 1][:6] == "靈感來了，佛"):
                    Event.music_controll.gai()
                elif(script[Event.ck - 1][:6] == "紫全：Cap"):
                    Event.music_controll.gai_stop()

                elif(script[Event.ck - 1][:6] == "喜帖：唐三藏！"):
                    Event.refresh_image(a[1], "invitation")
                elif(script[Event.ck - 1][:6] == "孫：接到師傅"):
                    Event.refresh_image(a[1], "jindocloud")
                elif(script[Event.ck - 1][:6] == "金：你我不同"):
                    Event.refresh_image(a[1], "fivefingermountain")
                elif(script[Event.ck - 1][:6] == "金：這是我們"):
                    Event.refresh_image(a[1], "kaoshung")
                elif(script[Event.ck - 1][:6] == "金：沒錯這就"):
                    Event.refresh_image(a[1], "hitdogbat")
                elif(script[Event.ck - 1][:6] == "金：是這樣說"):
                    Event.refresh_image(a[1], "blackmagicbat")
                elif(script[Event.ck - 1][:6] == "金：(滿臉不"):
                    Event.refresh_image(a[1], "jamesbond1")
                elif(script[Event.ck - 1][:6] == "金：那想必你"):
                    Event.refresh_image(a[1], "jamesbond2")
                elif(script[Event.ck - 1][:6] == "孫：你被仙人"):
                    Event.refresh_image(a[1], "jindocloud")
                elif(script[Event.ck - 1][:6] == "孫：師傅，五"):
                    Event.refresh_image(a[1], "smoking")
                elif(script[Event.ck - 1][:6] == "唐：叫悟淨天"):
                    Event.refresh_image(a[1], "darwin")
                elif(script[Event.ck - 1][:6] == "唐：你當初也"):
                    Event.refresh_image(a[1], "fivefingermountain")
                elif(script[Event.ck - 1][:6] == "唐：Jesu"):
                    Event.refresh_image(a[1], "christmassock")
                elif(script[Event.ck - 1][:6] == "佛：這就是聖"):
                    Event.refresh_image(a[1], "vasectomy")
                elif(script[Event.ck - 1][:6] == "唐：你幹嘛這"):
                    Event.refresh_image(a[1], "smoking")
                elif(script[Event.ck - 1][:6] == "唐：西天取經"):
                    Event.refresh_image(a[1], "westsky")
                elif(script[Event.ck - 1][:6] == "唐：恩恩Ze"):
                    Event.refresh_image(a[1], "zeus")
                elif(script[Event.ck - 1][:6] == "孫：那我們就"):
                    Event.refresh_image(a[1], "jindocloud")
                    Event.screen = 4
                elif(script[Event.ck - 1][:6] == "孫：好啊，欸"):
                    Event.refresh_image(a[1], "zeus")
                elif(script[Event.ck - 1][:9] == "神：吾乃天神，什麼"):
                    Event.refresh_image(a[1], "goldpaper")
                elif(script[Event.ck - 1][:6] == "神：當吾之年"):
                    Event.refresh_image(a[1], "eggplant1")
                elif(script[Event.ck - 1][:6] == "神：終有一日"):
                    Event.refresh_image(a[1], "eggplant2")
                elif(script[Event.ck - 1][:6] == "神：吾與吾友"):
                    Event.refresh_image(a[1], "shimachien")
                elif(script[Event.ck - 1][:6] == "孫：現在是想"):
                    Event.refresh_image(a[1], "wookongfight")
                elif(script[Event.ck - 1][:6] == "神：哼，吾之"):
                    Event.refresh_image(a[1], "laser")
                elif(script[Event.ck - 1][:6] == "唐：啊啊是雷"):
                    Event.refresh_image(a[1], "mirror")
                elif(script[Event.ck - 1][:6] == "唐：(走去踩"):
                    Event.refresh_image(a[1], "thompson")
                elif(script[Event.ck - 1][:6] == "唐：啊悟空，"):
                    Event.refresh_image(a[1], "jindocloud")
                elif(script[Event.ck - 1][:6] == "金：我們公司"):
                    Event.refresh_image(a[1], "maishiangchicken")
                elif(script[Event.ck - 1][:6] == "金：不喜歡垃"):
                    Event.refresh_image(a[1], "nowitzki")
                elif(script[Event.ck - 1][:6] == "金：有運動的"):
                    Event.refresh_image(a[1], "calculus")
                elif(script[Event.ck - 1][:6] == "金：阿唐真的"):
                    Event.refresh_image(a[1], "banana")
                elif(script[Event.ck - 1][:6] == "我這邊有一根"):
                    Event.refresh_image(a[1], "blackmagicbat")
                else:
                    if(Event.screen == 1):
                        Event.refresh_image(a[1], "city")
                    elif(Event.screen == 4):
                        Event.refresh_image(a[1], "olympus")
    

    












