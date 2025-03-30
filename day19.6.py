from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import os
import time

def download_images(search_term):
    # Create folder for downloads
    folder_name = f"images_{search_term}"
    os.makedirs(folder_name, exist_ok=True)
    
    # Start browser
    driver = webdriver.Chrome()
    driver.get("https://www.flickr.com")
    
    try:
        # Wait for page to load
        time.sleep(3)
        
        # Search for images
        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        search_box.click()  # Make sure element is focused
        time.sleep(1)
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for results
        
        # Find and download first 5 images
        images = driver.find_elements(By.CSS_SELECTOR, "img.photo-list-photo-view")
        for i, img in enumerate(images[:5]):
            # Get image URL
            img_url = img.get_attribute('src')
            if img_url:
                # Convert to full size image URL
                img_url = img_url.replace('_m.', '_b.')
                
                # Download image
                response = requests.get(img_url)
                if response.status_code == 200:
                    # Save image
                    file_path = os.path.join(folder_name, f"image_{i+1}.jpg")
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded image {i+1}")
                    time.sleep(1)
    
    finally:
        driver.quit()
        print("Done!")

if __name__ == "__main__":
    search_term = input("Enter what images to search for: ")
    download_images(search_term)