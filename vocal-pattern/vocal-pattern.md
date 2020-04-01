Following [this Librosa tutorial](https://www.thepythoncode.com/article/building-a-speech-emotion-recognizer-using-sklearn)
## Dependencies installation
```
brew install python3
brew install portaudio
brew install ffmpeg
virtualenv -p python3 venv
source venv/bin/activate
pip3 install librosa==0.6.3 numpy soundfile==0.9.0 sklearn pyaudio==0.2.11

```

You can download RAVDESS from [here](https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio/data)
* You have to extract in a new folder called `raw_data`
* Create a folder named `data`
* In order to reduce resolution and that Librosa can handle it, run this command `python convert_wavs.py  raw_data/Actor_01 data/Actor_01` for each of the Actor_* folders


