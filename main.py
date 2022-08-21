from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


l = []
n = 0
driver = webdriver.Firefox(executable_path='/home/ruan/.cargo/bin/geckodriver')

def get_speed():
    try:
        driver.get('https://fast.com/#')
        time.sleep(31)
        print("AAAAAAA")
        speed = driver.find_element(By.ID,'speed-value')
        speedUnits = driver.find_element(By.ID,'speed-units')
        print(f'{speed.text} {speedUnits.text}')
        dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print((dt, speed.text))
        return (dt, float(speed.text), speedUnits.text)

    except:
        time.sleep(31)
        print("BBBBBB")
        dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        speed = 0
        print((dt, speed))
        return (dt, speed, 'Mbps')


if __name__ == "__main__":
    with open("ispSpeed.csv", "w",  encoding="UTF-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['datetime', 'speed', 'unit'])
        while True:
            print(n)
            (dt, speed, unit) = get_speed()
            if unit == "Kbps":
                sped = speed / 1000
            writer.writerow([dt, speed, unit])
            n += 1
            driver.refresh()
