## Getting Started with ML Computer Vision
This library contains some simple examples that will help coaches prepare for the ML OpenHack. Click **Clone** above to clone this library to your own Azure notebooks account (or download the files if you want to use a local Jupyter instance). Note that these samples represent *some* ways to solve particular computer vision problems - they're **not** definitive solutions!

The samples in this library will cover around 80% of the skills required to complete the challenges in the ML OpenHack. After using these to get to grips wth the basics, you should explore the following topics:

### Provisioning an ML Development Environment
Azure Notebooks is fine for simple examples, but to work with large volumes of data and train complex models, you'll need a more comprehensive environment. The basic choice is between using a hosted data science virtual machine in Azure that has the most common tools already installed, or installing your own local environment. The following resources should help:
* <a href='https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview' target='_blank'>The Azure Data Science VM</a>
* <a href='https://docs.microsoft.com/en-us/azure/machine-learning/service/' target='_blank'>Azure Machine Learning Services</a>
* <a href='https://www.anaconda.com/download/' target='_blank'>Installing the Anaconda Python Distribution</a>
* <a href='http://jupyter.readthedocs.io/en/latest/install.html' target='_blank'>Jupyter Notebooks</a>

### Deploying a Machine Learning Model as a Web Service
After you've created a machine learning model, you'll need to deploy it so that it can be consumed. Increasingly, the preferred option for deploying an ML model is to wrap it up as a REST web service and deploy it to a container. Here are some links to help you:
* <a href='https://docs.microsoft.com/en-us/azure/machine-learning/desktop-workbench/model-management-service-deploy' target='_blank'>Deploying a Model with Azure Machine Learning</a>
* <a href='https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html' target='_blank'>Deploying a Keras Model with Flask</a>
* <a href='https://naadispeaks.wordpress.com/2018/01/12/deploy-machine-learning-models-in-a-production-environment-as-apis-python-flask-visual-studio/' target='_blank'>Deploying Machine Learning Models as APIs with Flask and Visual Studio</a>

### Object Detection
The examples in this library mostly cover *image classification* (categorizing an image based on its contents). The next step in computer vision from here is *object detection* (determining which objects an image contains, and their location within the image). This library contains an example of performing Object Detection with the *Custom Vision* service; but you should research object detection solutions in other commonly used ML frameworks. Here are some examples:
* <a href='https://docs.microsoft.com/en-us/cognitive-toolkit/Object-Detection-using-Fast-R-CNN' target='_blank'>Object Detection using Fast R-CNN in CNTK</a>
* <a href='https://docs.microsoft.com/en-us/cognitive-toolkit/Object-Detection-using-Faster-R-CNN' target='_blank'>Object Detection using Faster R-CNN in CNTK</a>
* <a href='https://www.oreilly.com/ideas/object-detection-with-tensorflow' target='_blank'>Object Detection with TensorFlow</a>
* <a href='https://medium.com/@WuStangDan/step-by-step-tensorflow-object-detection-api-tutorial-part-1-selecting-a-model-a02b6aabe39e' target='_blank'>Step by Step TensorFlow Object Detection</a>

### Online Courses
If you want a more rounded understanding of some of the underlying concepts of AI and Computer Vision, you might want to audit the following courses on edX.org:
* <a href='https://aka.ms/edx-dat263x-about' target='_blank'>Introduction to Artificial Intelligence</a>
* <a href='https://aka.ms/edx-dat208x-about' target='_blank'>Introduction to Python for Data Science</a>
* <a href='https://aka.ms/edx-dev290x-about' target='_blank'>Computer Vision and Image Analysis</a>
