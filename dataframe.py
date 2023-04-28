import pandas as pd

def table_data(df2, self):
    # 예시로 QTableWidget을 생성합니다.
    table = self.list_table

    # 데이터를 추출해서 데이터프레임으로 변환합니다.
    data = []
    columns = []
    for i in range(table.columnCount()):
        columns.append(table.horizontalHeaderItem(i).text())
    for i in range(table.rowCount()):
        row_data = []
        for j in range(table.columnCount()):
            item = table.item(i, j)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append("")
        data.append(row_data)

    df2 = pd.DataFrame(data, columns=columns)

    return df2