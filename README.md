### VITISH-KAVACH-HACKATHON
This repositry is for the project VITISH-KAVACH Hackathon conductted by VNEST and VIT
## Table of Contents
- [Getting Started](#getting-started)
- [Problem Statement](#problem-statement)
- [Problem ID](#problem-id)
- [About the Problem](#about-the-problem)
- [Our Understanding](#our-understanding)
- [Prototype](#prototype)
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
- The idea is to create a robust surveillance system that integrates data streams from multiple sources including CCTV cameras and dashcams. The system captures snapshots at regular intervals with metadata of timestamp and location. To process the captured frames, we use ANPR and FRS systems that extract data from the images. The data is stored in a database with logs grouped based on the License Plate number of vehicles. For identification of people, we use facial similarity with a dummy id assigned to faces without a suitable match in the database. The system enables dynamic storage of both known and unknown entities with minimal data loss. The system can operate in real-time surveillance mode with the ability to raise alerts based on encountered entities. The logs can be queried to trace the movements of entities. Concerned authorities (government) can add identity metadata for unknown entities to enhance identification accuracy.
