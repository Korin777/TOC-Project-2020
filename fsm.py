from transitions.extensions import GraphMachine

from utils import send_text_message, send_flex_message, send_push_message

from content import menu,pixiv,find_artwork_id, find_user_id

from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

import re
import urllib.request



import time


class TocMachine(GraphMachine):
    def __init__(self, driver,**machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.driver = driver
        self.stay = False
        self.in_pixiv = False
        self.last_state = "initial"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"
    
    def on_enter_menu(self, event):
        print("I'm entering menu")
        self.last_state = self.state
        user_id = event.source.user_id
        send_push_message(user_id,ImageSendMessage(original_content_url='https://testmylinebot777.herokuapp.com/',preview_image_url='https://testmylinebot777.herokuapp.com/'))
        self.in_pixiv = False
        reply_token = event.reply_token
        send_flex_message(reply_token, f"menu", menu)

    def is_going_to_pixiv(self, event):
        text = event.message.text
        return text.lower() == "pixiv"
    
    def on_enter_pixiv(self, event):
        print("I'm entering pixiv")
        self.last_state = self.state
        user_id = event.source.user_id
        if(not self.in_pixiv):
            self.driver.get("https://www.pixiv.net/")
            reply_token = event.reply_token
            send_push_message(user_id, TextSendMessage(text='請稍後回應...'))
            time.sleep(5)

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
                    print(picture_url[j])
                    j += 1
                else:
                    icon_url.append(picture[i].get_attribute("src"))
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
            print(len(picture_url),len(icon_url),len(title_name))
            print(len(pixiv["contents"])-1)
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
        return ((re.fullmatch(user_pattern,text.lower())) != None) or ((re.fullmatch(artwork_pattern,text.lower())) != None)
    
    def on_enter_find_pixiv_id(self, event):
        print("I'm entering find_pixiv_id")
        self.last_state = self.state
        url = "https://www.pixiv.net/" + event.message.text.lower().replace(" ","/")
        print(url)
        reply_token = event.reply_token
        if(not IsConnection(url)):
            self.back_pixiv()
            send_text_message(reply_token,"此id不存在")
            return
        self.driver.get(url)
        time.sleep(3)
        if(self.stay): #找作者
            tmp = self.driver.find_element_by_class_name("_2AOtfl9")
            twitter_url = tmp.find_element_by_tag_name("a").get_attribute("href")
            twitter_url = "https://twitter.com/" + twitter_url[twitter_url.find(".com%2" + "F")+7:]
            tmp = self.driver.find_element_by_class_name("sc-1asno00-0.ihWmWP")
            artist_name = tmp.get_attribute("title")
            icon_url = tmp.find_element_by_tag_name("img").get_attribute("src")
            icon_url = "https://i.pixiv.cat" + icon_url[icon_url.find("/user-profile/"):]
            picture_url = self.driver.find_element_by_class_name("rp5asc-10.kJsXQy").get_attribute("src")
            picture_url = "https://i.pixiv.cat/img-master" + picture_url[picture_url.find("/img/"):picture_url.rfind("_p0_")] + "_p0_master1200" + picture_url[-4:]

            find_user_id["header"]["contents"][0]["url"] = picture_url
            find_user_id["header"]["contents"][1]["contents"][0]["url"] = icon_url
            find_user_id["body"]["contents"][0]["text"] = artist_name
            find_user_id["footer"]["contents"][0]["contents"][0]["action"]["uri"] = url
            find_user_id["footer"]["contents"][1]["contents"][0]["action"]["uri"] = twitter_url

            send_flex_message(reply_token, f"find_pixiv_id", find_user_id)
        else: #找作品
            picture_url = self.driver.find_element_by_class_name("sc-1qpw8k9-1.fvHoJ").get_attribute("src")
            picture_url = "https://i.pixiv.cat/img-master" + picture_url[picture_url.find("/img/"):picture_url.rfind("_p0_")] + "_p0_master1200" + picture_url[-4:]
            tmp = self.driver.find_element_by_class_name("f30yhg-2.iKmMAb")
            artist_name = tmp.find_element_by_tag_name("div").get_attribute("title")
            icon_url = tmp.find_element_by_tag_name("img").get_attribute("src")
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
            send_push_message(user_id, TextSendMessage(text='menu =>進入選單'))
            self.ins_back_ini()
        elif(self.last_state == "menu"):
            send_push_message(user_id, TextSendMessage(text='menu =>進入選單\npixiv =>進入pixiv小工具'))
            self.ins_back_menu()
        elif(self.last_state == "pixiv"):
            send_push_message(user_id, TextSendMessage(text='menu =>進入選單\nusers id =>找繪師 ex:users 1234\nartworks id =>找作品 ex:artworks 1234'))
            self.ins_back_pix()
        elif(self.last_state == "find_pixiv_id"):
            send_push_message(user_id, TextSendMessage(text='menu =>進入選單\nad 年-月-日 =>找繪師從現在時間到某指定日期間的作品 ex:ad 2020-12-21\nrd 天數 =>找繪師從現在時間到幾天前之間的作品 ex:rd 10'))
            self.ins_back_find()

    def is_going_to_find_artist_artwork(self, event):
        text = event.message.text

        absdate_pattern = r"(ad )+([0-9]*)+(-)+([0-9]*)+(-)+[0-9]*"
        reldate_pattern = r"(rd )+[0-9]*"
        return ((re.fullmatch(absdate_pattern,text.lower())) != None) or ((re.fullmatch(reldate_pattern,text.lower())) != None) 

    def on_enter_find_artist_artwork(self, event):
        print("I'm entering find_pixiv_id")
        text = event.message.text
        reply_token = event.reply_token
        user_id = event.source.user_id
        self.last_state = self.state

        absdate_pattern = r"(ad )+([0-9]*)+(-)+([0-9]*)+(-)+[0-9]*"
        # reldate_pattern = r"(rd )+[0-9]*"
        if((re.fullmatch(absdate_pattern,text.lower())) != None): # 到某個指定日期
            localtime = time.time()
            # a = "2013-10-10 23:40:00"
            timeArray = time.strptime(text.split(" ")[1]+"00:00:00", "%Y-%m-%d %H:%M:%S")
            #轉換為時間戳:
            targettime = int(time.mktime(timeArray))
            picture_url = self.driver.find_elements_by_class_name("img.rp5asc-10.leQnFG")
            for i in range(len(picture_url)):
                picture_url[i] = picture_url[i].get_attribute("src")
                picture_time = picture_url[i][picture_url[i].find("/img/")+5:picture_url[i].find("/img/")+15]
                picture_time.replace("/","-")
                timeArray = time.strptime(picture_time.replace("/","-")+"00:00:00", "%Y-%m-%d %H:%M:%S")
                picture_time = int(time.mktime(timeArray))
                if(picture_time<targettime):
                    send_text_message(reply_token,"search end")
                    return 
                picture_url[i] = "https://i.pixiv.cat/img-master" + picture_url[i][picture_url[i].find("/img/"):picture_url[i].rfind("_p0_")] + "_p0_master1200" + picture_url[i][-4:]
                send_push_message(user_id,ImageSendMessage(original_content_url=picture_url[i],preview_image_url=picture_url[i]))
        else: #幾天前
            localtime = time.time()
            # a = "2013-10-10 23:40:00"
            targettime = localtime - int(text.split(" ")[1])*86400
            picture_url = self.driver.find_elements_by_class_name("img.rp5asc-10.leQnFG")
            print(localtime,targettime,len(picture_url))
            for i in range(len(picture_url)):
                picture_url[i] = picture_url[i].get_attribute("src")
                picture_time = picture_url[i][picture_url[i].find("/img/")+5:picture_url[i].find("/img/")+15]
                picture_time.replace("/","-")
                timeArray = time.strptime(picture_time.replace("/","-")+"00:00:00", "%Y-%m-%d %H:%M:%S")
                picture_time = int(time.mktime(timeArray))
                if(picture_time<targettime):
                    send_text_message(reply_token,"search end")
                    return 
                picture_url[i] = "https://i.pixiv.cat/img-master" + picture_url[i][picture_url[i].find("/img/"):picture_url[i].rfind("_p0_")] + "_p0_master1200" + picture_url[i][-4:]
                send_push_message(user_id,ImageSendMessage(original_content_url=picture_url[i],preview_image_url=picture_url[i]))
        self.back_id()   
            
        



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