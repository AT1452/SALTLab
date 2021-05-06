# SALT Lab: Assisted Learning With Facial Movements Research
This is the repository containing the software/tool for the Assisted Learning with Facial Movements study. We are using Openface: (https://github.com/TadasBaltrusaitis/OpenFace/) and Multitask-Emotion-Recognition-with-Incomplete-Labels: (https://github.com/wtomin/Multitask-Emotion-Recognition-with-Incomplete-Labels) to gather data on facial movements and interpret it in the context of learning with asynchronous intervention and feedback.  
  

To run the tool:  
Download all the requirements from both of the above repositories respectively  
```cd ./api```  
```python run_example.py```  
A webcam window should pop up that will record your facial movements. Press 1 or Q to stop at any time.  
Then, in the folder "examples" will be a file labeled multitask_preds.csv containing all the predictions for different metrics of facial movement and cues.  
