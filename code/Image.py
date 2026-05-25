import json
import requests
import copy
import time
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# 定义ComfyUI API的URL
COMFYUI_API_URL = "http://comfyui.matrix-studio.top:20000"

def load_workflow(workflow_path):
    """
    从指定路径加载工作流配置。

    Args:
        workflow_path (str): 工作流配置文件的路径。

    Returns:
        dict or None: 如果成功加载工作流配置,返回字典类型的工作流配置;如果文件未找到或JSON格式错误,返回None。

    Raises:
        无。

    """
    try:
        with open(workflow_path, 'r', encoding='utf-8') as file:
            workflow = json.load(file)
            return workflow
    except FileNotFoundError:
        print(f"The file {workflow_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"The file {workflow_path} contains invalid JSON.")
        return None

def check_result(prompt_id, res_json):
    """
    检查指定prompt_id的结果是否已完成。

    Args:
        prompt_id (str): 要检查的prompt的唯一标识符。
        res_json (dict): 包含多个prompt结果的JSON对象。

    Returns:
        bool: 如果指定prompt_id的结果已完成,则返回True;否则返回False。

    """
    if res_json.get(prompt_id, None):
        if res_json[prompt_id].get("status", None):
            if res_json[prompt_id]["status"]["completed"]:
                return True
    return False

def generate_image(workflow_input, prompt):
    """
    根据给定的prompt生成图像,并返回生成的图像的prompt_id。

    Args:
        workflow (dict): 工作流配置字典，用于生成图像。
        prompt (str): 要生成的图像的文本描述。

    Returns:
        str: 生成的图像的prompt_id。

    Raises:
        无。

    """
    workflow = copy.deepcopy(workflow_input)
    workflow["1"]["inputs"]["text"] = "Dunhuang,The ancient city of Century City in Gansu Province,China,features golden hues and orange tones,with mountains surrounding it. The traditional Chinese painting style depicts the Yellow River flowing through it,featuring small figures riding camels on its banks. In aerial perspective,watercolor techniques depict the complex composition of architecture,creating an overall warm atmosphere. It is presented as an illustration in the style of traditional Chinese painters," + prompt
    print("generate_image prompt: ", workflow["1"]["inputs"]["text"])
    data = json.dumps({"prompt": workflow}).encode("utf-8")
    req = requests.post(
        f"{COMFYUI_API_URL}/prompt",
        headers={
            "Content-Type": "application/json",
        },
        data=data,
    )
    print(req.text)
    prompt_id = req.json()["prompt_id"]
    return prompt_id

def get_image(workflow, prompt):
    """
    根据给定的工作流和提示生成图像,并返回生成的图像的URL。

    Args:
        workflow (dict): 工作流配置字典，用于生成图像。
        prompt (str): 用于生成图像的文本提示。

    Returns:
        str: 生成的图像的URL。

    Raises:
        无。

    """
    prompt_id = generate_image(workflow, prompt)
    history_url = f"{COMFYUI_API_URL}/history/{prompt_id}"
    res = requests.get(history_url)
    res_json = res.json()
    while not check_result(prompt_id, res_json):
        time.sleep(3)
        res = requests.get(history_url)
        res_json = res.json()
        if res_json:
            print(res_json)
    # 获取工作流执行输出
    outputs = res_json[prompt_id]["outputs"]
    # 假设输出中包含图像信息，需要根据实际情况调整获取图像URL的逻辑
    for node_id, output in outputs.items():
        if "images" in output:
            image_info = output["images"][0]
            image_url = f"{COMFYUI_API_URL}/view?filename={image_info['filename']}&subfolder={image_info['subfolder']}&type={image_info['type']}"
            return image_url
    return None

def display_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        plt.imshow(image)
        plt.axis('off')  # 不显示坐标轴
        plt.show()
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 示例使用
workflow = {
  "1": {
    "inputs": {
      "text": "dunhuang,This is a highly detailed, photorealistic image of a young woman dressed in traditional, elaborate attire, likely inspired by ancient Chinese or Tibetan culture. She stands confidently in front of a richly decorated, intricately painted backdrop featuring a large, ornate mandala with multiple depictions of serene, ethereal beings. The woman's attire is a stunning, multi-colored ensemble that includes a golden, strapless top with intricate patterns and a flowing, layered skirt in shades of beige, gold, and orange. Her outfit is adorned with ornate, golden accessories, including a large, elaborate headpiece that resembles a miniature stupa or crown, featuring golden and red hues. She wears multiple, sparkling jewelry pieces, including a prominent, blue-encrusted necklace and matching earrings. Her dark hair is styled in an elegant, up-swept manner, with a few loose strands framing her face. Her skin has a smooth, porcelain-like complexion, and her eyes are almond-shaped, with a subtle, enigmatic expression. The background's vibrant colors and detailed carvings create a sense of opulence and cultural significance, emphasizing the woman's regal and mystical presence. The lighting is soft and warm, highlighting the textures and colors of her attire and the background.",
      "clip": [
        "5",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "2": {
    "inputs": {
      "samples": [
        "7",
        0
      ],
      "vae": [
        "4",
        0
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE解码"
    }
  },
  "4": {
    "inputs": {
      "vae_name": "FLUX.1-dev/ae.safetensors"
    },
    "class_type": "VAELoader",
    "_meta": {
      "title": "加载VAE"
    }
  },
  "5": {
    "inputs": {
      "clip_name1": "FLUX.1-dev/clip_l.safetensors",
      "clip_name2": "FLUX.1-dev/t5xxl_fp8_e4m3fn.safetensors",
      "type": "flux",
      "device": "default"
    },
    "class_type": "DualCLIPLoader",
    "_meta": {
      "title": "双CLIP加载器"
    }
  },
  "6": {
    "inputs": {
      "unet_name": "FLUX.1-dev/flux1-schnell.safetensors",
      "weight_dtype": "fp8_e4m3fn"
    },
    "class_type": "UNETLoader",
    "_meta": {
      "title": "UNet加载器"
    }
  },
  "7": {
    "inputs": {
      "noise": [
        "11",
        0
      ],
      "guider": [
        "10",
        0
      ],
      "sampler": [
        "8",
        0
      ],
      "sigmas": [
        "9",
        0
      ],
      "latent_image": [
        "13",
        0
      ]
    },
    "class_type": "SamplerCustomAdvanced",
    "_meta": {
      "title": "自定义采样器（高级）"
    }
  },
  "8": {
    "inputs": {
      "sampler_name": "euler"
    },
    "class_type": "KSamplerSelect",
    "_meta": {
      "title": "K采样器选择"
    }
  },
  "9": {
    "inputs": {
      "scheduler": "ddim_uniform",
      "steps": 20,
      "denoise": 1,
      "model": [
        "14",
        0
      ]
    },
    "class_type": "BasicScheduler",
    "_meta": {
      "title": "基本调度器"
    }
  },
  "10": {
    "inputs": {
      "model": [
        "14",
        0
      ],
      "conditioning": [
        "12",
        0
      ]
    },
    "class_type": "BasicGuider",
    "_meta": {
      "title": "基本引导器"
    }
  },
  "11": {
    "inputs": {
      "noise_seed": 7777777
    },
    "class_type": "RandomNoise",
    "_meta": {
      "title": "随机噪波"
    }
  },
  "12": {
    "inputs": {
      "guidance": 3.5,
      "conditioning": [
        "1",
        0
      ]
    },
    "class_type": "FluxGuidance",
    "_meta": {
      "title": "Flux引导"
    }
  },
  "13": {
    "inputs": {
      "width": 1280,
      "height": 720,
      "batch_size": 2
    },
    "class_type": "EmptySD3LatentImage",
    "_meta": {
      "title": "空Latent图像(SD3)"
    }
  },
  "14": {
    "inputs": {
      "max_shift": 1.15,
      "base_shift": 0.5,
      "width": 1280,
      "height": 720,
      "model": [
        "21",
        0
      ]
    },
    "class_type": "ModelSamplingFlux",
    "_meta": {
      "title": "采样算法(Flux)"
    }
  },
  "20": {
    "inputs": {
      "filename_prefix": "image/ComfyUI",
      "images": [
        "2",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "保存图像"
    }
  },
  "21": {
    "inputs": {
      "lora_name": "FLUX.1-dev/pytorch_lora_weights_step2000.safetensors",
      "strength_model": 0.8,
      "model": [
        "6",
        0
      ]
    },
    "class_type": "LoraLoaderModelOnly",
    "_meta": {
      "title": "LoRA加载器(仅模型)"
    }
  }
}

if workflow:
    prompt = input("请输入你的prompt（例如：The undulating satin brocade has a Chinese pattern on it.silk light sense,miniature landscape,）：")
    image_url = get_image(workflow, prompt)
    if image_url:
        print(f"Generated image URL: {image_url}")
        display_image(image_url)
    else:
        print("Failed to get image URL.")