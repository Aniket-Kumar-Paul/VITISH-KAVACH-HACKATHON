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

## Automatic Number Plate Recognition
Here, what we try to achieve is to identify people based on the features extracted by an encoder mechanism. To get various models learn about the feature we attempt to build a __Contrastive Learning__ based methodologies to make the model learn about the similarity and the dis-similarity between different people.

The advantage of doing this is that:
- The encoder learns to cluster different __"similar"__ samples together.
    - The reason why we want to have this is because, in-case we want to use a classifier layer at the end, the final classification layer could learn a simpler hyperplane.

![simclr-v2](https://miro.medium.com/v2/resize:fit:1000/format:webp/1*uJNFn4zT3U3wNZqFsQgoiA.jpeg)

In our scenario, we train the encoder to learn the similar and dis-similar faces. Once, we do this, we can tell that the output of the model would be an ideal representation in the latent space and that vector alone is enough to cluster similar faces together.
