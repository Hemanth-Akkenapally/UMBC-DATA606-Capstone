## 1. Automatic Vechile Plate Recognition using YOLOv4 

- Automatic vechile plate recognition using YOLOv4
- Prepared for UMBC Data Science Master Degree Capstone by Hemanth Akkenapally  under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Hemanth Akkenapally
- LinkedIn: [Akkenapally Hemanth](https://www.linkedin.com/in/hemanthakkenapally/)
- GitHub: [Hemanth-Akkenapally](https://github.com/Hemanth-Akkenapally)
- PowerPoint presentation: https://docs.google.com/presentation/d/1-qIRI90KphTFXQbZrPj3djy2Kh5ZpV8zg_FYkYzFMy0/edit?usp=sharing
    
## 2. Background

- What is it about?
  - Automatic Number Plate recognition is a technology which uses optical character recognition to read vechile plates. 
  ANPR systems typically use cameras and specialized software to capture images of vehicles and extract the alphanumeric characters from their license plates.  
- Why does it matter? 
  - This technology is commonly used in law enforcement for purposes such as traffic enforcement, vehicle tracking, and security surveillance. ANPR systems can automatically identify vehicles of interest by matching their license plate numbers against databases of vehicles of interest, stolen vehicles, or vehicles with outstanding warrants.
- What are your research questions?
  - we can increase the accuracy, speed and adaptability using YOLOv4 algorithm.
  - We can develop a user friendly UI to utilize the model to detect the plates automatically upon providing a sample data.
## 3. Data 

Describe the datasets you are using to answer your research questions.

- Dataset is scrapped from open image dataset: "https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F01jfm_"
- Dataset contains Train, Validation and Test Images along with annotations.
  - Each image is scrapped with image file and a csv which contains the annotations of location of the plate.
- Train dataset contains: 10500 images (total 10500 images + 10500 annotated entries in a csv file)
- Validation dataset contains: 3000 images (total 3000 images + 3000 annotated entries in a csv file)
- Test dataset contains: 1500 images (total 1500 images + 1500 annotated entries in a csv file)

