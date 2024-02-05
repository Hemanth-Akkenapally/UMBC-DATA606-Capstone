## 1. Multi-Modal Brain Tumor Segmentation using Machine Learning 

- Brain Tumor segmentation using ML
- Prepared for UMBC Data Science Master Degree Capstone by Hemanth Akkenapally  under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Hemanth Akkenapally
- LinkedIn: [Akkenapally Hemanth](https://www.linkedin.com/in/hemanthakkenapally/)
- GitHub: [Hemanth-Akkenapally](https://github.com/Hemanth-Akkenapally)
- PowerPoint presentation: https://docs.google.com/presentation/d/1-qIRI90KphTFXQbZrPj3djy2Kh5ZpV8zg_FYkYzFMy0/edit?usp=sharing
    
## 2. Background

- What is it about?
  - Brain tumor segmentation involves using imaging techniques, often MRI, to accurately identify and delineate tumor regions from normal brain tissue, aiding in diagnosis and treatment planning.
- Why does it matter? 
  - brain tumor segmentation, one of the sophisticated diagnosis and wrong decision may lead to malignant growth. diagnosis using ML models nay help to take a quick decision even under critical situations.
- What are your research questions?
  - How can segmentation models effectively identify and segment small or subtle tumors that might be challenging to detect in medical imaging?
  - How can machine learning models be enhanced to improve the accuracy of brain tumor segmentation in diverse datasets?
## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data sources: https://www.synapse.org/#!Synapse:syn27046444/wiki/616992
- Data shape: MRI 1470 3D volumes (1251 Training + 219 Validation)
- Data Size: 7GB
- Time period : 2023
- What does each row represent?
  - Data is available in NIfTI files (.nii.gz).
  - native (T1)
  - post-contrast T1-weighted (T1Gd)
  - T2-weighted (T2)
  - T2 Fluid Attenuated Inversion Recovery (T2-FLAIR)  
- Data dictionary
  - Columns name
  - Data type: Neuroimaging information technology NIfTI
  - Definition: MRI scanned images
  - Potential values: 
- Which variable/column will be your target/label in your ML model?
- Which variables/columns may be selected as features/predictors for your ML models?