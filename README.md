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
The resulting file is a dataset with features ```[emotion, [list of images]]```

## 3. Emotions paried with colors 
### emotions_colors.py
This Python script reads in ```emotion_images.csv``` and returns the dominant color of each image associated with each emotion.  
### emotions_images.csv
The resulting file is a tidy dataset with features ```[emotion, color]```

