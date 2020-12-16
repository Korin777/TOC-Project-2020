from transitions.extensions import GraphMachine

from utils import send_text_message, send_flex_message

from content import menu,pixiv,find_pixiv_id

# import scraw

import time


class TocMachine(GraphMachine):
    def __init__(self, driver,**machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.driver = driver
        print(driver)
        print(self.driver)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"
    
    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_flex_message(reply_token, f"menu", menu)

    def is_going_to_pixiv(self, event):
        text = event.message.text
        return text.lower() == "pixiv"
    
    def on_enter_pixiv(self, event):
        print("I'm entering pixiv")
        self.driver.refresh()
        reply_token = event.reply_token
        send_text_message(reply_token, "正在進入Pixiv請稍後...")
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
                print(picture_url[j])
                j += 1
            else:
                icon_url.append(picture[i].get_attribute("src"))
                icon_url[k] = "https://i.pixiv.cat" + icon_url[k][icon_url[k].find("/user-profile/"):icon_url[k].rfind("_50")] + "_170" + icon_url[k][-4:]
                print(icon_url[k])
                k += 1
        j = 0
        for i in range(len(title)):
            title_name.append(title[i].text)
            title_page.append(title[i].get_attribute("href"))
            print(title_name[j],title_page[j])
            j += 1
        j = 0
        for i in range(len(artist)):
            artist_name.append(artist[i].text)
            artist_page.append(artist[i].get_attribute("href"))
            print(artist_name[j],artist_page[j])
            j += 1
        for i in range(4):
            pixiv["contents"][i+1]["hero"]["contents"][0]["url"] = picture_url[i+1]
            pixiv["contents"][i+1]["body"]["contents"][0]["text"] = title_name[i+1]
            pixiv["contents"][i+1]["body"]["contents"][0]["action"]["uri"] = title_page[i+1]
            pixiv["contents"][i+1]["footer"]["contents"][0]["contents"][0]["url"] = icon_url[i+1]
            pixiv["contents"][i+1]["footer"]["contents"][0]["contents"][0]["action"]["uri"] = artist_page[i+1]
            pixiv["contents"][i+1]["footer"]["contents"][1]["contents"][0]["text"] = artist_name[i+1]



        send_flex_message(reply_token, f"pixiv", pixiv)    
        
    def is_going_to_find_pixiv_id(self, event):
        text = event.message.text
        return text.lower() == "find_pixiv_id"
    
    def on_enter_find_pixiv_id(self, event):
        print("I'm entering find_pixiv_id")
        reply_token = event.reply_token
        send_flex_message(reply_token, f"find_pixiv_id", find_pixiv_id)


    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
