Following [this tutorial](https://realpython.com/python-speech-recognition/)

## Dependencies installation
```
pip install SpeechRecognition
brew install portaudio
pip install pyaudio
```

We replicate the code from the tutorial, we did some little tests using the library, we were able to use only the google api for the speech recognition, the other providers need api-keys, therefore they need payment.

## Result

We were able to replicate the speech recgnition tutorial successfully [here](recognizingWordsSpeech.py).

- Keep in mind that the reduce noise function is going to take some time to be calibrated, therefore some audio can be missed in the starting point.




