# 大三計算理論 Project LineBot 紀錄
>用到的一些工具:
>>Selenium,flask,heroku,transitions<br>

>fsm結構圖:
![image](https://raw.githubusercontent.com/Korin777/TOC-Project-2020/master/fsm.png)

>Heroku 設定套件 Buildpacks 及設定環境變數:
>>heroku buildpacks:set heroku/python
  heroku buildpacks:add --index 1 heroku-community/apt
  heroku buildpacks:set https://github.com/heroku/heroku-buildpack-google-chrome -a myapp
  heroku buildpacks:set https://github.com/heroku/heroku-buildpack-chromedriver -a myapp
  heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
  heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
  heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
  heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google-chrome
  
>圖片代理:
>>src:https://pixiv.cat/
