from setuptools import setup,find_packages

setup(
    name="chess2",  # 패키지 이름
    version="1.0.1",  # 버전
    description="A Python Chess Game supporting PGN and FEN formats",  # 설명
    long_description=open('README.md').read(),  # README.md 파일 내용
    long_description_content_type="text/markdown",  # Markdown 형식
    author="minjae",  # 작성자 이름
    author_email="minjaezzzang@gmail.com",  # 이메일  # 프로젝트 URL
    packages=find_packages(),  # 패키지 자동 검색
    install_requires=[],  # 의존성 목록
    classifiers=[  # PyPI에서 프로젝트 분류
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Python 버전 요구 사항
)
