import shutil
from fastapi import APIRouter, UploadFile


router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)


@router.post("/articles")
async def add_post_image(image_id: int, file: UploadFile):
    with open(f"app/static/images/{image_id}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)