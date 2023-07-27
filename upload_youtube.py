import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from text2image import dalle_call
from PIL import Image


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    if width > size[0] or height > size[1]:
        resized_image = original_image.resize(size, Image.ANTIALIAS)
        resized_image.save(output_image_path)
    else:
        original_image.save(output_image_path)


# Resize the image to be smaller.

# Setup the Youtube API
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CREDENTIALS_FILE = "inova.pickle"


def get_authenticated_service():
    credentials = None
    if os.path.exists(CREDENTIALS_FILE):
        print(f"Loading credentials from file: {CREDENTIALS_FILE}")
        with open(CREDENTIALS_FILE, "rb") as f:
            credentials = pickle.load(f)
    else:
        print(f"No credentials file found at {CREDENTIALS_FILE}")

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("Refreshing credentials")
            credentials.refresh(Request())
        else:
            print("Fetching new tokens")
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES
            )

            credentials = flow.run_local_server(port=0)

            with open(CREDENTIALS_FILE, "wb") as token:
                print(f"Saving credentials to: {CREDENTIALS_FILE}")
                pickle.dump(credentials, token)

    return build("youtube", "v3", credentials=credentials)


def initialize_upload(youtube, file, thumbnail_file, title, description, tags):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "22",  # Refer https://developers.google.com/youtube/v3/docs/videoCategories/list
            },
            "status": {"privacyStatus": "public"},  # or unlisted, private
        },
        media_body=MediaFileUpload(file),
    )
    response = request.execute()

    print(f'Uploaded file; id={response["id"]}')
    thumbnail_request = youtube.thumbnails().set(
        videoId=response["id"],
        media_body=MediaFileUpload(thumbnail_file, mimetype="image/jpeg"),
    )
    thumbnail_response = thumbnail_request.execute()

    print(f'Set thumbnail for {response["id"]}')


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # For local development only
    youtube = get_authenticated_service()
    initialize_upload(
        youtube, "final_video.mp4", "dd.jpg"
    ) 


def upload_youtube(video, thumbnail_prompt, title, description, tags):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # For local development only
    youtube = get_authenticated_service()
    thumbnail_file = os.path.join(
        os.path.join(os.getcwd(), "thumbnails/"), "thumbnail.png"
    )
    dalle_call(thumbnail_prompt, thumbnail_file)
    resize_image(thumbnail_file, thumbnail_file, (1280, 720))

    initialize_upload(youtube, video, thumbnail_file, title, description, tags)


# if __name__ == "__main__":
#    main()
