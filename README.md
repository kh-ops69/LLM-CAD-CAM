# LAD-LAM
7th Semester project for LLM-assisted CAD-CAM Model Generation

## Abstract
This repository takes inspiration from the original repository, [Query2CAD](https://github.com/akshay140601/Query2CAD?tab=readme-ov-file), and the subsequent research paper: [Query2CAD: Generating CAD models using natural language queries](https://arxiv.org/abs/2406.00144).

Computer-Aided Design (CAD) engineers typically do not achieve their best prototypes in a single attempt. Instead, they iterate and refine their designs to achieve optimal solutions through multiple revisions. This traditional approach, while effective, is time-consuming and heavily reliant on skilled expertise. To address these challenges, the original authors introduced Query2CAD, a novel framework that attempted to automate CAD design generation and refinement.

However, our LAD-LAM approach improves upon existing methods to yield better accuracy and model generation. It consists of two complementary novel approaches: an automated framework that utilizes a large language model to generate functional and fully-complete CAD macros, and executes them automatically in FreeCAD software, storing the resulting 3D models and code in the process. This has been carried out using the very capable [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) framework in Python.

## How to run the system
1. Download and setup the [FreeCAD](https://github.com/FreeCAD/FreeCAD) software. The system has been tested on all platforms with varying screen sizes.
2. Clone the repository.
```
git clone https://github.com/VenerableHarsha/LAD-LAM.git
```

3. Initial versions relied on using API keys to access OpenAI, Anthropic and Google's Large Language Models and retreive responses from them.
The current newer versions make use of OLLAMA, which can be downloaded here: https://ollama.com/download. OLLAMA helps in running openly available models locally, thus eliminating the need for API keys and rate limitations. Additionally, more the system resources, better is the quality of responses and creativity in them. 

4. Download Small Language Models (for computers with lesser hardware resources), for vision, entity extraction and code generation purposes. Ideally, these should be separate, and for our tests, we have used the following:
1. [Granite 3.2-Vision](https://ollama.com/library/granite3.2-vision) for visual assessment purposes
2. [Llama3.2-1B](https://ollama.com/library/llama3.2) for entity extraction
3. [Stable-Code 3B](https://ollama.com/library/stable-code) for code generation.

Feel free to use other models for better results.

## General
Our initial tests have shown promising results, with 50/50 queries being correctly answered with the automated method, largely due to improvement in Large Language Models(Specifically, ChatGPT) over the past 2 years. 

The image-assisted method is still undergoing rigorous testing.

## Future improvements
Currently, we are integrating both methods in an expressive front-end which allows users to generate executable macros and look at 3D Models directly. The front-end shall also allow for segregation of tasks and subsequent model generation tasks. 
