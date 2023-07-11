from code import Ui_Form
import pymysql, json
from PyQt5.QtWidgets import QMainWindow


class windows(Ui_Form,QMainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_s()

    def init_s(self):
        self.lineEdit.setPlaceholderText('请输入手机号')   #输入框内的默认文案
        self.lineEdit.setMaxLength(11)    #限制最大输入11位
        self.lineEdit.setClearButtonEnabled(True)   #在输入框内增加清除按钮
        self.pushButton.clicked.connect(self.getcode)


    def getcode(self):

        phone = self.lineEdit.text()
        try:
            connect = pymysql.connect(host='10.0.12.102', port=3306, user='usersms', passwd='kAKfbHMincmiBt7t',
                                      database='sms', charset='utf8')

            cur = connect.cursor()
            sql = 'SELECT message_body from sms_record WHERE phone=%s ORDER BY create_time DESC limit 1' % phone.strip()
            cur.execute(sql)
            result = cur.fetchone()
            code = json.loads(result[0]).get("code")
            self.textBrowser.setText('验证码：' + json.dumps(code))
            self.textBrowser.repaint()
            connect.commit()
            connect.close()
            cur.close()
        except Exception as e:

            self.textBrowser.setText('出现异常'+ str(e))
            self.textBrowser.repaint()