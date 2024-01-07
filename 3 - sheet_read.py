from openpyxl import load_workbook

# 1 - Lê pasta de trabalho e planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatório"]
print(sheet)