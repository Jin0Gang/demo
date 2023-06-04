# -*- coding = utf-8 -*-
# @Time : 2023/6/4 20:08
# @Author : Cat.E
# @File : demo_1.py
# @Software: PyCharm

import pandas as pd
from selenium import webdriver

# 设置Chrome浏览器驱动的路径
# 需要提前安装Chrome浏览器和对应版本的ChromeDriver
driver_path = 'path_to_chromedriver'

# 定义目标链接和请求参数
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
params = {
    'BONDCODE': '',
    'DEALYEAR': '2023',
    'BONDTYPE': 'Treasury+Bond',
}

# 创建Chrome浏览器实例
driver = webdriver.Chrome(driver_path)

# 发起GET请求并获取数据
driver.get(url)
for key, value in params.items():
    driver.execute_script(f"document.getElementById('{key}').value = '{value}';")
driver.execute_script("document.getElementById('queryBtn').click();")

# 等待页面加载完成
# 根据实际情况调整等待时间
driver.implicitly_wait(5)

# 解析表格数据
table = driver.find_element_by_css_selector('table.table')
headers = table.find_elements_by_css_selector('thead tr th')
rows = table.find_elements_by_css_selector('tbody tr')

data = []
for row in rows:
    cols = row.find_elements_by_css_selector('td')

    # 检查条件: Bond Type = Treasury Bond, Issue Year = 2023
    bond_type = cols[3].text.strip()
    issue_year = cols[4].text.strip()
    if bond_type == 'Treasury Bond' and issue_year == '2023':
        # 提取所需的数据列
        data.append([
            cols[0].text.strip(),
            cols[1].text.strip(),
            cols[2].text.strip(),
            bond_type,
            cols[5].text.strip(),
            cols[7].text.strip()
        ])

# 检查是否有满足条件的数据
if len(data) == 0:
    print("未找到满足条件的数据")
    exit()

# 将数据转换为DataFrame
df = pd.DataFrame(data, columns=['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])

# 保存为CSV文件
df.to_csv('bond_data.csv', index=False)

# 关闭浏览器实例
driver.quit()
