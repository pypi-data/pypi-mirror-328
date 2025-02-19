from setuptools import setup, find_packages

setup(
  name="doc-page-extractor",
  version="0.0.1",
  author="Tao Zeyu",
  author_email="i@taozeyu.com",
  description="doc page extractor can identify text and format in images and return structured data.",
  packages=find_packages(),
  long_description=open("./README.md", encoding="utf8").read(),
  long_description_content_type="text/markdown",
  install_requires=[
    "opencv-python>=4.11.0,<5.0",
    "pillow>=10.3,<11.0",
    "shapely>=2.0.0,<3.0",
    "transformers>=4.48.0,<5.0",
    "doclayout_yolo>=0.0.3",
    "paddlepaddle>=2.6.0,<3.0",
    "paddleocr>=2.9.0,<3.0",
  ],
)