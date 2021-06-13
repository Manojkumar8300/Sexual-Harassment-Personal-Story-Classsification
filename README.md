# Sexual-Harassment-Personal-Story-Classsification

## Problem Statement:
Given a Personal story, have to analyze and categorize various forms of Sexual Harassment.

## Data Overview:
In recent ages , an increasing number of Personal Stories about Sexual Harassement and sexual abuse have been shared online. It is tedious to categorize the various forms of sexual harassement based on the stories, because large manual power will be required. But with the help of Machine learning it is quite easy and faster actions can be taken.This data is provided by an Online Forum SafeCity. So here the main task is to classify the various forms of sexual harassement based on the stories.There are various forms of sexual harassement but in this dataset only top three categorizes such as Commenting, Ogling/Facial Expressions/Staring and Touching/Groping are considered.

## Multi-Label Classification:

The data for multi-label classification is given in four columns, with the first column being the description of the incident and the second, third, and fourth column being 1 if the category of sexual harassment is present and 0 if it is not.There are 7201 training samples, 990 development samples, and 1701 test samples.

## Example for Multi-Label Classification Dataset:
Description | Commenting | Ogling | Groping
----------|---------------|----------|---------------
Was walking along crowded street, holding mums hand, when an elderly man groped butt, I turned to look at h7m and he looked away, and did it again after a while.I was 12 yrs old then. |	0 |	0 |	1
This incident took place in the evening.I was in the metro when two guys started staring. | 0 | 1 | 0
Catcalls and passing comments were two of the ghastly things the Delhi police at the International Airport put me and my friend through. It is appalling that the protectors and law enforcers at the airport can make someone so uncomfortable. | 1 | 1 | 0



**-Number of Examples in Multi-Label Classification:**

Commenting | Ogling | Groping | Examples in Dataset
----------|---------------|----------|---------------
1 | 1 | 1 | 351
1 | 1 | 0 | 819
1 | 0 | 1 | 459
0 | 1 | 1 | 201
1 | 0 | 0 | 2256
0 | 0 | 1 | 1966
0 | 1 | 0 | 743
0 | 0 | 0 | 3097
## Business Objective and Constraints:
There is not much requirement for faster results similar to Search Engine(Eg:Google) but little lower than that like within few mins.

## This CaseStudy is based on ResearchPaper: https://arxiv.org/pdf/1809.04739.pdf




To create Webapp just run the command streamlit run selfcasestudy_streamlit.py in your Command Prompt
