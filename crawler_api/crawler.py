
# def generically_filter(something, include): 
#     results = list() 
#     for each in something: 
#         if each in include: 
#             results.append(each)
         
#     return results 



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

# from crawler_api.serializer import MenuSerializer
# from crawler_api.serializer import DishSerializer
# from TASBackend.models import dailyMenu
# from TASBackend.models import dish
# from mongoengine.errors import ValidationError
# import datetime
# # import re
# import time
# class color:
#    PURPLE = '\033[95m'
#    CYAN = '\033[96m'
#    DARKCYAN = '\033[36m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    RED = '\033[91m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    END = '\033[0m'
# # options.add_argument('--headless')

# # driver = webdriver.Chrome(chrome_options = options, executable_path = "/Users/christianlin/Downloads/chromedriver")
# # options = webdriver.ChromeOptions()


# def checkDishExisted(dishName):
#     try: 
#         d = dish.objects.get(Name = dishName)
#     except dish.DoesNotExist:
#         return False
#     except ValidationError:
#         return False
#     except:
#         return False

#     return d.id

# def saveDish(dishName, totalcal, totalFat, cholesterol, sodium, totalCarbs, protein, index, timestamp):
#     _id = checkDishExisted(dishName)

#     print()
#     print("-------> dish name: {}, _id; {}".format(dishName, _id))

#     if _id:
#         return str(_id)

#     if dishName is None:
#         return False
#     if totalcal is None:
#         return False
#     if totalFat is None:
#         return False
#     if cholesterol is None:
#         return False
#     if sodium is None:
#         return False
#     if totalCarbs is None:
#         return False
#     if protein is None:
#         return False
#     if index is None:
#         return False
#     if timestamp is None:
#         return False
    
#     serializer = DishSerializer(data = { 
#         'Name':str(dishName),
#         'Calories': int(totalcal),
#         'Total_Fat': float(totalFat),
#         'Cholesterol': int(cholesterol),
#         'Sodium': int(sodium),
#         'Total_Carbs' : int(totalCarbs),
#         'Protein': int(protein),
#         'Index': int(index),
#         'Timestamp': int(timestamp),
#     }) 
#     if serializer.is_valid():
#         serializer.save()
    
#     __id = checkDishExisted(dishName)
#     while __id is False:
#         __id = checkDishExisted(dishName)
#     print("xxxx> dish name: {}, __id; {}".format(dishName, __id))

#     if __id:
#         return str(__id)

# def checkMenuExisted(date):
#     try:
#         d = dailyMenu.objects.get(Date = date)
#     except dailyMenu.DoesNotExist:
#         return False
#     except ValidationError:
#         return False
#     except:
#         return False
    
#     return True
# def saveDailyMenu(date, restName, main, side, fruit):
#     if checkMenuExisted(date) is False:
#         return False
#     if main is None:
#         return False
#     if restName is None:
#         return False
#     if date is None:
#         return False
#     if side is None:
#         return False
#     if fruit is None:
#         return False
    
#     # serializer makes sure input data is changed to readable type
#     serializer = MenuSerializer(data = { 
#         'Main': main,
#         'RestName': restName,
#         'Date': date,
#         'Side': side,
#         'Fruit': fruit,
        
#     }) 

#     if serializer.is_valid():
#         serializer.save()


# def crawler():
#     driver = webdriver.Chrome(r"C:\Users\22berniec\Desktop\chromedriver_win32\chromedriver")
#     driver.get("https://tas.nutrislice.com/menu/tas/serving-line/2021-05-16")

#     wait = WebDriverWait(driver, 10)
#     wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[4]/p" )))
#     # time.sleep(2)

#     driver.maximize_window()
#     # button = driver.find_element(By.CLASS_NAME, "wf-roboto-n4
#     # -active wf-roboto-i7-active wf-roboto-n7-active wf-roboto-i4-active wf-montserrat-n6-active wf-montserrat-n4-active wf-montserrat-i4-active wf-montserrat-n2-active wf-montserrat-n7-active wf-montserrat-i6-active wf-active")

#     button = driver.find_element(By.XPATH, "/html/body")

#     button = button.find_element(By.CLASS_NAME, "splash-container")

#     button = button.find_element(By.CLASS_NAME, "primary")

#     button.click()

#     time.sleep(4) 

#     week = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[1]/ul")
#     days = week.find_elements(By.CLASS_NAME, "day")
#     for day in days:
#         date = day.find_element(By.CLASS_NAME, "day-label")
#         print(date.text)
#         item = day.find_element(By.CLASS_NAME, "items")
#         print("Entrees: ", end = "")
#         dishes = item.find_element(By.TAG_NAME, "ul")
#         dishes = dishes.find_elements(By.CLASS_NAME, "food-card")
#         entrees_id_array = []
#         for dish in dishes:
#             dishName = dish.find_element(By.CLASS_NAME, "food-name")
#             print(dishName.text, end = ": [")
#             dish.click()
#             # time.sleep(2)
#             wait = WebDriverWait(driver, 5)
#             wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/ul/li[1]/div/div/div[2]/div[2]/fieldset/ul")))
#             modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#             modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#             modalActive = modalList.find_element_by_css_selector("li.modal.active")
#             temp = modalActive.find_element(By.CLASS_NAME, "item-container")

#             info = temp.find_element(By.CLASS_NAME, "info")
#             tabActive = info.find_element_by_css_selector("div.tab.active")
#             infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#             calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#             text = ''.join(generically_filter(calories.text, '0123456789.')) 
#             CalText = text
#             print(text, end = " ")
#             infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#             fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
            
#             totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
            
#             text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#             FatText = text
#             print("Total Fat: ", text, end = " ")
            
#             carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#             cholesterol = carbs[2]
#             text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#             CholText = text
#             print("Cholesterol: ", text, end = " ")
#             protein = carbs[6]
#             text = ''.join(generically_filter(protein.text, '0123456789.')) 
#             ProText = text
#             print("Protein: ", text, end = " ")
#             sodium = carbs[3]
#             text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#             SodText = text
#             print("Sodium: ", text, end = " ")
#             carbs = carbs[4]
#             text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#             CarbText = text
#             print("Total Carbs: ", text, end = " ]")
            
#             modal = modalList.find_element_by_css_selector("li.modal.active")
#             close = modal.find_element_by_css_selector("a.modal-carousel.close")
#             entrees_id = saveDish(dishName.text, CalText, FatText, CholText, SodText, CarbText, ProText, 0, 0 )
#             if entrees_id is True:
#                 entrees_id_array.append(entrees_id)
#             #dishName, totalcal, totalFat, cholesterol, sodium, totalCarbs, protein, index, timestamp
#             close.click()
        
            

#         print("Sides: ", end = "")
#         dishes = item.find_elements(By.TAG_NAME, "ul")
#         dishes = dishes[1]
#         dishes = dishes.find_elements(By.CLASS_NAME, "food-card")
#         sides_id_array = []
#         for dish in dishes:
#             dishName = dish.find_element(By.CLASS_NAME, "food-name")
#             print(dishName.text, end = ": [")
#             dish.click()
#             time.sleep(2)
#             wait = WebDriverWait(driver, 5)
#             wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/ul")))
#             modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#             modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#             modalActive = modalList.find_element_by_css_selector("li.modal.active")
#             temp = modalActive.find_element(By.CLASS_NAME, "item-container")

#             info = temp.find_element(By.CLASS_NAME, "info")
#             tabActive = info.find_element_by_css_selector("div.tab.active")
#             infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#             calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#             text = ''.join(generically_filter(calories.text, '0123456789.')) 
#             CalText = text
#             print(text, end = " ")
#             infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#             fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
#             totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
            
#             text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#             FatText = text
#             print("Total Fat: ", text, end = " ")
            
#             carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#             cholesterol = carbs[2]
#             text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#             CholText = text
#             print("Cholesterol: ", text, end = " ")
#             protein = carbs[6]
#             text = ''.join(generically_filter(protein.text, '0123456789.')) 
#             ProText = text
#             print("Protein: ", text, end = " ")
#             sodium = carbs[3]
#             text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#             SodText = text
#             print("Sodium: ", text, end = " ")
#             carbs = carbs[4]
#             text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#             CarbText = text
#             print("Total Carbs: ", text, end = " ]")
            
#             # totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#             # print("Total Fat: ", totalFat.text, end = " ")
#             # carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#             # carbs = carbs[4]
#             # print("Total Carbs: ", carbs.text, end = " ]")

#             modal = modalList.find_element_by_css_selector("li.modal.active")
#             close = modal.find_element_by_css_selector("a.modal-carousel.close")
#             sides_id = saveDish(dishName.text, CalText, FatText, CholText, SodText, CarbText, ProText, 0, 0 )
#             if sides_id is True:
#                 sides_id_array.append(sides_id)
#             close.click()
#         print("Fruits & Desserts: ", end = "")
#         dishes = item.find_elements(By.TAG_NAME, "ul")
#         dishes = dishes[2]
#         dishes = dishes.find_elements(By.CLASS_NAME, "food-card")
#         fruits_id_array = []
#         for dish in dishes:
#             dishName = dish.find_element(By.CLASS_NAME, "food-name")
#             print(dishName.text, end = ": [")
#             dish.click()
#             time.sleep(2)
#             wait = WebDriverWait(driver, 5)
#             wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/ul/li[1]/div/div/div[2]/div[2]/fieldset/ul")))
#             modalDisplay = driver.find_element(By.CLASS_NAME, "modal-display")
#             modalList = modalDisplay.find_element(By.CLASS_NAME, "modal-list")
#             modalActive = modalList.find_element_by_css_selector("li.modal.active")
#             temp = modalActive.find_element(By.CLASS_NAME, "item-container")

#             info = temp.find_element(By.CLASS_NAME, "info")
#             tabActive = info.find_element_by_css_selector("div.tab.active")
#             infocontainer = tabActive.find_element(By.CLASS_NAME, "info-container")

#             calories = infocontainer.find_element(By.CLASS_NAME, "calories")
#             text = ''.join(generically_filter(calories.text, '0123456789.')) 
#             CalText = text
#             print(text, end = " ")
            
#             infocontainer = infocontainer.find_element(By.CLASS_NAME, "info-container")
#             fatSodium = infocontainer.find_element(By.CLASS_NAME, "fat-sodium")
#             totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
            
#             text = ''.join(generically_filter(totalFat.text, '0123456789.')) 
#             FatText = text
#             print("Total Fat: ", text, end = " ")
            
#             carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#             cholesterol = carbs[2]
#             text = ''.join(generically_filter(cholesterol.text, '0123456789.')) 
#             CholText = text
#             print("Cholesterol: ", text, end = " ")
#             protein = carbs[6]
#             text = ''.join(generically_filter(protein.text, '0123456789.')) 
#             ProText = text
#             print("Protein: ", text, end = " ")
#             sodium = carbs[3]
#             text = ''.join(generically_filter(sodium.text, '0123456789.')) 
#             SodText = text
#             print("Sodium: ", text, end = " ")
#             carbs = carbs[4]
#             text = ''.join(generically_filter(carbs.text, '0123456789.')) 
#             CarbText = text
#             print("Total Carbs: ", text, end = " ]")
#             # totalFat = fatSodium.find_element(By.TAG_NAME, "dd")
#             # print("Total Fat: ", totalFat.text, end = " ")
#             # carbs = fatSodium.find_elements(By.TAG_NAME, "dd")
#             # carbs = carbs[4]
#             # print("Total Carbs: ", carbs.text, end = " ]")

#             modal = modalList.find_element_by_css_selector("li.modal.active")
#             close = modal.find_element_by_css_selector("a.modal-carousel.close")

#             fruits_id = saveDish(dishName.text, CalText, FatText, CholText, SodText, CarbText, ProText, 0, 0 )
#             if sides_id is True:
#                 fruits_id_array.append(fruits_id)
#             close.click()
        

#         # is called each week, have to write a function that will see if within the week it changes month or year
#         dt = datetime.datetime.today() 
#         year = dt.year
#         month = dt.month
#         day = int(''.join(filter(str.isdigit, date.text)))
#         dt = datetime.datetime(year, month, day)

#         print("time: {}".format(dt))

#         saveDailyMenu(dt, "Lunch", entrees_id_array, sides_id_array, fruits_id_array)
