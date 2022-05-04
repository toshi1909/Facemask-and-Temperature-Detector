# Facemask-and-Temperature-Detector
Automated facemask and temperature checking system
Here we detect facemask by using CNN. We train our model on a dataset containing mask and no mask images.
Once the model is trained we save it for further use so that we don't have to train our model everytime we execute our program.
In our main function we wait for the arduino to send a signal 1 as that's when the proximity sensor detects a nearby object (or a person).
The former step is done to improve the efficiency of our program so that we are not trying to detect a mask when no one is standing in front.
Whether the model detects a mask or not a signal is send to arduino using serial communication.
The arduino detects the temperature of the person using the contactless MLX90614 temperature sensor. It also reads the data sent by python program mentioned in the previous step.
If the person is wearing a mask and their temperature is within the healthy range servo motor gets activated, indicating opening of the gate. Else the servo remains off.
This is how we make sure that whoever is entering our premises is following COVID protocols.
