+ https://civitai.com
+ https://stable-diffusion-art.com/qr-code/
+ https://stable-diffusion-art.com/controlnet/
+ https://www.shruggingface.com/blog/self-portraits-with-stable-diffusion-and-lora
+ https://huggingface.co/lllyasviel/ControlNet-v1-1
+ https://github.com/lllyasviel/ControlNet
+ https://github.com/Mikubill/sd-webui-controlnet
+ https://replicate.com/explore?query=lora

train face with "vasken man" so that it can really learn that it's a person and use pictures with different backgrounds, clothing, expressions and looking direction: https://tryolabs.com/blog/2022/10/25/the-guide-to-fine-tuning-stable-diffusion-with-your-own-images

embedding length = 16, 20'000 epochs and it still looks very deformed weird face. Not sure what the issue is...

trained it further to 100'000 epochs and still crappy

Looking at this link, it seems like 16 vector length was way too much. Since I have 60 images where a few are similar, I'll do 8 vectors.

https://www.reddit.com/r/StableDiffusion/comments/10jfn5f/how_do_number_of_vectors_per_token_work_when/

Based on Training Images?

In this video by Aitrepeneur is explained that the number depends on the amount of training images you have. The more training images, the higher the number should be:

    2-3 Vectors Per Token for <10 Training images

    5-6 Vectors Per Token for 10-30 Training images

    8-10 Vectors Per Token for 40-60 Training images

    10-12 Vectors Per Token for 60-100 Training images

    12-16 Vectors Per Token for 100+ Training images



https://bennycheung.github.io/stable-diffusion-training-for-embeddings


followed that. Using 4 tokens finally, subject_filewords.txt, generated a picture of a man in the txt2img panel and checked that box at the bottom too.