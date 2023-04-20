from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from openpyxl import load_workbook
from mail_control import send_mail
from main_w import Ui_mainWindow
from table_data import load_data
import pandas as pd

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.list_btn.clicked.connect(self.fileopen)
        self.attach_btn.clicked.connect(self.openurl)
        self.send_btn.clicked.connect(self.sendmail)
        self.delete_btn.clicked.connect(self.delete_items)
        self.add_btn.clicked.connect(self.add_items)
        self.list_edit.setReadOnly(True)
        self.attach_edit.setReadOnly(True)
        return

    def openurl(self):
        attach_url = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.attach_edit.setText(attach_url)
        return

    def fileopen(self):
        file_name = QFileDialog.getOpenFileName(self, 'Select File', '', 'Excel Files (*.xlsx)')
        self.list_edit.setText(file_name[0])
        df = pd.read_excel(file_name[0])
        load_data(df, self)
        return

    def sendmail(self):
        mail_id = self.id_edit.text()
        mail_pass = self.pass_edit.text()
        attach_url = self.attach_edit.text()
        list_name = self.list_edit.text()
        subject = self.subject_edit.text()
        body = self.body_edit.toPlainText()

        attach_url = str(attach_url)
        if mail_id == "":
            QMessageBox.information(self, 'Notice', '이메일을 입력하세요.')

        elif mail_pass == "":
            QMessageBox.information(self, 'Notice', '패스워드를 입력하세요.')

        elif attach_url == "":
            QMessageBox.information(self, 'Notice', '첨부파일 경로를 선택하세요.')

        elif list_name == "":
            QMessageBox.information(self, 'Notice', '메일 리스트를 선택하세요.')

        else:
            xlsx = load_workbook(list_name, read_only=True)
            if '리스트' not in xlsx.sheetnames:
                QMessageBox.information(self, 'Notice', '엑셀 파일에 리스트 시트가 없습니다.')
            else:
                self.send_btn.setText("전송중")
                self.send_btn.setDisabled(True)

                table = self.list_table

                selected_row = table.currentRow()

                for row in range(table.rowCount()):
                    name = table.item(row, 0).text()
                    email= table.item(row, 1).text()
                    print(name, email)
                    #table.setItem(row, 3, QTableWidgetItem("전송중"))
                    send_status = send_mail(mail_id, mail_pass, name, email, attach_url, subject, body)
                    table.setItem(row, 2, QTableWidgetItem(send_status))

                    if name is None:
                        break

                    # if item is not None:
                    #    data = item.text()


                # 이전소스
                # xlsx = load_workbook(list_name, read_only=True)
                # sheet = xlsx["리스트"]

                #for row in sheet.iter_rows(min_row=2):
                #    name = row[0].value
                #    email = row[1].value

                #    if name is None:
                #        break

                #    send_mail(mail_id, mail_pass, name, email, attach_url, subject, body)

                self.send_btn.setText("완료")
                QMessageBox.information(self, 'Notice', '전송 완료')
                self.send_btn.setDisabled(False)
                self.send_btn.setText("메일 전송")
                self.list_edit.setText("")
                self.attach_edit.setText("")

        return

    def xl_open(self):
        url_sel1 = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.xlurl_edit.setText(url_sel1)
        return

    def pdf_save(self):
        url_sel2 = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.pdfurl_edit.setText(url_sel2)
        return

    def msg_complete(self):
        QMessageBox.information(self, 'Notice', 'EXECL TO PDF 변환 완료')
        return

    def msg_error1(self):
        QMessageBox.information(self, 'Notice', 'EXECL 오류')
        return

    def msg_error2(self):
        QMessageBox.information(self, 'Notice', 'PDF 오류')
        return

    def delete_items(self):
        table = self.list_table
        selected_rows = []

        # 선택된 행의 인덱스를 담은 리스트를 생성합니다.
        for index in table.selectedIndexes():
            if index.row() not in selected_rows:
                selected_rows.append(index.row())

        # 선택된 행을 역순으로 정렬합니다.
        selected_rows.sort(reverse=True)

        # 선택된 행을 모두 삭제합니다.
        for row in selected_rows:
            table.removeRow(row)

        return

    def add_items(self):
        table = self.list_table
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        return



app = QApplication()
window = MainWindow()
window.show()
app.exec_()