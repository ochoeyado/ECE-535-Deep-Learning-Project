# ECE-535-Deep-Learning-Project
ECE 535 Deep Learning in Mobile Tracking Systems


## Motivation
Our motivation for this project comes from our excitement about the world of machine learning, which is a completely new field for both of us. This new field opnes up significant opportunities for learning and growth.

After studying the project and the research paper attached to it, we have gained a clear understanding of the path this research should take. The concept of Tartan VO and its wide-ranging applications has captured our interest and curiosity. We are also eager to explore this field because it has very strong potential to contribute to various domains. We believe that by embarking on this journey, we will not only enjoy the process but also expand our knowledge and skills in machine learning, while exploring the possibilities of Tartan VO and its applications.

## Design Goals
1. Accurate Tracking
2. Efficient Processing
3. Robust (can handle noise)
4. Security and Privacy


## Deliverables
1. Implement and understand an end-to-end learning approach for tracking – TartanVO
2. Benchmark TartanVO on two datasets to evaluate its performance (data & code provided) 
3. Analyze performance difference across datasets and reason about it

## System Blocks
Data Input
Data Preprocessing
Data to Feature
Pose Estimation
Mapping
Data Combination
Output
Testing
Documentation


## Hardware and Software Requirements
Python, Laptop with CUDA-enabled GPU


## Team Members and Responsibilities
- **Colin Leydon:** 
  - Software Setup, Research, Data Ananlysis, Writing

- **Ocho Eyado:** 
  - Project Planning, Hardware Setup, Data Analysis, Writing


## Project Timeline
- Month 1: Project Initiation and Planning
- Month 2: Model Development and Optimization
- Month 3: Validation, Integration, and Deployment

## Challenges
While working on the Tartan we ran into a few problems that required unique solutions. 

One of the major issues we ran into was the outdated code as most of Tartan seemed to be developed in 2017. TartanVO was written in Python 2, a legacy version of Python. This posed an issue as most libraries no longer support Python 2 and have moved on to the much more common Python 3 which is installed on our machines. This error was realized when attempting to run the provided scripts resulting in numerous syntax errors. Although offering a Python 3 version these issues still seemed to persist especially since there were many issues with the libraries. Since the writing of the provided files, many of the included libraries have since been updated leaving many of the functions outdated and needing updating. This primarily rose with CuPy, although still being updated it seems that the community is pushing towards Nvidia Container Toolkit to utilize the Cuda capabilities of certain General Processing Units.

Before receiving the archived files, we attempted to run Tartan on an Ubuntu machine. Fortunately, using a series of pip and sudo apt install commands we were capable of installing the necessary dependencies and libraries. The problems arose when we were trying to get the KiTTi and EuRoc tests. As the GitHub called for, we used the wget command which resulted in the error: "Externally-Managed-Environment". We attempted multiple workarounds such as pipx but this command is meant for downloading commands for your script rather than dependencies. There was also an option to modify the command and force an install, but our research showed that unless you know exactly what this file is it could be catastrophic for your operating system and require a complete wipe

Once we received these archived files there were still some changes that needed to be made. For instance, in the code, there was a command as_dcm which has since been updated to as_matrix. There were a few other minor issues such as this, but the code was mostly up to date. We did however run into an error with shape() which required us to implement error messages to figure out where the error was occurring. Utilizing these messages we figured the error occurred based on the sizes of our text files. Since we have to run our datasets against the ground truth, the datasets have to have the same dimensions. Luckily, all these files had the same number of columns, so we just needed to edit the number of rows to the same ground truth (734 lines).

## Results


## References
Github Link - [https://github.com/castacks/tartanvo](url)
TartanVO: A Generalizable Learning-based VO, [https://arxiv.org/pdf/2011.00359.pdf](url)
Datasets:
1. EuRoC: [https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets](url)
2. KITTI: [https://www.cvlibs.net/datasets/kitti/eval_odometry.php](url)
3. HoloSet:[ https://tinyurl.com/holoset-dataset](url)

