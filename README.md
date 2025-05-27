# 🀄 中文学习 Chinese Learning App

> **Master Chinese vocabulary through interactive flashcards and memory games**

A modern, minimalistic language learning application that helps users learn Chinese (Hanzi and Pinyin) from Spanish or English words. Built with Python and Streamlit, featuring an intuitive UI and gamified learning experience.

## ✨ Features

### 🎯 **Multiple Learning Modes**
- **Pinyin → Hanzi**: Learn Chinese characters from pronunciation
- **Pinyin → Spanish/English**: Practice pronunciation with translations
- **Hanzi → Spanish/English**: Master character recognition

### 🎮 **Interactive Learning Methods**
- **📚 Flashcards**: Self-paced learning with difficulty rating
- **🧩 Memory Game**: Match pairs to reinforce vocabulary retention
- **📊 Progress Tracking**: Real-time statistics and performance metrics

### 🎨 **Modern UI/UX**
- Clean, minimalistic design with smooth animations
- Responsive layout optimized for different screen sizes
- Gradient backgrounds and interactive card components
- Visual feedback for correct/incorrect answers

### 🔧 **Smart Features**
- Batch word input (paste multiple words at once)
- Automatic translation from Spanish to English, Hanzi, and Pinyin
- Session management with scoring system
- Completion celebration with detailed statistics

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chinese-learning-app.git
   cd chinese-learning-app
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas requests uuid
   ```

3. **Run the application**
   ```bash
   streamlit run chinese_learning_app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 🎮 How to Use

### 1. **Setup Your Learning Session**
- Choose your preferred learning mode from the dropdown
- Select the number of words you want to study (5-50)
- Pick between Flashcards or Memory Game

### 2. **Add Spanish Words**
- **Individual Entry**: Type one word at a time
- **Batch Import**: Paste multiple words (one per line)
- Words are automatically translated to English, Hanzi, and Pinyin

### 3. **Start Learning**
- **Flashcards**: Click "Show Answer" then rate your knowledge
- **Memory Game**: Click cards to flip and match pairs
- Track your progress with real-time statistics

### 4. **Review Results**
- View your final score and time taken
- Choose to study again or return to the main menu

## 📱 Screenshots

### Start Screen
```
🀄 中文学习 Chinese Learning
Master Chinese with interactive flashcards and memory games

🎯 Learning Mode          📚 Study Settings
┌─────────────────────┐   ┌──────────────────────┐
│ Pinyin → Hanzi      │   │ Words to study: 10   │
│ Pinyin → Spanish    │   │ Activity: Flashcards │
│ Pinyin → English    │   │                      │
│ Hanzi → Spanish     │   │ ○ Flashcards         │
│ Hanzi → English     │   │ ○ Memory Game        │
└─────────────────────┘   └──────────────────────┘
```

### Flashcard Interface
```
Progress: 3/10    Score: 12    Time: 45s

┌─────────────────────────────────────┐
│                                     │
│              你好                   │
│                                     │
│         [Show Answer]               │
└─────────────────────────────────────┘
```

## 🏗️ Architecture

### Core Components

- **`WordEntry`**: Data model for vocabulary entries
- **`ChineseTranslator`**: Handles word translation and processing
- **`GameSession`**: Manages learning sessions and progress
- **`ChineseLearningApp`**: Main application controller

### File Structure
```
chinese-learning-app/
├── chinese_learning_app.py    # Main application file
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── assets/                   # Static assets (images, icons)
└── docs/                    # Additional documentation
```

## 🛠️ Technical Stack

- **Frontend**: Streamlit with custom CSS
- **Backend**: Python with dataclasses
- **Styling**: Modern CSS with gradients and animations
- **State Management**: Streamlit session state
- **Data Processing**: Pandas for word management

## 🔮 Roadmap

### MVP Features (Current)
- [x] Multiple learning modes
- [x] Flashcard system
- [x] Memory matching game
- [x] Progress tracking
- [x] Modern UI design
- [x] Batch word input

### Planned Features
- [ ] **Real Translation APIs**
  - Google Translate integration
  - Azure Translator support
  - Baidu Translate for better Chinese accuracy

- [ ] **Enhanced Learning**
  - Audio pronunciation
  - Character stroke order animation
  - Spaced repetition algorithm
  - Difficulty adjustment based on performance

- [ ] **User Management**
  - User accounts and authentication
  - Progress persistence across sessions
  - Learning analytics and insights
  - Achievement system

- [ ] **Database Integration**
  - PostgreSQL for production
  - User progress tracking
  - Custom vocabulary lists
  - Learning history

- [ ] **Advanced Features**
  - Offline mode support
  - Mobile app version
  - Social features (share progress)
  - Custom study sets

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup

1. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/chinese-learning-app.git
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Run tests**
   ```bash
   python -m pytest tests/
   ```

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include tests for new features
- Update documentation as needed

## 📋 Requirements

### Production Requirements
For a full production deployment, consider:

- **Translation APIs**: Google/Azure/Baidu for accurate translations
- **Database**: PostgreSQL or MongoDB for data persistence
- **Caching**: Redis for translation and session caching
- **Authentication**: JWT-based user management
- **Hosting**: Docker containers with cloud deployment

### Current Dependencies
```txt
streamlit>=1.28.0
pandas>=1.5.0
requests>=2.28.0
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit Team** for the amazing web app framework
- **Chinese Language Community** for inspiration and feedback
- **Open Source Contributors** who help improve this project

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/chinese-learning-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/chinese-learning-app/discussions)
- **Email**: your.email@example.com

---

<div align="center">

**Made with ❤️ for Chinese language learners worldwide**

[⭐ Star this repo](https://github.com/yourusername/chinese-learning-app) | [🐛 Report Bug](https://github.com/yourusername/chinese-learning-app/issues) | [💡 Request Feature](https://github.com/yourusername/chinese-learning-app/issues)

</div>
