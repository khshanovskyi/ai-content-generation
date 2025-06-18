# Image Generation and Analysis with DIAL API

A Python implementation task to work with AI image generation and analysis capabilities via DIAL API

## 🎓 Learning Goals

By completing these tasks, you will learn:
- How to generate images from text prompts using DALL-E 3
- How to analyze images using different AI models (GPT-4o, Claude-3-Sonnet)
- Two different approaches for handling images in AI systems:
   - **OpenAI approach**: Base64 encoding for direct embedding
   - **DIAL approach**: Bucket storage with attachment references
- How to work with file uploads, downloads, and async operations
- How to adapt requests across different AI model vendors through DIAL Core

## 📋 Requirements

- Python 3.11+
- pip
- API key for DIAL service
- Basic understanding of HTTP requests and async/await
- `dialx-banner.png` image file in project root (provided)

## 🔧 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key:**
   - Ensure that you are connected to the EPAM VPN
   - Get the DIAL API key here: https://support.epam.com/ess?id=sc_cat_item&table=sc_cat_item&sys_id=910603f1c3789e907509583bb001310c
   - Update the `API_KEY` constant in `task/_utils/constants.py`
   - Get available models from: https://ai-proxy.lab.epam.com/openai/models

3. **Project structure:**
   ```
   task/
   ├── _models/
   │   ├── conversation.py          # ✅ Complete
   │   ├── message.py               # ✅ Complete  
   │   ├── role.py                  # ✅ Complete
   │   └── custom_content.py        # ✅ Complete
   ├── _utils/
   │   ├── model_client.py          # ✅ Complete
   │   ├── bucket_client.py         # ✅ Complete
   │   ├── constants.py             # ✅ Complete
   │   └── request.py               # ✅ Complete
   ├── image_to_text/
   │   ├── openai/
   │   │   ├── message.py           # ✅ Complete
   │   │   └── task_openai_itt.py   # 🚧 TODO
   │   └── task_dial_itt.py         # 🚧 TODO
   └── text_to_image/
       └── task_tti.py              # 🚧 TODO
   dialx-banner.png                 # 📁 Sample image
   ```

## 📝 Your Tasks

Complete the implementation of these three practice files:

### 1. **task_openai_itt.py** - OpenAI-Style Image Analysis
**Goal:** Analyze an image using base64 encoding approach
- Create DialModelClient with GPT-4o model (and other models)
- Encode image as base64 data URL
- Send ContentedMessage with text and image content
- **Key Learning:** Direct image embedding in messages

### 2. **task_dial_itt.py** - DIAL-Style Image Analysis
**Goal:** Analyze an image using bucket storage approach
- Upload image to DIAL bucket storage
- Create message with attachment reference
- Test with different AI models
- **Key Learning:** File storage and attachment handling

### 3. **task_tti.py** - Text-to-Image Generation
**Goal:** Generate images from text prompts
- Create text prompt for image generation
- Use DALL-E 3 model for generation
- Download and save generated images
- **Key Learning:** AI image generation and file handling


## 🔍 Understanding the Approaches

### OpenAI Approach (Base64)
- **Pros:** Simple, direct embedding
- **Cons:** Large request sizes, limited to specific models
- **Use case:** Quick prototyping, OpenAI-compatible models

### DIAL Approach (Attachments)
- **Pros:** Efficient, works across all model vendors
- **Cons:** Requires additional upload step
- **Use case:** Production systems, multi-vendor support

## 🎯 Expected Outputs

### Text-to-Image Task
- Generated image file saved locally with timestamp
- Console output showing request/response details

### Image-to-Text Tasks
- AI description of the `dialx-banner.png` image
- Comparison between different models' responses

## 🛠️ Troubleshooting

**Common Issues:**
- **Empty API key:** Update `constants.py` with your DIAL API key
- **VPN connection:** Ensure EPAM VPN is active
- **File not found:** Verify `dialx-banner.png` exists in project root
- **Network errors:** Check DIAL service status and connectivity

## 🌟 Bonus Challenges

Once you complete the basic tasks, try these extensions:
1. **Multi-model comparison:** Run the same image analysis with different models
2. **Custom prompts:** Create your own text-to-image prompts
3. **Batch processing:** Analyze multiple images at once
4. **Error handling:** Add robust error handling and retries

## 📚 Key Concepts Covered

- **Multimodal AI:** Working with both text and images
- **API Design Patterns:** Different approaches to handle media content
- **Async Programming:** File operations and HTTP requests
- **Model Abstraction:** How DIAL Core adapts requests across vendors
- **File Management:** Upload, download, and storage operations

---

**Happy coding! 🚀**

Remember: The goal is to understand how different AI models can work with images and how various API design patterns solve the same problems in different ways.

# <img src="dialx-banner.png">