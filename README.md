# 🇨🇳 Chinese Learning App

A modern, interactive desktop application for learning Chinese vocabulary through flashcards and matching games. Built with Python and tkinter, featuring a sleek UI with smooth animations and multiple learning modes.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

### 🎯 **7 Learning Modes**
- **Pinyin → Hanzi** - Learn Chinese characters from pronunciation
- **Pinyin → Spanish** - Connect pronunciation to Spanish translations
- **Pinyin → English** - Connect pronunciation to English translations
- **Hanzi → Spanish** - Learn Spanish meanings from Chinese characters
- **Hanzi → English** - Learn English meanings from Chinese characters
- **Hanzi + Pinyin → Spanish** - Combined character and pronunciation to Spanish
- **Hanzi + Pinyin → English** - Combined character and pronunciation to English

### 📚 **Interactive Learning Tools**
- **Flashcards Mode** - Self-paced study with show/hide answers
- **Matching Game** - Interactive pair-matching with animations
- **Progress Tracking** - Visual progress bars and completion statistics
- **Customizable Sessions** - Choose 3-15 words per session

### 🎨 **Modern User Interface**
- **Professional Design** - Clean, modern interface with Segoe UI typography
- **Smooth Animations** - Cards fade and disappear when matched
- **Visual Feedback** - Color-coded responses and hover effects
- **Responsive Layout** - Adapts to different word counts and screen sizes

### 🎮 **Enhanced Matching Game**
- **Color Animation** - Cards turn green when matched correctly
- **Fade Effect** - Matched pairs gradually disappear from the grid
- **Mismatch Feedback** - Red flash for incorrect pairs
- **Score Tracking** - 10 points per successful match

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)

### Installation

1. **Clone or download the project**
```bash
git clone <repository-url>
cd chinese-learning-app
```

2. **Create directory structure**
```
chinese-learning-app/
├── main.py
├── utils.py
├── README.md
└── data/
    └── sample_vocabulary.py
```

3. **Run the application**
```bash
python main.py
```

That's it! No additional packages required.

## 📁 Project Structure

```
chinese-learning-app/
├── main.py                    # Main application coordinator
├── utils.py                   # UI components and game logic
├── README.md                  # This documentation
└── data/
    └── sample_vocabulary.py   # Vocabulary database (50+ words included)
```

### File Descriptions

- **`main.py`** - Simple, clean main application that coordinates the app flow
- **`utils.py`** - All UI components, styling, animations, and game logic
- **`data/sample_vocabulary.py`** - Vocabulary data in JSON-like format

## 🎮 How to Use

### 1. **Start Screen**
- Choose your preferred learning mode from 7 options
- Adjust the number of words using the slider (3-15 words)
- Select either Flashcards or Matching Game

### 2. **Flashcards Mode**
- Study words at your own pace
- Click "Show Answer" to reveal translations
- Click "Next" to proceed to the next word
- Complete all cards to see your progress

### 3. **Matching Game**
- Click two cards to attempt a match
- Correct pairs turn green and disappear
- Incorrect pairs flash red and reset
- Match all pairs to complete the game

### 4. **Results**
- View your completion stats
- Choose to study again or return to menu

## 📖 Vocabulary Format

Add your own Chinese vocabulary to `data/sample_vocabulary.py`:

```python
vocabulary_data = [
    {
        "hanzi": "你好",
        "pinyin": "nǐ hǎo", 
        "english": "hello",
        "spanish": "hola"
    },
    {
        "hanzi": "谢谢",
        "pinyin": "xiè xiè",
        "english": "thank you", 
        "spanish": "gracias"
    },
    # Add more entries...
]
```

### Required Fields
- **`hanzi`** - Chinese characters
- **`pinyin`** - Romanized pronunciation with tone marks
- **`english`** - English translation
- **`spanish`** - Spanish translation

## 🎨 UI Features

### Modern Design Elements
- **Color Scheme** - Professional blues, greens, and grays
- **Typography** - Segoe UI font family throughout
- **Animations** - Smooth card transitions and fade effects
- **Visual Hierarchy** - Clear information organization

### Interactive Elements
- **Hover Effects** - Buttons respond to mouse interaction
- **Selection Feedback** - Cards highlight when selected
- **Progress Bars** - Visual learning progress indication
- **Status Updates** - Real-time score and progress tracking

## 🔧 Customization

### Adding Vocabulary
1. Open `data/sample_vocabulary.py`
2. Add new entries following the required format
3. Restart the app to load new vocabulary

### Modifying Learning Modes
Edit the `get_learning_modes()` function in `utils.py` to add new combinations.

### Changing Colors/Styling
Modify the color values in `utils.py` functions like `create_start_screen()` and `setup_styles()`.

### Adjusting Word Limits
Change the slider range in `create_start_screen()` function.

## 📊 Included Vocabulary

The app comes with 50+ Chinese words across categories:

- **🤝 Greetings** - 你好, 谢谢, 再见, 对不起
- **⏰ Time** - 今天, 明天, 昨天, 现在
- **🌊 Elements** - 水, 火, 土, 风, 雨
- **🗣️ Verbs** - 吃, 喝, 看, 听, 说, 学习
- **👥 People** - 朋友, 家人, 老师, 学生
- **📏 Adjectives** - 大, 小, 好, 坏, 快, 慢
- **🔢 Numbers** - 一, 二, 三... 十
- **🎨 Colors** - 红色, 蓝色, 绿色, 黄色
- **🍎 Food** - 米饭, 面条, 苹果, 香蕉
- **🏠 Places** - 家, 学校, 医院, 银行

## 🛠️ Technical Details

### Architecture
- **Modular Design** - Separated concerns between main app and utilities
- **Event-Driven** - Uses tkinter's event system for interactions
- **State Management** - Clean state handling for games and navigation

### Performance
- **Lightweight** - No external dependencies beyond Python standard library
- **Responsive** - Smooth animations without blocking the UI
- **Memory Efficient** - Minimal resource usage

### Compatibility
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Python 3.6+** - Compatible with modern Python versions
- **Tkinter** - Uses Python's built-in GUI library

## 🚀 Future Enhancements

Potential features for future versions:

- **🔊 Audio Support** - Pronunciation playback
- **📈 Progress Tracking** - Long-term learning analytics  
- **🌐 Online Sync** - Cloud vocabulary storage
- **🎯 Spaced Repetition** - Intelligent review scheduling
- **📱 Touch Support** - Better touch screen compatibility
- **🎪 More Games** - Additional learning game modes
- **📊 Statistics** - Detailed learning analytics
- **🎨 Themes** - Customizable color themes

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Areas for Contribution
- Additional vocabulary sets
- New learning modes
- UI/UX improvements
- Performance optimizations
- Bug fixes and testing

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Chinese Language Community** - For vocabulary and learning insights
- **Python/Tkinter** - For providing excellent GUI capabilities
- **Open Source Community** - For inspiration and best practices

## 📞 Support

If you encounter any issues or have questions:

1. **Check the README** - Most common questions are answered here
2. **Open an Issue** - Report bugs or request features
3. **Contribute** - Submit improvements via pull requests

---

**Happy Learning! 🎉 Start your Chinese language journey today!**

Made with ❤️ for Chinese language learners everywhere.