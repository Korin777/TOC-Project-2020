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
        print(self.driver)
        # picture_url= scraw.get_pixiv_picture_url()
        time.sleep(3)

        input = self.driver.find_element_by_id("LoginComponent").find_elements_by_tag_name("input")
        input[0].send_keys('k777k777tw123@gmail.com')
        input[1].send_keys('ko95701ko')
        input[1].submit()
        time.sleep(8)
        container = self.driver.find_element_by_class_name("gtm-toppage-thumbnail-illustration-recommend-works-zone")
        picture = container.find_elements_by_tag_name("img")
        picture_url = []
        j = 0
        for i in range(len(picture)):
            if(picture[i].get_attribute("class") == "rp5asc-10 leQnFG"):
                picture_url.append(picture[i].get_attribute("src"))
                picture_url[j] = "https://i.pixiv.cat/img-master" + picture_url[j][picture_url[j].find("/img/"):picture_url[j].rfind("_p0_")] + "_p0_master1200.jpg"
                print(picture_url[j])
                j += 1
        reply_token = event.reply_token
        pixiv["contents"][1]["hero"]["url"] = picture_url[0]
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
