from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='chatgptTTS',
  version='1.0.0',
  author='soyll',
  author_email='soyll@vk.com',
  description='This is the simplest module for AI Conversations with TTS.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/soyll/chatgpt-tts',
  packages=find_packages(),
  install_requires=[
          'aiohttp==3.8.5',
          'aiosignal==1.3.1',
          'antlr4-python3-runtime==4.9.3',
          'async-timeout==4.0.3',
          'attrs==23.1.0',
          'blinker==1.6.2',
          'browser-cookie3==0.19.1',
          'certifi==2023.7.22',
          'cffi==1.16.0',
          'charset-normalizer==3.3.0',
          'click==8.1.7',
          'colorama==0.4.6',
          'curl-cffi==0.5.9',
          'filelock==3.12.4',
          'Flask==3.0.0',
          'Flask-Cors==4.0.0',
          'frozenlist==1.4.0',
          'g4f==0.1.4.2',
          'idna==3.4',
          'itsdangerous==2.1.2',
          'Jinja2==3.1.2',
          'Js2Py==0.74',
          'lz4==4.3.2',
          'MarkupSafe==2.1.3',
          'mpmath==1.3.0',
          'multidict==6.0.4',
          'networkx==3.1',
          'numpy==1.26.0',
          'omegaconf==2.3.0',
          'pycparser==2.21',
          'pycryptodome==3.19.0',
          'pycryptodomex==3.19.0',
          'PyExecJS==1.5.1',
          'pyjsparser==2.7.1',
          'PyYAML==6.0.1',
          'requests==2.31.0',
          'six==1.16.0',
          'soundfile==0.12.1',
          'sympy==1.12',
          'torch==2.0.1',
          'torchaudio==2.0.2',
          'typing_extensions==4.8.0',
          'tzdata==2023.3',
          'tzlocal==5.0.1',
          'urllib3==2.0.5',
          'websockets==11.0.3',
          'Werkzeug==3.0.0',
          'yarl==1.9.2'
  ],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='ai chatgpt tts text-to-speech chat-gpt torch silero audio voice',
  project_urls={
    'GitHub': 'https://github.com/soyll'
  },
  python_requires='>=3.6'
)