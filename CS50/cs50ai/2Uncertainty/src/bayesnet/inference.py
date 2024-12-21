from model import model

# Calculate predictions
# Pass into the model the evidence that has been observed
predictions = model.predict_proba({
    "train": "delayed"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")


# python inference.py
# rain
#       none: 0.4583
#       light: 0.3069
#       heavy: 0.2348
# maintenance
#       yes: 0.3568
#       no: 0.6432
# train: delayed
# appointment
#       miss: 0.4000
#       attend: 0.6000

# As the appointment is only dependent on whether the train is delayed or not
# if you add "rain": "heavy" to the predictions
# the probability distribution of track maintenance will change as it is dependent on the rain node
# but it will not affect the distribution of the appointment
# python inference.py
# rain: heavy
# maintenance
#       yes: 0.1176
#       no: 0.8824
# train: delayed
# appointment
#       attend: 0.6000
#       miss: 0.4000