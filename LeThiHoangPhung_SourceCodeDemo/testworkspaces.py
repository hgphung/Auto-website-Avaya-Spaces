import datetime
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from wait_for import wait_for
from venv import logger
from selenium.webdriver.common.action_chains import ActionChains
from robot.api import logger as api_log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values.media_stream_mic': 1,
                                                 'profile.default_content_setting_values.media_stream_camera':1})

class testworkspaces():
    def __init__ (self):
        self.driver=webdriver.Chrome(options=chrome_options)
        # self.driver=webdriver.Chrome()
        self.INPUT_TEXT = "//div[@class='ql-editor ql-blank']"
        self.CLOSE_POST = "//span[@class='zang-icon icon-close']"
        self.CHAT_BUTTON = "//span[contains(text(),'Chat')]"
        self.POST_MENU = "//div[@class='post-container']//*[text()='{}']"
        self.ICON_EDIT = "//i[@class='zang-icon icon-edit']"
        self.ICON_DELETE = "//i[@class='zang-icon icon-trash']"
        self.COMMENT_POST= "//p[contains(text(),'{}')]"
        self.NAME_SPACE_1 = "//div[@class='globalHeader-main-topic-title' and text()='{}']"
        self.SAVED = "//div[@class='status-text green' and text()='Successfully saved']"
        self.SAVE_BUTTON = "//span[@class='btn save-btn']"
        self.DESCRIPTION_POST = "div[class='ql-editor']"
        self.POST_TAB = "//div[@class ='tab-container space_posts_tab_feature']//span[text()='Posts']"
        self.BTN_NEW_POST = "//button[@data-tip='write a new post']"
        self.INPUT_POST_NAME = "//input[@class='form-control']"
        self.BTN_SUBMIT = "//button[@type='submit']"
        self.BTN_VERIFY_YES = "//button[@class='btn btn-success']"    
        self.DROP_DOWN_BUTTON = "//div[@class='drop-down-menu restore-menu show-arrow']"
        self.EDIT_SPACE = "//span[contains(text(),'Edit space')]"
        self.DELETE_SPACE_1 = "//div[@class='space-options-with-confirm__ask-confirm space-options-with-confirm__ask-confirm--red']"
        self.DELETE_SPACE_2 = "//div[@class='space-options-with-confirm__ask-confirm space-options-with-confirm__ask-confirm--red space-options-with-confirm__ask-confirm--submit-button']"
        self.BTN_ROLE = "//div[@class='react-select__single-value css-qc6sy-singleValue' and text()='{}']"
        self.BTN_CREATE_SPACE = "//span[contains(text(),'Create Space')]"
        self.BTN_DOWN_ROLE = "//div[@class='react-select__indicators css-13c9uqx']"
        self.NAME_SPACE_2 = "//span[contains(text(),'{}')]"
        self.BTN_LEAVE = "//span[contains(text(),'Leave')]"
        self.INPUT_POST_DESCRIPTION = "div[class='composerContainer description'] div[class='ql-container'] div[class*='ql-editor']"
        self.BTN_DOWN_POST = "//p[text()='{}']//..//../../../../../../..//i[@class='zang-icon icon-ellipses-verticle']"
        self.BTN_START_MEETING = "//button[@class='spaceButton blue-bg white-text']//span[text()='Start Meeting']"
        self.BTN_ALLOW = "//android.widget.TextView[(@resource-id='com.android.permissioncontroller:id/permission_message' or @resource-id='com.android.packageinstaller:id/permission_message') and @text='Allow Avaya Spaces to take pictures and record video?']"
        self.ADD_FAVORITE = "//span[contains(text(),'Favorite this Space')]"
        self.SEARCH_SPACE = "//input[@class='search-input']"
        self.ICON_FAVOURITE = "//*[text()='{}']/../../../../..//i[@class='zang-icon icon-favourite-fill']"

    def open_browser_spaces(self, link):
        self.driver.maximize_window()
        self.driver.get(link)
        
    def login_spaces(self,username,password):
        try:
            if wait_for.wait_for_exists_by_name(self, self.driver, "username",10):
                elem= self.driver.find_element(By.NAME,("username"))
                elem.clear()
                elem.send_keys(username)
            wait_for.wait_and_click_by_id(self, self.driver, "GetStartedBtn",10)
            if wait_for.wait_for_exists_by_name(self, self.driver,"password",10):
                elem=self.driver.find_element(By.NAME, "password")
                elem.clear()
                elem.send_keys(password)
            wait_for.wait_and_click_by_id(self, self.driver, "GetStartedBtn",10)
            wait_for.wait_and_click_by_name(self, self.driver, "continue",10) 
            logger.info("Login successfully!!!")
            time.sleep(3)
        except Exception:
            raise RuntimeError('Function exception:' + str(sys.exc_info()))
        finally:
            image= self.take_screenshot
            logger.info(image)    
    def create_spaces(self, namespace, member=None, role=None):
        wait_for.wait_and_click_by_class_name(self, self.driver, "sidebar-add-new-space-btn", 10)
        wait_for.wait_and_click_by_xpath(self, self.driver, "//p[contains(text(),'Create a New Space')]",10 )
        wait_for.wait_and_sendkeys_by_xpath(self, self.driver, "//input[@class='form-control placeholder-no-fix']", namespace, 10 )
        if member == None:
            wait_for.wait_and_click_by_xpath(self, self.driver, self.BTN_CREATE_SPACE, 10)
            logger.info('Create Group Space Successfully !')
        else:
            self.invite_member(member, role)
            wait_for.wait_and_click_by_xpath(self, self.driver, self.BTN_CREATE_SPACE, 10)
            logger.info('Create Group Space Successfully !')
            
    def create_post(self, postname, description):                                       
        try:
            if wait_for.wait_for_exists_by_xpath(self, self.driver, self.POST_TAB, 10):
                wait_for.click_element_by_xpath(self, self.driver, self.POST_TAB)
                logger.info("Click post tab successfully !")
            if wait_for.wait_for_exists_by_xpath(self, self.driver, self.BTN_NEW_POST, 5):
                wait_for.click_element_by_xpath(self, self.driver, self.BTN_NEW_POST)
                wait_for.wait_and_sendkeys_by_xpath(self, self.driver, self.INPUT_POST_NAME, postname, 5)
                wait_for.wait_and_sendkeys_by_css(self, self.driver, self.INPUT_POST_DESCRIPTION, description,5)
                wait_for.click_element_by_xpath(self, self.driver, self.BTN_SUBMIT)
                logger.info("Post created successfully !")
            else:
                logger.info("Post created unsuccessfully !")
                return False
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
    
    def verify_create_post(self, postname):
        try:
            wait_for.wait_for_exists_by_xpath(self,self.driver,self.CHAT_BUTTON,5)
            wait_for.click_element_by_xpath(self,self.driver,self.CHAT_BUTTON)
            if wait_for.wait_for_exists_by_xpath(self, self.driver,self.POST_MENU.format(postname),5):
                logger.info("%s exists in Chat !" %postname)
            else:
                logger.info("%s doesn't exist in Chat !" %postname)
                return False
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        finally:
            image=self.take_screenshot()
            logger.info(image)
        
    def click_to_postname(self, postname):
        try:
            if wait_for.wait_for_exists_by_xpath(self,self.driver,self.CHAT_BUTTON,5):
                wait_for.click_element_by_xpath(self,self.driver,self.CHAT_BUTTON)
                wait_for.wait_for_exists_by_xpath(self, self.driver, self.POST_MENU.format(postname),5)
                wait_for.click_element_by_xpath(self, self.driver, self.POST_MENU.format(postname))
                logger.info("Click post successfully !")
                return True
            return False
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def edit_post(self, postname):
        try:
            if self.click_to_postname(postname):
                wait_for.wait_for_exists_by_xpath(self, self.driver, self.ICON_EDIT, 10)
                wait_for.click_element_by_xpath(self, self.driver, self.ICON_EDIT)
                logger.info("Click edit post is successfully !")
                return True
            else:
                logger.info("Click edit post is unsuccessfully !")
                return False
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def delete_posts(self, postname):
        try:
            if self.edit_post(postname):
                if wait_for.wait_for_exists_by_xpath(self, self.driver, self.ICON_DELETE, 10):
                    wait_for.click_element_by_xpath(self, self.driver, self.ICON_DELETE)
                wait_for.wait_for_exists_by_xpath(self, self.driver, self.BTN_VERIFY_YES, 10)
                wait_for.click_element_by_xpath(self, self.driver, self.BTN_VERIFY_YES)
                logger.info("Delete post successfully !")
                return True
            else:
                logger.info("Delete post unsuccessfully !")
                return False
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def delete_space(self):
        try:
            wait_for.click_element_by_xpath(self, self.driver, self.DROP_DOWN_BUTTON)
            wait_for.click_element_by_xpath(self, self.driver, self.EDIT_SPACE)
            wait_for.click_element_by_xpath(self, self.driver, self.DELETE_SPACE_1)
            wait_for.wait_and_click_by_xpath(self, self.driver, self.DELETE_SPACE_2, 10)
            logger.info("Delete Space successfully !")
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def action_invite_member(self, namemember):
        try:
            logger.info("Start function action invite member")
            wait_for.wait_and_sendkeys_by_css(self, self.driver, "input[role='combobox']",namemember)
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def invite_member(self, namemember, role=None ):
        logger.info("Start function invite member")
        try:
            if role == None or role=="Member":
                self.action_invite_member(namemember)
            elif role=="Admin":
                self.action_invite_member(namemember)
                if wait_for.wait_and_click_by_xpath(self, self.driver, self.BTN_DOWN_ROLE, 10):
                    logger.info("Click choose role admin")
                    wait_for.wait_and_click_by_xpath(self, self.driver, "//*[text()='Admin']")
                    wait_for.wait_for_exists_by_xpath(self, self.driver, self.BTN_ROLE.format(role))
                logger.info("Add member with role Admin successfully !")
            else:
                self.action_invite_member(namemember)
                wait_for.wait_and_click_by_xpath(self, self.driver, self.BTN_DOWN_ROLE, 10)
                wait_for.wait_and_click_by_xpath(self, self.driver, "//*[text()='Guest']")
                wait_for.click_element_by_xpath(self, self.driver, self.BTN_ROLE.format(role))
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def get_link_invited(self):
        try:
            wait_for.wait_and_click_by_xpath(self, self.driver, "//i[@class='neo-icon-chevron-down']", 10)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//span[contains(text(),'Copy link')]", 10)
            wait_for.wait_and_click_by_xpath(self, self.driver, self.INPUT_TEXT, 10)
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(10)
            if wait_for.wait_for_exists_by_css(self, self.driver, "div[class='ql-editor']>p>a", 5):
                link_data = str(self.driver.find_element(By.CSS_SELECTOR, "div[class='ql-editor']>p>a").get_attribute('text'))
                logger.info("Link value: %s" % link_data)
                return link_data
            else:
                return False
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
    def logout_space(self):
        wait_for.wait_and_click_by_xpath(self, self.driver, "//div[@class='display-name']", 10)
        wait_for.wait_and_click_by_xpath(self, self.driver, "//span[contains(text(),'Sign out')]", 10)
        wait_for.wait_and_click_by_xpath(self, self.driver, "//button[@class='btn btn-success']", 10)
        logger.info("Logout Avaya Spaces Successfully !")
        
    def comment_posts(self, postname, comment):
        try:
            self.click_to_postname(postname)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//div[@data-placeholder='Add your comments here']", 10)
            wait_for.send_keys(self, self.driver, comment)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//button[@class='submit-button']", 10)
            logger.info("Comment Post Successfully !")
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def save_posts_changed(self):
        try: 
            wait_for.wait_for_exists_by_xpath(self, self.driver, self.SAVE_BUTTON,5)
            wait_for.click_element_by_xpath(self, self.driver, self.SAVE_BUTTON)
            if wait_for.wait_for_exists_by_xpath(self, self.driver, self.SAVED,3):
                wait_for.click_element_by_xpath(self, self.driver, self.SAVED)
                logger.info("Update post successfully !")
            else:
                logger.info("Update post unsuccessfully !")
            wait_for.wait_for_exists_by_xpath(self, self.driver,self.CLOSE_POST,5)
            wait_for.click_element_by_xpath(self, self.driver, self.CLOSE_POST)
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def change_posts_name(self, postname, new_postname):
        try:
            if self.edit_post(postname):
                wait_for.wait_for_exists_by_xpath(self, self.driver,"//div[@class='todo-tasklist-wrapper']",5)
                wait_for.send_keys(self, self.driver, new_postname)
                self.save_posts_changed()
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))    
    
    def change_post_description(self, postname, descriptionchanged):
        try:
            self.edit_post(postname)
            if wait_for.wait_for_exists_by_css(self, self.driver,"div[class='ql-editor']",5):
                elem = self.driver.find_element(By.CSS_SELECTOR,("div[class='ql-editor']"))
                elem.clear()
                elem.send_keys(descriptionchanged)
            self.save_posts_changed()
        except Exception:
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def verify_comment_posts(self, comment=None):
        try: 
            if wait_for.wait_for_exists_by_xpath(self, self.driver,self.CLOSE_POST,5):
                wait_for.click_element_by_xpath(self, self.driver,self.CLOSE_POST) 
                wait_for.wait_for_exists_by_xpath(self, self.driver,self.COMMENT_POST.format(comment),5)
                logger.info("Comment %s has been sent !" %comment)
            else:
                logger.info("Comment %s hasn't been sent !" %comment )
                return False
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def verify_create_space(self,spacename):
        try:
            if wait_for.wait_for_exists_by_xpath(self, self.driver,self.NAME_SPACE_1.format(spacename),5):
                logger.info("%s exists in Group space !" %spacename )
            else:
                logger.info("%s doesn't exist in Group space !" %spacename )
                return False
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
            
        
    def edit_comment(self, comment, new_comment):
        try:
            wait_for.wait_and_click_by_xpath(self, self.driver, self.CHAT_BUTTON, 5)
            hoverable = self.driver.find_elements(By.XPATH, "//div[@class='message-item out']")
            ActionChains(self.driver).move_to_element(hoverable[len(hoverable)-1]).perform()
            wait_for.wait_and_click_by_xpath(self, self.driver, self.BTN_DOWN_POST.format(comment), 5)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//div[@class='list-row']//p[ text()='Edit']",5)
            if wait_for.wait_for_exists_by_css(self, self.driver,"div[data-placeholder='Edit Message']",5):
                elem = self.driver.find_element(By.CSS_SELECTOR,("div[data-placeholder='Edit Message']"))
                elem.clear()
                elem.send_keys(new_comment)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//div[@data-placeholder='Edit Message']/../../../..//button[@class='chat-send-button']",5)
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))  
           
    def verify_user2_invited(self, spacename):
        try:
            if wait_for.wait_for_exists_by_xpath(self, self.driver,self.NAME_SPACE_1.format(spacename),5):
                logger.info("User 2 has been existed in %s  !" %spacename )
            else:
                logger.info("User 2 hasn't been existed in %s  !" %spacename )
                return False
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))
        
    def delete_comment(self, postname):
        try:
            self.click_to_postname(postname)
            if wait_for.wait_and_click_by_xpath(self, self.driver, "//i[@class='zang-icon icon-close remove-comment']", 5):
                logger.info("Click delete icon successfully!!!")
            else:
                logger.info("Click delete icon unsuccessfully!!!")
                return False
            wait_for.wait_and_click_by_xpath(self, self.driver, self.BTN_VERIFY_YES, 5)
            wait_for.wait_and_click_by_xpath(self, self.driver, self.CLOSE_POST, 5)
            logger.info("Delete comment succcessfully!!!")
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))    
              
    def close_browser(self):
        self.driver.quit()
 
    def take_screenshot(self, screenshot_directory=None):
        try:
            logger.info('Taking screenshot...')
            base_path = "D:/Python_example/selenium/Selenium/"
            if screenshot_directory == None:
                screenshot_directory = base_path + "LOGS/screenshots/"
            file_name = str(datetime.datetime.now()) + '.png'
            file_name = file_name.replace(" ", "-").replace(":", "-")
            screenshot_name = screenshot_directory + file_name
            save_dir = screenshot_name.replace(screenshot_directory, r"../screenshots/")
            save_dir1 = screenshot_name.replace(r"/var/www/html/autorobot/LOGS/screenshots", r"../../screenshots")
            logger.info('screenshot_name: ' + str(screenshot_name))
            logger.info('save_dir: <a href="%s"> Link to Image </a>' % str(save_dir))
            if not os.path.exists(base_path + 'LOGS/screenshots'):
                logger.info('Start creating folder screenshots ...')
                os.makedirs(base_path + 'LOGS/screenshots')
            if self.driver.save_screenshot(screenshot_name):
                logger.info('Take screenshot successfully with path: ' + str(screenshot_name))
                if "ae" in screenshot_name:
                    api_log.info('<img src="{0}" alt="{0}" width="50%">'.format(save_dir), html=True)
                    api_log.info('<img src="{0}" alt="{0} 1" width="50%">'.format(save_dir1), html=True)
                    logger.info('<'+ str(screenshot_name)+'>')
                else:
                    api_log.info('<img src="{0}" alt="{0}" width="80%">'.format(save_dir), html=True)
                    api_log.info('<img src="{0}" alt="{0} 1" width="80%">'.format(save_dir1), html=True)
                    logger.info('<'+ str(screenshot_name)+'>')
                return screenshot_name
            else:
                logger.info('Failed to take screenshot')
                return 'error'
        except:
            self.print_exception()
            logger.info('Exception '+str(sys.exc_info()))
            return False    

    # @staticmethod
    # def allow_presence_btn():
    #     return By.NAME, "Allow"
            
    def start_meeting(self):
        try:
            if wait_for.wait_for_exists_by_xpath(self, self.driver, self.BTN_START_MEETING, 10):
                wait_for.click_element_by_xpath(self, self.driver, self.BTN_START_MEETING)
                logger.info("Click Start Meeting button successfully!")
            # wait_for.wait_for_exists_by_name(self, self.driver, self.BTN_ALLOW, 10)
            # wait_for.click_on_element(self.driver, self.BTN_ALLOW)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//span[@class='call-btn-text']", 10)
            time.sleep(5)
            logger.info("Start meeting successfully")
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info()))   
        finally:
            image= self.take_screenshot()
            logger.info(image)

    def end_meeting(self):
        try:
            wait_for.wait_and_click_by_xpath(self, self.driver, "//i[@class='neo-icon-end-call']", 10)
            wait_for.wait_and_click_by_xpath(self, self.driver, "//button[@class='btn btn-success']", 10)
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info())) 
        finally:
            image= self.take_screenshot()
            logger.info(image)       

    def add_favorite(self):
        try:
            wait_for.click_element_by_xpath(self, self.driver, self.DROP_DOWN_BUTTON)
            wait_for.click_element_by_xpath(self, self.driver, self.ADD_FAVORITE)            
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info())) 
        # finally:
        #     image= self.take_screenshot()
        #     logger.info(image) 

    def verify_add_favorite(self, spacename):
        try:
            wait_for.wait_for_exists_by_xpath(self, self.driver, self.ICON_FAVOURITE.format(spacename),10)  
            # wait_for.click_element_by_xpath(self, self.driver, self.ICON_FAVOURITE.format(spacename),10)        
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info())) 
        finally:
            image= self.take_screenshot()
            logger.info(image) 

    def search_space(self, spacename):
        try:
            wait_for.wait_for_exists_by_xpath(self, self.driver, self.SEARCH_SPACE, 10)
            wait_for.wait_and_sendkeys_by_xpath(self, self.driver, self.SEARCH_SPACE, 10)
            if wait_for.click_element_by_xpath(self, self.driver, self.NAME_SPACE_1.format(spacename),5):
                logger.info ("Space exists")
            else:
                logger.info("No results found")
        except Exception:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: ' + str(sys.exc_info())) 
        finally:
            image= self.take_screenshot()
            logger.info(image)
        
    

    




        
                
                
            
            