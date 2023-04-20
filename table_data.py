from PySide6.QtWidgets import QTableWidgetItem


def load_data(df, self):

    # 테이블 위젯 생성 및 데이터 추가
    table = self.list_table
    table.setRowCount(len(df.index))
    table.setColumnCount(len(df.columns) + 1)
    # 데이터 추가
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            item = QTableWidgetItem(str(df.iloc[i, j]))
            table.setItem(i, j, item)
            table.setItem(i, j+len(df.columns), QTableWidgetItem('대기중'))

    return
