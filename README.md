# Portfolio Repository(Read Me)

# Introdudction

This repository is a collection of my personal/team projects, open-source contribution and self-study, covering topics such as AI, Data Science, Backend Engineering, and Frontend Development (Vue.js, Android). It includes all sorts of topics I’ve explored since I started programming.

# Projects

### 1. Visa Assistant Chatbot with RAG

- **Tags:** LLM, Backend,
- **Description:** Chatbot service for foreigners who wants to get information about Korean visa system, administration services.
- **Tools:** FastAPI, PostgreSQL, Docker, AWS, Langchain
- **Role & Responsibilities:**
    - Developed a RAG (Retrieval-Augmented Generation) based chatbot.
    - Collected and processed large-scale textual data through web crawling.
    - Set up CI/CD pipelines for automated testing and deployment.
    - Optimized API performance by introducing streaming responses and mitigating cold start issues.
- **Key Achievements:**
    - Secured 2nd place in the Korean National Information Society Agency (NIA) government funding program. [🔗](https://www.koit.co.kr/news/articleView.html?idxno=126995)
    - Integrated service on a social media platform (kakaotalk channel)
- **Resources:**
    - Blog Post (on going)
    - App store (Launching soon)

### 2. Korean Pronounciation Correction Service

- **Tags:** Deep Learning, NLP(Natural Language Processing)
- **Tools:** Flask, Pytorch, Huggingface
- **Role & Responsibilities:**
    - Developed a pronunciation correction service for foreigners learning Korean.
    - Collected and preprocessed Korean speech and text data.
    - Implemented an OAuth authentication system (Google Login) using Flask.
- **Resources:**
    - [Github Repository](https://github.com/bom1215/level3_nlp_finalproject-nlp-13)

### 3. Toilet Korea App (Personal)

- **Tag:** Android
- **Description:** An Android app that aims to enhance hygiene by offering a platform for users to find information about public toilets
- **Resources:**
    - [Google Play Store](https://play.google.com/store/apps/details?id=com.codeJP.toiletkorea)
    - [Github repository](https://github.com/bom1215/ToiletKorea)

# Open Source Contributions

I actively contribute to open-source projects to improve my coding skills and collaborate with the community. Here are some of my contributions:

| Project | Contribution | PR |
| --- | --- | --- |
| **Pykrx : stock data scraper** | Fix bugs : replace `append` with `pd.concat` | [#157](https://github.com/sharebook-kr/pykrx/pull/157) (Merged) |
| **pydantic-sqlalchemy** | Migrate deprecated code to the latest version | [#160](https://github.com/tiangolo/pydantic-sqlalchemy/pull/160) |

# Deep Learning Study

### Building Deep Learning Models from scratch

- **Description**: Building deep learning models from scratch without using PyTorch or TensorFlow and applying them to real-world tasks

**Works**

- [Can numerical differentiation replace backpropagation in a Multilayer Perceptron (MLP)?](https://github.com/bom1215/portfolio/blob/main/deep_learning_from_scratch/train_mnist_mlp.ipynb)

## Getting Started

To execute the code files, please install the following dependencies:

```bash
pip install -r requirements.txt
```