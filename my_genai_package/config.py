from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Groq Chatbot API"
    groq_api_key: str
    model: str = "llama-3.3-70b-versatile"

    class Config:
        env_file = ".env"
        extra="ignore" # This tells Pydantic: "Don't crash if you see extra stuff"

settings = Settings()
