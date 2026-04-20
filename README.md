<div align="center">

# 🔮 **WordCloud Pro**

**A Premium Streamlit Word Cloud Generator**  
*Modern • Glassmorphism • Real-time • SaaS-grade UI*

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00C853?style=for-the-badge)
![Last Updated](https://img.shields.io/badge/Updated-April_2026-8B5CF6?style=for-the-badge)

**Built by [Hammad Zahid](https://github.com/hammadzahid)**  
*AI & Data Science Enthusiast | Python Developer*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-8B5CF6?style=for-the-badge&logo=streamlit&logoColor=white)](https://wordcloud-pro.streamlit.app) 
[![GitHub Stars](https://img.shields.io/github/stars/hammadzahid/wordcloud-pro?style=for-the-badge)](https://github.com/hammadzahid/wordcloud-pro/stargazers)

</div>

<br>

---

## ✨ **Project Highlights**

Transform any text into **stunning, customizable word clouds** with a beautiful glassmorphism interface inspired by modern AI dashboards.

Built with attention to every detail — smooth animations, real-time preview, animated analytics, and professional branding.

**Perfect for portfolios, data visualization lovers, content creators, and AI enthusiasts.**

---

## 📸 **Preview**

![Hero Section](screenshots/hero.png)
![Word Cloud + Metrics](screenshots/wordcloud.png)
![Analytics Dashboard](screenshots/chart.png)

> *Dark gradient theme with purple-blue neon accents, glassmorphism cards, hover animations, and Plotly charts.*

---

## 🚀 **Key Features**

### **Core Functionality**
- **Multi-format Support**: `.txt`, `.pdf`, `.docx` + direct text input
- **Real-time Customization** with instant preview
- **8 Premium Color Palettes** (Neon Purple, Aurora Borealis, Sunset Warm, Ocean Cool, etc.)
- **Background Themes**: Dark, Light, or Custom Color Picker
- **Shape Masks**: Circle, Square, Rounded Square, Diamond, Star

### **Visualizations & Analytics**
- High-resolution word cloud with **glow effect**
- **Animated Plotly** horizontal bar chart (Top Word Frequencies)
- **4 Glassmorphism Metric Cards**:
  - Total Words
  - Unique Words
  - Most Frequent Word
  - Rarest Word

### **Premium UX/UI**
- Modern **dark gradient + glassmorphism** design
- Subtle animations, fade-ins, hover effects, and loading spinners
- Fully responsive layout using Streamlit columns
- Styled download buttons (PNG, JPG, Data)
- Professional success/error notifications

---

## 🛠 **Tech Stack**

- **Framework**: Streamlit
- **Word Cloud Engine**: `wordcloud` + Pillow + NumPy
- **Charts**: Plotly
- **Document Processing**: PyPDF2, python-docx
- **Styling**: Custom CSS (Glassmorphism, Gradients, Keyframe Animations)
- **Architecture**: Modular (components + utils)

---

## 📥 **Installation & Setup**

```bash
# Clone the repository
git clone https://github.com/hammadzahid/wordcloud-pro.git
cd wordcloud-pro

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On macOS/Linux
# venv\Scripts\activate         # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```
# 📁 Project Structure
```
wordcloud-pro/
├── app.py                    # Main Streamlit application
├── requirements.txt
├── README.md
├── sample.txt
├── utils/
│   ├── styling.py            # Custom CSS & color palettes
│   ├── text_processor.py     # Text extraction & stats
│   └── wordcloud_engine.py   # Word cloud generation logic
├── components/
│   ├── hero.py
│   ├── sidebar.py
│   ├── metrics.py
│   ├── uploader.py
│   ├── wordcloud_viz.py
│   ├── frequency_chart.py
│   └── download_panel.py
└── screenshots/              # App preview images
```
## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request
# 👨‍💻 About the Author
Hammad Zahid
AI & Data Science Enthusiast | Python Developer
# Change these URLs:
https://github.com/Hamad-Ansari  # Your repo URL
https://www.linkedin.com/in/hammad-zahid-xyz/           # Your LinkedIn
https://github.com/hammadzahid                # Your GitHub
https://wordcloud-pro-hammadzahid.streamlit.app  # Your deployed app
mrhammadzahid24@gmail.com # Your email

