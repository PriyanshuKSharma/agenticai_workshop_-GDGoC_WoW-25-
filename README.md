# agenticai_workshop
This repository contains materials and code examples for an academic hands-on workshop focused on developing Agentic AI solutions on the Google Cloud Platform (GCP). Participants will explore key concepts, tools, and services within GCP to build and deploy intelligent agents. 
This repository serves as a central hub for workshop participants to access code samples, notebooks, setup instructions, and any supplementary resources needed for a successful learning experience.

Intended Audience: Students, researchers, and academics interested in gaining practical experience with Agentic AI development on the Google Cloud Platform.

You need a GCP project to execute the notebooks. Follow the instructions given in this video for creating a free tier account : https://www.youtube.com/watch?v=ogzJovMsDIU
DO NOT  click on button called "Activate Full Account "
## Getting started 
1. Open Google drive
2. Create a new colab (You may need to install the Colab App)
3. Enter following code
   ``` from google.colab import drive
       drive.mount('/content/drive')
   
5. Complete Authentication Process
6. Enter following code
   ```
       %%bash
       cd /content/drive/MyDrive/
       mkdir -p wow_pune
       cd wow_pune
       git clone https://github.com/BhushanGarware/agenticai_workshop.git '''

## Setting up GCP Project 
1. On GCP homepage, search for 'Vertex AI' and click on **Enable All Recommended APIs**

