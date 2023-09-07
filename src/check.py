import pandas as pd
import config

# 读取附件1的数据
df1 = pd.read_excel(config.TEST_FILE_1)

df4_sheet1 = pd.read_excel(config.TEST_FILE_2, sheet_name='Sheet1')

# 获取两个数据表中“单品编码”的列
codes_df1 = set(df1['单品编码'])
codes_df4_sheet1 = set(df4_sheet1['单品编码'])

# 检查附件1中的单品编码是否全部出现在附件4的Sheet1中
missing_codes = codes_df1 - codes_df4_sheet1
additional_codes = codes_df4_sheet1 - codes_df1

# 创建两个字典，用于存储两个文件中“单品编码”与“单品名称”的对应关系
code_to_name_df1 = {row['单品编码']: row['单品名称'] for index, row in df1.iterrows()}
code_to_name_df4_sheet1 = {row['单品编码']: row['单品名称'] for index, row in df4_sheet1.iterrows()}

# 检查两个字典是否完全一致
are_mappings_identical = code_to_name_df1 == code_to_name_df4_sheet1

# 如果不一致，找出不一致的单品编码和对应的单品名称
inconsistent_mappings = {}

if not are_mappings_identical:
    for code, name in code_to_name_df1.items():
        if code_to_name_df4_sheet1.get(code) != name:
            inconsistent_mappings[code] = {
                '附件1中的单品名称': name,
                '附件4_Sheet1中的单品名称': code_to_name_df4_sheet1.get(code)
            }

print("Missing codes:", missing_codes)
print("Additional codes:", additional_codes)
print("Are mappings identical:", are_mappings_identical)
print("Inconsistent mappings:", inconsistent_mappings)

'''
Missing codes: set()
Additional codes: set()
Are mappings identical: True
Inconsistent mappings: {}
经过检查，发现"附件1"中的所有"单品编码"都能在"附件4"的"Sheet1"中找到。同时，"附件4"的"Sheet1"中也没有额外的"单品编码"。
简而言之，这两个文件中的"单品编码"是相同的，只是排列顺序不同
'''