# Super-Resolution and Interpolation Methods for Hepatic Vessel Segmentation

**Comprehensive research reveals a growing but still nascent field at the intersection of super-resolution, vessel enhancement, and hepatic segmentation**. While classical interpolation and vesselness filtering dominate current approaches, recent breakthroughs in diffusion models and deep learning-based super-resolution show promising directions for improving vascular structure visibility in 3D medical imaging.

## Hepatic vessel segmentation represents an underexplored frontier for super-resolution methods

Despite the critical importance of accurate hepatic vessel segmentation for surgical planning and disease diagnosis, **only one paper explicitly applies deep learning-based super-resolution to hepatic vessels**. The field predominantly relies on classical interpolation methods combined with vesselness filtering rather than advanced generative or super-resolution approaches. The Medical Segmentation Decathlon Task08 dataset (443 portal venous phase CT scans) has been utilized in multiple studies but primarily with traditional enhancement techniques.

**Self Super-Resolution emerges as most direct approach**: The 2024 paper by Jaouen et al. represents the first and only dedicated application of deep super-resolution to hepatic vessels, achieving **Dice 0.69 and centerline Dice (clDice) 0.65** on the IRCADb dataset. Their SMORE-based method addresses anisotropic voxel spacing (e.g., 0.7×0.7×4 mm³ to 0.7×0.7×0.7 mm³) through self-supervised learning, showing particular benefit for topology preservation—a critical metric for vascular networks that standard Dice scores fail to capture.

**Task08 dataset utilization remains limited**: Only Alirr & Rahni's 2023 work explicitly leverages the full Task08 dataset, achieving **Dice 79%, sensitivity 82.2%** using vesselness enhancement and coherence enhancing diffusion (CED) filtering preprocessing combined with modified U-Net architecture. Their approach demonstrates that classical preprocessing can significantly boost deep learning segmentation performance without requiring super-resolution networks.

## Generative models show remarkable potential but minimal hepatic application

The generative AI landscape for vascular enhancement has exploded since 2020, with diffusion models emerging as the dominant paradigm over GANs. However, **none of these methods have been directly applied to hepatic vessel segmentation**, representing a significant research gap.

**Diffusion models lead the generative revolution**: Three breakthrough papers from 2023-2025 demonstrate diffusion models' superiority for vascular applications. VasTSD (2025) introduces tree-state space diffusion for angiography synthesis, achieving **Dice 0.90-0.92 for 3D vascular morphology** and **connectivity scores of 9.59** across brain and lung datasets—the highest among compared methods. The model's novel state space serialization constructs vascular topologies through dynamic programming, ensuring anatomically continuous vasculature generation.

**Efficient diffusion solves practical deployment challenges**: Res-SRDiff (2024) dramatically advances clinical viability by reducing sampling from 1000+ steps to just 4 steps through residual error shifting. On 7T brain MRI and prostate datasets, it achieves **PSNR 27.37-27.72, SSIM 0.80-0.81** while reconstructing in under 1 second per slice—a 20-66× speedup over traditional diffusion methods. This efficiency makes real-time clinical deployment feasible for the first time.

**GANs maintain relevance for specific applications**: Despite diffusion dominance, GANs excel in particular niches. CAS-GAN (2024) functions as a "virtual contrast agent," synthesizing X-ray angiographies from non-contrast images through disentanglement learning, addressing clinical needs to minimize contrast agent exposure. RV-GAN (2021) demonstrates **AUC 0.9887-0.9914** for retinal vessel segmentation using multi-scale dual-generator architecture with weighted feature matching loss.

**Normalizing flows remain underexplored**: Only one paper applies normalizing flows to vessel-relevant CT reconstruction (Denker et al., 2020), integrating physics-based conditioning with FBP. The approach offers unique advantages in uncertainty quantification and training stability compared to GANs, suggesting untapped potential for vascular applications.

## General vascular super-resolution methods demonstrate strong cross-domain applicability

Eight papers across diverse anatomical regions (brain, coronary, retinal, pulmonary) establish robust super-resolution paradigms that could transfer to hepatic applications, though none have been explicitly adapted for liver imaging.

**Pulmonary vessels achieve state-of-the-art with I2SR module**: HiPaS (2025) incorporates Inter-and-Intra-slice Super Resolution, achieving **DSC 92.25%/89.09% for arteries/veins** on 1,073 CT volumes. The I2SR module mutually learns multi-scale features to address spatial anisotropy, resampling to 0.65×0.65×1.00 mm³ resolution. Notably, it maintains **DSC 89.51%/88.34% even on low-resolution CT** (≥1.25mm slice thickness), detecting 95% of vessel skeleton length—critical for distal small vessel visualization.

**Coronary CT super-resolution reaches clinical deployment**: Nagayama et al.'s 2023 SR-DLR trained on ultra-high-resolution CT data delivers **21% vessel sharpness increase** (560 vs 463 HU/mm) and **31% noise reduction** while improving stenosis grading agreement with invasive angiography (weighted κ=0.83 vs 0.77). The method synthesizes UHR-quality from standard scans without specialized equipment, demonstrating immediate translational value for surgical planning.

**Brain vessel super-resolution addresses multiple clinical scenarios**: Two papers tackle brain vessel enhancement from different angles. Iglesias et al. (2022) synthesize 1mm isotropic MPRAGE-like scans from portable 0.064T MRI, achieving **SSIM 0.9852** and enabling accurate segmentation of veins, sinuses, and CSF on low-cost scanners. The complementary 2022 Frontiers paper uses deep attention mechanisms for multi-sequence (T1/T2/FLAIR) super-resolution on cerebral small vessel disease, validated on 61 patients with **SSIM 0.9852** and significantly reduced false positives versus interpolation.

**Retinal vessels pioneer SR-segmentation integration**: SuperVessel (2022) explicitly combines super-resolution as an auxiliary branch with segmentation, using Upsampling with Feature Decomposition (UFD) to extract high-resolution detail features from low-resolution input. The GAN-based approach by Mahapatra & Bozorgtabar (2018) performs **16× upscaling** with saliency-weighted loss, maintaining segmentation accuracy comparable to original resolution while specifically enhancing small and blurred vessels.

**Ultrasound localization microscopy breaks diffraction limits**: Deep-ULM (2018) achieves super-resolution vascular imaging through precise microbubble localization via CNN, processing **70 high-resolution patches per second** on standard hardware. The method handles high microbubble densities where traditional sparse recovery fails, enabling visualization of microvascular structures at hundreds of microns scale.

## Deep learning architectures evolve toward hybrid transformer-CNN designs

Recent architectural innovations emphasize multi-scale feature fusion, attention mechanisms, and knowledge transfer, with performance consistently exceeding pure CNN or pure transformer approaches.

**TransUNext establishes new performance ceiling**: The 2024 hybrid Transformer-CNN architecture integrates Efficient Self-attention with ConvNeXt blocks throughout the entire model, not just embedding transformers into CNNs. The Global Multi-Scale Fusion (GMSF) module achieves semantic and spatial fusion across all scales through all-to-all attention, delivering superior performance on high-resolution fundus datasets (DRIVE, STARE, CHASE-DB1, HRF).

**Knowledge transfer enables LR-to-HR capability transfer**: The 2024 Multi-scale Knowledge Transfer Vision Transformer (KT-ViT) pioneered transferring fine-scale vessel distribution modeling from high-resolution networks to low-resolution networks through multi-level loss functions. This addresses the critical practical problem where HR MRI acquisition is difficult or impossible, enabling near-HR segmentation quality from commonly-available LR clinical images.

**ResU-Net variants dominate hepatic applications**: CerebralDoc (2020) applies optimized 3D-CNN with bottleneck-ResNet for head and neck vessels, achieving **DSC 0.944-0.951** across 18,766 CTA scans with clinical deployment reducing reconstruction time 3-fold (14.22 to 4.94 minutes). The Connected Growth Prediction Model ensures vessel continuity, critical for surgical planning applications.

## Classical methods establish enduring foundations

Six seminal papers from 1999-2017 established paradigms that continue to influence current research, with their core insights remaining relevant despite dramatic advances in deep learning.

**SRCNN pioneered end-to-end learning for SR** (Dong et al., 2015): The first deep CNN for single-image super-resolution demonstrated that traditional sparse-coding methods could be viewed as deep networks, but joint optimization delivers **0.5-1.5 dB PSNR improvements** over bicubic interpolation. This established the learning-based SR paradigm adopted by all subsequent methods.

**U-Net defined medical image segmentation architecture** (Ronneberger et al., 2015): The encoder-decoder with skip connections became the universal standard for vessel segmentation. Its ability to train from very few images through aggressive data augmentation, combined with multi-scale feature learning, makes it foundational for vascular applications. Virtually every modern vessel segmentation method builds on U-Net's architectural insights.

**SRGAN introduced perceptual quality optimization** (Ledig et al., 2017): The first GAN framework for photo-realistic 4× SR fundamentally shifted how super-resolution quality is measured and optimized. By combining adversarial loss with VGG feature-based content loss, SRGAN demonstrated that pushing solutions toward natural image manifolds produces perceptually superior results despite sometimes lower PSNR. This insight influenced all subsequent GAN-based medical imaging work.

**DRIVE dataset enabled standardized vessel evaluation** (Staal et al., 2004): The 40 retinal images (20 training, 20 test) from diabetic retinopathy screening became the gold standard benchmark for vessel segmentation algorithms for nearly two decades. The ridge-based segmentation method achieving **ROC AUC 0.95** established that feature-based approaches could match human expert performance.

**Interpolation survey established fundamental principles** (Lehmann et al., 1999): The comprehensive IEEE TMI evaluation of interpolation kernels demonstrated that **large kernels (N≥6) significantly outperform small kernels (N=2,3)** for preserving vessel details during resampling (p\u003c\u003c0.005). The recommended cubic 6×6 interpolator remains widely used, and the framework for evaluating interpolation methods continues to guide medical image processing decisions.

**Medical SR methods comparison revealed trade-offs** (2020): The systematic evaluation of SRCNN, VDSR, DRCN, and ESRGAN on OCT retinal images established that different SR approaches have different strengths—MSE-based methods achieve higher PSNR while perceptual loss methods produce qualitatively superior images for clinical visualization.

## Vesselness filtering remains the dominant enhancement approach

Despite super-resolution advances, traditional vesselness filters combined with interpolation represent the most commonly deployed vessel enhancement strategy across both hepatic and general vascular applications.

**Filter fusion outperforms individual filters**: Garret et al. (2024) demonstrate that concatenating multiple vesselness filters (Frangi, Jerman, Sato, Zhang, Meijering, RORPO) as multi-channel U-Net input significantly improves small vessel segmentation. Third-order B-spline interpolation to isotropic spacing (e.g., 0.65×0.65×1.5 to 0.65×0.65×0.65 mm³) proves essential for filter effectiveness, with novel evaluation including bifurcation-specific assessment and vessel size partitioning.

**Comprehensive filter comparison quantifies enhancement benefits**: Survarachakan et al. (2021) systematically evaluated Frangi, Hessian, Meijering, and Sato filters with gamma correction on 57 clinical hepatic CT volumes. The best individual filter achieved **Dice 0.800 versus 0.740 unenhanced**, with gamma correction adding ~2% improvement. Fused approaches reached **Dice 0.830**—statistically significant improvements (p\u003c0.05) demonstrating preprocessing value.

**Preprocessing integration with deep learning shows additive benefits**: Multiple papers confirm that vesselness enhancement combined with modern architectures outperforms either alone. CED filtering integration improves vessel contrast and intensity homogeneity, while multi-scale filtering at different scales (e.g., 4-8) captures vessels of varying diameters.

## Critical research gaps and future directions

**Hepatic vessels remain dramatically understudied for SR methods**: Only 1 of 30+ papers identified applies dedicated super-resolution to hepatic vessels, despite liver surgery planning requiring precise vascular mapping. The successful application of I2SR to pulmonary vessels and SR-DLR to coronary vessels suggests strong potential for adaptation.

**Generative models show zero direct hepatic application**: Despite remarkable advances in diffusion models and GANs for brain, retinal, and coronary vessels, no papers apply these techniques to liver imaging. Given diffusion models' superior topology preservation and connectivity scores, this represents a high-value research opportunity.

**Task08 dataset utilization lags potential**: With 443 annotated CT scans, Task08 offers substantial training data, yet only 2 papers leverage it. Most hepatic vessel research uses smaller datasets (20-57 volumes), limiting model generalization. Expanding Task08 usage with modern architectures and SR preprocessing could advance the field significantly.

**Anisotropic resolution remains fundamental challenge**: Nearly all papers identify through-plane resolution (typical CT: 0.7×0.7×4 mm³) as the primary limitation for small vessel detection. While self-supervised SR addresses this, supervised methods trained on paired HR/LR data could potentially achieve superior performance.

**Topology preservation metrics underutilized**: Only the SSR hepatic paper explicitly uses centerline Dice (clDice), yet vessel connectivity is critical for surgical planning. Standard Dice scores poorly capture vascular network integrity. Adopting connectivity scores (as in VasTSD) and clDice more broadly would better reflect clinical utility.

**Knowledge transfer and few-shot learning unexplored for hepatic vessels**: The KT-ViT approach transferring HR knowledge to LR networks shows promise but hasn't been applied to liver imaging. Given clinical CT acquisition variability, methods robust to resolution changes are essential.

## Conclusion

The landscape of vessel enhancement for segmentation spans from classical interpolation to cutting-edge diffusion models, yet hepatic vessels remain underserved by advanced super-resolution techniques. While vesselness filtering combined with deep learning delivers solid performance (Dice 0.79-0.83 on hepatic datasets), recent advances in other anatomical domains—pulmonary I2SR achieving 92% Dice, coronary SR-DLR improving stenosis grading, and diffusion models reaching 90-92% Dice with superior topology preservation—demonstrate significant untapped potential. The convergence of efficient diffusion models (4-step sampling), hybrid transformer-CNN architectures, and self-supervised learning paradigms positions the field for breakthrough advances in hepatic vessel segmentation. Researchers should prioritize adapting generative models to liver CT/MRI, expanding Task08 dataset utilization, and emphasizing topology-preserving metrics that align with surgical planning requirements.

---

## Papers by Category

### Hepatic Vessel-Specific (Task08 and Liver Datasets)

**1. Self Super Resolution for Hepatic Vessel CT Segmentation** (2024)  
Authors: Vincent Jaouen, Ziqiao Wang, Pierre-Henri Conze, Dimitris Visvikis  
Dataset: IRCADb (20 CT scans)  
Method: Self-supervised SR using EDSR and SMORE for through-plane resolution enhancement (anisotropic to isotropic)  
Vessel Upscaling: **YES** - 0.7×0.7×4 mm³ to 0.7×0.7×0.7 mm³  
Generative Models: **NO** - Discriminative EDSR  
Metrics: Dice 0.69, clDice 0.65 (vs baseline 0.68/0.62)  
Novelty: First self-SR application to hepatic vessels; topology-preserving clDice metric  
PDF: https://hal.science/hal-04470666/file/Self_Super_Resolution_for_Hepatic_Vessel_CT_segmentation.pdf

**2. Hepatic Vessels Segmentation Using Deep Learning and Preprocessing Enhancement** (2023)  
Authors: Osama I. Alirr, Ahmad A. A. Rahni  
Dataset: **Medical Segmentation Decathlon Task08** (443 CT scans - 303 training, 140 testing) + 3Dircadb-01  
Method: CED filtering + vesselness filtering preprocessing with modified U-Net (ResDense blocks)  
Vessel Upscaling: **YES** - Isotropic resampling to 1 mm³  
Generative Models: **NO**  
Metrics: Dice 79%, Sensitivity 82.2%, Specificity 95.1%  
Novelty: First comprehensive preprocessing (CED + vesselness) for Task08; novel ResDense architecture  
PDF: https://pmc.ncbi.nlm.nih.gov/articles/PMC10161019/

**3. Effects of Enhancement on Deep Learning Based Hepatic Vessel Segmentation** (2021)  
Authors: Shanmugapriya Survarachakan, Egidijus Pelanis, Zohaib Amjad Khan, Rahul Prasanna Kumar, Bjørn Edwin, Frank Lindseth  
Dataset: In-house clinical CT (57 volumes)  
Method: Comprehensive comparison of vesselness filters (Frangi, Hessian, Meijering, Sato) with gamma correction + 3D U-Net  
Vessel Upscaling: **YES** - Interpolation for isotropic spacing  
Generative Models: **NO**  
Metrics: Best Dice 0.830 (fused segmentation), individual filters 0.800 (vs 0.740 unenhanced)  
Novelty: First comprehensive vesselness filter comparison for hepatic vessels; statistical validation of enhancement  
PDF: https://www.mdpi.com/2079-9292/10/10/1165

**4. Deep Vessel Segmentation Based on a New Combination of Vesselness Filters** (2024)  
Authors: Guillaume Garret, Antoine Vacavant, Carole Frindel  
Dataset: 3Dircadb-01/IRCAD (20 CT scans, liver vessels) + Bullitt (33 MRA, brain vessels)  
Method: Filter fusion (Frangi, Jerman, Sato, Zhang, Meijering, RORPO) as multi-channel U-Net input  
Vessel Upscaling: **YES** - Third-order B-spline interpolation to isotropic resolution (e.g., 0.65×0.65×1.5 to 0.65×0.65×0.65 mm³)  
Generative Models: **NO**  
Metrics: Improved small vessel segmentation, novel bifurcation assessment  
Novelty: First comprehensive integration of 7 major vesselness filters; multi-scale evaluation methodology  
PDF: https://arxiv.org/abs/2402.14509

**5. Improving Vessel Segmentation with Multi-Task Learning and Auxiliary Data** (2025)  
Authors: Daniel Sobotka, Alexander Herold, Matthias Perkonigg, Lucian Beer, Nina Bastati, Alina Sablatnig, Ahmed Ba-Ssalamah, Georg Langs  
Dataset: Liver MRI (paired native and contrast-enhanced)  
Method: Multi-task Y-Net using contrast-enhanced MRI as auxiliary modality during training only  
Vessel Upscaling: **NO** - Focus on multi-modal learning  
Generative Models: **NO** - Multi-task discriminative learning  
Metrics: Improved Dice for vessel segmentation, benefits with limited annotations  
Novelty: Novel semi-supervised approach using privileged information (contrast-enhanced) available only during training  
PDF: https://arxiv.org/abs/2509.03975

---

### Generative Models for Vascular Enhancement

**6. VasTSD - 3D Vascular Tree-State Space Diffusion Model** (2025)  
Authors: Zhifeng Wang, Renjiao Yi, Xin Wen, Chenyang Zhu, Kai Xu  
Dataset: ITKTubeTK (20 CT brain), ISICDM 2020 (pulmonary), Topcow2024 (Circle of Willis) - Multiple MRI/CT modalities  
Method: Tree-state space diffusion model for angiography synthesis with dynamic spanning tree construction  
Vessel Upscaling: **NO** - Synthesis not upscaling  
Generative Models: **YES - Diffusion Model** (tree-state space)  
Metrics: PSNR 27.36-29.92, SSIM 0.9372-0.9562, Dice 0.90-0.92, Connectivity 9.59  
Novelty: First state space model for angiography synthesis; cross-slice attention for 3D structure  
PDF: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VasTSD_Learning_3D_Vascular_Tree-state_Space_Diffusion_Model_for_Angiography_CVPR_2025_paper.pdf

**7. MedSegDiff - Medical Image Segmentation with Diffusion Model** (2023)  
Authors: Junde Wu, Rao Fu, Huihui Fang, Yu Zhang, Yehui Yang, Haoyi Xiong, Huiying Liu, Yanwu Xu  
Dataset: DRIVE, CHASE-DB1, STARE (retinal vessels), BraTS (brain), REFUGE, multiple ultrasound/MRI  
Method: First DPM-based segmentation with Dynamic Conditional Encoding and Feature Frequency Parser  
Vessel Upscaling: **NO** - Segmentation focus  
Generative Models: **YES - Diffusion Probabilistic Model**  
Metrics: Dice 0.9727 (liver), outperforms SOTA on vessel segmentation  
Novelty: First diffusion model for medical segmentation; FF-Parser eliminates high-frequency noise  
PDF: https://arxiv.org/pdf/2211.00611

**8. Res-SRDiff - Efficient MRI Super-Resolution with Residual Shifting** (2024)  
Authors: Mojtaba Safari, Xiaofeng Yang, Chih-Wei Chang, Richard L J Qiu, Ali Fatemi, Louis Archambault  
Dataset: 7T brain T1 maps (142 patients, 14,566 training slices), Prostate T2w MRI (334 patients, PROSTATEx)  
Method: Efficient diffusion with residual error shifting (4 steps vs 1000+), U-net with Swin Transformer  
Vessel Upscaling: **YES** - 4× SR in each direction (16× volume), preserves vascular structures  
Generative Models: **YES - Diffusion Model** (efficient variant)  
Metrics: Brain PSNR 27.37±2.02, SSIM 0.80±0.06; Prostate PSNR 27.72±2.26, SSIM 0.81±0.05; \u003c1 sec/slice  
Novelty: First 4-step diffusion for medical SR; Swin Transformer integration; 20-66× faster than traditional  
PDF: https://pmc.ncbi.nlm.nih.gov/articles/PMC11908366/

**9. CAS-GAN - Contrast-free Angiography Synthesis** (2024)  
Authors: Multiple authors  
Dataset: XCAD (X-ray angiography), coronary vessels  
Method: GAN with disentanglement representation learning and vessel semantic guidance as "virtual contrast agent"  
Vessel Upscaling: **NO** - Enhancement not upscaling  
Generative Models: **YES - GAN** (with disentanglement and semantic guidance)  
Metrics: FID improvements 0.11-1.89, statistically significant (p\u003c0.05)  
Novelty: First contrast-free X-ray angiography synthesis; novel vessel semantic guidance in generator and loss  
PDF: https://arxiv.org/pdf/2410.08490

**10. RV-GAN - Retinal Vessel Segmentation** (2021)  
Authors: Sharif Amit Kamran, Khondker Fariha Hossain, Alireza Tavakkoli, Stewart Lee Zuckerbrod  
Dataset: DRIVE, CHASE-DB1, STARE (retinal vessels)  
Method: Multi-scale GAN with dual generators and dual autoencoding discriminators, weighted feature matching loss  
Vessel Upscaling: **YES (Indirectly)** - Better microvessel extraction  
Generative Models: **YES - GAN** (multi-scale dual generator/discriminator)  
Metrics: AUC 0.9887 (DRIVE), 0.9914 (CHASE-DB1), 0.9887 (STARE)  
Novelty: First multi-scale dual-GAN for vessels; weighted feature matching prioritizes decoder features  
PDF: https://arxiv.org/pdf/2101.00535

**11. Conditional Normalizing Flows for Low-Dose CT Reconstruction** (2020)  
Authors: Alexander Denker, Maximilian Schmidt, Johannes Leuschner, Peter Maass  
Dataset: AAPM-Mayo Clinic Low-Dose CT Challenge (abdominal CT)  
Method: Hybrid conditional normalizing flow with FBP conditioning for physics-integrated reconstruction  
Vessel Upscaling: **YES (Indirectly)** - Improves vessel visibility by noise reduction  
Generative Models: **YES - Normalizing Flow** (conditional, hybrid)  
Metrics: Superior SSIM, stable training vs GANs, uncertainty quantification  
Novelty: First conditional normalizing flow for CT reconstruction; physics-based conditioning; explicit likelihood  
PDF: https://arxiv.org/pdf/2006.06270

---

### General Vascular Super-Resolution (Non-Hepatic)

**12. HiPaS - Deep Learning for Pulmonary Artery and Vein Segmentation** (2025)  
Authors: Yuetan Chu, Gongning Luo, Longxi Zhou, Juexiao Zhou, et al.  
Dataset: 1,073 CT volumes (315 CTPA + 758 non-contrast CT), 17,817 public chest CT  
Method: Inter-and-Intra-slice Super Resolution (I2SR) module for spatial normalization followed by Saliency-Transmission Segmentation  
Vessel Upscaling: **YES** - I2SR resamples to 0.65×0.65×1.00 mm³, addresses LRCT (≥1.25mm thickness)  
Generative Models: **NO** - CNN with masked autoencoder pretraining  
Metrics: Normal-res DSC 92.25%/89.09% (artery/vein), LR-CT DSC 89.51%/88.34%, Sensitivity 97-98%, AUC 99.82-99.93%  
Novelty: First accurate artery-vein segmentation on non-contrast CT; I2SR handles inter/intra-slice resolution  
PDF: https://www.nature.com/articles/s41467-025-56505-6.pdf

**13. CerebralDoc - Rapid Vessel Segmentation of Head and Neck Angiograms** (2020)  
Authors: Fei Fu, Jianxun Wei, Mingxuan Zhang, Feiyu Yu, et al.  
Dataset: 18,766 head and neck CTA scans (5 tertiary hospitals)  
Method: Optimized 3D-CNN (ResU-Net) with bottleneck-ResNet for bone and vessel segmentation, Connected Growth Prediction Model  
Vessel Upscaling: **NO** - Architecture improves feature extraction  
Generative Models: **NO**  
Metrics: Vessel DSC 0.944-0.951, clinical qualification 92.1%, 3× time reduction (14.22 to 4.94 min)  
Novelty: First comprehensive automatic head-neck CTA reconstruction; CGPM ensures vessel continuity; clinical deployment  
PDF: https://www.nature.com/articles/s41467-020-18606-2.pdf

**14. SuperVessel - High-Resolution Retinal Vessel Segmentation** (2022)  
Authors: Yan Hu, Zhongxi Qiu, Dan Zeng, Li Jiang, Chen Lin, Jiang Liu  
Dataset: DRIVE, STARE, CHASE-DB1 (retinal vessels)  
Method: SR auxiliary branch with Upsampling with Feature Decomposition (UFD) and Feature Interaction Module (FIM)  
Vessel Upscaling: **YES** - Explicit SR auxiliary branch for HR detail features from LR input  
Generative Models: **NO** - U-Net with feature decomposition  
Metrics: Improved tiny vessel detection and continuity vs non-SR methods  
Novelty: First explicit SR+segmentation combination for retinal vessels; UFD module; SR branch removable in inference  
PDF: https://arxiv.org/pdf/2207.13882

**15. GAN-Based Retinal Vasculature Segmentation with Super-Resolution** (2018)  
Authors: Dwarikanath Mahapatra, Behzad Bozorgtabar  
Dataset: DRIVE, STARE (fundus images)  
Method: GAN-based super-resolution (up to 16× scaling) with local saliency maps defining novel saliency loss  
Vessel Upscaling: **YES** - Explicit 16× super-resolution targeting small/blurred vessels  
Generative Models: **YES - GAN** (with saliency loss)  
Metrics: SR images maintain segmentation accuracy comparable to original resolution  
Novelty: First GAN-based SR with saliency-weighted loss for retinal vessels; 16× upscaling preserves segmentation accuracy  
PDF: https://arxiv.org/pdf/1710.04783

**16. Super-Resolution Deep Learning Reconstruction for Coronary CT Angiography** (2023)  
Authors: Yasunori Nagayama, Takafumi Emoto, Yuki Kato, Masafumi Kidoh, et al.  
Dataset: 58 patients, 320-row coronary CT angiography  
Method: SR-DLR trained on ultra-high-resolution CT data using deep CNNs with model-based iterative reconstruction  
Vessel Upscaling: **YES** - Vessel sharpness +21% (560 vs 463 HU/mm), stent struts thinner (0.72 vs 1.01mm)  
Generative Models: **NO** - Deep CNN reconstruction  
Metrics: Noise -31% (12.6 vs 18.2 HU), stenosis grading κ=0.83 (vs 0.77 standard), improved SNR/CNR  
Novelty: First SR-DLR trained on UHR-CT for coronary imaging; UHR-quality from standard scans without special equipment  
PDF: https://pmc.ncbi.nlm.nih.gov/articles/PMC10485715/pdf/ryct.230085.pdf

**17. Accurate Super-Resolution Low-Field Brain MRI** (2022)  
Authors: Juan Eugenio Iglesias et al. (10 authors)  
Dataset: Paired low-field (0.064T) and high-field (1.5-3T) MRI, 61 cerebral small vessel disease patients  
Method: ML super-resolution synthesizing 1mm isotropic MPRAGE-like scans from low-field T1/T2 with deep attention  
Vessel Upscaling: **YES** - Low-field to high-resolution synthesis, improves cerebrovascular structure characterization  
Generative Models: **UNCLEAR** - Deep learning with attention, not explicitly stated  
Metrics: SSIM 0.9852, mean intensity ratio differences 0.0010-0.0784, fewer false positives than interpolation  
Novelty: First comprehensive SR for portable low-field MRI; clinical validation on small vessel disease; deep attention  
PDF: https://arxiv.org/pdf/2202.03564

**18. Deep Learning for Super-Resolution Vascular Ultrasound Imaging** (2018)  
Authors: Ruud J.G. van Sloun, Oren Solomon, Matthew Bruce, Zin Z Khaing, Yonina C. Eldar, Massimo Mischi  
Dataset: In-silico and in-vivo vascular ultrasound with microbubbles  
Method: Deep-ULM CNN for precise microbubble localization achieving super-resolution ultrasound localization microscopy  
Vessel Upscaling: **YES** - Breaks diffraction limit, visualizes microvascular structures at hundreds of microns scale  
Generative Models: **NO** - CNN for localization  
Metrics: Superior detection rate and precision vs centroid/sparse methods, 70-1250 patches/sec, handles high densities  
Novelty: First deep learning for ultrasound localization microscopy; real-time super-resolution vascular imaging  
PDF: https://arxiv.org/pdf/1804.07661

**19. Deep Attention Super-Resolution of Brain MRI** (2022)  
Authors: Multiple authors  
Dataset: 61 patients with sporadic cerebral small vessel disease, T1/T2/FLAIR MRI  
Method: Deep attention framework for multi-sequence (T1/T2/FLAIR) super-resolution with Gaussian clustering for vessel segmentation  
Vessel Upscaling: **YES** - Clinical MRI to HR for cerebrovascular structures (veins, sinuses, CSF)  
Generative Models: **UNCLEAR** - Deep attention, not explicitly GAN/diffusion  
Metrics: SSIM 0.9852, mean intensity differences 0.0010-0.0784, fewer false positives than interpolation  
Novelty: First deep attention SR for clinical MRI protocols; multi-sequence simultaneous processing; validated on small vessel disease  
PDF: https://www.frontiersin.org/articles/10.3389/fncom.2022.887633/pdf

---

### Recent Deep Learning Architectures (2020-2024)

**20. Deep-Learning-Based Image Quality Enhancement of Compressed Sensing MRI** (2020)  
Authors: Di Eun, Renjie Jang, Won-Seok Ha, Young Seung Kim, et al.  
Dataset: Intracranial vessel wall MRI (14 volunteers, 3T Philips), HRPD imaging with CS acceleration 5.8×  
Method: Self-supervised U-Net (Gaussian noise training) vs unsupervised CycleGAN for CS MRI denoising/enhancement  
Vessel Upscaling: **YES (Indirectly)** - Enhances resolution and reduces noise in CS MRI for vessel wall imaging (0.51×0.51×0.45 mm³)  
Generative Models: **YES - CycleGAN** (unsupervised approach)  
Metrics: Significantly improved SNR and decreased noise (P\u003c0.05), BRISQUE ~26 to ~20, improved radiomics reproducibility  
Novelty: First comparison of self-supervised vs unsupervised DL for medical enhancement without paired data  
PDF: https://www.nature.com/articles/s41598-020-69932-w

**21. TransUNext - Advanced U-Shaped Framework for Vessel Segmentation** (2024)  
Authors: Xiang Li, Mingsi Liu, Lixin Duan  
Dataset: DRIVE, STARE, CHASE-DB1, HRF (high-resolution fundus images)  
Method: Hybrid Transformer-CNN with Efficient Self-attention and Global Multi-Scale Fusion (GMSF) module  
Vessel Upscaling: **YES** - Multi-scale fusion preserves fine vessel details and large vessel structures at multiple resolutions  
Generative Models: **NO** - Hybrid CNN-Transformer  
Metrics: Superior AUC, specificity, sensitivity across all datasets; excellent high-resolution performance  
Novelty: First fully hybrid Transformer-ConvNeXt throughout model; GMSF all-to-all attention across scales  
PDF: https://arxiv.org/pdf/2411.02724

**22. Double U-Net for Super-Resolution and Segmentation** (2022)  
Authors: Mayur Bhandary, Jesús Pineda, Ashraf Hadid, Asser Vartiainen  
Dataset: Live cell microscopy images (low-resolution cellular)  
Method: Cascaded two-stage: First U-Net for super-resolution, second U-Net for segmentation on enhanced images  
Vessel Upscaling: **YES** - Explicit SR stage upsamples before segmentation  
Generative Models: **NO** - Cascaded U-Net  
Metrics: SR preprocessing improves segmentation accuracy vs direct LR segmentation  
Novelty: First explicit SR preprocessing for medical segmentation in resource-constrained scenarios; establishes SR+segmentation paradigm  
PDF: https://arxiv.org/pdf/2212.02028

**23. Multi-Scale Knowledge Transfer Vision Transformer** (2024)  
Authors: Multiple authors  
Dataset: 3D vessel datasets from MRI (brain and scalp blood vessels for neurosurgical planning)  
Method: KT-ViT combining convolutional embeddings with transformer; knowledge transfer from HR to LR models at multiple levels  
Vessel Upscaling: **YES (Explicitly)** - Enables LR images to achieve near-HR vessel segmentation through knowledge transfer  
Generative Models: **NO** - Vision Transformer with knowledge distillation  
Metrics: Outperforms SOTA on public datasets, superior fine-scale vessel segmentation from LR images  
Novelty: First resolution inter-dependency exploration via knowledge transfer; transfers fine-scale vessel distribution modeling HR→LR  
PDF: Subscription required (https://www.sciencedirect.com/science/article/abs/pii/S0097849324001110) - Represents important SOTA work

---

### Foundational & Seminal Methods

**24. SRCNN - Image Super-Resolution Using Deep Convolutional Networks** (2015)  
Authors: Chao Dong, Chen Change Loy, Kaiming He, Xiaoyu Tang  
Dataset: 91 images + 200 Berkeley Segmentation; tested on Set5, Set14, BSD100  
Method: First end-to-end deep learning method for single image SR using 3-layer CNN learning LR-HR mapping  
Vessel Upscaling: **NO** - General SR, adapted to medical imaging subsequently  
Generative Models: **NO** - Supervised CNN with MSE loss  
Metrics: PSNR +0.5-1.5 dB over bicubic, \u003c1 sec inference  
Novelty: Pioneered deep learning for image SR; established learning-based SR paradigm  
PDF: https://arxiv.org/pdf/1501.00092.pdf

**25. U-Net - Convolutional Networks for Biomedical Image Segmentation** (2015)  
Authors: Olaf Ronneberger, Philipp Fischer, Thomas Brox  
Dataset: ISBI neuronal structures (EM stacks), ISBI cell tracking 2015  
Method: U-shaped encoder-decoder with skip connections for precise localization, strong data augmentation  
Vessel Upscaling: **YES** - Enables precise segmentation of thin vessel-like structures through multi-scale learning  
Generative Models: **NO** - Supervised segmentation  
Metrics: Won ISBI 2015, \u003c1 sec for 512×512 on GPU  
Novelty: Established U-Net architecture as universal standard for medical segmentation; skip connections preserve spatial info  
PDF: https://arxiv.org/pdf/1505.04597.pdf

**26. SRGAN - Photo-Realistic Single Image Super-Resolution** (2017)  
Authors: Christian Ledig, Lucas Theis, Ferenc Huszár, Jose Caballero, et al.  
Dataset: Set5, Set14, BSD100; trained on ImageNet  
Method: First GAN framework for photo-realistic 4× SR using perceptual loss (adversarial + VGG content loss)  
Vessel Upscaling: **NO** - General natural image SR, adapted to medical imaging  
Generative Models: **YES - GAN** (generator + discriminator)  
Metrics: Superior MOS perceptual quality, PSNR 23-24 dB  
Novelty: First photo-realistic SR using GANs; introduced perceptual loss fundamentally changing SR optimization  
PDF: https://arxiv.org/pdf/1609.04802.pdf

**27. Ridge-Based Vessel Segmentation in Color Images of the Retina (DRIVE Dataset)** (2004)  
Authors: Joes Staal, Michael D. Abràmoff, Meindert Niemeijer, Max A. Viergever, Bram van Ginneken  
Dataset: **DRIVE** (40 color fundus images - 20 training, 20 test), 584×565 pixels  
Method: Ridge-based vessel centerline extraction with kNN classification using ridge and local structure features  
Vessel Upscaling: **NO** - Segmentation at native resolution  
Generative Models: **NO** - Classical ML (kNN)  
Metrics: ROC AUC 0.95, comparable to human observers  
Novelty: Introduced DRIVE dataset as gold standard benchmark for 2 decades; established ridge-based feature extraction  
PDF: https://www.researchgate.net/publication/8619377_Ridge-Based_Vessel_Segmentation_in_Color_Images_of_the_Retina

**28. Medical Image Enhancement Using Super Resolution Methods** (2020)  
Authors: Multiple authors  
Dataset: OCT images of optic nerve head (Fukushima Medical University)  
Method: Comprehensive evaluation of SRCNN, VDSR, DRCN, ESRGAN for OCT retinal image enhancement  
Vessel Upscaling: **YES** - Enhances blood vessel visibility in retinal OCT from single scans to multi-frame quality  
Generative Models: **YES (ESRGAN)** - GAN with perceptual loss; others are CNNs with MSE  
Metrics: High PSNR for SRCNN/VDSR/DRCN; ESRGAN best qualitative despite lower PSNR  
Novelty: First systematic SR architecture comparison for medical OCT; demonstrated PSNR vs perceptual quality trade-off  
PDF: https://pmc.ncbi.nlm.nih.gov/articles/PMC7302556/

**29. Survey: Interpolation Methods in Medical Image Processing** (1999)  
Authors: T.M. Lehmann, C. Gönner, K. Spitzer  
Dataset: 50 direct digital X-rays from clinical routine  
Method: Comprehensive comparison of interpolation kernels (sinc, nearest neighbor, linear, B-spline, cubic, Lagrange, Gaussian); kernel sizes 1×1 to 8×8  
Vessel Upscaling: **YES** - Interpolation fundamental for vessel visualization during resampling  
Generative Models: **NO** - Classical signal processing  
Metrics: Large kernels (N≥6) significantly outperform small (N=2,3) for vessel details (p\u003c\u003c0.005); cubic 6×6 recommended  
Novelty: Established comprehensive framework for medical image interpolation; standardized evaluation methodology  
PDF: https://www.cs.tau.ac.il/~turkel/imagepapers/interpolation-medical.PDF

---

## Performance Metrics Summary Table

| Paper | Year | Dataset/Region | Dice/DSC | Other Metrics | Enhancement Type |
|-------|------|----------------|----------|---------------|------------------|
| Self SR Hepatic | 2024 | IRCADb (liver) | 0.69 | clDice 0.65 | SR (EDSR) |
| Hepatic Vessels (Task08) | 2023 | Task08 (liver) | 0.79 | Sens 82.2%, Spec 95.1% | Vesselness + CED |
| Effects of Enhancement | 2021 | Hepatic (57 CT) | 0.83 | Fused segmentation | Vesselness filters |
| VasTSD | 2025 | Brain/lung | 0.90-0.92 | SSIM 0.94-0.96, Connect 9.59 | Diffusion model |
| MedSegDiff | 2023 | Multi-organ | 0.9727 (liver) | - | Diffusion model |
| Res-SRDiff | 2024 | Brain/prostate | - | PSNR 27.4, SSIM 0.80-0.81 | Diffusion SR (4-step) |
| HiPaS (Pulmonary) | 2025 | Pulmonary | 0.92/0.89 | Sens 97-98%, AUC 99.9% | I2SR |
| CerebralDoc | 2020 | Head/neck | 0.94-0.95 | Clinical qual 92.1% | 3D-CNN |
| SR-DLR Coronary | 2023 | Coronary | - | Sharpness +21%, Noise -31% | SR-DLR |
| Low-Field Brain | 2022 | Brain vessels | - | SSIM 0.9852 | Deep attention SR |
| RV-GAN | 2021 | Retinal | - | AUC 0.99 | Multi-scale GAN |
| DRIVE Ridge-based | 2004 | Retinal | - | AUC 0.95 | Classical (kNN) |

---

## Methodology Distribution

**Enhancement Approaches:**
- Vesselness filtering: 6 papers (most common for hepatic vessels)
- Deep learning SR: 8 papers (growing rapidly)
- Diffusion models: 3 papers (newest, best topology preservation)
- GANs: 4 papers (perceptual quality focus)
- Classical interpolation: 2 papers (foundational)
- Normalizing flows: 1 paper (underexplored)

**Architectural Patterns:**
- U-Net variants: 15 papers (dominant backbone)
- Transformer-CNN hybrids: 3 papers (emerging SOTA)
- ResNet-based: 5 papers
- Attention mechanisms: 6 papers

**Dataset Usage:**
- Task08 (hepatic): 2 papers only
- DRIVE/STARE (retinal): 8 papers (most common benchmark)
- Custom clinical datasets: 12 papers
- Multi-organ public datasets: 7 papers