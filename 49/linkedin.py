from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR EMAIL"
ACCOUNT_PASSWORD = 'PASSWORD'
PHONE = "YOUR PHONE NUMBER"

def close_btn():
  close_button = driver.find_element(by=By.CLASS_NAME, value='artdeco-modal__dismiss')
  close_button.click()

def abort_aplication():
  # Click Close Button
  close_btn()
  
  time.sleep(2)
  # Click Discard Button
  discard_button = driver.find_element(by=By.CSS_SELECTOR, value="[data-control-name='discard_application_confirm_btn']")
  discard_button.click()

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102478259&keywords=production%20planning%20control&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

try:
  # Click Sign in Button
  time.sleep(2)
  sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
  sign_in_button.click()
  
  # Sign in
  time.sleep(5)
  email_field = driver.find_element(by=By.ID, value="username")
  email_field.send_keys(ACCOUNT_EMAIL)
  password_field = driver.find_element(by=By.ID, value="password")
  password_field.send_keys(ACCOUNT_PASSWORD)
  password_field.send_keys(Keys.ENTER)
except:
  # Click Sign in Button
  time.sleep(2)
  sign_in_button = driver.find_element(by=By.CLASS_NAME, value="sign-in-modal")
  sign_in_button.click()
  
  # Sign in
  time.sleep(5)
  email_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
  email_field.send_keys(ACCOUNT_EMAIL)
  password_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
  password_field.send_keys(ACCOUNT_PASSWORD)
  password_field.send_keys(Keys.ENTER)

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value='.job-card-container--clickable')

# Apply for Jobs
for listing in all_listings:
  print('Opening Listing')
  listing.click()
  time.sleep(2)
  try:
    # Click Apply Button
    apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
    apply_button.click()
    
    # Check the Submit Button
    submit_button = driver.find_element(by=By.CLASS_NAME, value='artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
    if submit_button.get_attribute('aria-label') == 'Continue to next step':
      abort_aplication()
      print('Complex application, skipped.')
      continue
    else:
      # Click Submit Button
      print('Submitting job application')
      submit_button.click()
    
    time.sleep(2)
    # Click Close Button
    close_btn()
    
  except NoSuchElementException:
    abort_aplication()
    print('No application button, skipped.')
    continue

time.sleep(5)
driver.quit()