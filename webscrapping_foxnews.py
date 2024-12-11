#webscrapping headlines of foxnews
# -*- coding: utf-8 -*-
#Author: RichardrahciR, MarcycraM

import functions_framework
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import numpy as np
from google.cloud import storage
from datetime import datetime

@functions_framework.http
def foxnews(request):

  """
  Scrapes headlines from Fox News website.

  Returns:
      list: List of headline text strings.
  """
  #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/mac/Desktop/Spring 2024/Industrial_Organization452/gemini-pr-da9b951b7459.json'
  client = storage.Client() 
  bucket_name = "foxnews_sam" 
  top_level_folder_name = "headlines_webscrapping"
  
  url = "https://www.foxnews.com"
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception if there's an HTTP error

  soup = BeautifulSoup(response.content, "html.parser")

  # Find all headline elements (adjust the selector if needed)
  headlines = soup.find_all("h3", class_="title") 

  # Extract the headline text
  headline_texts = [headline.text.strip() for headline in headlines]
  
  # Save the headlines to a CSV file
  headlines_df = pd.DataFrame(headline_texts, columns=["headline"])

  now_time = datetime.now().strftime("%Y%m%d%H%M%S")
  object_name = f"fox_headlines_{now_time}.csv"
  # Get the bucket
  bucket = client.bucket(bucket_name)
  blob = bucket.blob(f"headlines_webscrapping/fox_headlines_{now_time}.csv")

# Upload the csv to the blob with object name
  blob.upload_from_string(headlines_df.to_csv(index=False), content_type="text/csv")
    
  if blob.exists():
      print(f"Object '{object_name}' uploaded to bucket '{bucket_name}'")
  else:
        print(f"Error uploading object '{object_name}'")
  

  return headline_texts








