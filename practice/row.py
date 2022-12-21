from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://letcode.in/table")
table_t1 = driver.find_element(By.XPATH,"//table[@class='mat-sort table is-bordered is-striped is-narrow is-hoverable is-fullwidth']")
table_rows = table_t1.find_elements(By.TAG_NAME, "tr")
table_header=table_t1.find_elements(By.TAG_NAME,"th")
rows_count = len(table_rows)
header_count=len(table_header)
print("count of rows   : ",rows_count)
print("count of header   : ",header_count)

l



























