#!/usr/bin/env python3
"""
Chinese Learning App - Standalone Python Script
A modern, interactive Chinese vocabulary learning application with flashcards and matching games.

Requirements:
- Python 3.6+
- tkinter (usually comes with Python)

Usage:
    python main.py

Author: Created for Chinese language learning
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys
import os
from pathlib import Path

# Try to import vocabulary from data file, fallback to sample data
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
    from sample_vocabulary import vocabulary_data
except ImportError:
    # Fallback sample data
    vocabulary_data = [
        {"hanzi": "今天", "pinyin": "jīntiān", "english": "today", "spanish": "hoy"},
        {"hanzi": "明天", "pinyin": "míngtiān", "english": "tomorrow", "spanish": "mañana"},
        {"hanzi": "昨天", "pinyin": "zuótiān", "english": "yesterday", "spanish": "ayer"},
        {"hanzi": "水", "pinyin": "shuǐ", "english": "water", "spanish": "agua"},
        {"hanzi": "火", "pinyin": "huǒ", "english": "fire", "spanish": "fuego"},
        {"hanzi": "你好", "pinyin": "nǐ hǎo", "english": "hello", "spanish": "hola"},
        {"hanzi": "谢谢", "pinyin": "xiè xiè", "english": "thank you", "spanish": "gracias"},
        {"hanzi": "再见", "pinyin": "zài jiàn", "english": "goodbye", "spanish": "adiós"},
        {"hanzi": "学习", "pinyin": "xuéxí", "english": "to study", "spanish": "estudiar"},
        {"hanzi": "朋友", "pinyin": "péngyǒu", "english": "friend", "spanish": "amigo"},
        {"hanzi": "吃", "pinyin": "chī", "english": "to eat", "spanish": "comer"},
        {"hanzi": "喝", "pinyin": "hē", "english": "to drink", "spanish": "beber"},
        {"hanzi": "看", "pinyin": "kàn", "english": "to see", "spanish": "ver"},
        {"hanzi": "听", "pinyin": "tīng", "english": "to listen", "spanish": "escuchar"},
        {"hanzi": "说", "pinyin": "shuō", "english": "to speak", "spanish": "hablar"}
    ]

class ChineseLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🇨🇳 Chinese Learning App")
        self.root.geometry("900x700")
        self.root.configure(bg='#f8f9fa')
        
        # App state
        self.vocabulary = vocabulary_data
        self.selected_words = []
        self.current_mode = ""
        self.num_words = 5
        self.current_card_index = 0
        self.score = 0
        self.game_pairs = []
        self.selected_cards = []
        self.matched_pairs = []
        self.game_buttons = []
        self.current_game_mode = ""
        
        # Style configuration
        self.setup_styles()
        
        # Initialize UI
        self.create_main_frame()
        self.show_start_screen()
        
        # Center window
        self.center_window()
    
    def setup_styles(self):
        """Configure ttk styles for modern appearance"""
        style = ttk.Style()
        
        # Configure modern button styles
        style.configure('Primary.TButton',
                       font=('Arial', 12, 'bold'),
                       padding=(20, 10))
        
        style.configure('Success.TButton',
                       font=('Arial', 12, 'bold'),
                       padding=(20, 10))
        
        style.configure('Warning.TButton',
                       font=('Arial', 10),
                       padding=(15, 5))
        
        style.configure('Game.TButton',
                       font=('Arial', 10, 'bold'),
                       padding=(10, 20))
        
        # Configure label styles
        style.configure('Title.TLabel',
                       font=('Arial', 24, 'bold'),
                       background='#f8f9fa',
                       foreground='#2c3e50')
        
        style.configure('Heading.TLabel',
                       font=('Arial', 14, 'bold'),
                       background='#f8f9fa',
                       foreground='#2c3e50')
        
        style.configure('Card.TLabel',
                       font=('Arial', 16),
                       background='#ffffff',
                       foreground='#2c3e50',
                       padding=20)
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_main_frame(self):
        """Create the main container frame"""
        self.main_frame = tk.Frame(self.root, bg='#f8f9fa', padx=40, pady=30)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
    
    def clear_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_start_screen(self):
        """Display the initial configuration screen"""
        self.clear_frame()
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                               text="🇨🇳 Chinese Learning App",
                               style='Title.TLabel')
        title_label.pack(pady=(0, 40))
        
        # Mode selection
        mode_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        mode_frame.pack(pady=20)
        
        ttk.Label(mode_frame, text="Choose Learning Mode:", 
                 style='Heading.TLabel').pack(pady=(0, 10))
        
        self.mode_var = tk.StringVar(value="pinyin-hanzi")
        mode_options = [
            ("Pinyin → Hanzi", "pinyin-hanzi"),
            ("Pinyin → Spanish", "pinyin-spanish"),
            ("Pinyin → English", "pinyin-english"),
            ("Hanzi → Spanish", "hanzi-spanish"),
            ("Hanzi → English", "hanzi-english")
        ]
        
        for text, value in mode_options:
            ttk.Radiobutton(mode_frame, text=text, variable=self.mode_var, 
                           value=value, style='TRadiobutton').pack(anchor=tk.W, pady=2)
        
        # Word count selection
        words_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        words_frame.pack(pady=30)
        
        ttk.Label(words_frame, text="Number of Words:", 
                 style='Heading.TLabel').pack(pady=(0, 10))
        
        self.words_var = tk.IntVar(value=5)
        words_scale = tk.Scale(words_frame, from_=3, to=min(15, len(self.vocabulary)),
                              orient=tk.HORIZONTAL, variable=self.words_var,
                              length=300, font=('Arial', 12),
                              bg='#f8f9fa', fg='#2c3e50',
                              activebackground='#667eea')
        words_scale.pack()
        
        # Current value display
        self.words_label = ttk.Label(words_frame, text=f"Selected: {self.words_var.get()} words")
        self.words_label.pack(pady=(10, 0))
        words_scale.configure(command=self.update_words_label)
        
        # Buttons
        button_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        button_frame.pack(pady=40)
        
        flashcard_btn = ttk.Button(button_frame, text="📚 Start Flashcards",
                                  command=self.start_flashcards,
                                  style='Primary.TButton')
        flashcard_btn.pack(side=tk.LEFT, padx=20)
        
        game_btn = ttk.Button(button_frame, text="🎮 Start Matching Game",
                             command=self.start_matching_game,
                             style='Success.TButton')
        game_btn.pack(side=tk.LEFT, padx=20)
        
        # Info footer
        info_label = ttk.Label(self.main_frame, 
                              text=f"📚 {len(self.vocabulary)} words available for learning",
                              font=('Arial', 10), foreground='#7f8c8d', background='#f8f9fa')
        info_label.pack(side=tk.BOTTOM, pady=(40, 0))
    
    def update_words_label(self, value):
        """Update the words count label"""
        self.words_label.config(text=f"Selected: {value} words")
    
    def prepare_words(self):
        """Prepare the selected words based on user preferences"""
        self.current_mode = self.mode_var.get()
        self.num_words = self.words_var.get()
        self.selected_words = random.sample(self.vocabulary, 
                                          min(self.num_words, len(self.vocabulary)))
        self.current_card_index = 0
        self.score = 0
    
    def get_question_answer(self, word):
        """Get question and answer based on selected mode"""
        mode_map = {
            "pinyin-hanzi": (word["pinyin"], word["hanzi"]),
            "pinyin-spanish": (word["pinyin"], word["spanish"]),
            "pinyin-english": (word["pinyin"], word["english"]),
            "hanzi-spanish": (word["hanzi"], word["spanish"]),
            "hanzi-english": (word["hanzi"], word["english"])
        }
        return mode_map.get(self.current_mode, (word["pinyin"], word["hanzi"]))
    
    def start_flashcards(self):
        """Start flashcard learning mode"""
        self.current_game_mode = "flashcards"
        self.prepare_words()
        self.show_flashcard()
    
    def show_flashcard(self):
        """Display current flashcard"""
        if self.current_card_index >= len(self.selected_words):
            self.show_flashcard_results()
            return
        
        self.clear_frame()
        
        word = self.selected_words[self.current_card_index]
        question, answer = self.get_question_answer(word)
        
        # Progress section
        progress_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        progress_frame.pack(fill=tk.X, pady=(0, 30))
        
        progress_text = f"Flashcard {self.current_card_index + 1} of {len(self.selected_words)}"
        ttk.Label(progress_frame, text=progress_text, style='Heading.TLabel').pack()
        
        # Progress bar
        progress_bar_frame = tk.Frame(progress_frame, bg='#ecf0f1', height=10)
        progress_bar_frame.pack(fill=tk.X, pady=(10, 0))
        progress_bar_frame.pack_propagate(False)
        
        progress_width = int((self.current_card_index + 1) / len(self.selected_words) * 100)
        progress_fill = tk.Frame(progress_bar_frame, bg='#667eea', height=10)
        progress_fill.place(relwidth=progress_width/100, relheight=1)
        
        # Card frame with modern styling
        card_frame = tk.Frame(self.main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
        card_frame.pack(pady=30, padx=50, fill=tk.BOTH, expand=True)
        
        # Mode display
        mode_text = self.current_mode.replace('-', ' → ').title()
        ttk.Label(card_frame, text=f"Mode: {mode_text}",
                 font=('Arial', 12), foreground='#7f8c8d', background='#ffffff').pack(pady=(20, 0))
        
        # Question
        question_label = tk.Label(card_frame, text=question,
                                 font=('Arial', 32, 'bold'),
                                 bg='#ffffff', fg='#2c3e50')
        question_label.pack(pady=40)
        
        # Answer (initially hidden)
        self.answer_frame = tk.Frame(card_frame, bg='#ffffff')
        self.answer_frame.pack(pady=(20, 40))
        
        separator = tk.Frame(self.answer_frame, bg='#ecf0f1', height=2)
        separator.pack(fill=tk.X, pady=(0, 20))
        
        self.answer_label = tk.Label(self.answer_frame, text=answer,
                                    font=('Arial', 24),
                                    bg='#ffffff', fg='#27ae60')
        
        # Initially hide answer
        self.answer_shown = False
        
        # Buttons
        button_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        button_frame.pack(pady=20)
        
        show_btn = ttk.Button(button_frame, text="Show Answer",
                             command=self.show_answer)
        show_btn.pack(side=tk.LEFT, padx=10)
        
        correct_btn = ttk.Button(button_frame, text="✓ Correct",
                               command=lambda: self.answer_flashcard(True),
                               style='Success.TButton')
        correct_btn.pack(side=tk.LEFT, padx=10)
        
        incorrect_btn = ttk.Button(button_frame, text="✗ Incorrect",
                                 command=lambda: self.answer_flashcard(False))
        incorrect_btn.pack(side=tk.LEFT, padx=10)
        
        # Back button
        back_btn = ttk.Button(self.main_frame, text="← Back to Menu",
                             command=self.show_start_screen,
                             style='Warning.TButton')
        back_btn.pack(pady=(20, 0))
    
    def show_answer(self):
        """Show the answer on the flashcard"""
        if not self.answer_shown:
            self.answer_label.pack()
            self.answer_shown = True
    
    def answer_flashcard(self, correct):
        """Process flashcard answer and move to next"""
        if correct:
            self.score += 1
        self.current_card_index += 1
        self.show_flashcard()
    
    def show_flashcard_results(self):
        """Show flashcard session results"""
        self.clear_frame()
        
        percentage = (self.score / len(self.selected_words)) * 100
        
        # Results frame
        results_frame = tk.Frame(self.main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
        results_frame.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(results_frame, text="📊 Flashcard Results",
                 font=('Arial', 24, 'bold'), background='#ffffff',
                 foreground='#2c3e50').pack(pady=(40, 20))
        
        # Emoji
        emoji_label = tk.Label(results_frame, text="🎉",
                              font=('Arial', 48), bg='#ffffff')
        emoji_label.pack(pady=20)
        
        # Score
        score_text = f"Score: {self.score}/{len(self.selected_words)}"
        tk.Label(results_frame, text=score_text,
                font=('Arial', 20, 'bold'), bg='#ffffff', fg='#27ae60').pack(pady=10)
        
        # Accuracy
        accuracy_text = f"Accuracy: {percentage:.1f}%"
        tk.Label(results_frame, text=accuracy_text,
                font=('Arial', 16), bg='#ffffff', fg='#2c3e50').pack(pady=10)
        
        # Performance message
        if percentage >= 90:
            message = "Excellent work! 🌟"
            color = '#27ae60'
        elif percentage >= 70:
            message = "Good job! Keep practicing! 👍"
            color = '#f39c12'
        else:
            message = "Keep studying! You'll improve! 💪"
            color = '#e74c3c'
        
        tk.Label(results_frame, text=message,
                font=('Arial', 14), bg='#ffffff', fg=color).pack(pady=(20, 40))
        
        # Buttons
        button_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        button_frame.pack(pady=30)
        
        retry_btn = ttk.Button(button_frame, text="🔄 Try Again",
                              command=self.start_flashcards,
                              style='Primary.TButton')
        retry_btn.pack(side=tk.LEFT, padx=20)
        
        menu_btn = ttk.Button(button_frame, text="🏠 Main Menu",
                             command=self.show_start_screen,
                             style='Success.TButton')
        menu_btn.pack(side=tk.LEFT, padx=20)
    
    def start_matching_game(self):
        """Start the matching pairs game"""
        self.current_game_mode = "matching"
        self.prepare_words()
        self.setup_matching_game()
        self.show_matching_game()
    
    def setup_matching_game(self):
        """Setup the matching game pairs"""
        self.game_pairs = []
        self.matched_pairs = []
        self.selected_cards = []
        
        for word in self.selected_words:
            question, answer = self.get_question_answer(word)
            self.game_pairs.extend([
                {"text": question, "pair_id": len(self.game_pairs) // 2, "type": "question"},
                {"text": answer, "pair_id": len(self.game_pairs) // 2, "type": "answer"}
            ])
        
        random.shuffle(self.game_pairs)
    
    def show_matching_game(self):
        """Display the matching game"""
        self.clear_frame()
        
        # Header
        header_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        ttk.Label(header_frame, text="🎮 Matching Game", style='Title.TLabel').pack()
        
        # Score display
        score_text = f"Score: {self.score} | Pairs Found: {len(self.matched_pairs)}/{len(self.selected_words)}"
        ttk.Label(header_frame, text=score_text,
                 font=('Arial', 14, 'bold'), background='#f8f9fa',
                 foreground='#27ae60').pack(pady=10)
        
        mode_text = self.current_mode.replace('-', ' with ').title()
        ttk.Label(header_frame, text=f"Click two cards to match {mode_text}",
                 font=('Arial', 12), background='#f8f9fa',
                 foreground='#7f8c8d').pack()
        
        # Game grid
        game_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        game_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Calculate grid dimensions
        total_cards = len(self.game_pairs)
        cols = 4 if total_cards <= 12 else 5
        rows = (total_cards + cols - 1) // cols
        
        self.game_buttons = []
        for i, pair in enumerate(self.game_pairs):
            row = i // cols
            col = i % cols
            
            btn = tk.Button(game_frame, text=pair["text"],
                           font=('Arial', 10, 'bold'),
                           bg='#667eea', fg='white',
                           activebackground='#5a6fd8',
                           width=15, height=3,
                           command=lambda idx=i: self.card_clicked(idx))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            
            # Store pair info
            btn.pair_info = pair
            btn.index = i
            self.game_buttons.append(btn)
        
        # Configure grid weights for responsive layout
        for i in range(cols):
            game_frame.grid_columnconfigure(i, weight=1)
        for i in range(rows):
            game_frame.grid_rowconfigure(i, weight=1)
        
        # Back button
        back_btn = ttk.Button(self.main_frame, text="← Back to Menu",
                             command=self.show_start_screen,
                             style='Warning.TButton')
        back_btn.pack(pady=(30, 0))
    
    def card_clicked(self, index):
        """Handle card click in matching game"""
        btn = self.game_buttons[index]
        
        # Ignore if card already matched or already selected
        if index in self.matched_pairs or btn in self.selected_cards:
            return
        
        # Add to selected cards
        self.selected_cards.append(btn)
        btn.configure(bg='#4facfe', activebackground='#3d8bfe')  # Highlight selected
        
        # Check if we have 2 selected cards
        if len(self.selected_cards) == 2:
            self.root.after(500, self.check_match)  # Delay for visual feedback
    
    def check_match(self):
        """Check if selected cards match"""
        card1, card2 = self.selected_cards
        
        if card1.pair_info["pair_id"] == card2.pair_info["pair_id"]:
            # Match found!
            self.score += 10
            self.matched_pairs.extend([card1.index, card2.index])
            
            # Update button appearance
            card1.configure(bg='#27ae60', activebackground='#229954', state='disabled')
            card2.configure(bg='#27ae60', activebackground='#229954', state='disabled')
            
            # Check if game complete
            if len(self.matched_pairs) == len(self.game_pairs):
                self.root.after(1000, self.show_game_results)
            else:
                # Update score display
                self.show_matching_game()
        else:
            # No match - reset buttons
            card1.configure(bg='#667eea', activebackground='#5a6fd8')
            card2.configure(bg='#667eea', activebackground='#5a6fd8')
        
        self.selected_cards = []
    
    def show_game_results(self):
        """Show matching game results"""
        self.clear_frame()
        
        # Results frame
        results_frame = tk.Frame(self.main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
        results_frame.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(results_frame, text="🎉 Game Complete!",
                 font=('Arial', 24, 'bold'), background='#ffffff',
                 foreground='#2c3e50').pack(pady=(40, 20))
        
        # Trophy
        trophy_label = tk.Label(results_frame, text="🏆",
                               font=('Arial', 48), bg='#ffffff')
        trophy_label.pack(pady=20)
        
        # Score
        score_text = f"Final Score: {self.score}"
        tk.Label(results_frame, text=score_text,
                font=('Arial', 20, 'bold'), bg='#ffffff', fg='#e67e22').pack(pady=10)
        
        # Achievement
        achievement_text = f"All {len(self.selected_words)} pairs matched!"
        tk.Label(results_frame, text=achievement_text,
                font=('Arial', 16), bg='#ffffff', fg='#2c3e50').pack(pady=10)
        
        # Congratulations
        tk.Label(results_frame, text="Excellent work! 🌟",
                font=('Arial', 14), bg='#ffffff', fg='#27ae60').pack(pady=(20, 40))
        
        # Buttons
        button_frame = tk.Frame(self.main_frame, bg='#f8f9fa')
        button_frame.pack(pady=30)
        
        play_again_btn = ttk.Button(button_frame, text="🎮 Play Again",
                                   command=self.start_matching_game,
                                   style='Primary.TButton')
        play_again_btn.pack(side=tk.LEFT, padx=20)
        
        menu_btn = ttk.Button(button_frame, text="🏠 Main Menu",
                             command=self.show_start_screen,
                             style='Success.TButton')
        menu_btn.pack(side=tk.LEFT, padx=20)

def main():
    """Main function to run the application"""
    print("🚀 Starting Chinese Learning App...")
    print(f"📚 Loaded {len(vocabulary_data)} words")
    
    # Create and configure the main window
    root = tk.Tk()
    
    # Set window icon (if available)
    try:
        # You can add an icon file here
        # root.iconbitmap('icon.ico')
        pass
    except:
        pass
    
    # Initialize the app
    app = ChineseLearningApp(root)
    
    print("🎨 UI ready!")
    print("🎉 App started! Enjoy learning Chinese!")
    
    # Start the GUI event loop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n👋 Thanks for using Chinese Learning App!")
        root.quit()

if __name__ == "__main__":
    main()