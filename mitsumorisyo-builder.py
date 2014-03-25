#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

c = canvas.Canvas("test.pdf", pagesize=A4)
pdfmetrics.registerFont(TTFont('Osaka', u'/Library/Fonts/Osaka.ttf'))

# title
c.setFillColorRGB(float(229)/255, float(255)/255, float(218)/255)
c.setStrokeColor(colors.white)
c.rect(50, 730, 230, 70, fill=True)

c.setFont('Osaka', 18)
c.setFillColor(colors.black)
c.drawString(115, 758, u"御  見  積  書")

# 得意先
c.setFont('Osaka', 9)
c.drawString(50, 715, u"株式会社 xxxxx 様")

c.setFont('Osaka', 8)
c.drawString(50, 675, "TEL:%s" % "011-123-1234")

# 見積内容
c.setFont('Osaka', 11)
c.drawString(50, 655, u"下記の通りお見積り申し上げます。")

c.setStrokeColor(colors.green)
c.setLineWidth(.5)
[c.line(50, 630-(i*20), 280, 630-(i*20)) for i in range(0, 5)]

c.setFont('Osaka', 9)
c.drawString(50, 635, u"件名：４月分御見積り")
c.drawString(50, 615, u"納期：４月末")
c.drawString(50, 595, u"支払い条件：２０日締翌月末現金")
c.drawString(50, 575, u"見積もり有効期限：３０日")
c.drawString(50, 555, u"見積もり条件：ｘｘｘ")

# 合計金額
c.setLineWidth(1.5)
c.line(50, 525, 330, 525)

c.setFont('Osaka', 14)
c.drawString(50, 530, u"御見積金額合計")
c.drawString(155, 530, u"￥1,080,000 -")

# 自社
c.setFont('Osaka', 9)
c.drawString(340, 715, u"お見積り日: 2014年03月25日")

c.setFont('Osaka', 9)
c.drawString(340, 695, u"〒123-1234")
c.drawString(410, 695, u"札幌市中央区大通り1-2-3-4-5")
c.drawString(410, 675, u"xxxマンション1234号室")
c.drawString(340, 655, u"山田 太郎")
c.drawString(340, 635, u"TEL: 987-6543-2211")

# 印鑑
xlist = (420, 460, 500, 540)
ylist = (525, 565)
c.grid(xlist, ylist)
c.setFillColor(colors.red)
c.setStrokeColor(colors.red)
c.setLineWidth(1.5)
c.circle(440, 545, 18)
c.setFont('Osaka', 16)
c.drawString(432, 546, u"山")
c.drawString(432, 532, u"田")

# 下の枠
c.setStrokeColor(colors.green)
c.setLineWidth(.5)
xlist = (50, 300, 370, 460, 540)
ylist = (50, 75)
c.grid(xlist, ylist)

c.setLineWidth(.5)
xlist = (50, 240, 270, 300, 370, 460, 540)

for i in range(75, 500, 25):
    if i % 2 != 0 and i != 475:
        c.setFillColorRGB(float(229)/255, float(255)/255, float(218)/255)
        c.rect(50, i, 490, 25, fill=True)
    ylist = (i, i+25)
    c.grid(xlist, ylist)

c.setLineWidth(1.5)
c.rect(50, 50, 490, 450)

c.line(50, 75, 540, 75)

c.setFillColor(colors.green)
c.setFont('Osaka', 8)
c.drawString(128, 480, u"商　品　名")
c.drawString(246, 480, u"単位")
c.drawString(277, 480, u"数量")
c.drawString(323, 480, u"単　価")
c.drawString(402, 480, u"金　額")
c.drawString(489, 480, u"備　考")

c.setFillColor(colors.black)
c.setFont('Osaka', 9)
c.drawString(53, 455, u"item1")
c.drawString(290, 455, u"1")
c.drawString(328, 455, u"250,000")
c.drawString(417, 455, u"250,000")

c.drawString(53, 430, u"item2")
c.drawString(290, 430, u"2")
c.drawString(328, 430, u"250,000")
c.drawString(417, 430, u"500,000")

c.drawString(53, 405, u"item3")
c.drawString(290, 405, u"1")
c.drawString(328, 405, u"250,000")
c.drawString(417, 405, u"250,000")

c.drawString(53, 380, u"<税抜き額合計>")
c.drawString(408, 380, u"1,000,000")

c.drawString(53, 355, u"<消費税>")
c.drawString(423, 355, u"80,000")

c.setFillColor(colors.green)
c.drawString(323, 60, u"合　計")

c.setFillColor(colors.black)
c.drawString(408, 60, u"1,080,000")

c.showPage()
c.save()
