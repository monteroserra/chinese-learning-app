"""
utils.py - Helper functions and utilities for Chinese Learning App
Contains all the game logic, UI components, and utility functions.
"""

import tkinter as tk
from tkinter import ttk
import random
import sys
import os

# Try to import vocabulary from data file, fallback to sample data
def load_vocabulary():
    """Load vocabulary data from file or use fallback data"""
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
        from sample_vocabulary import vocabulary_data
        return vocabulary_data
    except ImportError:
        # Fallback sample data
        return [
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

def setup_styles():
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
    
    # Configure label styles
    style.configure('Title.TLabel',
                   font=('Arial', 24, 'bold'),
                   background='#f8f9fa',
                   foreground='#2c3e50')
    
    style.configure('Heading.TLabel',
                   font=('Arial', 14, 'bold'),
                   background='#f8f9fa',
                   foreground='#2c3e50')

def center_window(root):
    """Center the window on screen"""
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

def clear_frame(frame):
    """Clear all widgets from frame"""
    for widget in frame.winfo_children():
        widget.destroy()

def get_learning_modes():
    """Return available learning modes"""
    return [
        ("Pinyin → Hanzi", "pinyin-hanzi"),
        ("Pinyin → Spanish", "pinyin-spanish"),
        ("Pinyin → English", "pinyin-english"),
        ("Hanzi → Spanish", "hanzi-spanish"),
        ("Hanzi → English", "hanzi-english"),
        ("Hanzi + Pinyin → Spanish", "hanzi+pinyin-spanish"),
        ("Hanzi + Pinyin → English", "hanzi+pinyin-english")
    ]

def get_question_answer(word, mode):
    """Get question and answer based on selected mode"""
    mode_map = {
        "pinyin-hanzi": (word["pinyin"], word["hanzi"]),
        "pinyin-spanish": (word["pinyin"], word["spanish"]),
        "pinyin-english": (word["pinyin"], word["english"]),
        "hanzi-spanish": (word["hanzi"], word["spanish"]),
        "hanzi-english": (word["hanzi"], word["english"]),
        "hanzi+pinyin-spanish": (f"{word['hanzi']} ({word['pinyin']})", word["spanish"]),
        "hanzi+pinyin-english": (f"{word['hanzi']} ({word['pinyin']})", word["english"])
    }
    return mode_map.get(mode, (word["pinyin"], word["hanzi"]))

def prepare_words(vocabulary, mode_var, words_var):
    """Prepare the selected words based on user preferences"""
    current_mode = mode_var.get()
    num_words = words_var.get()
    selected_words = random.sample(vocabulary, min(num_words, len(vocabulary)))
    return current_mode, selected_words

def update_words_label(words_label, value):
    """Update the words count label"""
    words_label.config(text=f"Selected: {value} words")

def create_start_screen(main_frame, vocabulary, mode_var, words_var, 
                       start_flashcards_callback, start_game_callback):
    """Create and display the start screen"""
    clear_frame(main_frame)
    
    # Title
    title_label = ttk.Label(main_frame, 
                           text="🇨🇳 Chinese Learning App",
                           style='Title.TLabel')
    title_label.pack(pady=(0, 40))
    
    # Mode selection
    mode_frame = tk.Frame(main_frame, bg='#f8f9fa')
    mode_frame.pack(pady=20)
    
    ttk.Label(mode_frame, text="Choose Learning Mode:", 
             style='Heading.TLabel').pack(pady=(0, 10))
    
    mode_options = get_learning_modes()
    for text, value in mode_options:
        ttk.Radiobutton(mode_frame, text=text, variable=mode_var, 
                       value=value, style='TRadiobutton').pack(anchor=tk.W, pady=2)
    
    # Word count selection
    words_frame = tk.Frame(main_frame, bg='#f8f9fa')
    words_frame.pack(pady=30)
    
    ttk.Label(words_frame, text="Number of Words:", 
             style='Heading.TLabel').pack(pady=(0, 10))
    
    words_scale = tk.Scale(words_frame, from_=3, to=min(15, len(vocabulary)),
                          orient=tk.HORIZONTAL, variable=words_var,
                          length=300, font=('Arial', 12),
                          bg='#f8f9fa', fg='#2c3e50',
                          activebackground='#667eea')
    words_scale.pack()
    
    # Current value display
    words_label = ttk.Label(words_frame, text=f"Selected: {words_var.get()} words")
    words_label.pack(pady=(10, 0))
    words_scale.configure(command=lambda v: update_words_label(words_label, v))
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg='#f8f9fa')
    button_frame.pack(pady=40)
    
    flashcard_btn = ttk.Button(button_frame, text="📚 Start Flashcards",
                              command=start_flashcards_callback,
                              style='Primary.TButton')
    flashcard_btn.pack(side=tk.LEFT, padx=20)
    
    game_btn = ttk.Button(button_frame, text="🎮 Start Matching Game",
                         command=start_game_callback,
                         style='Success.TButton')
    game_btn.pack(side=tk.LEFT, padx=20)
    
    # Info footer
    info_label = ttk.Label(main_frame, 
                          text=f"📚 {len(vocabulary)} words available for learning",
                          font=('Arial', 10), foreground='#7f8c8d', background='#f8f9fa')
    info_label.pack(side=tk.BOTTOM, pady=(40, 0))

def create_flashcard_screen(main_frame, word, current_mode, current_index, total_cards,
                           show_answer_callback, next_card_callback, back_callback):
    """Create and display a flashcard"""
    clear_frame(main_frame)
    
    question, answer = get_question_answer(word, current_mode)
    
    # Progress section
    progress_frame = tk.Frame(main_frame, bg='#f8f9fa')
    progress_frame.pack(fill=tk.X, pady=(0, 30))
    
    progress_text = f"Flashcard {current_index + 1} of {total_cards}"
    ttk.Label(progress_frame, text=progress_text, style='Heading.TLabel').pack()
    
    # Progress bar
    progress_bar_frame = tk.Frame(progress_frame, bg='#ecf0f1', height=10)
    progress_bar_frame.pack(fill=tk.X, pady=(10, 0))
    progress_bar_frame.pack_propagate(False)
    
    progress_width = int((current_index + 1) / total_cards * 100)
    progress_fill = tk.Frame(progress_bar_frame, bg='#667eea', height=10)
    progress_fill.place(relwidth=progress_width/100, relheight=1)
    
    # Card frame with modern styling
    card_frame = tk.Frame(main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
    card_frame.pack(pady=30, padx=50, fill=tk.BOTH, expand=True)
    
    # Mode display
    mode_text = current_mode.replace('-', ' → ').replace('+', ' + ').title()
    ttk.Label(card_frame, text=f"Mode: {mode_text}",
             font=('Arial', 12), foreground='#7f8c8d', background='#ffffff').pack(pady=(20, 0))
    
    # Question
    question_label = tk.Label(card_frame, text=question,
                             font=('Arial', 28, 'bold'),
                             bg='#ffffff', fg='#2c3e50',
                             wraplength=600)
    question_label.pack(pady=40)
    
    # Answer (initially hidden)
    answer_frame = tk.Frame(card_frame, bg='#ffffff')
    answer_frame.pack(pady=(20, 40))
    
    separator = tk.Frame(answer_frame, bg='#ecf0f1', height=2)
    separator.pack(fill=tk.X, pady=(0, 20))
    
    answer_label = tk.Label(answer_frame, text=answer,
                           font=('Arial', 20),
                           bg='#ffffff', fg='#27ae60',
                           wraplength=500)
    
    # Store references for show_answer callback
    answer_frame.answer_label = answer_label
    answer_frame.answer_shown = False
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg='#f8f9fa')
    button_frame.pack(pady=20)
    
    show_btn = ttk.Button(button_frame, text="Show Answer",
                         command=lambda: show_answer_callback(answer_frame))
    show_btn.pack(side=tk.LEFT, padx=20)
    
    next_btn = ttk.Button(button_frame, text="Next →",
                         command=next_card_callback,
                         style='Success.TButton')
    next_btn.pack(side=tk.LEFT, padx=20)
    
    # Back button
    back_btn = ttk.Button(main_frame, text="← Back to Menu",
                         command=back_callback,
                         style='Warning.TButton')
    back_btn.pack(pady=(20, 0))

def show_flashcard_answer(answer_frame):
    """Show the answer on the flashcard"""
    if not answer_frame.answer_shown:
        answer_frame.answer_label.pack()
        answer_frame.answer_shown = True

def create_flashcard_results(main_frame, total_cards, retry_callback, menu_callback):
    """Show flashcard session completion"""
    clear_frame(main_frame)
    
    # Results frame
    results_frame = tk.Frame(main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
    results_frame.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
    
    # Title
    ttk.Label(results_frame, text="📚 Flashcards Complete!",
             font=('Arial', 24, 'bold'), background='#ffffff',
             foreground='#2c3e50').pack(pady=(40, 20))
    
    # Emoji
    emoji_label = tk.Label(results_frame, text="🎉",
                          font=('Arial', 48), bg='#ffffff')
    emoji_label.pack(pady=20)
    
    # Completion message
    completion_text = f"You reviewed {total_cards} words!"
    tk.Label(results_frame, text=completion_text,
            font=('Arial', 18), bg='#ffffff', fg='#2c3e50').pack(pady=10)
    
    # Encouragement message
    tk.Label(results_frame, text="Great job studying! 🌟",
            font=('Arial', 16), bg='#ffffff', fg='#27ae60').pack(pady=(20, 40))
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg='#f8f9fa')
    button_frame.pack(pady=30)
    
    retry_btn = ttk.Button(button_frame, text="🔄 Study Again",
                          command=retry_callback,
                          style='Primary.TButton')
    retry_btn.pack(side=tk.LEFT, padx=20)
    
    menu_btn = ttk.Button(button_frame, text="🏠 Main Menu",
                         command=menu_callback,
                         style='Success.TButton')
    menu_btn.pack(side=tk.LEFT, padx=20)

def setup_matching_game(selected_words, current_mode):
    """Setup the matching game pairs"""
    game_pairs = []
    
    for word in selected_words:
        question, answer = get_question_answer(word, current_mode)
        game_pairs.extend([
            {"text": question, "pair_id": len(game_pairs) // 2, "type": "question"},
            {"text": answer, "pair_id": len(game_pairs) // 2, "type": "answer"}
        ])
    
    random.shuffle(game_pairs)
    return game_pairs

def create_matching_game_screen(main_frame, game_pairs, current_mode, score, matched_pairs,
                               selected_words, card_click_callback, back_callback):
    """Display the matching game"""
    clear_frame(main_frame)
    
    # Header
    header_frame = tk.Frame(main_frame, bg='#f8f9fa')
    header_frame.pack(fill=tk.X, pady=(0, 30))
    
    ttk.Label(header_frame, text="🎮 Matching Game", style='Title.TLabel').pack()
    
    # Score display
    score_text = f"Score: {score} | Pairs Found: {len(matched_pairs)}/{len(selected_words)}"
    ttk.Label(header_frame, text=score_text,
             font=('Arial', 14, 'bold'), background='#f8f9fa',
             foreground='#27ae60').pack(pady=10)
    
    mode_text = current_mode.replace('-', ' with ').replace('+', ' + ').title()
    ttk.Label(header_frame, text=f"Click two cards to match {mode_text}",
             font=('Arial', 12), background='#f8f9fa',
             foreground='#7f8c8d').pack()
    
    # Game grid
    game_frame = tk.Frame(main_frame, bg='#f8f9fa')
    game_frame.pack(fill=tk.BOTH, expand=True, pady=20)
    
    # Calculate grid dimensions
    total_cards = len(game_pairs)
    cols = 4 if total_cards <= 12 else 5
    rows = (total_cards + cols - 1) // cols
    
    game_buttons = []
    for i, pair in enumerate(game_pairs):
        row = i // cols
        col = i % cols
        
        btn = tk.Button(game_frame, text=pair["text"],
                       font=('Arial', 9, 'bold'),
                       bg='#667eea', fg='white',
                       activebackground='#5a6fd8',
                       width=12, height=3,
                       wraplength=100,
                       command=lambda idx=i: card_click_callback(idx))
        btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        # Store pair info
        btn.pair_info = pair
        btn.index = i
        game_buttons.append(btn)
    
    # Configure grid weights for responsive layout
    for i in range(cols):
        game_frame.grid_columnconfigure(i, weight=1)
    for i in range(rows):
        game_frame.grid_rowconfigure(i, weight=1)
    
    # Back button
    back_btn = ttk.Button(main_frame, text="← Back to Menu",
                         command=back_callback,
                         style='Warning.TButton')
    back_btn.pack(pady=(30, 0))
    
    return game_buttons

def create_game_results(main_frame, score, selected_words, play_again_callback, menu_callback):
    """Show matching game results"""
    clear_frame(main_frame)
    
    # Results frame
    results_frame = tk.Frame(main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
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
    score_text = f"Final Score: {score}"
    tk.Label(results_frame, text=score_text,
            font=('Arial', 20, 'bold'), bg='#ffffff', fg='#e67e22').pack(pady=10)
    
    # Achievement
    achievement_text = f"All {len(selected_words)} pairs matched!"
    tk.Label(results_frame, text=achievement_text,
            font=('Arial', 16), bg='#ffffff', fg='#2c3e50').pack(pady=10)
    
    # Congratulations
    tk.Label(results_frame, text="Excellent work! 🌟",
            font=('Arial', 14), bg='#ffffff', fg='#27ae60').pack(pady=(20, 40))
    
    # Buttons
    button_frame = tk.Frame(main_frame, bg='#f8f9fa')
    button_frame.pack(pady=30)
    
    play_again_btn = ttk.Button(button_frame, text="🎮 Play Again",
                               command=play_again_callback,
                               style='Primary.TButton')
    play_again_btn.pack(side=tk.LEFT, padx=20)
    
    menu_btn = ttk.Button(button_frame, text="🏠 Main Menu",
                         command=menu_callback,
                         style='Success.TButton')
    menu_btn.pack(side=tk.LEFT, padx=20)