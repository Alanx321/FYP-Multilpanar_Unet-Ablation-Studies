#  🩺FYP - Medical Image Segmentation

This repository contains implementations of various deep learning models for medical image segmentation as part of my Final Year Project (FYP). The models explored are:
- Based Model U-net
- Probabilistic U-Net
- Multiplanar U-Net
- Mixture of Experts (MoE) [under development - haven't execute yet]

## 📌Project Overview
Medical image segmentation plays a critical role in diagnostics and treatment planning. This project evaluates multiple architectures to analyze their performance in terms of accuracy, efficiency, and robustness.

## 📂Repository Structure
- main/  
  ├── main.py 
- notebooks/  
  ├── probabilistic_unet.ipynb  
  ├── multiplanar_unet.ipynb  
  ├── mixture_of_experts.ipynb  
- README.md  

## 🚀Models Implemented
### 1. Based Model U-net
- Baseline UNet performance report (metrics + images).
- Act as a benchmark
  
### 2. Probabilistic U-Net
- Captures uncertainty in segmentation tasks.
- Produces multiple plausible segmentation outputs.

### 3. Multiplanar U-Net
- Incorporates multiple imaging planes.
- Improves spatial context understanding.

### 4. Mixture of Experts (MoE)
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
- All experiments are conducted using Kaggle for GPU acceleration.
- Dataset preprocessing steps are documented in each notebook.

## 👨‍💻Author
- Alan
- BSc Computer Science (Artificial Intelligence)

## 🎯Timeline
### Phase 1: Setup & Dataset (Week 1–2)
#### 📆 22 Sept – 5 Oct (2 weeks)
- Set up Kaggle notebook environment (PyTorch + GPU).
- Download & explore 1 dataset (start with Lung CT from Kaggle).
- Preprocess: convert DICOM/nii to 2D slices, normalize, resize.
- Write simple data loader in PyTorch.
- Deliverable: Small script that loads and visualizes CT slices + masks. 

### Phase 2: Baseline UNet (Week 3–4)
#### 📆 6 Oct – 19 Oct (2 weeks)
- Implement 2D UNet in PyTorch (train slice-by-slice).
- Train on small subset (10–20 patients).
- Evaluate with Dice/IoU.
- Save results + visualizations.
- Deliverable: Baseline UNet performance report (metrics + images).

### Phase 3: Multi-Planar UNet (Week 5–7)
#### 📆 20 Oct – 9 Nov (3 weeks)
- Train 3 separate UNets (axial, sagittal, coronal views).
- Implement simple fusion strategy (average or weighted sum).
- Compare with baseline UNet.
- Deliverable: Performance table (Baseline vs Multi-Planar).

### Phase 4: Probabilistic UNet (Week 8–10)
#### 📆 10 Nov – 30 Nov (3 weeks)
- Implement Probabilistic UNet (with latent space + uncertainty).
- Train on same dataset.
- Evaluate uncertainty maps (show where model is “unsure”).
- Deliverable: Results + uncertainty visualization.

### Phase 5: Novel Model (Your Contribution) (Week 11–14)
#### 📆 1 Dec – 28 Dec (4 weeks)
- 👉 Your “special” twist: MOE-UNet (Mixture of Experts)
- Design architecture: gating network decides between experts (Multi-Planar + Probabilistic).
- Implement & debug training loop.
- Run training on subset of dataset.
- Compare vs previous models.
- Deliverable: Novel model results + comparison table.

### Phase 6: Experiments on 2nd Dataset (Week 15–17)
#### 📆 29 Dec – 18 Jan (3 weeks)
- Choose second dataset (e.g., LiTS Liver CT or Brain MRI).
- Retrain baseline + your model.
- Collect performance metrics across both datasets.
- Deliverable: Cross-dataset comparison (shows robustness).

### Phase 7: Report Writing (Week 18–22)
#### 📆 19 Jan – 22 Feb (5 weeks)
##### Structure of thesis/report:
- Introduction (motivation, objectives).
- Background (UNet, Multi-Planar, Probabilistic, MOE).
- Methodology (datasets, preprocessing, models).
- Results (metrics, visualizations).
- Discussion (pros, cons, novelty).
- Conclusion + Future Work.
- Start writing while running experiments.
- Keep updating with results & figures.
- Deliverable: First draft of report ready by end of Feb.

### Phase 8: Final Refinement (Week 23–27)
#### 📆 23 Feb – 1 Apr (5 weeks)
- Polish results + finalize all figures/graphs.
- Proofread & finalize thesis.
- Prepare presentation slides.
- Make demo notebook (show segmentation on 1–2 scans).
- Practice viva presentation.
##### Final Deliverables:
- Thesis report (PDF).
- Presentation slides.
- GitHub repo (code + trained weights).
- Demo (Kaggle notebook or Colab).

## ✨ Contribution Statement (What makes this project unique)
This project makes the following contributions to medical image segmentation research:
- Efficient 3D-aware segmentation on limited hardware
- Demonstrates how multi-planar learning can capture 3D anatomical correlations from 2D slices, enabling effective training on resource-constrained GPUs (Kaggle T4/P100) instead of requiring heavy 3D CNNs.
- Integration of uncertainty estimation in segmentation
- Incorporates Probabilistic UNet to quantify predictive uncertainty, producing both segmentation masks and confidence maps, which are clinically valuable for identifying ambiguous regions in CT/MRI scans.
- Novel Mixture-of-Experts (MOE) fusion strategy
- Proposes a hybrid approach where a gating network adaptively combines outputs from multi-planar and probabilistic experts, allowing the model to leverage both anatomical context and uncertainty-awareness.
- Cross-dataset validation for robustness
- Evaluates the proposed framework on multiple public medical datasets (lungs CT, liver CT, and/or brain MRI), demonstrating generalizability beyond a single organ or modality.

## 📜License
This project is for academic purposes.
Feel free to use the code with proper citation.

