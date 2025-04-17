import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from win11toast import notify
from datetime import datetime 
driver = webdriver.Chrome()

driver.get("https://jeemain.nta.nic.in/")

while True:
    pointsList = driver.find_elements(By.XPATH, "/html/body/main/section/div[2]/div/div/div[3]/div[3]/div/div/div/ul/li")

    if(len(pointsList)>=5):
        print("RESULT UPLOADED!!!")
        notify(app_id="Jee Results Checker",title="Jee Mains Results Out!!", body="The final results are out finally!!")
        break

    else:
        print(f"Result not uploaded. Last checked: 0{datetime.now().hour-12}:{datetime.now().minute}:{datetime.now().second}")
        driver.refresh()
        time.sleep(10)
        
driver.close()
notify(app_id="Jee Results Checker",title="Jee Mains Results Out!!", body="The final results are out finally!!")


