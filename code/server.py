import http.server
import json
import requests
import copy
import time
from io import BytesIO
from http import HTTPStatus
from PIL import Image
from datetime import datetime


# 定义ComfyUI API的URL
COMFYUI_API_URL = "http://comfyui.matrix-studio.top:20000"


def load_workflow(workflow_path):
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
    if res_json.get(prompt_id, None):
        if res_json[prompt_id].get("status", None):
            if res_json[prompt_id]["status"]["completed"]:
                return True
    return False


def generate_image(workflow_input, prompt):
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


def save_image(image_url, prompt):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        # 获取当前时间并格式化为合适的字符串
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{current_time}.png"
        image.save(filename)
        return filename
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        prompt = data.get('prompt')

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

        image_url = get_image(workflow, prompt)
        if image_url:
            filename = save_image(image_url, prompt)
            if filename:
                response_data = {"status": "success", "filename": filename, "prompt": prompt}
            else:
                response_data = {"status": "error", "message": "Failed to save image."}
        else:
            response_data = {"status": "error", "message": "Failed to get image URL."}

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    print('Starting web server...')
    httpd.serve_forever()