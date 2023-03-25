### VITISH-KAVACH-HACKATHON
This repositry is for the project VITISH-KAVACH Hackathon conductted by VNEST and VIT
## Table of Contents
- [Getting Started](#getting-started)
- [Problem Statement](#problem-statement)
- [Problem ID](#problem-id)
- [Our Understanding](#our-understanding)
- [Prototype](#prototype)
    - [Automatic Number Plate Recognition](#automatic-number-plate-recognition)
    - [Feature Matching](#feature-matching)
    - [Web Application](#web-application)     
- [Architecture Diagram](#architecture-diagram)
- [Submissions](#submissions)
- [Authors](#authors)

## Problem Statement
 - Design and develop a technological solution that can accurately perform the Automatic Number Plate Recognition (ANPR) along with Facial Recognition from the available CCTV feeds. The solution should be able to recognize number plates that are written in typical non-standard ways using varying font styles, sizes, designs, symbols, languages etc., i.e. difficult to recognize by existing ANPR Systems.

## Problem ID
 - KVH-005 
 
 ## Our Understanding
 - A custom model for Indian number plate recognition would be tailored specifically to the unique characteristics of Indian number plates, such as the fonts, sizes, and colors used on them. 
- This would result in a more accurate and efficient model compared to using a generic OCR model. 
- By fine-tuning the pre-trained CNN architecture specifically for Indian number plate recognition, the model can achieve higher accuracy compared to a generic OCR model. 
- For the Face Recognition System, instead of going with the classical approaches such as “dlib”, we implement models which use Contrastive Learning methodologies using Siamese Networks.
- We experiment various encoders to get best representations as possible. 
- We typically experimented with ResNet101, ResNeXt50_32x4d, ConvNeXt, Swin and ViT.
 
 ## Prototype
 - It is divided into three modules

   - Automatic Number Plate Recognition
   - Feature Matching
   - Web Application

## Automatic Number Plate Detection
- A custom model for Indian number plate recognition would be tailored specifically to the unique characteristics of Indian number plates, such as the fonts, sizes, and colors used on them. This would result in a more accurate and efficient model compared to using a generic OCR model.
   
   ![car](https://user-images.githubusercontent.com/50861092/227682124-9a500d1f-62ca-4bac-be29-d0b80e58207b.jpg)

   ![img](https://user-images.githubusercontent.com/50861092/227682145-87a1037a-0080-4276-95f4-002ec50f52b9.jpg)
   
- Output


   ![image](https://user-images.githubusercontent.com/50861092/227682152-e449b0f6-e7a7-4cc5-9649-52d295c2a2aa.png)

## Automatic Face Recognition
Here, what we try to achieve is to identify people based on the features extracted by an encoder mechanism. To get various models learn about the feature we attempt to build a __Contrastive Learning__ based methodologies to make the model learn about the similarity and the dis-similarity between different people.

The advantage of doing this is that:
- The encoder learns to cluster different __"similar"__ samples together.
    - The reason why we want to have this is because, in-case we want to use a classifier layer at the end, the final classification layer could learn a simpler hyperplane.

![simclr-v2](https://miro.medium.com/v2/resize:fit:1000/format:webp/1*uJNFn4zT3U3wNZqFsQgoiA.jpeg)

In our scenario, we train the encoder to learn the similar and dis-similar faces. Once, we do this, we can tell that the output of the model would be an ideal representation in the latent space and that vector alone is enough to cluster similar faces together.

## Web Application
- **Home Page** - The home page has two options: Search by People and Search by Vehicle

![Homepage](https://user-images.githubusercontent.com/50861092/227689594-f85b62c2-ef85-4e72-b8a3-5161e83adfcd.jpg)

- **Search People Page** - This page has a search bar using which you can search a person by name and also by using ID. The ID can be a government Id like Aadhar Card. Based on that, We get the results as shown below and we can choose the required one.

![Search Bar (People)](https://user-images.githubusercontent.com/50861092/227689751-afd93e62-1eb0-40e1-a06d-1d941ec5e4f5.jpg)

![Search People Results](https://user-images.githubusercontent.com/50861092/227689791-6e1996cd-2340-4b29-8183-eff62538f880.jpg)

- **People Details Page** - This page consists of all the details of the selected person and also a locate button which redirects to a map showing all the locations 
where the person was tracked.

![People Details](https://user-images.githubusercontent.com/50861092/227689873-8c0ebede-045f-420e-aa86-79da54791839.jpg)

- **Search Vehicle Page** - This page also has a search bar which can be used to search for a vehicle using the vechicle number. Based on the results, all the details of that vehicle is displayed.

![Search Bar (Vehicle)](https://user-images.githubusercontent.com/50861092/227689953-a89825f0-7b18-4ec4-9af0-f776ea4a6ae1.jpg)

![Vehicle Details](https://user-images.githubusercontent.com/50861092/227689946-e77c3d31-aaa5-42d0-9ebc-9c6a49a92783.jpg)

- **Map Page** - This page takes longitudes and latitudes of wherever the person or the vehicle has been tracked and marks them down on the map.

![Map](https://user-images.githubusercontent.com/87603658/227695612-a58b86b8-5729-46e4-97e3-06b96533843f.png)

