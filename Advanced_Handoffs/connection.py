import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
 raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Setup Gemini OpenAI-compatible client
external_client = AsyncOpenAI(
 api_key=gemini_api_key,
 base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model
model = OpenAIChatCompletionsModel(
 model="gemini-2.0-flash",
 openai_client=external_client
)

# Create run configuration
config = RunConfig(
 model=model,
 model_provider=external_client,
 tracing_disabled=True
)