# 🩺 FYP - Multiplanar Approach for Hepatic Vessel Segmentation

This repository contains the implementation and evaluation of a multiplanar approach for hepatic vessel segmentation as part of my Final Year Project (FYP). The project uses **nnU-Net** as the benchmark model to establish baseline performance.

## 📌 Project Overview
Hepatic vessel segmentation is crucial for liver surgery planning, tumor assessment, and transplant procedures. This project explores multiplanar learning approaches to improve hepatic vessel segmentation accuracy and robustness, with a focus on capturing 3D anatomical information from multiple imaging planes.

## 📂 Repository Structure
```
FYP-Medical-Image-Segmentation/
├── Benchmark/
│   ├── NNunet_Training_Benchmark.ipynb
│   ├── training_analysis.ipynb
│   ├── checkpoint_best.pth
│   ├── checkpoint_latest.pth
│   ├── training_log_2025_10_20_15_44_11.txt
│   ├── comprehensive_training_analysis.png
│   ├── progress.png
│   ├── smoothed_training_curves.png
│   └── training_summary_report.png
├── Main/
│   └── main.py
├── FinalDeliverables/
│   ├── YapYuKang_20509407_Final_Report.pdf
│   └── YapYuKang_20509407_Software.ipynb
└── README.md
```

### 📊 Benchmark Folder
The **Benchmark** folder contains comprehensive nnU-Net training analysis and evaluation:
- **Training Notebooks**: nnU-Net baseline training and detailed analysis notebooks
- **Checkpoints**: Best and latest model checkpoints for reproducibility
- **Training Logs**: Detailed training logs with timestamps
- **Visualizations**: 
  - Comprehensive training analysis graphs
  - Progress tracking visualizations
  - Smoothed training curves
  - Summary reports

### 🧪 Software Notebook
`FinalDeliverables/YapYuKang_20509407_Software.ipynb` is the full multiplanar pipeline, run end-to-end on Colab with Google Drive persistence:
- **Training**: axial, sagittal, and coronal 3D full-resolution nnU-Net models (fold 0)
- **clDice enhancement**: custom trainer adding a topology-aware loss (Dice + CE + clDice) to improve vessel connectivity
- **Fusion strategies**: majority voting, soft probability averaging, and a learned fusion CNN
- **Combined-model experiment**: single model trained on all three orientations pooled together
- **Evaluation**: Dice, clDice, HD95, sensitivity, specificity, precision — with Wilcoxon signed-rank significance testing
- **Post-processing**: connected-component filtering to remove false-positive fragments
- **Figure generation**: reproduces all dissertation figures from verified per-case CSV results

## 🚀 Models & Methodology

### 1. nnU-Net (Benchmark)
- **Purpose**: Establish baseline performance for hepatic vessel segmentation
- **Implementation**: Standard nnU-Net architecture with automated preprocessing
- **Training**: Conducted on hepatic vessel dataset
- **Results**: Training metrics, checkpoints, and visualizations available in `Benchmark/`

### 2. Multiplanar Approach (Proposed Method)
- **Core Concept**: Leverage multiple imaging planes (axial, sagittal, coronal) to capture comprehensive 3D vessel structure
- **Advantages**: 
  - Enhanced spatial context understanding
  - Better capture of vessel continuity across different orientations
  - Improved segmentation of complex vascular structures
- **Implementation**: [To be detailed during development]

## 📊 Dataset
- **Focus**: Hepatic (liver) vessel segmentation
- **Imaging Modality**: CT scans
- **Preprocessing**: DICOM/NIfTI to 2D slices, normalization, standardization
- **Data Split**: Training, validation, and test sets

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FYP-Medical-Image-Segmentation.git
   cd FYP-Medical-Image-Segmentation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Access benchmark materials:**
   - Navigate to `Benchmark/` for nnU-Net training notebooks
   - Review training visualizations and analysis
   - Load checkpoints for inference or continued training

4. **Run experiments:**
   - Open notebooks in Google Colab or Kaggle
   - Ensure GPU acceleration is enabled (T4 or P100 recommended)
   - Follow preprocessing steps documented in each notebook

## 📊 Evaluation Metrics

### Primary Metrics
- **Dice Similarity Coefficient (DSC)**: Measures overlap between prediction and ground truth
- **Intersection over Union (IoU)**: Evaluates segmentation accuracy
- **Hausdorff Distance (HD)**: Measures boundary accuracy
- **Average Surface Distance (ASD)**: Evaluates surface-level precision

### Additional Metrics
- **Sensitivity/Recall**: Ability to detect all vessel pixels
- **Specificity**: Ability to avoid false positives
- **Precision**: Accuracy of predicted vessel pixels

### Visualization
Comprehensive training analysis available in the `Benchmark/` folder includes:
- Training and validation loss curves
- Performance metrics over epochs
- Smoothed training progression
- Visual comparison of segmentation results

## ✨ Contribution Statement

*[To be completed after experimental results and analysis]*

This project aims to explore the effectiveness of multiplanar approaches for hepatic vessel segmentation, with potential contributions in:
- Comparative analysis of nnU-Net vs multiplanar methods for vascular structures
- Investigation of optimal fusion strategies for multi-view predictions
- Evaluation of computational efficiency vs accuracy trade-offs

## 🎯 Timeline

### Phase 1: Literature Review & Setup (Week 1–3)
**📆 Sept – Oct 2025**
- ✅ Literature review on hepatic vessel segmentation methods
- ✅ Review nnU-Net architecture and multiplanar approaches
- ✅ Set up Kaggle/Colab environment (PyTorch + GPU)
- ✅ Acquire and explore hepatic vessel dataset
- **Deliverable**: ✅ Environment setup and dataset understanding

### Phase 2: Benchmark - nnU-Net Implementation (Week 4–6)
**📆 Oct 2025**
- ✅ Implement nnU-Net for hepatic vessel segmentation
- ✅ Train nnU-Net on hepatic vessel dataset
- ✅ Evaluate performance with standard metrics (Dice, IoU, HD)
- ✅ Generate comprehensive training analysis and visualizations
- **Deliverable**: ✅ Baseline nnU-Net performance report (available in `Benchmark/`)

### Phase 3: Multiplanar Architecture Design (Week 7–9)
**📆 Nov 2025** - *Current Phase*
- Design multiplanar architecture for hepatic vessels
- Plan fusion strategy for multi-view predictions
- Implement data preprocessing for multiple planes
- Create training pipeline for multiplanar model
- **Deliverable**: Multiplanar architecture design document

### Phase 4: Multiplanar Model Implementation (Week 10–13)
**📆 Nov – Dec 2025**
- Implement multiplanar segmentation model
- Train separate models for axial, sagittal, and coronal views
- Develop fusion mechanism (weighted average, learned fusion, or attention-based)
- Debug and optimize training process
- **Deliverable**: Trained multiplanar model with initial results

### Phase 5: Comparative Evaluation (Week 14–16)
**📆 Dec 2025 – Jan 2026**
- Run comprehensive evaluation on test set
- Compare nnU-Net vs multiplanar approach
- Analyze failure cases and edge scenarios
- Generate qualitative visualizations (3D renderings, slice-by-slice comparisons)
- Statistical significance testing
- **Deliverable**: Comparative analysis report with metrics and visualizations

### Phase 6: Optimization & Ablation Studies (Week 17–19)
**📆 Jan 2026**
- Hyperparameter tuning for multiplanar model
- Ablation studies (impact of each plane, fusion strategies)
- Investigate different fusion mechanisms
- Optimize inference speed and memory usage
- **Deliverable**: Optimized model and ablation study results

### Phase 7: Report Writing (Week 20–24)
**📆 Jan – Feb 2026**

**Report Structure:**
- **Introduction**: Motivation, clinical significance, research objectives
- **Literature Review**: Hepatic vessel segmentation, nnU-Net, multiplanar methods
- **Methodology**: 
  - Dataset description and preprocessing
  - nnU-Net baseline implementation
  - Multiplanar architecture design
  - Training procedures and hyperparameters
- **Results**: 
  - Quantitative metrics comparison
  - Qualitative visual analysis
  - Ablation study results
  - Statistical analysis
- **Discussion**: 
  - Interpretation of results
  - Advantages and limitations
  - Clinical implications
- **Conclusion & Future Work**

**Deliverable**: First draft of thesis/report

### Phase 8: Final Refinement & Presentation (Week 25–28)
**📆 Feb – Mar 2026**
- Polish results and finalize all figures/graphs
- Proofread and finalize thesis
- Prepare presentation slides
- Create demo notebook showcasing segmentation results
- Practice viva presentation
- Prepare poster (if required)

**Final Deliverables:**
- ✅ Thesis report (PDF)
- ✅ Presentation slides
- ✅ GitHub repository with code + trained weights
- ✅ Demo notebook (Colab/Kaggle)

## 📝 Notes
- All experiments are conducted using **Kaggle** for GPU acceleration
- Dataset preprocessing steps are documented in each notebook
- Training checkpoints and logs are stored in the `Benchmark/` folder
- Comprehensive visualizations track training progress and model performance

## 👨‍💻 Author
**Alan**  
BSc Computer Science (Artificial Intelligence)

## 📜 License
This project is for academic purposes.  
Feel free to use the code with proper citation.

---

*Last Updated: October 2025*  
*Current Status: Phase 3 - Multiplanar Architecture Design*
