# Emotion-Colors

This repo contains the supporting data for my EmotaPal library. 

# Data

## 1. List of emotions
### emotions.csv
A list of 264 emotion words. These emotion words were taken from the Center for Non-Violent Communication. 
https://www.cnvc.org/training/resource/feelings-inventory

## 2. Emotions paired with images
### emotions_images.py
This Python script reads in ```emotions.csv``` and scrapes the top 100 images for each emotion. 
### emotions_images.csv
The resulting file is a dataset with features ```[emotion, image]```

## 3. Emotions paried with colors 
### emotions_images_colors.py
This Python script reads in ```emotion_images.csv``` and returns the dominant color of each image associated with each emotion.  
### emotions_images_colors.csv
The resulting file is a dataset with features ```[emotion, image, dominant color]```

## 4. Clean data 
### clean_data.py
This Python script reads in ```emotion_images_colors.csv``` and removes any NaN values or duplicates. 
### cleaned_data.json
The resulting file is a dataset with features ```[emotion, dominant color]```

# Model 

### train_knn.py 
This file uses ```cleaned_data.json``` to build a classifier that can prediction emotions from colors. The classifier is a KNN classifier with a custom loss function. That function penalizes the semantic distance between words. This file returns ```clf.pkl```. 
