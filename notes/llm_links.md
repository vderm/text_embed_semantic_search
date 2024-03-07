---
author: Vasken Dermardiros
categories: note
tags:
- research
- llm
- generative-AI
title: Large-Language Model (LLM) links
---

ChatGPT is fun, but ClosedAI doesn't want to play nice. As alternatives, there are a few other alternatives popping up and it might be worth exploring.

Someone did a sort of analysis on this already in [this blog](https://simonwillison.net/), someone made a list [here](https://github.com/nichtdax/awesome-totally-open-chatgpt) as well.

## LLaMA

+ [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) along with [their paper](https://arxiv.org/abs/2302.13971) and [model weights](https://github.com/facebookresearch/llama/pull/73).
+ [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) which seems to be a bit more direct that ChatGPT. [GitHub repo](https://github.com/tatsu-lab/stanford_alpaca) also available.
+ [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp)
+ [alpaca-LoRA Low-Rank LLaMA Instruct-Tuning](https://github.com/tloen/alpaca-lora)
+ [Dalai](https://cocktailpeanut.github.io/dalai/#/) to run it with the least amount of effort.
+ [Using LLaMA with M1 Mac](https://dev.l1x.be/posts/2023/03/12/using-llama-with-m1-mac/) which is taking the model, quantizing it and compiles in C++.
+ [George Hotz put that in tinygrad](https://www.youtube.com/watch?v=0kRDs9BW2NU&ab_channel=georgehotzarchive) but let's not get crazy here.
+ [llama-4bit-65b](https://huggingface.co/maderix/llama-65b-4bit) quantize the shit out of it! And here's a [YouTube video](https://www.youtube.com/watch?v=OtAZHHyJSqU&ab_channel=1littlecoder) on how to run it.
+ [llama 4bit setup](https://rentry.org/llama-tard-v2#bonus-4-4bit-llama-basic-setup)
+ [simp 4 satoshi twitter post](https://twitter.com/iamgingertrash/status/1636180818606592000): just someone saying that they got it working with 3x A100 GPUs
+ [MiniLLM: Large Language Models on Consumer GPUs](https://github.com/kuleshov/minillm): MiniLLM uses the the GPTQ algorithm for up to 3-bit compression and large reductions in GPU memory usage.
+ [Simple LLaMA Finetuner](https://github.com/lxe/simple-llama-finetuner)
+ [Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/) preferred over Alpaca
+ [Wizard Vicuna quantized](https://huggingface.co/TheBloke/wizard-vicuna-13B-GPTQ) this one scores better than vicuna!
+ [Guanaco QLoRa](https://the-decoder.com/guanaco-is-a-chatgpt-competitor-trained-on-a-single-gpu-in-one-day/) and HF page: <https://huggingface.co/JosephusCheung/Guanaco>

## Open-Assistant, FauxPilot

+ [GitHub repo](https://github.com/LAION-AI/Open-Assistant) for the Open-Assistant project. [Video](https://www.youtube.com/watch?v=6OozhhI6U4g&ab_channel=YannicKilcher) of the guy live coding.
+ [FauxPilot](https://github.com/fauxpilot/fauxpilot)
+ [Chatbot with INFINITE MEMORY using OpenAI & Pinecone - GPT-3, Embeddings, ADA, Vector DB, Semantic](https://www.youtube.com/watch?v=2xNzB7xq8nk&ab_channel=DavidShapiro~AI)

## Code generator

+ [Replit Code](https://huggingface.co/replit/replit-code-v1-3b)

## ChatGPT VSCode Extension

+ [ChatGPT VSCode Extension](https://marketplace.visualstudio.com/items?itemName=gencay.vscode-chatgpt).

## Text generation UI

+ [GitHub repo](https://github.com/oobabooga/text-generation-webui/)

Was able to install this, fetch pre-trained models from HuggingFace, run it and generate some text. It's okay. I think the bigger models would do better since the smaller ones ended up just collapsing and repeating the same sentence over and over.

+ [FastChat](https://github.com/lm-sys/FastChat) simpler UI

## LoRA

Tutorials and explanation.

+ Video 1 (background): <https://www.youtube.com/watch?v=dA-NhCtrrVE&ab_channel=ChrisAlexiuk>
+ Video 2 (demo): <https://www.youtube.com/watch?v=iYr1xZn26R8&ab_channel=ChrisAlexiuk>
+ LoRA paper: [LORA: LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS](https://arxiv.org/pdf/2106.09685.pdf)
+ Predecessor that says attention matrix might be low-rank [Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning](https://arxiv.org/pdf/2012.13255.pdf)
  + <https://colab.research.google.com/drive/1iERDk94Jp0UErsPf7vXyPKeiM4ZJUQ-a?usp=sharing#scrollTo=o0BZjNgEBvXH>

## General Note

+ [HuggingFace tutorial on how to fine-tune a model](https://huggingface.co/docs/transformers/training).
+ [HuggingFace Parameter-Efficient Fine-Tuning (PEFT)](https://github.com/huggingface/peft)
+ [High-throughput Generative Inference of Large Language Models with a Single GPU](https://arxiv.org/abs/2303.06865).
+ [From Books to Knowledge Graphs](https://arxiv.org/pdf/2204.10766.pdf) -> data quality is extremely important!
+ [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/): refers to methods for how to communicate with LLM to steer its behavior for desired outcomes without updating the model weights.
+ [We have no moat](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither) Google allegedly saying how open source will win given how fast things move

## Other Models (I guess worth exploring if LLaMA is shit)

As per a YouTuber comment: LLaMA is interesting, but I think that GPT-Neo-125M, Pythia-70M, Pythia-160M, GPT-2, OPT-125M and OPT-350M is the best to run and fine tune in Google Colab, they are fast, can run fast on CPU and fast fine tune it on GPU.

 GPT-Neo-125M, Pythia-70M, Pythia-160M, GPT-2, OPT-125M and OPT-350M are free and open source.

## Agents -> where all this shit is heading

+ [The Anatomy of Autonomy: Why Agents are the next AI Killer App after ChatGPT](https://www.latent.space/p/agents)
+ [LangChain is overrated, go down a level instead](https://minimaxir.com/2023/07/langchain-problem/) too much fluff and pointless classes
  + so the author made this [simpleaichat](https://github.com/minimaxir/simpleaichat) instead

## Semantic Search

+ [Building a Semantic Search Engine With OpenAI and Pinecone](https://sigmoidprime.com/post/searchthearxiv/)
+ [beerose/semantic-search](https://github.com/beerose/semantic-search)
+ <https://www.chatpdf.com/>
+ <https://consensus.app/>
+ <https://www.researchrabbit.ai/>
+ <https://elicit.org/>
+ <https://scite.ai/>
+ [Sentence transformers](https://www.sbert.net/index.html): package to help transform a sentence to an embedding to them apply search
  + <https://www.sbert.net/docs/pretrained_models.html#scientific-publications>
  + [FAISS (Facebook AI Similarity Search)](https://ai.meta.com/tools/faiss/)

## Vasken's Desiderata

As a Vasken, I want to have some sort of ChatGPT equivalent that will be a sort of personal assistant and can...

1. Help with suggesting Python code
2. Help with writing via a prompt
3. Help with writing by offering auto-complete
4. Be able to, given a bunch of files, summarize what's in them
5. (Non-ChatGPT strictly related) Would want to have a semantic clustering of articles from online sources, i.e. ArXiV, so that given the history of the type of papers I've liked, it can suggest more.
6. Maybe that can be pushed further to search/collect jobs/contracts online.
