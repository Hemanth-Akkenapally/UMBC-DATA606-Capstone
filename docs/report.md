# Automatic License Number Plate Recognition using YOLOv4 and darknet

- Automatic License Number plate recognition using YOLOv4
- Prepared for UMBC Data Science Master Degree Capstone by Hemanth Akkenapally under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Hemanth Akkenapally
- LinkedIn: Akkenapally Hemanth
- GitHub: Hemanth-Akkenapally
- PowerPoint presentation: https://github.com/Hemanth-Akkenapally/UMBC-DATA606-Capstone/blob/main/docs/Capstone_Hemanth.pptx
    
## 1. Introduction

- YOLO is You Only Look Once, it is an object detection model. they are trained to look at an image and search for a specified object classes. After founding the objects, they are bounded by a box and class is identified.
- yolov4 architecture is shown in pictorial representation where it has 2 stages to detect the class which is mentioned in configuration file. 
- Backbone Network:
YOLOv4 starts with a stable and consistent backbone network, often based on Darknet architecture. This network extracts essential features from the input image through convolutional layers. Components like CSPDarknet53 to enhance feature reuse and reduce computational complexity.
- Detection Head:
YOLOv4's detection head predicts bounding boxes and class probabilities. It utilizes feature pyramid networks (FPN) for multiscale feature fusion, enabling precise and accurate detection across different object sizes. Techniques like Mish activation functions and spatial pyramid pooling (SPP) enhance feature representation and context modeling for improved accuracy.

<img src="/workspace/UMBC-DATA606-Capstone/docs/images/yolov4arch.png" alt="yolov4arch" style="display: block; margin-left: auto; margin-right: auto; width: 300px; height: 150px;">

- Darknet is a deep convolutional neural network (CNN) architecture designed for fast and efficient object detection. It is known for its simplicity and effectiveness in processing visual data, making it suitable for real-time applications like YOLOv4.
- Darknet is loaded from the following github: https://github.com/AlexeyAB/darknet.
- 
## 2. Background

- What is it about?
  - Automatic License Number Plate recognition is a technology which uses optical character recognition to read vehicle plates. 
  ANPR systems typically use cameras and specialized software to capture images of vehicles and extract the alphanumeric characters from their license plates.  
- Why does it matter? 
  - This technology is commonly used in law enforcement for purposes such as traffic enforcement, vehicle tracking, and security surveillance. ANPR systems can automatically identify vehicles of interest by matching their license plate numbers against databases of vehicles of interest, stolen vehicles, or vehicles with outstanding warrants.
- What are your research questions?
  - we can increase the accuracy, speed and adaptability using YOLOv4 algorithm.
  - We can develop a user friendly UI to utilize the model to detect the plates automatically upon providing a sample data.
  
## 3. Data 

- Dataset is scrapped from open image dataset: "https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F01jfm_"
- Dataset contains Train, Validation and Test Images along with annotations.
  - Each image is scrapped with image file and a csv which contains the annotations of location of the plate.
- Train dataset contains: 1500 images (total 1500 images + 1500 annotated entries in a csv file)
- Validation dataset contains: 300 images (total 300 images + 300 annotated entries in a csv file)
- Test dataset contains: 300 images (total 300 images + 300 annotated entries in a csv file)

## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using **Plotly Express**)
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows? 
- Find out if the data require splitting, merging, pivoting, melting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 

## 5. Model Training 

- What models you will be using for predictive analytics?
- How will you train the models?
  - Train vs test split (80/20, 70/30, etc.)
  - Python packages to be used (scikit-learn, NLTK, spaCy, etc.)
  - The development environments (your laptop, Google CoLab, GitHub CodeSpaces, etc.)
- How will you measure and compare the performance of the models?

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit Application :** 

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction

## 8. References 

1. https://www.mdpi.com/2075-1680/12/5/424
2. https://roboflow.com/model/yolov4
3. https://github.com/kiyoshiiriemon/yolov4_darknet
4. https://blog.51cto.com/u_15067242/3553533
5. https://arxiv.org/abs/2004.10934 
6. https://developer.nvidia.com/cuda-toolkit 
7. https://pjreddie.com/darknet/yolo/
