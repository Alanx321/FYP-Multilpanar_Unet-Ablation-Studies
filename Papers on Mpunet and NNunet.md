# Literature Review: Multi-Planar Segmentation vs. nnU-Net for Hepatic Vessel Segmentation

## Section 1: Multiplanar Approaches on Hepatic Vessels

### Paper: Kumar et al., 2024, "A Flexible 2.5D Medical Image Segmentation Approach with In-Slice and Cross-Slice Attention" (CSA-Net)

**Problem Statement:**
The authors address the challenge of segmenting 2.5D medical images—images with high in-plane resolution but low through-plane resolution. Conventional 2D methods fail to capture inter-slice relationships, while 3D methods face challenges with computational complexity, resolution inconsistencies, and susceptibility to overfitting on limited data[40].

**Dataset Used:**
- Brain MRI dataset (private): 57 T2-weighted brain MRI volumes from infants, with 42 for training and 15 for testing
- Promise12 Dataset (public): 80 T2-weighted prostate MR images, 50 for training and 30 for testing
- ProstateX Dataset (public): 98 T2-weighted prostate MRI images, 68 for training and 30 for testing

*Note:* This paper does not directly use hepatic vessel datasets, but demonstrates multiplanar fusion principles applicable to vascular structures.

**Model/Method:**
CSA-Net is a 2.5D segmentation architecture comprising:
1. **Feature Extractor:** ResNet-50 encoder extracts features from three consecutive slices (previous, center, next)
2. **Cross-Slice Attention (CSA) Module:** Uses cross-attention mechanism where the center slice provides key-value pairs and neighboring slices provide queries, enabling inter-slice information integration. Two CSA modules capture correlations between center-previous and center-next slices
3. **In-Slice Attention (ISA) Module:** Self-attention mechanism learns long-range dependencies within the center slice
4. **Attention Aggregation:** Outputs from two CSA modules and one ISA module are concatenated and refined
5. **Vision Transformer Encoder:** Pre-trained 12-layer ViT with 1×1 patch size processes aggregated features
6. **CNN Decoder:** Four decoder blocks with transposed convolutions upsample features to generate final segmentation
7. **Loss Function:** Combination of cross-entropy and Dice loss (0.5 × L_CE + 0.5 × L_DSC)[40]

**Quantitative Performance:**
- Brain Dataset: Brain DSC = 0.967, Ventricles DSC = 0.826, Brain HD95 = 0.682 mm, Ventricles HD95 = 2.12 mm
- Promise12 Dataset (Binary Prostate): DSC = 0.921, HD95 = 1.06 mm
- ProstateX Dataset (Multi-class Prostate): Average DSC = 0.659, Average HD95 = 2.70 mm
  - Transition Zone: DSC = 0.851, HD95 = 2.26 mm
  - Peripheral Zone: DSC = 0.720, HD95 = 3.43 mm
  - Urethra: DSC = 0.653, HD95 = 1.43 mm
  - Anterior: DSC = 0.413, HD95 = 3.71 mm[40]

**Analysis:**

*Engineering Contribution:* CSA-Net's core innovation lies in its pixel-level cross-slice and in-slice attention mechanisms, allowing selective information extraction from neighboring slices. Unlike simpler 2.5D approaches that concatenate adjacent slices as multi-channel inputs, CSA-Net learns *where* to attend across slices[40].

*Dimension Approach:* This is a **2.5D multiplanar** method. It processes three consecutive slices (axial-only in the paper's implementation, though the method could theoretically be extended to sagittal and coronal planes). The method operates on 2D slices but captures 3D context through attention mechanisms.

*Fusion Strategy:* The model employs attention-based fusion. Cross-slice attention dynamically weights information from neighboring slices based on learned correlations with the center slice. Multi-head attention (16 heads) captures diverse feature relationships. The aggregated attention outputs are concatenated and processed through a ViT encoder for global feature refinement[40].

*Loss Functions:* Standard combination of cross-entropy (pixel-wise classification) and Dice loss (region overlap). No topology-aware or vessel-specific losses are used (inferred from the paper)[40].

**Pros:**
- **Computational Efficiency:** 2.5D approach reduces GPU memory requirements compared to 3D models—approximately 20× less memory than equivalent 3D architectures[203]
- **Superior to 2D Methods:** Consistently outperforms pure 2D approaches by 1-2% DSC across all three datasets, demonstrating the value of inter-slice context[40]
- **Flexible Input:** Can handle varying numbers of slices in a volume (processes three at a time), unlike some 2.5D methods (e.g., CAT-Net) that require fixed slice counts[40]
- **Strong Small Structure Performance:** The urethra segmentation improvement (DSC from 0.615 to 0.653) suggests effectiveness on small, complex structures potentially analogous to small hepatic vessels[40]
- **Multi-head Attention:** Captures diverse feature relationships; ablation studies show 16 heads optimal for balancing performance and complexity[40]

**Cons:**
- **No Direct Hepatic Vessel Validation:** Performance on vascular structures, especially thin branching vessels, is not demonstrated
- **Limited Multi-Planar Exploitation:** Only uses single-plane (axial) slices; does not fuse information from sagittal/coronal/axial orientations as true tri-planar methods do
- **No Topology Preservation:** Absence of centerline-Dice (clDice) or connectivity-preserving losses may lead to vessel fragmentation—critical for hepatic vessel segmentation
- **Memory-Accuracy Tradeoff:** While more efficient than 3D, still underperforms 3D methods in some contexts when sufficient GPU memory is available[203]
- **Limited Vessel-Specific Features:** No vessel enhancement preprocessing, multi-scale dilated convolutions targeting tubular structures, or vesselness filtering

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Topology-Aware Loss:** CSA-Net would benefit from clDice loss[157] or centerline-boundary Dice (cbDice)[155] to maintain vessel connectivity, especially critical for hepatic vessels where fragmented predictions are clinically problematic
2. **True Tri-Planar Fusion:** Extending CSA to fuse axial, sagittal, and coronal slices simultaneously (as in tri-planar CNNs[125][127]) could capture vessel orientation better than single-plane processing
3. **Vessel-Specific Preprocessing:** Integration of coherence-enhancing diffusion (CED) filtering or RORPO enhancement[31] could improve contrast of small hepatic vessels before segmentation
4. **Scale-Aware Features:** Multi-scale dilated convolutions in the encoder could better capture vessels of varying calibers

*Next Logical Engineering Step?*
Extend CSA-Net to a **multi-planar cross-slice attention network** where three CSA-Net branches process axial, sagittal, and coronal views independently, then fuse their outputs with a late-fusion strategy. Add topology-preserving clDice loss to maintain vessel continuity.

*How Could My FYP Extend It?*
**Proposed Extension:** "Multi-Planar CSA-Net with Topology-Aware Loss for Hepatic Vessel Segmentation"
1. **Tri-Planar CSA Architecture:** Three parallel CSA-Net streams for axial, sagittal, and coronal orientations
2. **Plane Fusion Module:** Attention-based or statistical fusion (e.g., majority voting, average) of three plane predictions
3. **Hybrid Loss Function:** Combine Dice + Cross-Entropy + clDice (with weighting like 0.4 × Dice + 0.1 × CE + 0.5 × clDice)
4. **Lightweight Design for Limited GPU:** Use depthwise separable convolutions or MobileNet-style blocks in encoder to reduce VRAM footprint (~6GB for RTX 3050)[203]
5. **Validation:** Test on MSD Task08 Hepatic Vessels dataset (303 training cases)[96][99] with comparison to baseline nnU-Net

**Relevance to FYP:**
CSA-Net provides a strong foundation for multi-planar fusion concepts, but requires adaptation for hepatic vessels including topology preservation and tri-planar integration.

---

### Paper: Hung, 2022, "Slow Fusion Triplanar Convolutional Neural Networks for Liver Tumor Segmentation"

**Problem Statement:**
The thesis addresses challenges in liver tumor segmentation from CT scans, including: (i) similar intensities between liver tumor and liver tissues, (ii) small and indeterminate liver tumors difficult to characterize, and (iii) liver tumors with irregular shapes and boundaries. The work explores triplanar CNNs to leverage multiple views (axial, sagittal, coronal) for improved discrimination[132].

**Dataset Used:**
- MICCAI 2017 Liver Tumor Segmentation (LiTS) Challenge dataset
- CT images of liver with tumor annotations
- Specific dataset size not mentioned in available abstract (inferred: standard LiTS has 131 training cases)[132]

**Model/Method:**
"Slow Fusion Triplanar Convolutional Neural Networks"
1. **Triplanar Input Streams:** Three parallel CNNs process axial, sagittal, and coronal views of the same voxel-of-interest (VOI)
2. **Slow Fusion Strategy:** Rather than immediate fusion, features from the three planes are fused gradually through the network depth—contrasting with early fusion (concatenation at input) or late fusion (combining only final outputs)
3. **Feature Learning:** Each stream extracts discriminative features from its respective plane to classify liver tumor vs. healthy liver tissue
4. **Architecture Details:** Not fully specified in available abstract, but triplanar CNNs typically use shared or separate weights across planes (inferred)[132]

**Quantitative Performance:**
Performance metrics not provided in the accessible thesis abstract. Typical triplanar liver tumor segmentation achieves volume overlap error of 3.6-6.7% on 3DIRCADb[127] (inferred from related work, not this specific thesis).

**Analysis:**

*Engineering Contribution:* The "slow fusion" strategy is the key innovation—gradually integrating multi-view information throughout the network rather than at input or output only. This allows the model to learn view-specific low-level features while progressively combining them for higher-level semantic understanding.

*Dimension Approach:* **2.5D triplanar** method. Three 2D CNNs operate on orthogonal planes (axial, sagittal, coronal), effectively capturing 3D context without full 3D convolutions.

*Fusion Strategy:* "Slow fusion" refers to hierarchical fusion at multiple depths. Early layers process each plane independently; middle layers begin cross-plane interaction; deeper layers fully integrate multi-view features. This contrasts with:
- **Early fusion:** Concatenating three planes as 3-channel input
- **Late fusion:** Averaging or voting on three independent plane predictions[132]

*Loss Functions:* Not specified in available abstract (inferred: likely Dice or cross-entropy for tumor segmentation).

**Pros:**
- **Multi-View Exploitation:** Captures vessel/tumor orientation information better than single-plane methods—critical for hepatic vessels that may appear as dots in one plane but elongated in another
- **Hierarchical Fusion:** Slow fusion allows learning plane-specific features (e.g., vessel cross-sections in axial) before multi-view integration
- **Reduced Computational Cost vs. 3D:** Triplanar 2D CNNs require ~20× less GPU memory than equivalent 3D CNNs[203]
- **Robustness to Orientation:** Tumors/vessels with complex 3D geometry are better characterized when viewed from multiple orthogonal directions

**Cons:**
- **Limited Methodological Details:** Thesis abstract does not provide architectural specifics, making replication challenging
- **Lack of Quantitative Results:** Performance metrics not available for comparison
- **Tumor-Focused, Not Vessel-Optimized:** Designed for tumor segmentation (larger, blob-like structures) rather than thin, branching hepatic vessels—may lack vessel-specific design elements
- **No Topology Preservation Mentioned:** Unlikely to include clDice or connectivity constraints (inferred), which are crucial for vessel segmentation
- **Fusion Mechanism Unclear:** The exact slow fusion implementation (attention-based? concatenation? weighted sum?) is not described[132]

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Vessel-Specific Architectural Components:** Multi-scale dilated convolutions or RORPO enhancement filters to improve thin vessel detection
2. **Topology-Aware Loss:** clDice loss to maintain vessel continuity across fusion planes
3. **Attention Mechanisms:** Cross-plane attention (like CSA-Net) could improve fusion quality compared to simple slow fusion
4. **Quantitative Validation on Vessel Dataset:** Testing on MSD Task08 or 3DIRCADb hepatic vessel segmentation would demonstrate vessel applicability

*Next Logical Engineering Step?*
Combine slow fusion triplanar strategy with attention-based cross-plane fusion and topology-preserving losses.

*How Could My FYP Extend It?*
**Proposed Extension:** "Attention-Guided Slow Fusion Triplanar U-Net for Hepatic Vessels"
1. **Triplanar U-Net Backbone:** Three U-Net encoders for axial, sagittal, coronal planes
2. **Slow Fusion with Attention:** At each encoder depth level, apply cross-plane attention (similar to CSA-Net's cross-slice attention) to progressively fuse features
3. **Topology-Aware Loss:** 0.5 × Dice + 0.5 × clDice to preserve vessel connectivity
4. **Vesselness Enhancement Preprocessing:** Apply Frangi or RORPO vesselness filter before input to enhance small vessels
5. **Lightweight Encoder Design:** Use EfficientNet or MobileNet encoder to reduce VRAM usage for RTX 3050 (~6GB)

**Relevance to FYP:**
Provides multiplanar fusion baseline concept, but requires vessel-specific enhancements (topology loss, vesselness, attention) for hepatic vessel application.

---

### Paper: Wang et al., 2018, "Triplanar Convolutional Neural Network for Automatic Liver and Tumor Image Segmentation"

**Problem Statement:**
Automatic liver and tumor segmentation is critical for hepatocellular carcinoma diagnosis and treatment. The work proposes a triplanar fully convolutional network (FCN) to leverage multi-dimensional features for 3D segmentation. A cascaded structure balances positive/negative samples for tumor segmentation[127].

**Dataset Used:**
- 3D-IRCADb-01 dataset: 20 3D CT volumes (inferred: standard 3D-IRCADb has 20 cases for training)
- Contains liver and tumor annotations
- Hepatic tumors present in 75% of cases[127]

**Model/Method:**
"Triplanar Fully Convolutional Network (FCN)"
1. **Three 2D CNNs:** Separate networks process transverse (axial), coronal, and sagittal planes
2. **Multi-Dimensional Feature Extraction:** Each plane CNN extracts 2D features; fusion captures 3D spatial information
3. **Cascaded Structure:** Two-stage approach where liver segmentation is followed by tumor segmentation within the liver region, balancing class imbalance[127]
4. **Architecture:** FCN-based (likely similar to FCN-8s or FCN-16s architectures, inferred)

**Quantitative Performance:**
- **Liver Segmentation:** Volume Overlap Error (VOE) = 6.7%
- **Tumor Segmentation:** Volume Overlap Error (VOE) = 3.6%
- Outperforms existing methods (not specified) on 3D-IRCADb[127]

**Analysis:**

*Engineering Contribution:* The triplanar FCN architecture captures 3D context through multi-view 2D processing. The cascaded liver-then-tumor approach addresses class imbalance (tumors are much smaller than liver), which is analogous to the challenge in hepatic vessels (vessels are sparse within liver parenchyma).

*Dimension Approach:* **2.5D triplanar** method using three orthogonal 2D CNNs.

*Fusion Strategy:* The paper likely uses late fusion (averaging or voting on plane predictions, inferred) or soft-max fusion. Exact fusion mechanism not specified in available abstract[127].

*Loss Functions:* Not specified (inferred: likely cross-entropy or Dice for segmentation tasks).

**Pros:**
- **Strong Performance:** VOE of 6.7% for liver and 3.6% for tumor indicates high accuracy
- **Cascaded Design:** Two-stage approach (liver → tumor) is analogous to liver → vessel segmentation, addressing region-of-interest localization first
- **Demonstrated on Liver Domain:** Unlike CSA-Net, this is validated on liver CT data—more relevant to hepatic vessel task
- **Multi-View Integration:** Three orthogonal planes capture vessel orientation diversity

**Cons:**
- **No Direct Vessel Segmentation:** Focuses on liver parenchyma and tumors, not the vascular tree—vessels have different morphology (tubular, branching) than tumors (blob-like)
- **Limited Architectural Details:** FCN architecture is less sophisticated than modern U-Net variants with skip connections
- **No Topology Preservation:** Likely lacks clDice or connectivity constraints (inferred), critical for vessel continuity
- **Small Dataset:** Only 20 cases in 3D-IRCADb limits generalization assessment
- **Unclear Fusion Mechanism:** The method of combining three plane predictions is not described[127]

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Vessel-Specific Design:** The tumor segmentation task differs from vessel segmentation—vessels require centerline accuracy and connectivity preservation, while tumors require boundary precision
2. **Modern Architecture:** FCN lacks skip connections; upgrading to U-Net or attention-based models would improve performance
3. **Topology-Aware Loss:** clDice or centerline loss to maintain vessel continuity
4. **Vessel Enhancement:** Frangi, Sato, or RORPO vesselness filtering to improve vessel contrast

*Next Logical Engineering Step?*
Replace FCN with U-Net architecture, incorporate attention-based multi-plane fusion, and add topology-aware loss for vessel-specific optimization.

*How Could My FYP Extend It?*
**Proposed Extension:** "Cascaded Triplanar U-Net with Topology Preservation for Hepatic Vessels"
1. **Stage 1 (Liver Localization):** 3D U-Net or nnU-Net segments liver parenchyma
2. **Stage 2 (Vessel Segmentation):** Triplanar U-Net operates on liver ROI:
   - Three U-Net branches for axial, sagittal, coronal planes
   - Each branch outputs vessel probability map
   - Fusion: Soft-max averaging of three plane predictions
3. **Topology-Aware Loss:** 0.5 × Dice + 0.5 × clDice on fused output
4. **RORPO Preprocessing:** Apply RORPO vesselness enhancement on each plane before segmentation[31]
5. **Validation:** Compare against nnU-Net baseline on MSD Task08 with clDice and branching metrics

**Relevance to FYP:**
Provides proof-of-concept for triplanar segmentation on liver CT data, but requires adaptation for vessel morphology (tubular structures) and topology preservation.

---

### Paper: Prasoon et al., 2013, "Deep Feature Learning for Knee Cartilage Segmentation Using a Triplanar Convolutional Neural Network"

**Problem Statement:**
Segmentation of tibial cartilage in low-field knee MRI is challenging due to noise and speckle. The authors propose a triplanar CNN to integrate 2D features from three orthogonal planes (xy, yz, zx) for 3D voxel classification[125].

**Dataset Used:**
- 114 low-field knee MRI scans
- 45 scans for training (120,000 voxels)
- 12 scans for validation
- 10 scans for testing
- Manual segmentation by radiologist as ground truth[125]

**Model/Method:**
"Triplanar Convolutional Neural Network"
1. **Three 2D CNNs:** Each CNN processes one plane (xy = axial, yz = sagittal, zx = coronal)
2. **Patch Extraction:** For each target voxel, three patches (one per plane, centered on the voxel) are extracted
3. **Feature Fusion:** Outputs (feature vectors) from three CNNs are concatenated
4. **Voxel Classification:** Concatenated features fed to fully connected layers for binary classification (cartilage vs. background)
5. **Training:** Uses only 120,000 training voxels (vs. 2.1 million in baseline), demonstrating data efficiency[125]

**Quantitative Performance:**
- **DSC:** 0.8249 ± 4.26%
- **Accuracy:** 99.93% ± 1.86%
- **Sensitivity:** 81.92% ± 7.62%
- **Specificity:** 99.97% ± 1.74%
- **Comparison:** Outperforms state-of-the-art kNN-based method (DSC = 0.8135) using 17× fewer training samples[125]

**Analysis:**

*Engineering Contribution:* The triplanar CNN pioneered multi-view deep learning for medical image segmentation (2013, early deep learning era). The key insight is that orthogonal 2D patches provide complementary 3D context without 3D convolutions, achieving better performance than 3D CNN (DSC ~2% lower for 3D) while being computationally efficient[125].

*Dimension Approach:* **2.5D triplanar** voxel-wise classification. Three 2D CNNs operate on orthogonal planes.

*Fusion Strategy:* **Feature-level fusion** via concatenation of CNN outputs before classification. This is an intermediate fusion approach (between early and late fusion).

*Loss Functions:* Not specified (inferred: cross-entropy for binary classification, standard for 2013-era CNNs).

**Pros:**
- **Data Efficiency:** Achieves superior performance with 17× fewer training samples than baseline, suggesting strong feature learning from multi-view integration[125]
- **Computational Efficiency:** 2D CNNs are faster and require less memory than 3D CNNs; triplanar approach better than single 3D CNN in this study
- **Pioneering Work:** Early demonstration of multi-view deep learning for medical segmentation—established foundation for later triplanar methods
- **Robust to Noise:** Performs well on low-field MRI with noise and speckle, suggesting potential for challenging hepatic vessel segmentation in low-contrast CT[125]

**Cons:**
- **Outdated Architecture:** Uses basic CNNs without batch normalization, residual connections, or modern regularization—would not be competitive with 2025 standards
- **No Topology Preservation:** Voxel-wise classification without connectivity constraints—would produce fragmented vessel predictions
- **Limited to Cartilage:** Cartilage is a relatively uniform structure; hepatic vessels have complex branching topology requiring different design considerations
- **Patch-Based Inference:** Voxel-by-voxel classification is slow; modern FCN/U-Net approaches are more efficient for dense prediction
- **No Vessel-Specific Features:** Lacks multi-scale analysis, vesselness filtering, or dilated convolutions for tubular structures[125]

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Modern Architecture:** Replace basic CNNs with U-Net or ResNet encoders with skip connections
2. **Topology-Aware Loss:** Add clDice loss to maintain vessel connectivity
3. **Dense Prediction:** Move from patch-based voxel classification to fully convolutional dense segmentation for efficiency
4. **Multi-Scale Features:** Incorporate dilated convolutions or feature pyramid networks to capture vessels of varying calibers

*Next Logical Engineering Step?*
Upgrade triplanar architecture to modern U-Net-based design with dense prediction, attention-based fusion, and topology-preserving loss.

*How Could My FYP Extend It?*
**Proposed Extension:** "Modern Triplanar U-Net with Cross-Plane Attention for Hepatic Vessels"
1. **Triplanar U-Net:** Three 2D U-Net encoders for axial, sagittal, coronal planes
2. **Cross-Plane Attention Fusion:** Replace concatenation with attention-based fusion (inspired by CSA-Net) to selectively weight plane contributions
3. **Topology-Aware Loss:** 0.5 × Dice + 0.5 × clDice
4. **Multi-Scale Encoder:** Use dilated convolutions with rates [1, 2, 4, 8] to capture vessels of multiple scales
5. **Dense Prediction:** Output full 2D segmentation map per plane, fuse at output level
6. **Validation:** MSD Task08 with comparison to nnU-Net, measuring Dice, clDice, and branch detection rate

**Relevance to FYP:**
Historical foundation for triplanar methods, but requires substantial modernization for hepatic vessel application (U-Net, topology loss, attention fusion).

---

## Section 2: nnU-Net on Hepatic Vessels

### Paper: Isensee et al., 2021, "nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation" (Medical Segmentation Decathlon Results)

**Problem Statement:**
Medical image segmentation requires task-specific network configurations (architecture, preprocessing, augmentation, loss functions), leading to poor generalization across domains. nnU-Net proposes a self-configuring framework that automatically adapts to dataset properties, achieving state-of-the-art performance across diverse tasks without manual tuning[96][99].

**Dataset Used:**
Medical Segmentation Decathlon (MSD) challenge comprising 10 tasks across different organs, modalities, and target structures:
- **Task 08: Hepatic Vessel** (relevant to FYP)
  - **Modality:** CT (portal venous phase)
  - **Size:** 443 3D volumes (303 training + 140 testing)
  - **Source:** Memorial Sloan Kettering Cancer Center
  - **Target:** Hepatic vessels and tumors
  - **Challenge:** Small, tubular structures near heterogeneous tumors[96][99][176]

**Model/Method:**
**nnU-Net (no-new-U-Net) Framework**
1. **Self-Configuring Pipeline:**
   - **Automatic Preprocessing:** Analyzes dataset properties (spacing, intensity distribution) and applies resampling, normalization, and cropping
   - **Architecture Selection:** Chooses between 2D U-Net, 3D U-Net (full-resolution), or 3D U-Net (cascade) based on image dimensions and GPU memory
   - **Hyperparameter Optimization:** Automatically configures patch size, batch size, learning rate, data augmentation
2. **U-Net Variants:**
   - **2D U-Net:** For slice-wise segmentation
   - **3D U-Net (full-res):** For volumetric segmentation with manageable memory
   - **3D U-Net (cascade):** Two-stage coarse-to-fine for large 3D volumes
3. **Training:**
   - **Loss Function:** Combination of Dice and cross-entropy
   - **Optimizer:** SGD with momentum and Nesterov acceleration
   - **Data Augmentation:** Rotation, scaling, elastic deformation, Gaussian noise, brightness adjustment
4. **Inference:** Ensemble of multiple models with test-time augmentation[89][96][99]

**Quantitative Performance:**

**Medical Segmentation Decathlon Challenge (Overall):**
- **Development Phase (10 tasks, 13 target ROIs):** Median DSC = 0.79 (IQR: 0.61–0.88)
- **Mystery Phase (4 tasks, 4 target ROIs):** Median DSC = 0.71 (IQR: 0.58–0.82)
- **Ranking:** 1st place in both phases—most robust method across all tasks[96][99]

**Task 08: Hepatic Vessel Segmentation (from MSD Paper):**
- **Median DSC:** 0.63 (development phase, nnU-Net)
- **Performance Note:** Lower than other MSD tasks due to small vessel challenge. The median DSC across all participants for hepatic vessel task ranged from 0.16 (worst method) to ~0.63 (nnU-Net)[96][99]
- *Note:* MSD paper reports aggregated results; specific vessel vs. tumor breakdown not provided.

**Task 08: Hepatic Vessel (from Related Studies):**
- **Hille et al., 2024 (nnU-Net on MSD Task08):**
  - **Dice:** 0.714 on LiVS dataset, 0.696 on MSD dataset[73]
- **Wang et al., 2020:**
  - **Dice:** 0.6343 on MSD Task08 (baseline nnU-Net)[94][176]

**Hepatic Vessel Segmentation (Other Datasets - nnU-Net Performance):**
- **Chierici et al., 2025 (nnU-Net on CRLM portal phase CT):**
  - **Portal Vein:** Dice = 0.76 ± 0.076, clDice = 0.758 ± 0.078
  - **Hepatic Veins:** Dice = 0.795 ± 0.059, clDice = 0.762 ± 0.080
  - **Cava Vein:** Dice = 0.812 ± 0.117, clDice = 0.805 ± 0.082
  - External Validation: Portal Vein clDice = 0.736, Hepatic Veins clDice = 0.577[94][95][141][151]

**Analysis:**

*Engineering Contribution:* nnU-Net's innovation is not a novel architecture but a **self-configuring methodology** that automatically determines optimal preprocessing, architecture (2D/3D), patch size, augmentation, and training hyperparameters based on dataset fingerprinting. This "no-new" philosophy emphasizes that proper configuration often outperforms novel architectures.

*Dimension Approach:* **Adaptive 2D/3D**. nnU-Net automatically selects:
- **3D U-Net full-resolution:** For datasets with manageable memory requirements (likely used for MSD Task08 given volumetric nature)
- **3D U-Net cascade:** For very large volumes
- **2D U-Net:** For datasets with anisotropic resolution or memory constraints[96]

*Fusion Strategy:* When multiple configurations are used (e.g., 2D + 3D full-res + 3D cascade), nnU-Net employs **ensemble averaging** of predicted probability maps to produce final segmentation.

*Loss Functions:* **Dice + Cross-Entropy** (equal weighting by default). nnU-Net does not use topology-aware losses like clDice in standard configuration (inferred)[96].

**Pros:**
- **State-of-the-Art Generalization:** Won MSD challenge across 10 diverse tasks, demonstrating robustness—important for FYP where a general-purpose baseline is needed[96][99]
- **Automatic Configuration:** Reduces manual tuning burden; suitable for FYP with limited time for hyperparameter optimization
- **Well-Documented and Reproducible:** Open-source implementation with extensive documentation; widely used as benchmark in medical segmentation literature[96]
- **Strong Liver Vessel Performance:** clDice ~0.76 for portal/hepatic veins indicates good topology preservation despite not using clDice loss[94][95]
- **Handles Small Vessels Reasonably:** Achieves 0.63-0.71 Dice on MSD Task08, though room for improvement exists[73][94]
- **Ensemble Strategy:** Combining 2D and 3D models improves robustness[96]

**Cons:**
- **Not Vessel-Optimized:** nnU-Net is a general-purpose framework lacking vessel-specific design elements:
  - No multi-scale vesselness filtering
  - No topology-preserving clDice loss (in standard config)
  - No specialized architecture for tubular structures
- **Moderate Performance on Thin Vessels:** Dice 0.63-0.71 on MSD Task08 suggests difficulty with small, branching hepatic vessels—multiplanar or topology-aware methods may improve[73][94]
- **High Computational Requirements (3D variant):** 3D U-Net requires ~3200 MB GPU memory vs. 190 MB for 2D—may be challenging on RTX 3050 (6GB)[203]
- **Limited Interpretability:** Automatic configuration is a "black box"—difficult to understand which design choices drive performance
- **No Multi-View Integration:** nnU-Net processes single 3D volume or 2D slices; does not leverage tri-planar fusion[96]

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Topology-Aware Loss:** Adding clDice or cbDice loss would improve vessel connectivity. Shit et al. (2021) showed clDice improves topology preservation in tubular structures[157]
2. **Vesselness Enhancement:** Preprocessing with RORPO or Frangi filters could boost small vessel contrast. Alirr et al. (2023) showed vesselness + nnU-Net improved hepatic vessel Dice by ~3%[93]
3. **Multi-Planar Fusion:** Combining axial, sagittal, coronal predictions could improve vessel orientation detection, especially for thin distal branches
4. **Multi-Scale Features:** Dilated convolutions or attention modules targeting vessels at multiple scales (as in LVSNet[56]) could improve performance

*Next Logical Engineering Step?*
Extend nnU-Net with topology-aware loss and vesselness preprocessing while maintaining self-configuring pipeline.

*How Could My FYP Extend It?*
**Proposed Extension:** "Multi-Planar nnU-Net with Topology-Aware Loss for Hepatic Vessels"
1. **Baseline:** Standard nnU-Net 3D full-resolution on MSD Task08 (303 training cases)
2. **Multiplanar Extension:** Train three 2D nnU-Net models on axial, sagittal, coronal slices; fuse predictions via soft-max averaging
3. **Topology-Aware Loss:** Modify nnU-Net loss to: 0.4 × Dice + 0.1 × CE + 0.5 × clDice
4. **RORPO Preprocessing:** Apply RORPO vesselness enhancement[31] on input images to boost small vessel contrast
5. **Validation Metrics:** Report Dice, clDice, centerline recall, branch detection rate
6. **Comparison:** Multi-planar nnU-Net + clDice vs. baseline nnU-Net

**Expected FYP Contribution:**
Demonstrate that multiplanar fusion and topology-aware loss improve small vessel segmentation over baseline nnU-Net, especially for thin distal branches. Provide quantitative analysis of trade-offs (Dice vs. clDice, computational cost, qualitative vessel connectivity).

---

### Paper: Kazami et al., 2024, "Hepatic Vessel Segmentation and Classification in CTA Images Using nnU-Net with Centerline Regression"

**Problem Statement:**
Manual segmentation of liver vessels is time-consuming and prone to variability, affecting treatment planning for hepatocellular carcinoma. The authors participate in VEELA 2025 challenge, utilizing nnU-Net with centerline regression and enhanced loss functions to improve hepatic and portal vein segmentation and classification[4].

**Dataset Used:**
- **VEELA 2025 Challenge Data:** 20 training + 20 testing hepatic and portal vein labeled CTA images
- **Additional Training Data:** Medical Segmentation Decathlon (MSD), LIRCAD, VEELA 2025 (combined due to limited CTA annotations)
- **Modality:** CTA (Computed Tomography Angiography) and contrast-enhanced CT[4]

**Model/Method:**
**nnU-Net with Centerline Regression and Enhanced Loss Functions**
1. **Baseline:** nnU-Net framework (3D full-resolution, inferred)
2. **Multi-Dataset Training:** Combined CTA and contrast-enhanced CT data to address limited labeled CTA availability
3. **Enhanced Loss Functions (5 models tested):**
   - **Model 1:** Dice Similarity Coefficient (DSC) + Cross-Entropy
   - **Model 2:** DSC + Cross-Entropy + **Centerline Dice Loss (clDice)** (topology preservation)
   - **Model 3:** DSC + Cross-Entropy + Edge Map Dice Loss (boundary precision)
   - **Model 4:** Centerline Regression Cross-Entropy for minor vessel classification
   - **Model 5 (Final):** **Weighted Loss Strategy** prioritizing pixel-wise classification while reinforcing spatial consistency and structure preservation (combination of above)
4. **Key Innovation:** Centerline regression cross-entropy for minor vessel classification—helps identify small vessel branches
5. **Data Augmentation:** nnU-Net's standard augmentation pipeline[4]

**Quantitative Performance:**
- **VEELA 2025 Challenge Ranking:** **1st place (top-ranked)**
- **Specific Metrics:** Not provided in abstract (detailed results likely in full paper)
- **Key Achievement:** Best performance in vessel segmentation and classification, with particular strength in topology continuity (inferred due to clDice loss)[4]

**Analysis:**

*Engineering Contribution:* The paper extends nnU-Net with **centerline regression and hybrid loss functions** (Dice + CE + clDice + Edge Dice) to address vessel topology and boundary precision simultaneously. The centerline regression component is particularly novel, enabling classification of minor vessel branches—critical for hepatic vessel characterization.

*Dimension Approach:* **3D** (inferred from nnU-Net framework and volumetric CTA data).

*Fusion Strategy:* Not a multi-planar fusion approach; single 3D nnU-Net model.

*Loss Functions:* **Hybrid weighted loss strategy:**
- **Dice Loss:** Region overlap
- **Cross-Entropy:** Pixel-wise classification
- **clDice Loss:** Topology preservation (centerline continuity)[157]
- **Edge Map Dice Loss:** Boundary precision
- **Centerline Regression CE:** Minor vessel classification

This multi-objective loss balances segmentation accuracy, topology, and boundary sharpness[4].

**Pros:**
- **Challenge Winner:** 1st place in VEELA 2025 demonstrates state-of-the-art performance on hepatic vessel segmentation and classification[4]
- **Topology-Aware:** clDice loss improves vessel connectivity—crucial for clinical applications requiring complete vascular tree reconstruction
- **Small Vessel Classification:** Centerline regression enables classification of minor vessels, addressing key challenge in hepatic vessel characterization
- **Multi-Dataset Training:** Leveraging MSD, LIRCAD, and VEELA data mitigates limited labeled CTA availability—practical strategy for FYP with limited resources
- **Weighted Loss Strategy:** Balances multiple objectives (overlap, boundary, topology) for comprehensive segmentation quality

**Cons:**
- **Limited Methodological Details:** Abstract does not provide:
  - Exact weighted loss formulation
  - Centerline regression architecture details
  - Quantitative metrics (Dice, clDice values)
- **Computational Cost:** nnU-Net 3D requires substantial GPU memory (~3.2 GB for standard, possibly higher with centerline regression)[203]—may be challenging on RTX 3050
- **No Multi-Planar Fusion:** Single 3D model; does not leverage multi-view information that could improve vessel orientation detection
- **Limited Generalization Assessment:** Validated on single challenge dataset (VEELA 2025); performance on MSD Task08 or 3DIRCADb not reported

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Multi-Planar Integration:** Centerline regression could benefit from multi-view inputs (axial, sagittal, coronal) to better classify vessel branches with complex orientations
2. **Quantitative Analysis:** Detailed ablation study comparing contributions of each loss component (clDice vs. Edge Dice vs. Centerline Regression)
3. **Computational Efficiency:** Centerline regression adds parameters; lightweight alternatives (e.g., depthwise separable convolutions) could reduce VRAM
4. **Public Benchmark:** Testing on MSD Task08 would enable comparison with other hepatic vessel methods

*Next Logical Engineering Step?*
Integrate multi-planar processing with centerline regression to improve vessel classification in complex orientations.

*How Could My FYP Extend It?*
**Proposed Extension:** "Multi-Planar nnU-Net with Centerline Regression for Hepatic Vessel Classification"
1. **Triplanar nnU-Net:** Three 2D nnU-Net branches for axial, sagittal, coronal slices
2. **Centerline Regression per Plane:** Each branch outputs:
   - Vessel segmentation mask
   - Centerline probability map
   - Vessel classification (portal vein, hepatic vein, tumor vessel)
3. **Multi-Planar Fusion:** Fuse three plane outputs with weighted averaging (weights learned during training)
4. **Hybrid Loss:** 0.3 × Dice + 0.1 × CE + 0.4 × clDice + 0.2 × Centerline Regression CE
5. **Validation:** MSD Task08 with metrics: Dice, clDice, centerline recall, vessel classification accuracy, branch detection rate
6. **Comparison:** Multi-planar variant vs. single 3D nnU-Net (baseline)

**Relevance to FYP:**
Demonstrates state-of-the-art nnU-Net extension for hepatic vessels with topology awareness. FYP can build on this by adding multi-planar fusion to improve vessel orientation and classification.

---

### Paper: Hille et al., 2024, "Deep Learning-Based Liver Vessel Segmentation"

**Problem Statement:**
Liver vessel segmentation in CT is challenging due to: (1) imbalanced distribution within liver parenchyma, (2) small, branched vessels with low contrast, and (3) scarcity of high-resolution/high-contrast images. The study applies nnU-Net and transformer-based VT-UNet to three public datasets to benchmark state-of-the-art methods[73].

**Dataset Used:**
Three publicly available hepatic vessel datasets:
1. **3D-IRCADb-01:** 20 CT volumes (20 training + 2 testing, inferred from standard split)
2. **Medical Segmentation Decathlon Task 08 (MSD):** 443 CT volumes (303 training + 140 testing)
3. **LiVS (Liver Vessel Segmentation) dataset:** More recent, large-scale dataset (exact size not specified)[73]

**Model/Method:**
Two state-of-the-art architectures compared:
1. **nnU-Net (fully convolutional):** Self-configuring U-Net framework with automatic preprocessing, architecture selection, and hyperparameter optimization
2. **VT-UNet (transformer-based):** U-Net encoder replaced with Vision Transformer (ViT) for global feature learning, retaining U-Net decoder[73]

**Quantitative Performance:**

**nnU-Net Results:**
- **3D-IRCADb:** Dice = **0.761**
- **LiVS:** Dice = **0.714**
- **MSD Task08:** Dice = **0.696**

**VT-UNet Results:**
- **3D-IRCADb:** Dice = **0.795** (best)
- **LiVS:** Dice = **0.713**
- **MSD Task08:** Dice = **0.610** (worst)

**Analysis:**
- VT-UNet outperforms nnU-Net on 3D-IRCADb and achieves similar performance on LiVS
- nnU-Net outperforms VT-UNet on MSD Task08 (likely due to larger dataset favoring CNN's inductive bias)
- Performance varies significantly across datasets (Dice range: 0.61–0.795), indicating dataset-specific challenges[73]

**Analysis:**

*Engineering Contribution:* This is a **benchmarking study** comparing fully convolutional (nnU-Net) vs. transformer-based (VT-UNet) approaches on hepatic vessel segmentation. The key finding is that no single architecture dominates across all datasets—VT-UNet excels on smaller, high-quality data (3D-IRCADb), while nnU-Net is more robust on larger, heterogeneous data (MSD Task08).

*Dimension Approach:* **3D** for both nnU-Net and VT-UNet (inferred from volumetric CT data and architectural descriptions).

*Fusion Strategy:* Not applicable (single models, not multi-planar fusion).

*Loss Functions:* nnU-Net uses Dice + Cross-Entropy; VT-UNet likely uses similar (not specified)[73].

**Pros:**
- **Comprehensive Benchmarking:** Evaluates two leading architectures on three diverse hepatic vessel datasets, providing robust performance assessment
- **Dataset Diversity:** Testing on 3D-IRCADb (20 cases), MSD (443 cases), and LiVS captures performance across different scales and imaging protocols
- **Transformer Comparison:** VT-UNet's superior performance on 3D-IRCADb (Dice 0.795) suggests transformers can improve small dataset segmentation via global context
- **Baseline Establishment:** nnU-Net Dice of 0.696–0.761 provides FYP baseline for MSD Task08
- **Reproducibility:** Uses public datasets, enabling FYP replication and comparison

**Cons:**
- **No Topology Metrics:** Only reports Dice; lacks clDice, centerline recall, or branch detection rate—important for assessing vessel connectivity
- **Limited Architectural Innovation:** Study is comparative, not proposing novel methods; FYP should extend beyond pure benchmarking
- **No Multi-Planar Evaluation:** Single 3D models; does not explore whether multi-planar fusion could improve performance
- **Dataset Imbalance:** MSD (443 cases) vs. 3D-IRCADb (20 cases) makes cross-dataset comparison challenging; performance may reflect data quantity, not just method quality
- **Lack of Vessel-Specific Design:** Neither nnU-Net nor VT-UNet incorporate vesselness filtering, clDice loss, or multi-scale vessel-aware modules

**Critical Evaluation / How to Improve:**

*What is Missing?*
1. **Topology-Aware Metrics:** Reporting clDice, branch detection rate, and centerline recall would better assess vessel segmentation quality beyond Dice
2. **Ablation Studies:** Testing nnU-Net/VT-UNet with clDice loss, vesselness preprocessing, or multi-scale dilated convolutions to identify performance bottlenecks
3. **Multi-Planar Fusion:** Comparing 3D models with triplanar 2D ensembles to evaluate multi-view benefits
4. **Qualitative Analysis:** Visualizing failure cases (e.g., missed small vessels, broken branches) to guide architectural improvements

*Next Logical Engineering Step?*
Extend nnU-Net with topology-aware loss and vesselness preprocessing; compare with VT-UNet + same enhancements.

*How Could My FYP Extend It?*
**Proposed Extension:** "Multi-Planar nnU-Net vs. Baseline nnU-Net for Hepatic Vessel Segmentation on MSD Task08"
1. **Baseline:** Reproduce nnU-Net results on MSD Task08 (expected Dice ~0.70)
2. **Multi-Planar nnU-Net:** Train three 2D nnU-Net models on axial, sagittal, coronal slices; fuse with soft-max averaging
3. **Enhancements:**
   - Add clDice loss: 0.5 × Dice + 0.5 × clDice
   - Apply RORPO vesselness preprocessing
4. **Evaluation:**
   - Quantitative: Dice, clDice, centerline recall, branch detection rate
   - Qualitative: Visualize vessel connectivity, small vessel preservation
5. **Analysis:** Determine whether multi-planar fusion improves small vessel segmentation and topology preservation over baseline nnU-Net

**Relevance to FYP:**
Provides baseline nnU-Net performance on MSD Task08 (Dice 0.696). FYP can build on this by evaluating whether multi-planar fusion and topology-aware loss improve upon this baseline, especially for thin distal vessels.

---

## Section 3: Comparison and FYP Implications

### Multiplanar on Hepatic Vessels vs. nnU-Net on Hepatic Vessels

#### **1. Performance on Small/Thin Vessel Branches**

**Multiplanar Approaches:**
- **Theoretical Advantage:** Multiplanar methods (CSA-Net, triplanar CNNs) capture vessel orientation from multiple viewpoints (axial, sagittal, coronal). This is particularly beneficial for thin vessels that may appear as small dots in one plane but elongated tubular structures in orthogonal planes[40][125][127].
- **Evidence from Related Domains:** CSA-Net's urethra segmentation improvement (DSC 0.615 → 0.653) on small structures suggests multiplanar fusion helps small object detection[40]. Triplanar CNN outperformed 3D CNN on knee cartilage (DSC 0.8249 vs. ~0.80)[125].
- **Limitation:** **No direct hepatic vessel validation** for CSA-Net or recent triplanar methods. Triplanar FCN on liver tumors (VOE 3.6%)[127] does not test thin vessels.
- **Inferred Performance:** If extended with topology-aware loss (clDice), multiplanar methods could improve small vessel connectivity by enforcing centerline continuity across planes. However, without such enhancements, they may fragment thin vessels similarly to nnU-Net.

**nnU-Net:**
- **Quantitative Performance:** Dice 0.63–0.71 on MSD Task08 hepatic vessels[73][94][96]. Chierici et al. reported clDice ~0.76 for portal/hepatic veins, indicating moderate topology preservation[94][95].
- **Small Vessel Challenge:** nnU-Net struggles with thin distal branches (inferred from moderate Dice and literature reports[73]). Lack of topology-aware loss (in standard configuration) leads to vessel fragmentation.
- **Enhancement Potential:** Adding clDice loss and vesselness preprocessing improves small vessel Dice by 3-5% (inferred from Alirr et al.[93] and related studies).

**Comparison:**
- **Current State:** nnU-Net (Dice 0.70) likely performs **similarly or slightly better** than un-optimized multiplanar methods on small vessels, given its robust self-configuration and large-scale training.
- **With FYP Extensions:** Multiplanar + clDice + vesselness could **outperform** baseline nnU-Net on small vessel segmentation by:
  1. Capturing vessel orientation from multiple views
  2. Enforcing topology continuity via clDice
  3. Enhancing vessel contrast via RORPO/Frangi filtering

**Verdict:** **Multiplanar methods have potential to be stronger for small/thin vessels** if properly extended with topology-aware loss and vessel-specific preprocessing, but **unenhanced multiplanar methods are unlikely to exceed baseline nnU-Net**.

---

## References

[1] Springer (2024). "CSSD: Cross-Supervision and Self-denoising for Hybrid-Supervised Hepatic Vessel Segmentation." *MICCAI 2024*.

[2] Springer (2023). "SCAN: sequence-based context-aware association network for hepatic vessel segmentation." *Medical & Biological Engineering & Computing*.

[3] SPIE (2023). "Combining arterial and venous CT scans in a multi-encoder network for improved hepatic vessel segmentation."

[4] IEEE (2025). "Hepatic Vessel Segmentation and Classification in CTA Images Using nnU-Net with Centerline Regression." *VEELA 2025 Challenge*.

[5] ACM (2022). "SU-UNet: A Novel Self-Updating Network for Hepatic Vessel Segmentation in CT Images."

[6] Springer (2021). "Noisy Labels are Treasure: Mean-Teacher-Assisted Confident Learning for Hepatic Vessel Segmentation." *MICCAI 2021*.

[8] BMC Medical Imaging (2023). "Hepatic vessel segmentation based on 3D swin-transformer with inductive biased multi-head self-attention."

[9] IEEE (2021). "3D Graph-Connectivity Constrained Network for Hepatic Vessel Segmentation."

[10] Electronics (2021). "Effects of Enhancement on Deep Learning Based Hepatic Vessel Segmentation."

[31] MDPI (2022). "Automatic Hepatic Vessels Segmentation Using RORPO Vessel Enhancement Filter and 3D V-Net with Variant Dice Loss Function."

[40] arXiv (2024). Kumar et al., "A Flexible 2.5D Medical Image Segmentation Approach with In-Slice and Cross-Slice Attention" (CSA-Net).

[56] IEEE (2020). Yan et al., "An Attention-Guided Deep Neural Network with Multi-Scale Feature Fusion for Liver Vessel Segmentation." (LVSNet)

[73] Hille et al. (2024). "Deep Learning-Based Liver Vessel Segmentation." *Current Directions in Biomedical Engineering*.

[87] IEEE (2022). "Learning to Jointly Segment the Liver, Lesions and Vessels from Partially Annotated Datasets."

[93] AAPM (2023). Alirr et al., "Hepatic vessels segmentation using deep learning and preprocessing enhancement."

[94] Cureus (2025). Chierici et al., "Fully Automatic Artificial Intelligence Liver Anatomy Segmentation in the Management of Colorectal Liver Metastases."

[95] Cureus (2025). Chierici et al., "Fully Automatic Artificial Intelligence Liver Anatomy Segmentation in the Management of Colorectal Liver Metastases" (PDF version).

[96] Nature Communications (2022). Antonelli et al., "The Medical Segmentation Decathlon."

[99] Nature Communications (2022). Antonelli et al., "The Medical Segmentation Decathlon" (Supplementary Material).

[125] Prasoon et al. (2013). "Deep Feature Learning for Knee Cartilage Segmentation Using a Triplanar Convolutional Neural Network." *MICCAI 2013*.

[127] Wang et al. (2018). "Triplanar Convolutional Neural Network for Automatic Liver and Tumor Image Segmentation." *International Journal of Performability Engineering*.

[132] Hung (2022). "Slow Fusion Triplanar Convolutional Neural Networks for Liver Tumor Segmentation." Thesis, University of Science Malaysia.

[141] Cureus (2025). Chierici et al., "Fully Automatic Artificial Intelligence Liver Anatomy Segmentation..." (clDice results).

[151] PubMed (2025). Chierici et al., "Fully Automatic Artificial Intelligence Liver Anatomy Segmentation..." (Abstract).

[155] arXiv (2024). Shi et al., "Centerline Boundary Dice Loss for Vascular Segmentation." *MICCAI 2024*.

[157] CVPR (2021). Shit et al., "clDice - a Novel Topology-Preserving Loss Function for Tubular Structure Segmentation."

[176] PMC (2022). Zhang et al., "Techniques and Algorithms for Hepatic Vessel Skeletonization in Medical Imaging: A Survey."

[203] PMC (2023). Avesta et al., "Comparing 3D, 2.5D, and 2D Approaches to Brain Image Auto-Segmentation."
