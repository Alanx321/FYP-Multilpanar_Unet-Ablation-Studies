#  🩺FYP - Medical Image Segmentation

This repository contains implementations of various deep learning models for medical image segmentation as part of my Final Year Project (FYP). The models explored are:
- Probabilistic U-Net
- Multiplanar U-Net
- Mixture of Experts (MoE) [under development - haven't execute yet]

## 📌Project Overview
Medical image segmentation plays a critical role in diagnostics and treatment planning. This project evaluates multiple architectures to analyze their performance in terms of accuracy, efficiency, and robustness.

## 📂Repository Structure
- notebooks/  
  ├── probabilistic_unet.ipynb  
  ├── multiplanar_unet.ipynb  
  ├── mixture_of_experts.ipynb  
- README.md  
- requirements.txt  

## 🚀Models Implemented
### 1. Probabilistic U-Net
- Captures uncertainty in segmentation tasks.
- Produces multiple plausible segmentation outputs.

### 2. Multiplanar U-Net
- Incorporates multiple imaging planes.
- Improves spatial context understanding.

### 3. Mixture of Experts (MoE)
- Uses specialized experts for different aspects of segmentation.
- A gating mechanism combines their outputs for final prediction.

## ⚙️Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/FYP-Medical-Image-Segmentation.git
2. Install dependencies (if requirements.txt is provided):
   ```bash
   pip install -r requirements.txt
3. Open and run the Colab notebooks inside notebooks/.

## 📊Results and Evaluation
- Metrics: Dice Coefficient, IoU, and Accuracy.
- Comparative analysis between the models will be documented in the final report.

## 📌Notes
- All experiments are conducted using Google Colab for GPU acceleration.
- Dataset preprocessing steps are documented in each notebook.

## 👨‍💻Author
- Alan
- BSc Computer Science (Artificial Intelligence)

## 📜License
This project is for academic purposes.
Feel free to use the code with proper citation.
   
