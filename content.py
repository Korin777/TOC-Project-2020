
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
        "url": "https://s.pximg.net/www/js/build/14e52f8ff79c3dc931eb16c6f4b53890.svg#",
        "size": "full",
        "aspectMode": "fit",
        "action": {
          "type": "uri",
          "uri": "http://linecorp.com/"
        },
        "offsetTop": "-40px"
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
        ],
        "offsetTop": "-80px"
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

find_pixiv_id = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "originalContentUrl": "https://s.pixiv.cat/www/js/build/14e52f8ff79c3dc931eb16c6f4b53890.svg#",
        "size": "full",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "offsetTop": "-40px"
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