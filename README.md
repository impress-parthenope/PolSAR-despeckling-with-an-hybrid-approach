# Training Dataset for PolSAR Despeckling with an Hybrid Approach

This repository contains a training dataset built following the hybrid approach presented in the [Training supervised neural networks for PolSAR despeckling with an hybrid approach, IEEE GRSL](https://ieeexplore.ieee.org/document/10319732) paper.

For accessing the dataset, refer to *release* section.

if you use this dataset or find it useful for further research, please cite the paper as the following: 

```
@ARTICLE{10319732,
  author={Lu, Xialei and Vitale, Sergio and Aghababei, Hossein and Ferraioli, Giampaolo and Pascazio, Vito},
  journal={IEEE Geoscience and Remote Sensing Letters}, 
  title={Training Supervised Neural Networks for PolSAR Despeckling With an Hybrid Approach}, 
  year={2024},
  volume={21},
  number={},
  pages={1-5},
  doi={10.1109/LGRS.2023.3333671}}
```
and insert the following acknowledgement:
```
UAVSAR data courtesy NASA/JPL-Caltech
```


In this paper study on the effect of different training approaches for PolSAR despeckling is provided.
Inspired by similar analysis on SAR amplitude case in [Hybrid-MONet](https://ieeexplore.ieee.org/document/9474572) and [G-MOnet](https://ieeexplore.ieee.org/document/10250969)
a multi-temporal and training approach for training a CNN for PolAR despeckling is provided. The dataset has been tested on [MONet](https://ieeexplore.ieee.org/document/9261137) customized for the PolSAR case.

# Team members
 Xialei Lu (xialei.lu001@studenti.uniparthenope.it);
 Sergio Vitale (contact person, sergio.vitale@uniparthenope.it);
 Hossein Aghababei (h.aghababaei@utwente.nl)
 Giampaolo Ferraioli (giampaolo.ferraioli@uniparthenope.it);
 Vito Pascazio (vito.pascazio@uniparthenope.it);
 
# License
Copyright (c) 2023 Dipartimento di Ingegneria and Dipartimento di Scienze e Tecnologie of Università degli Studi di Napoli "Parthenope".

All rights reserved. This work should only be used for nonprofit purposes.

By downloading and/or using any of these files, you implicitly agree to all the
terms of the license, as specified in the document LICENSE.txt
(included in this directory)

# Dataset Description
The dataset has been built by 27 fully polarimetric UAVSAR images over Sacramento-San Joaquin Delta, CA.
The dataset contains 37260 noisy covariance matrices (64 x 64 patches) and correspondent noise-free covariance matrices.

The noise-free covariance matrices have been estimated by temporal multi-looking the 27 covariance matrices obtained from the UAVSAR dataset.
The noisy covariance matrices have been created follwoing the hybrid approach described in the paper.

The released dataset is in the form ready-to-train as described in the paper.
More precisely, considering the simmetry of covariance matrix, only the upper triangle has been considered.
Each element of dataset is a multi-channel patch of dimension 9x64x64:
- three channels for intensity components
- three channels for real part of off-diagonal elements (upper triangle)
- three channels imaginary part of off-diagonal elements (upper triangle)

If you want to proceed to data augmentation as suggested in the paper, you need to perform a 180° rotation.
- data2cov.py is provided for converting the flattended covariance matrix (9x64x64) in a covariance matrix of dimension (3x3x64x64) if necessary 


