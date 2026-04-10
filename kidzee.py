import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

client = genai.Client()

operation = client.models.generate_videos(
    model="veo-3.1-fast-generate-preview",
    prompt="""

Subject & Action
A cheerful 4-year-old child wearing a colorful superhero cape rides a large, friendly blue dolphin. The dolphin leaps over sparkling ocean waves while the child cheers with both arms raised high.

Style
Pixar/Disney-style 3D animation. Smooth, high-quality CGI with soft subsurface skin shading, expressive cartoon facial features, and slightly exaggerated proportions. Cinematic render quality with warm volumetric lighting and soft ambient occlusion.

Camera
Side-profile tracking shot. Camera moves parallel to the dolphin, maintaining a wide frame that shows the full arc of the leap. The motion conveys speed and energy.

Composition
Wide shot. Vast open ocean fills the background. Sparkling water splashes frame the dolphin mid-leap.

Lighting & Mood
Bright daylight with warm golden tones. High-energy, joyful atmosphere. Overall mood is cheerful and uplifting.

""",
    config=types.GenerateVideosConfig(
      negative_prompt="barking, woofing",
      aspect_ratio="9:16",
      resolution="720p",
    ),
)

# Waiting for the video(s) to be generated
while not operation.done:
    time.sleep(20)
    operation = client.operations.get(operation)
    print(operation)

generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("golden_retriever.mp4")