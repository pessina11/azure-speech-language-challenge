import azure.cognitiveservices.speech as speechsdk

def transcribe_audio(audio_path):
    speech_key = "<YOUR_SPEECH_API_KEY>"
    region = "<YOUR_REGION>"
    audio_config = speechsdk.audio.AudioConfig(filename=audio_path)
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
    
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once()
    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
    else:
        print("Speech Recognition failed")

