import os
import json
import http.client
from dotenv import load_dotenv

# import azure.cognitiveservices.speech as speechsdk
from common import next_story_directory


def generate_speech(
    story, model="eleven_labs", voice="Bella", stability=0, similarity_boost=0
):
    current_directory = os.getcwd()
    AUDIO_DIR = current_directory + "//" + "audio"
    CUR_AUDIO_DIR, _ = next_story_directory(base_dir=AUDIO_DIR, name="story")
    if model == "eleven_labs":
        name2id = {
            "Rachel": "21m00Tcm4TlvDq8ikWAM",
            "Domi": "AZnzlk1XvdvUeBnXmlld",
            "Bella": "EXAVITQu4vr4xnSDxMaL",
            "Antoni": "ErXwobaYiN019PkySvjV",
            "Elli": "MF3mGyEYCl7XYWbV9V6O",
            "Josh": "TxGEqnHWrfWFTfGW9XjX",
            "Arnold": "VR6AewLTigWG4xSOukaG",
            "Adam": "pNInz6obpgDQGcFmaJgB",
            "Sam": "yoZ06aMxZJJ28mfd3POQ",
        }
        load_dotenv()
        api_key = os.getenv("ELEVEN_LABS_API_KEY")
        conn = http.client.HTTPSConnection("api.elevenlabs.io")
        headers = {
            "accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        }

        # Request payload
        for idx, script in enumerate(story, start=1):
            narration = script["script"]
            print(len(narration))
            payload = {
                "text": narration,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": stability,
                    "similarity_boost": similarity_boost,
                },
            }
            voice_id = name2id[voice]
            conn.request(
                "POST",
                f"/v1/text-to-speech/{voice_id}?optimize_streaming_latency=0",
                headers=headers,
                body=json.dumps(payload),
            )
            response = conn.getresponse()
            if response.status == 200:
                filename = os.path.join(CUR_AUDIO_DIR, f"narration{idx}.mp3")
                with open(filename, "wb") as file:
                    file.write(response.read())
                print("Speech generated successfully!")
            else:
                print("Error:", response)
            conn.close()
    else:
        print(os.getenv("SPEECH_KEY"))
        print(os.environ.get("SPEECH_KEY"), os.environ.get("SPEECH_REGION"))
        speech_config = speechsdk.SpeechConfig(
            subscription=os.environ.get("SPEECH_KEY"),
            region=os.environ.get("SPEECH_REGION"),
        )

        for idx, script in enumerate(story, start=1):
            narration = script["narration"]
            print(CUR_AUDIO_DIR, f"narration{idx}.wav")
            filename = os.path.join(CUR_AUDIO_DIR, f"narration{idx}.wav")
            audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
            speech_config.speech_synthesis_voice_name = "en-US-AriaNeural	"  # The language of the voice that speaks (change this)
            speech_synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=speech_config, audio_config=audio_config
            )
            speech_synthesis_result = speech_synthesizer.speak_text_async(
                narration
            ).get()
            if (
                speech_synthesis_result.reason
                == speechsdk.ResultReason.SynthesizingAudioCompleted
            ):
                print("Speech synthesized for text [{}]".format(narration))
            elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_synthesis_result.cancellation_details
                print(
                    "Speech synthesis canceled: {}".format(cancellation_details.reason)
                )
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    if cancellation_details.error_details:
                        print(
                            "Error details: {}".format(
                                cancellation_details.error_details
                            )
                        )
                        print("Did you set the speech resource key and region values?")
