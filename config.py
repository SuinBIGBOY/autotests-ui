from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from typing import Self
from pathlib import Path

class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = Path("./videos")
        tracing_dir = Path("./tracing")
        browser_state_file = Path("browser-state.json")
        allure_results_dir = Path("./allure-results")

        allure_results_dir.mkdir(exist_ok=True)
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        # noinspection PyArgumentList
        return cls(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file,
        )

settings = Settings.initialize()