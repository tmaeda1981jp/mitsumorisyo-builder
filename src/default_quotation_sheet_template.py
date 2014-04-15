#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from datetime import datetime


class DefaultQuotationSheetTemplate:

    def __init__(self, file_path):
        self.pdf = canvas.Canvas(file_path, pagesize=A4)
        pdfmetrics.registerFont(
            TTFont('Osaka', u'/Library/Fonts/Osaka.ttf'))

    def draw(self):

        # title
        self.pdf.setFillColorRGB(
            float(229)/255, float(255)/255, float(218)/255)
        self.pdf.setStrokeColor(colors.white)
        self.pdf.rect(50, 730, 230, 70, fill=True)
        self.pdf.setFont('Osaka', 18)
        self.pdf.setFillColor(colors.black)
        self.pdf.drawString(115, 758, u"御  見  積  書")

        # summary
        self.pdf.setFont('Osaka', 11)
        self.pdf.drawString(50, 655, u"下記の通りお見積り申し上げます。")

        self.pdf.setStrokeColor(colors.green)
        self.pdf.setLineWidth(.5)
        [self.pdf.line(50, 630-(i*20), 280, 630-(i*20)) for i in range(0, 5)]

        self.pdf.setLineWidth(1.5)
        self.pdf.line(50, 525, 330, 525)
        self.pdf.setFont('Osaka', 14)
        self.pdf.drawString(50, 530, u"御見積金額合計")

        # stamp
        xlist = (420, 460, 500, 540)
        ylist = (525, 565)
        self.pdf.grid(xlist, ylist)

        # details
        self.pdf.setStrokeColor(colors.green)
        self.pdf.setLineWidth(.5)
        xlist = (50, 300, 370, 460, 540)
        ylist = (50, 75)
        self.pdf.grid(xlist, ylist)

        self.pdf.setLineWidth(.5)
        xlist = (50, 240, 270, 300, 370, 460, 540)

        for i in range(75, 500, 25):
            if i % 2 != 0 and i != 475:
                self.pdf.setFillColorRGB(float(229)/255, float(255)/255, float(218)/255)
                self.pdf.rect(50, i, 490, 25, fill=True)
            ylist = (i, i+25)
            self.pdf.grid(xlist, ylist)

        self.pdf.setLineWidth(1.5)
        self.pdf.rect(50, 50, 490, 450)

        self.pdf.line(50, 75, 540, 75)
        self.pdf.setFillColor(colors.green)
        self.pdf.setFont('Osaka', 8)

        self.pdf.drawString(128, 480, u"商　品　名")
        self.pdf.drawString(246, 480, u"単位")
        self.pdf.drawString(277, 480, u"数量")
        self.pdf.drawString(323, 480, u"単　価")
        self.pdf.drawString(402, 480, u"金　額")
        self.pdf.drawString(489, 480, u"備　考")

        self.pdf.setFillColor(colors.green)
        self.pdf.drawString(323, 60, u"合　計")

        return self

    def set_contractor(self, contractor):
        self.pdf.setFillColor(colors.black)
        self.pdf.setFont('Osaka', 9)
        # http://bugs.python.org/issue5398
        self.pdf.drawString(340, 715, u"お見積り日: %s" %
                            u"" + datetime.now().strftime("%Y年%m月%d日").decode('utf-8'))
        self.pdf.drawString(340, 695, u"〒%s" % contractor.postal_code)
        self.pdf.drawString(410, 695, contractor.address1)
        self.pdf.drawString(410, 675, contractor.address2)
        self.pdf.drawString(340, 655, contractor.name)
        self.pdf.drawString(340, 635, u"TEL: %s" % contractor.tel)
        return self

    def set_client(self, client):
        self.pdf.setFillColor(colors.black)
        self.pdf.setFont('Osaka', 9)
        self.pdf.drawString(50, 715, u'%s 様' % client.name)
        self.pdf.setFont('Osaka', 8)
        self.pdf.drawString(50, 675, "TEL:%s" % client.tel)
        return self

    def set_quotation(self, quotation):
        self.pdf.setFillColor(colors.black)
        self.pdf.setFont('Osaka', 9)
        self.pdf.drawString(50, 635, u"件名：%s" % quotation.title)
        self.pdf.drawString(50, 615, u"納期：%s" % quotation.time_for_payment)
        self.pdf.drawString(50, 595, u"支払い条件：%s" % quotation.payment_terms)
        self.pdf.drawString(50, 575, u"見積もり有効期限：%s" %
                            quotation.quote_expiration_date)
        self.pdf.drawString(50, 555, u"見積もり条件：%s" %
                            quotation.estimate_conditions)

        # 合計金額
        self.pdf.setFont('Osaka', 14)
        self.pdf.drawString(155, 530, u"￥%s -" %
                            quotation.get_total_amount_with_tax())

        # details
        self.pdf.setFont('Osaka', 9)
        pos_y = 455
        pos_x_for_amount = 450
        for item in quotation.items:
            self.pdf.drawString(53,  pos_y, item['item'])
            self.pdf.drawRightString(295, pos_y, str(item['quantity']))
            self.pdf.drawRightString(360, pos_y, str(item['price']))
            self.pdf.drawRightString(pos_x_for_amount, pos_y, str(item['price'] * item['quantity']))
            pos_y = pos_y - 25

        self.pdf.drawString(53,  pos_y, u"<税抜き額合計>")
        self.pdf.drawRightString(pos_x_for_amount, pos_y, str(quotation.get_total_amount_without_tax()))

        pos_y = pos_y - 25

        self.pdf.drawString(53,  pos_y, u"<消費税>")
        self.pdf.drawRightString(pos_x_for_amount, pos_y, str(quotation.get_consumption_tax()))

        # total
        self.pdf.drawRightString(pos_x_for_amount, 60, str(quotation.get_total_amount_with_tax()))

        return self

    def save(self):
        self.pdf.showPage()
        self.pdf.save()
