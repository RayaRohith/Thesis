
# Quantifying the Effectiveness of Targeted Website Fingerprinting on Tor Browser

## Overview

This repository contains the implementation, datasets, feature extraction pipeline, and machine learning experiments developed for my MSc Cyber Security, Privacy and Trust dissertation at the University of Edinburgh.

The research investigates whether encrypted Tor Browser traffic can reveal not only the website being visited (traditional Website Fingerprinting), but also browser configuration characteristics such as JavaScript settings, cache behaviour, screen resolution, user-agent configuration, and browser version.

The project evaluates the feasibility of targeted website fingerprinting attacks across multiple Tor Browser versions using statistical traffic analysis and supervised machine learning techniques.

---

## Research Objectives

The dissertation addresses the following research questions:

### RQ1

Can Tor Browser client configurations be reliably classified using encrypted network traffic metadata?

### RQ2

Which traffic feature families contribute most strongly to configuration fingerprinting?

### RQ3

How robust are targeted fingerprinting models across Tor Browser version updates?

### RQ4

What are the broader implications of targeted fingerprinting for Tor user anonymity?

---

## Key Contributions

* Development of a customised Tor Browser traffic collection framework
* Extension of the tor-browser-selenium crawler for targeted fingerprinting experiments
* Collection of datasets across multiple Tor Browser versions (12.5, 13, and 14.5)
* Feature engineering pipeline for packet volume, timing, size, and burst characteristics
* Comparative evaluation of Random Forest and Linear SVM classifiers
* Cross-version analysis of fingerprinting robustness
* Feature importance and ablation studies to identify information leakage sources

---

## Methodology

### Data Collection

Traffic traces were collected using:

* Tor Browser
* Selenium automation
* dumpcap
* tshark
* Kali Linux

Two experimental settings were evaluated:

#### Non-Targeted Website Fingerprinting

* Fixed browser configuration
* 10 monitored websites
* 100 visits per website
* Goal: classify visited websites

#### Targeted Configuration Fingerprinting

* Fixed website set
* Multiple browser configurations
* Goal: classify client-side browser settings

Parameters tested:

| Parameter         | Values             |
| ----------------- | ------------------ |
| JavaScript        | Enabled / Disabled |
| Cache             | Enabled / Disabled |
| Screen Resolution | 800×600, 1200×800  |
| User Agent        | Default / Modified |
| Cookies           | Enabled / Disabled |
| Browser Version   | 12.5, 13, 14.5     |

---

## Feature Extraction

The following traffic feature families were extracted from PCAP traces:

### Volume Features

* Total packets
* Total bytes
* Upload/download ratios
* Session duration

### Timing Features

* Inter-arrival times
* Timing percentiles
* Directional timing statistics

### Size Features

* Packet size distributions
* TLS/Tor cell statistics

### Burst Features

* Burst counts
* Burst lengths
* Burst byte distributions

---

## Machine Learning Models

The following classifiers were evaluated:

### Random Forest

Used as the primary model due to:

* Strong performance on heterogeneous traffic features
* Robustness to noise
* Feature importance analysis

### Linear Support Vector Machine (SVM)

Used as a baseline classifier for comparison.

Evaluation metrics:

* Accuracy
* Macro F1 Score
* AUROC
* 5-Fold Stratified Cross Validation

---

## Results

### Baseline Website Fingerprinting

| Model         | Accuracy | Macro F1 |
| ------------- | -------- | -------- |
| Random Forest | 81%      | 0.79     |
| Linear SVM    | 76%      | 0.72     |

### Targeted Configuration Fingerprinting

Targeted fingerprinting achieved classification accuracies of up to **88%** in stable Tor Browser versions.

Key findings:

* Packet volume and timing features were the strongest indicators.
* Browser configuration settings leave measurable signatures in encrypted traffic.
* Tor Browser updates significantly reduced classifier effectiveness.
* Version changes can act as a practical defensive mechanism against fingerprinting attacks.

---

## Repository Structure

```text
├── data/
│   ├── raw_pcaps/
│   ├── processed_features/
│   └── metadata/
│
├── crawler/
│   ├── targeted_mode/
│   └── non_targeted_mode/
│
├── feature_extraction/
│
├── machine_learning/
│   ├── random_forest/
│   └── svm/
│
├── results/
│   ├── figures/
│   ├── confusion_matrices/
│   └── feature_importance/
│
└── dissertation/
```

---

## Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Selenium
* Tor Browser
* Wireshark
* tshark
* dumpcap
* Kali Linux

---

## Academic Context

This work was completed as part of the MSc Cyber Security, Privacy and Trust programme at the University of Edinburgh.

Dissertation Title:

**Quantifying the Effectiveness of Targeted Website Fingerprinting on Tor Browser**

---

## Future Work

Potential extensions include:

* Deep learning approaches (CNNs, Transformers)
* Real-world browsing environments
* Additional Tor configuration parameters
* TLS fingerprint analysis
* Adaptive fingerprinting defences
* Large-scale distributed data collection

---

## Author

Raya Rohith Yadav

MSc Cyber Security, Privacy and Trust
University of Edinburgh

LinkedIn: [Add Link]
Portfolio: [Add Link]

---

## Disclaimer

This repository was developed solely for academic research and educational purposes. The work is intended to improve understanding of traffic analysis risks and support future privacy-enhancing technologies.
