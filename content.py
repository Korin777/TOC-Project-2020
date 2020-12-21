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
        "spacing": "md",
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
      },
      "styles": {
        "hero": {
          "backgroundColor": "#272727"
        }
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
          "label": "action",
          "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "12345",
            "align": "center",
            "contents": [],
            "size": "xl",
            "offsetBottom": "5px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#c70039"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.pixiv.cat/user-profile/img/2020/01/16/23/25/09/16863083_5d7fb313ca00a0e1a7c7d9e4d32384a5_170.jpg",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "72px",
            "height": "72px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": "繪師名稱",
                "align": "center",
                "margin": "md",
                "contents": []
              }
            ],
            "offsetTop": "20px"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#F0F0F0F0"
        }
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
          "label": "action",
          "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "12345",
            "align": "center",
            "contents": [],
            "size": "xl",
            "offsetBottom": "5px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#c70039"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.pixiv.cat/user-profile/img/2020/01/16/23/25/09/16863083_5d7fb313ca00a0e1a7c7d9e4d32384a5_170.jpg",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "72px",
            "height": "72px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": "繪師名稱",
                "align": "center",
                "margin": "md",
                "contents": []
              }
            ],
            "offsetTop": "20px"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#F0F0F0F0"
        }
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
          "label": "action",
          "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "12345",
            "align": "center",
            "contents": [],
            "size": "xl",
            "offsetBottom": "5px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#c70039"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.pixiv.cat/user-profile/img/2020/01/16/23/25/09/16863083_5d7fb313ca00a0e1a7c7d9e4d32384a5_170.jpg",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "72px",
            "height": "72px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": "繪師名稱",
                "align": "center",
                "margin": "md",
                "contents": []
              }
            ],
            "offsetTop": "20px"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#F0F0F0F0"
        }
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
          "label": "action",
          "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "12345",
            "align": "center",
            "contents": [],
            "size": "xl",
            "offsetBottom": "5px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#c70039"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.pixiv.cat/user-profile/img/2020/01/16/23/25/09/16863083_5d7fb313ca00a0e1a7c7d9e4d32384a5_170.jpg",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "72px",
            "height": "72px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": "繪師名稱",
                "align": "center",
                "margin": "md",
                "contents": []
              }
            ],
            "offsetTop": "20px"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#F0F0F0F0"
        }
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
          "label": "action",
          "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "12345",
            "align": "center",
            "contents": [],
            "size": "xl",
            "offsetBottom": "5px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#c70039"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.pixiv.cat/user-profile/img/2020/01/16/23/25/09/16863083_5d7fb313ca00a0e1a7c7d9e4d32384a5_170.jpg",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              }
            ],
            "width": "72px",
            "height": "72px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": "繪師名稱",
                "align": "center",
                "margin": "md",
                "contents": []
              }
            ],
            "offsetTop": "20px"
          }
        ],
        "backgroundColor": "#F0F0F0F0"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#F0F0F0F0"
        }
      }
    }
  ]
}

# find_pixiv_id = {
#     "type": "bubble",
#     "hero": {
#         "type": "image",
#         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Pixiv_logo.svg/154px-Pixiv_logo.svg.png",
#         "size": "50%",
#         "aspectMode": "fit",
#         "action": {
#         "type": "uri",
#         "uri": "https://www.pixiv.net/"
#         }
#     },
#     "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#         {
#             "type": "text",
#             "text": "Pixiv小工具",
#             "weight": "bold",
#             "size": "xl"
#         },
#         {
#             "type": "box",
#             "layout": "vertical",
#             "spacing": "sm",
#             "contents": [
#             {
#                 "type": "text",
#                 "text": "找繪師",
#                 "color": "#666666",
#                 "size": "md"
#             },
#             {
#                 "type": "text",
#                 "text": "找作品",
#                 "wrap": True,
#                 "color": "#666666",
#                 "size": "md"
#             }
#             ]
#         }
#         ]
#     },
#     "footer": {
#         "type": "box",
#         "layout": "vertical",
#         "spacing": "sm",
#         "contents": [
#         {
#             "type": "button",
#             "style": "link",
#             "height": "sm",
#             "action": {
#             "type": "uri",
#             "label": "GO Pixiv",
#             "uri": "https://www.pixiv.net/"
#             }
#         }
#         ],
#         "flex": 0
#     }
# }

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

find_artwork_id = {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#",
    "size": "full",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg#"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "12345",
        "align": "center",
        "contents": [],
        "size": "xl",
        "offsetBottom": "5px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        }
      },
      {
        "type": "separator",
        "margin": "sm",
        "color": "#c70039"
      }
    ],
    "backgroundColor": "#F0F0F0F0"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://i.pixiv.cat/user-profile/img/2020/01/16/23/25/09/16863083_5d7fb313ca00a0e1a7c7d9e4d32384a5_170.jpg",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          }
        ],
        "width": "72px",
        "height": "72px",
        "cornerRadius": "100px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
          {
            "type": "text",
            "text": "繪師名稱",
            "align": "center",
            "margin": "md",
            "contents": []
          }
        ],
        "offsetTop": "20px"
      }
    ],
    "backgroundColor": "#F0F0F0F0"
  },
  "styles": {
    "hero": {
      "backgroundColor": "#F0F0F0F0"
    }
  }
}