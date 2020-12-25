from transitions.extensions import GraphMachine

from utils import send_text_message, send_flex_message, send_push_message

from content import menu,pixiv,find_artwork_id,walk_around

from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage

import re
import urllib.request
import random
import zipfile
import shutil
#載入requests套件
import requests
#需要載入os套件，可處理文件和目錄
import os
import time


class TocMachine(GraphMachine):
    def __init__(self, driver,**machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.driver = driver
        self.stay = False
        self.in_pixiv = False
        self.in_artist = False
        self.last_state = "initial"
        self.correct_picture_url = []
        self.icon_url = []
        self.correct_title_name = []
        self.container = []
        self.title_page = []
        self.artist_name = []
        self.artist_page = []
        self.re_scraw = True
        self.correct = 0
        self.appear_list = []
        self.download_url = []


    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"
    
    def on_enter_menu(self, event):
        print("I'm entering menu")
        self.last_state = self.state
        user_id = event.source.user_id
        self.in_pixiv = False
        self.in_artist = False
        reply_token = event.reply_token
        send_flex_message(reply_token, f"menu", menu)

    def is_going_to_pixiv(self, event):
        text = event.message.text
        return text.lower() == "pixiv"
    
    def on_enter_pixiv(self, event):
        print("I'm entering pixiv")
        self.last_state = self.state
        self.in_artist = False
        user_id = event.source.user_id
        if(not self.in_pixiv):
            self.driver.get("https://www.pixiv.net/")
            reply_token = event.reply_token
            send_push_message(user_id, TextSendMessage(text='請稍後回應...'))
            time.sleep(3)

            container = self.driver.find_element_by_class_name("gtm-toppage-thumbnail-illustration-recommend-works-zone")
            picture = container.find_elements_by_tag_name("img")
            title = self.driver.find_elements_by_class_name("iasfms-4.hegAwd.gtm-toppage-thumbnail-illustration-recommend-works")
            artist = self.driver.find_elements_by_class_name("sc-1rx6dmq-2.eMBcTW.gtm-illust-recommend-user-name")
            picture_url = []
            icon_url = []
            title_name = []
            title_page = []
            artist_name = []
            artist_page = []
            j = 0
            k = 0
            for i in range(len(picture)):
                if(picture[i].get_attribute("class") == "rp5asc-10 leQnFG"):
                    picture_url.append(picture[i].get_attribute("src"))
                    picture_url[j] = "https://i.pixiv.cat/img-master" + picture_url[j][picture_url[j].find("/img/"):picture_url[j].rfind("_p0_")] + "_p0_master1200" + picture_url[j][-4:]
                    # print(picture_url[j])
                    j += 1
                else:
                    icon_url.append(picture[i].get_attribute("src"))
                    if(icon_url[k] != "https://s.pximg.net/common/images/no_profile_s.png"):
                        icon_url[k] = "https://i.pixiv.cat" + icon_url[k][icon_url[k].find("/user-profile/"):icon_url[k].rfind("_50")] + "_170" + icon_url[k][-4:]
                    # print(icon_url[k])
                    k += 1
            j = 0
            for i in range(len(title)):
                title_name.append(title[i].text)
                title_page.append(title[i].get_attribute("href"))
                # print(title_name[j],title_page[j])
                j += 1
            j = 0
            for i in range(len(artist)):
                artist_name.append(artist[i].text)
                artist_page.append(artist[i].get_attribute("href"))
                # print(artist_name[j],artist_page[j])
                j += 1
            # print(len(picture_url),len(icon_url),len(title_name))
            # print(len(pixiv["contents"])-1)
            for i in range(len(pixiv["contents"])-1):
                pixiv["contents"][i+1]["hero"]["url"] = picture_url[i]
                pixiv["contents"][i+1]["hero"]["action"]["uri"] = picture_url[i]
                pixiv["contents"][i+1]["body"]["contents"][0]["text"] = title_name[i]
                pixiv["contents"][i+1]["body"]["contents"][0]["action"]["uri"] = title_page[i]
                pixiv["contents"][i+1]["footer"]["contents"][0]["contents"][0]["url"] = icon_url[i]
                pixiv["contents"][i+1]["footer"]["contents"][0]["contents"][0]["action"]["uri"] = artist_page[i]
                pixiv["contents"][i+1]["footer"]["contents"][1]["contents"][0]["text"] = artist_name[i]

            send_flex_message(reply_token, f"pixiv", pixiv)
            self.in_pixiv = True    

    def is_going_to_find_pixiv_id(self, event):
        text = event.message.text
        user_pattern = r"(users )+[0-9]*"
        artwork_pattern = r"(artworks )+[0-9]*"
        if((re.fullmatch(user_pattern,text.lower())) != None):
            self.stay = True
        else:
            self.stay = False
        return ((re.fullmatch(user_pattern,text.lower())) != None) or ((re.fullmatch(artwork_pattern,text.lower())) != None)
    
    def on_enter_find_pixiv_id(self, event):
        print("I'm entering find_pixiv_id")
        self.last_state = self.state
        if(not self.in_artist):
            url = "https://www.pixiv.net/" + event.message.text.lower().replace(" ","/")
            print(url)
            reply_token = event.reply_token
            if(not IsConnection(url)):
                send_text_message(reply_token,"此id不存在")
                self.back_pixiv(event)
                return
            self.driver.get(url)
            time.sleep(3)
            if(self.stay): #找作者
                find_user_id = {
                    "type": "bubble",
                    "size": "giga",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg",
                            "size": "full",
                            "aspectMode": "cover"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                                "size": "full",
                                "aspectMode": "cover"
                            }
                            ],
                            "width": "100px",
                            "height": "100px",
                            "cornerRadius": "100px",
                            "offsetStart": "35%",
                            "position": "absolute",
                            "paddingAll": "none",
                            "offsetTop": "10%"
                        }
                        ],
                        "spacing": "none",
                        "position": "relative",
                        "width": "400px",
                        "height": "150px",
                        "paddingAll": "0px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "作者名稱",
                            "weight": "bold",
                            "style": "normal"
                        }
                        ],
                        "alignItems": "center"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "Pixiv",
                                "uri": "http://linecorp.com/"
                                },
                                "color": "#111111"
                            }
                            ],
                            "cornerRadius": "10px",
                            "borderColor": "#6C6C6C",
                            "borderWidth": "normal"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "Twitter",
                                "uri": "http://linecorp.com/"
                                },
                                "color": "#111111"
                            }
                            ],
                            "borderWidth": "normal",
                            "borderColor": "#6C6C6C",
                            "cornerRadius": "10px",
                            "margin": "10px"
                        }
                        ]
                    }
                }
                twitter, picture = True, True               
                tmp = self.driver.find_element_by_class_name("_2AOtfl9")
                twitter_url = ""
                try:
                    tmp_twitter_url = tmp.find_elements_by_tag_name("a")
                    for i in range(len(tmp_twitter_url)):
                        tmp_twitter_url[i] = tmp_twitter_url[i].get_attribute("href")
                        if(tmp_twitter_url[i].contain("twitter")):
                            twitter_url = tmp_twitter_url[i]
                            twitter_url = "https://twitter.com/" + twitter_url[twitter_url.find(".com%2" + "F")+7:]
                            break
                except:
                    twitter = False
                if(twitter_url == ""):
                    twitter = False
                tmp = self.driver.find_element_by_class_name("sc-1asno00-0.ihWmWP")
                artist_name = tmp.get_attribute("title")
                icon_url = tmp.find_element_by_tag_name("img").get_attribute("src")
                if(icon_url != "https://s.pximg.net/common/images/no_profile.png"):
                    icon_url = "https://i.pixiv.cat" + icon_url[icon_url.find("/user-profile/"):]
                try:
                    picture_url = self.driver.find_element_by_class_name("rp5asc-10.leQnFG").get_attribute("src")
                    picture_url = "https://i.pixiv.cat/img-master" + picture_url[picture_url.find("/img/"):picture_url.rfind("_p0_")] + "_p0_master1200" + picture_url[-4:]
                except:
                    picture = False
                find_user_id["header"]["contents"][1]["contents"][0]["url"] = icon_url
                find_user_id["body"]["contents"][0]["text"] = artist_name
                find_user_id["footer"]["contents"][0]["contents"][0]["action"]["uri"] = url
                if(twitter):
                    find_user_id["footer"]["contents"][1]["contents"][0]["action"]["uri"] = twitter_url
                else:
                    del find_user_id["footer"]["contents"][1]
                if(picture):
                    find_user_id["header"]["contents"][0]["url"] = picture_url
                else:
                    del find_user_id["header"]["contents"][0]
                send_flex_message(reply_token, f"find_pixiv_id", find_user_id)
                self.in_artist = True
            else: #找作品
                picture_url = self.driver.find_element_by_class_name("sc-1qpw8k9-1.fvHoJ").get_attribute("src")
                picture_url = "https://i.pixiv.cat/img-master" + picture_url[picture_url.find("/img/"):picture_url.rfind("_p0_")] + "_p0_master1200" + picture_url[-4:]
                tmp = self.driver.find_element_by_class_name("f30yhg-2.iKmMAb")
                artist_name = tmp.find_element_by_tag_name("div").get_attribute("title")
                icon_url = tmp.find_element_by_tag_name("img").get_attribute("src")
                if(icon_url != "https://s.pximg.net/common/images/no_profile_s.png"):
                    icon_url = "https://i.pixiv.cat" + icon_url[icon_url.find("/user-profile/"):icon_url.rfind("_50")] + "_170" + icon_url[-4:]
                artist_page = tmp.find_element_by_tag_name("a").get_attribute("href")
                title_page = url
                title_name = self.driver.find_element_by_class_name("sc-1u8nu73-3.feoVvS").text
                
                find_artwork_id["hero"]["url"] = picture_url
                find_artwork_id["hero"]["action"]["uri"] = picture_url
                find_artwork_id["body"]["contents"][0]["text"] = title_name
                find_artwork_id["body"]["contents"][0]["action"]["uri"] = title_page
                find_artwork_id["footer"]["contents"][0]["contents"][0]["url"] = icon_url
                find_artwork_id["footer"]["contents"][0]["contents"][0]["action"]["uri"] = artist_page
                find_artwork_id["footer"]["contents"][1]["contents"][0]["text"] = artist_name
                
                send_flex_message(reply_token, f"find_artwork_id", find_artwork_id)
                self.back_pixiv(event)


    def is_going_to_instruction(self, event):
        text = event.message.text
        return text.lower() == "instruction" 

    def on_enter_instruction(self, event):
        print("I'm entering instuction")
        user_id = event.source.user_id
        reply_token = event.reply_token
        if(self.last_state == "initial"):
            send_push_message(user_id, TextSendMessage(text='menu => 進入選單'))
            self.ins_back_ini()
        elif(self.last_state == "menu"):
            send_push_message(user_id, TextSendMessage(text='menu => 進入選單\n\npixiv => 進入pixiv小工具'))
            self.ins_back_menu()
        elif(self.last_state == "pixiv"):
            send_push_message(user_id, TextSendMessage(text='menu => 進入選單\n\nusers id => 找繪師 ex:users 1234\n\nartworks id => 找作品 ex:artworks 1234\n\nwa scraw_depth => 隨便看看，scraw_depth為爬蟲深度 ex:wa 20\n\nwa => 隨便看看，圖從上一次爬蟲之中隨機挑選出'))
            self.ins_back_pix()
        elif(self.last_state == "find_pixiv_id"):
            send_push_message(user_id, TextSendMessage(text='menu => 進入選單\n\npixiv => 回pixiv小工具\n\nad 年-月-日 => 找繪師從現在時間到某指定日期間的作品 ex:ad 2020-12-21\n\nrd 天數 => 找繪師從現在時間到幾天前之間的作品 ex:rd 10\n\ndownload => 透過網址下載圖片(圖片為透過ad、rd指令取得的那些，建議將網址複製到無痕視窗，如果用一般視窗開的話可能要先清一下紀錄0.0)'))
            self.ins_back_find()

    def is_going_to_find_artist_artwork(self, event):
        text = event.message.text

        absdate_pattern = r"(ad )+([0-9]*)+(-)+([0-9]*)+(-)+[0-9]*"
        reldate_pattern = r"(rd )+[0-9]*"
        return ((re.fullmatch(absdate_pattern,text.lower())) != None) or ((re.fullmatch(reldate_pattern,text.lower())) != None) 

    def on_enter_find_artist_artwork(self, event):
        print("I'm entering find_artist_artwork")
        text = event.message.text
        reply_token = event.reply_token
        user_id = event.source.user_id
        page = 2
        url = self.driver.current_url
        
        self.driver.get(url + "/artworks")
        print(self.driver.current_url)
        time.sleep(3)
        self.download_url = []

        absdate_pattern = r"(ad )+([0-9]*)+(-)+([0-9]*)+(-)+[0-9]*"
        # reldate_pattern = r"(rd )+[0-9]*"
        if((re.fullmatch(absdate_pattern,text.lower())) != None): # 到某個指定日期
            localtime = time.time()
            # a = "2013-10-10 23:40:00"
            timeArray = time.strptime(text.split(" ")[1]+" 00:00:00", "%Y-%m-%d %H:%M:%S")
            #轉換為時間戳:
            targettime = int(time.mktime(timeArray))
            while(True):
                picture_url = self.driver.find_elements_by_css_selector("img.rp5asc-10.leQnFG")
                print(len(picture_url))
                if(len(picture_url) == 0):
                    send_push_message(user_id, TextSendMessage(text='search end'))
                    # send_text_message(reply_token,"search end")
                    self.driver.get(url + "/artworks")
                    self.back_id()  
                    return                 
                # print(localtime,targettime,len(picture_url))
                for i in range(len(picture_url)):
                    picture_url[i] = picture_url[i].get_attribute("src")
                    picture_time = picture_url[i][picture_url[i].find("/img/")+5:picture_url[i].find("/img/")+15]
                    picture_time.replace("/","-")
                    # print(picture_time)
                    timeArray = time.strptime(picture_time.replace("/","-")+" 00:00:00", "%Y-%m-%d %H:%M:%S")
                    picture_time = int(time.mktime(timeArray))
                    # print(picture_time)
                    if(picture_time<targettime):
                        send_push_message(user_id, TextSendMessage(text='search end'))
                        self.driver.get(url + "/artworks")
                        # send_text_message(reply_token,"search end")
                        self.back_id()  
                        return 
                    picture_url[i] = "https://i.pixiv.cat/img-master" + picture_url[i][picture_url[i].find("/img/"):picture_url[i].rfind("_p0_")] + "_p0_master1200" + picture_url[i][-4:]
                    self.download_url.append(picture_url[i])
                    send_push_message(user_id,ImageSendMessage(original_content_url=picture_url[i],preview_image_url=picture_url[i]))
                self.driver.get(url + "/artworks?p=" + str(page))
                time.sleep(3)
                page += 1
        else: #幾天前
            localtime = time.time()
            targettime = localtime - int(text.split(" ")[1])*86400
            while(True):
                picture_url = self.driver.find_elements_by_css_selector("img.rp5asc-10.leQnFG")
                if(len(picture_url) == 0):
                    send_push_message(user_id, TextSendMessage(text='search end'))
                    self.driver.get(url + "/artworks")
                    # send_text_message(reply_token,"search end")
                    self.back_id()  
                    return 
                print(localtime,targettime,len(picture_url))
                for i in range(len(picture_url)):
                    picture_url[i] = picture_url[i].get_attribute("src")
                    picture_time = picture_url[i][picture_url[i].find("/img/")+5:picture_url[i].find("/img/")+15]
                    picture_time.replace("/","-")
                    print(picture_time)
                    timeArray = time.strptime(picture_time.replace("/","-")+" 00:00:00", "%Y-%m-%d %H:%M:%S")
                    picture_time = int(time.mktime(timeArray))
                    print(picture_time)
                    if(picture_time<targettime):
                        send_push_message(user_id, TextSendMessage(text='search end'))
                        self.driver.get(url + "/artworks")
                        # send_text_message(reply_token,"search end")
                        self.back_id()  
                        return 
                    picture_url[i] = "https://i.pixiv.cat/img-master" + picture_url[i][picture_url[i].find("/img/"):picture_url[i].rfind("_p0_")] + "_p0_master1200" + picture_url[i][-4:]
                    self.download_url.append(picture_url[i])
                    send_push_message(user_id,ImageSendMessage(original_content_url=picture_url[i],preview_image_url=picture_url[i]))
                self.driver.get(url + "/artworks?p=" + str(page))
                time.sleep(3)
                page += 1        
        self.back_id()   
        
    def is_going_to_walk_around(self,event):
        text = event.message.text
        pattern = r"(wa )+([0-9]*)"
        if(re.fullmatch(pattern,text.lower())):
            self.re_scraw = True

        return (re.fullmatch(pattern,text.lower()) != None) or (text.lower() == "wa")

    def on_enter_walk_around(self,event):
        print("I'm entering work around")

        text = event.message.text
        user_id = event.source.user_id
        reply_token = event.reply_token
        if(self.re_scraw):
            self.driver.get("https://www.pixiv.net/ranking.php")
            send_push_message(user_id, TextSendMessage(text='請稍後回應...'))
            time.sleep(4)
            try:
                end = int(text.split(" ")[1])
            except:
                end = 10
                print(end)
            if(end < 10):
                end = 10
            if(end > 40):
                end = 40
            for x in range(1, end):
                self.driver.execute_script("window.scrollTo(0,"+str(1000*x)+")")
                time.sleep(0.25)
            time.sleep(3)
            picture_url = self.driver.find_elements_by_class_name("_thumbnail.ui-scroll-view")
            self.correct_picture_url = []
            self.icon_url = []
            title_name = self.driver.find_elements_by_css_selector("a.title")
            self.correct_title_name = []
            self.container = self.driver.find_elements_by_class_name("user-container.ui-profile-popup")
            self.title_page = []
            self.artist_name = []
            self.artist_page = []
            append_num = []
            self.correct = 0
            print(len(picture_url),len(self.container))
            for i in range(len(picture_url)):
                picture_url[i] = picture_url[i].get_attribute("src")
                # print(i,picture_url[i])
                if "https:" not in picture_url[i]:
                    self.correct = i
                else:
                    picture_url[i] = "https://i.pixiv.cat/img-master" + picture_url[i][picture_url[i].find("/img/"):picture_url[i].rfind("_p0_")] + "_p0_master1200" + picture_url[i][-4:]
                    self.correct_picture_url.append(picture_url[i])
                    append_num.append(i)
            for i in append_num:
                self.icon_url.append(self.container[i].get_attribute("data-profile_img"))
                # print(icon_url[i])
                if(self.icon_url[-1] != "https://s.pximg.net/common/images/no_profile_s.png"):
                    self.icon_url[-1] = "https://i.pixiv.cat" + self.icon_url[-1][self.icon_url[-1].find("/user-profile/"):self.icon_url[-1].rfind("_50")] + "_170" + self.icon_url[-1][-4:]
                # print(icon_url[i])
            for i in append_num:
                self.title_page.append(title_name[i].get_attribute("href"))
                self.correct_title_name.append(title_name[i].text)
                # print(title_name[i],title_page[i])
            for i in append_num:
                self.artist_name.append(self.container[i].get_attribute("data-user_name"))
                self.artist_page.append(self.container[i].get_attribute("href"))
                # print(artist_name[i],artist_page[i])
            self.appear_list = []
            self.re_scraw = False
            self.driver.get("https://www.pixiv.net/ranking.php")
            print(len(append_num))
            print(len(self.correct_picture_url),len(self.icon_url),len(self.artist_name),len(self.artist_page),len(self.correct_title_name),len(self.title_page))

        for i in range(len(walk_around["contents"])):
            tmp = random.randint(0,len(self.correct_picture_url)-1)
            while(tmp in self.appear_list):
                tmp = random.randint(0,len(self.correct_picture_url)-1)
            self.appear_list.append(tmp)
            if( (len(self.correct_picture_url)-len(self.appear_list))<10 or (len(self.appear_list)/len(self.correct_picture_url))>0.75):
                self.appear_list = []
            print(tmp)
            print(self.correct_picture_url[tmp],self.icon_url[tmp],self.correct_title_name[tmp])
            walk_around["contents"][i]["hero"]["url"] = self.correct_picture_url[tmp]
            walk_around["contents"][i]["hero"]["action"]["uri"] = self.correct_picture_url[tmp]
            walk_around["contents"][i]["body"]["contents"][0]["text"] = self.correct_title_name[tmp]
            walk_around["contents"][i]["body"]["contents"][0]["action"]["uri"] = self.title_page[tmp]
            walk_around["contents"][i]["footer"]["contents"][0]["contents"][0]["url"] = self.icon_url[tmp]
            walk_around["contents"][i]["footer"]["contents"][0]["contents"][0]["action"]["uri"] = self.artist_page[tmp]
            walk_around["contents"][i]["footer"]["contents"][1]["contents"][0]["text"] = self.artist_name[tmp]

        # send_flex_message(reply_token, f"walk_around", walk_around)
        send_push_message(user_id,FlexSendMessage(alt_text='error',contents=walk_around))
        self.back_pixiv(event)

    def is_going_to_download(self,event):
        text = event.message.text

        return text.lower() == "download"

    def on_enter_download(self,event):
        user_id = event.source.user_id
        if(len(self.download_url) != 0):
            yourPath = "img"
            try:
                shutil.rmtree(yourPath)
            except OSError as e:
                print(e)
            else:
                print("The directory is deleted successfully")

            os.makedirs('img/',exist_ok=True)

            for i in range(len(self.download_url)):
                url = self.download_url[i]
                r = requests.get(self.download_url[i])
                with open('img/'+self.download_url[i][self.download_url[i].find("/img/")+5:].replace("/","_"),'wb') as f:
                #將圖片下載下來
                    f.write(r.content)
            allFileList = os.listdir(yourPath)
            with zipfile.ZipFile('img/archive.zip', 'w') as zf:
                for i in range(len(allFileList)):
                    print(allFileList[i])
                    zf.write('img/'+allFileList[i])
                    os.remove('img/'+allFileList[i])
            send_push_message(user_id, TextSendMessage(text="https://testmylinebot777.herokuapp.com/download  (開無痕視窗輸入網址)"))
        else:
            send_push_message(user_id, TextSendMessage(text="沒有要下載的圖片"))
        self.back_artist_artwork()
        
    def is_going_to_fsm(self,event):
        text = event.message.text

        return text.lower() == "fsm"

    def on_enter_fsm(self,event):
        print("I'm entering work fsm")
        user_id = event.source.user_id
        reply_token = event.reply_token   

        send_push_message(user_id,ImageSendMessage(original_content_url='https://testmylinebot777.herokuapp.com/',preview_image_url='https://testmylinebot777.herokuapp.com/'))         
        send_text_message(reply_token,"current state:"+str(self.last_state))
        if(self.last_state == "initial"):
            self.ins_back_ini()
        elif(self.last_state == "menu"):
            self.ins_back_menu()
        elif(self.last_state == "pixiv"):
            self.ins_back_pix()
        elif(self.last_state == "find_pixiv_id"):
            self.ins_back_find()

def IsConnection(url):
    """
        檢查連線是否失敗。
    """
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req)
    except urllib.request.HTTPError as e:
        print(e.reason)
        return False
    return True

