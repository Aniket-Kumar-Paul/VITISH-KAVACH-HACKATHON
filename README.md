### VITISH-KAVACH-HACKATHON
This repositry is for the project VITISH-KAVACH Hackathon conductted by VNEST and VIT
## Table of Contents
- [Getting Started](#getting-started)
- [Problem Statement](#problem-statement)
- [Problem ID](#problem-id)
- [About the Problem](#about-the-problem)
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
 - A custom model for Indian number plate recognition would be tailored specifically to the unique characteristics of Indian number plates, such as the fonts, sizes, and colors used on them. This would result in a more accurate and efficient model compared to using a generic OCR model. By fine-tuning the pre-trained CNN architecture specifically for Indian number plate recognition, the model can achieve higher accuracy compared to a generic OCR model. For the Face Recognition System, instead of going with the classical approaches such as “dlib”, we implement models which use Contrastive Learning methodologies using Siamese Networks.
We experiment various encoders to get best representations as possible. We typically experimented with ResNet101, ResNeXt50_32x4d, ConvNeXt, Swin and ViT.
We use the concepts used in FaceTransformers paper to get proper embedding of the faces
 
 ## Prototype
 - It is divided into three modules

   - Automatic Number Plate Recognition
   - Feature Matching
   - Web Application

## Automatic Number Plate Recognition
   - A custom model for Indian number plate recognition would be tailored specifically to the unique characteristics of Indian number plates, such as the fonts, sizes, and colors used on them. This would result in a more accurate and efficient model compared to using a generic OCR model.
   
   ![car](https://user-images.githubusercontent.com/50861092/227682124-9a500d1f-62ca-4bac-be29-d0b80e58207b.jpg)

   ![WhatsApp Image 2023-03-24 at 19 14 25](https://user-images.githubusercontent.com/50861092/227682145-87a1037a-0080-4276-95f4-002ec50f52b9.jpg)
   
- Output


   ![image](https://user-images.githubusercontent.com/50861092/227682152-e449b0f6-e7a7-4cc5-9649-52d295c2a2aa.png)

