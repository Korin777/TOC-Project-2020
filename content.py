
menu = {
    "type":"bubble",
    "header": {
        "type":"box",
        "layout":"vertical",
        "spacing":"md",
        "contents":[
            {
                "type":"text",
                "text":"Korin's Bot",
                "size":"lg",
                "weight":"bold",
                "color":"#c70039"
            }
        ]
    },
    "body":{
        "type":"box",
        "layout":"vertical",
        "spacing":"md",
        "contents":[
            {
                "type":"separator",
                "color":"#c70039",
            },
            {
                "type":"text",
                "text":"第一個物件",
                "size":"md"              
            },
            {
                "type":"separator",
                "color":"#c70039"
            },
            {
                "type":"text",
                "text":"第二個物件",
                "size":"md"              
            }        
        ]
    }
}


pixiv = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Pixiv_logo.svg/154px-Pixiv_logo.svg.png",
        "size": "50%",
        "aspectMode": "fit",
        "action": {
          "type": "uri",
          "uri": "https://www.pixiv.net/"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Pixiv小工具",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "找繪師",
                "color": "#666666",
                "size": "md"
              },
              {
                "type": "text",
                "text": "找作品",
                "wrap": True,
                "color": "#666666",
                "size": "md"
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": "GO Pixiv",
              "uri": "https://www.pixiv.net/"
            }
          }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#",
        "size": "full",
        "aspectMode": "fit",
        "action": {
          "type": "uri",
          "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "繪師名稱",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "作品名稱",
                "color": "#666666",
                "size": "md"
              },
              {
                "type": "text",
                "text": "網址",
                "wrap": True,
                "color": "#666666",
                "size": "md"
              }
            ]
          }
        ]
      }
    }
  ]
}
print(pixiv["contents"][1]["hero"]["url"])

find_pixiv_id = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Pixiv_logo.svg/154px-Pixiv_logo.svg.png",
        "size": "50%",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "https://www.pixiv.net/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Pixiv小工具",
            "weight": "bold",
            "size": "xl"
        },
        {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "text",
                "text": "找繪師",
                "color": "#666666",
                "size": "md"
            },
            {
                "type": "text",
                "text": "找作品",
                "wrap": True,
                "color": "#666666",
                "size": "md"
            }
            ]
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "GO Pixiv",
            "uri": "https://www.pixiv.net/"
            }
        }
        ],
        "flex": 0
    }
}