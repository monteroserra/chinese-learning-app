"""
utils.py - Ultra-Enhanced Helper functions with stunning UI for Chinese Learning App
Contains all the game logic, UI components, and utility functions with beautiful modern styling.
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
    """Configure ultra-enhanced ttk styles for stunning appearance"""
    style = ttk.Style()
    
    # Set theme
    try:
        style.theme_use('clam')
    except:
        pass
    
    # Ultra-enhanced button styles
    style.configure('Primary.TButton',
                   font=('Segoe UI', 16, 'bold'),
                   padding=(30, 18),
                   relief='flat',
                   borderwidth=0,
                   focuscolor='none')
    
    style.map('Primary.TButton',
              background=[('active', '#4c1d95'),
                         ('pressed', '#3730a3'),
                         ('!active', '#5b21b6')])
    
    style.configure('Success.TButton',
                   font=('Segoe UI', 16, 'bold'),
                   padding=(30, 18),
                   relief='flat',
                   borderwidth=0,
                   focuscolor='none')
    
    style.map('Success.TButton',
              background=[('active', '#059669'),
                         ('pressed', '#047857'),
                         ('!active', '#0d9488')])

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

def create_gradient_label(parent, text, font_size=24, fg_color='#1f2937', bg_start='#f3f4f6', bg_end='#e5e7eb'):
    """Create a label with gradient-like background effect"""
    frame = tk.Frame(parent, bg=bg_start)
    label = tk.Label(frame, text=text, font=('Segoe UI', font_size, 'bold'),
                    fg=fg_color, bg=bg_start)
    label.pack(pady=10, padx=20)
    return frame

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
    """Create and display the compact stunning start screen"""
    clear_frame(main_frame)
    
    # Create main container with beautiful gradient background
    container = tk.Frame(main_frame, bg='#0f172a')
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Compact header section
    header_frame = tk.Frame(container, bg='#1e293b', height=80)
    header_frame.pack(fill=tk.X, pady=(0, 15))
    header_frame.pack_propagate(False)
    
    # Compact title with beautiful styling
    title_label = tk.Label(header_frame, 
                          text="🇨🇳 Chinese Learning App",
                          font=('Segoe UI', 28, 'bold'),
                          bg='#1e293b',
                          fg='#f8fafc')
    title_label.pack(pady=(15, 5))
    
    subtitle_label = tk.Label(header_frame,
                             text="Master Chinese vocabulary through interactive learning",
                             font=('Segoe UI', 12),
                             bg='#1e293b',
                             fg='#94a3b8')
    subtitle_label.pack()
    
    # Create scrollable content area to ensure everything fits
    canvas = tk.Canvas(container, bg='#0f172a', highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#0f172a')
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Mode selection card with compact styling
    mode_card = tk.Frame(scrollable_frame, bg='#1e293b', relief=tk.RAISED, bd=1)
    mode_card.pack(pady=10, padx=20, fill=tk.X)
    
    mode_title = tk.Label(mode_card, 
                         text="🎯 Choose Learning Mode",
                         font=('Segoe UI', 16, 'bold'),
                         bg='#1e293b',
                         fg='#f8fafc')
    mode_title.pack(pady=(15, 10))
    
    # Compact mode selection in two columns
    mode_options = get_learning_modes()
    
    # Create two columns for mode options
    modes_container = tk.Frame(mode_card, bg='#1e293b')
    modes_container.pack(padx=15, pady=(0, 15))
    
    left_col = tk.Frame(modes_container, bg='#1e293b')
    left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
    
    right_col = tk.Frame(modes_container, bg='#1e293b')
    right_col.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
    
    for i, (text, value) in enumerate(mode_options):
        parent_col = left_col if i < 4 else right_col
        
        radio_btn = tk.Radiobutton(parent_col, 
                                  text=text, 
                                  variable=mode_var, 
                                  value=value,
                                  font=('Segoe UI', 11),
                                  bg='#1e293b',
                                  fg='#e2e8f0',
                                  activebackground='#334155',
                                  activeforeground='#f1f5f9',
                                  selectcolor='#5b21b6',
                                  bd=0,
                                  highlightthickness=0)
        radio_btn.pack(anchor=tk.W, pady=2, padx=10)
    
    # Compact word count card
    words_card = tk.Frame(scrollable_frame, bg='#1e293b', relief=tk.RAISED, bd=1)
    words_card.pack(pady=10, padx=20, fill=tk.X)
    
    words_title = tk.Label(words_card, 
                          text="📊 Number of Words",
                          font=('Segoe UI', 16, 'bold'),
                          bg='#1e293b',
                          fg='#f8fafc')
    words_title.pack(pady=(15, 10))
    
    # Compact scale
    scale_frame = tk.Frame(words_card, bg='#1e293b')
    scale_frame.pack(pady=5)
    
    words_scale = tk.Scale(scale_frame, 
                          from_=3, 
                          to=min(15, len(vocabulary)),
                          orient=tk.HORIZONTAL, 
                          variable=words_var,
                          length=300, 
                          font=('Segoe UI', 11),
                          bg='#1e293b', 
                          fg='#e2e8f0',
                          activebackground='#5b21b6',
                          troughcolor='#334155',
                          highlightthickness=0,
                          bd=0)
    words_scale.pack()
    
    # Compact value display
    words_label = tk.Label(words_card, 
                          text=f"Selected: {words_var.get()} words",
                          font=('Segoe UI', 12, 'bold'),
                          bg='#1e293b',
                          fg='#5b21b6')
    words_label.pack(pady=(5, 15))
    words_scale.configure(command=lambda v: update_words_label(words_label, v))
    
    # Compact action buttons
    button_frame = tk.Frame(scrollable_frame, bg='#0f172a')
    button_frame.pack(pady=20)
    
    # Compact flashcards button
    flashcard_btn = tk.Button(button_frame, 
                             text="📚 Start Flashcards",
                             command=start_flashcards_callback,
                             font=('Segoe UI', 14, 'bold'),
                             bg='#5b21b6',
                             fg='white',
                             activebackground='#4c1d95',
                             activeforeground='white',
                             relief=tk.FLAT,
                             bd=0,
                             padx=25,
                             pady=12,
                             cursor='hand2')
    flashcard_btn.pack(side=tk.LEFT, padx=15)
    
    # Compact matching game button
    game_btn = tk.Button(button_frame, 
                        text="🎮 Start Matching Game",
                        command=start_game_callback,
                        font=('Segoe UI', 14, 'bold'),
                        bg='#0d9488',
                        fg='white',
                        activebackground='#0f766e',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=25,
                        pady=12,
                        cursor='hand2')
    game_btn.pack(side=tk.LEFT, padx=15)
    
    # Compact info footer
    info_frame = tk.Frame(scrollable_frame, bg='#334155', relief=tk.FLAT, bd=0)
    info_frame.pack(fill=tk.X, pady=(15, 0), padx=20)
    
    info_label = tk.Label(info_frame, 
                         text=f"📚 {len(vocabulary)} words • 🎯 7 modes • 🚀 Interactive learning",
                         font=('Segoe UI', 10),
                         bg='#334155',
                         fg='#cbd5e1')
    info_label.pack(pady=12)
    
    # Bind mousewheel to canvas for scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

def create_flashcard_screen(main_frame, word, current_mode, current_index, total_cards,
                           show_answer_callback, next_card_callback, back_callback):
    """Create and display an ultra-beautiful flashcard"""
    clear_frame(main_frame)
    
    # Stunning main container
    container = tk.Frame(main_frame, bg='#0f172a')
    container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
    
    question, answer = get_question_answer(word, current_mode)
    
    # Beautiful progress section
    progress_frame = tk.Frame(container, bg='#1e293b', height=120)
    progress_frame.pack(fill=tk.X, pady=0)
    progress_frame.pack_propagate(False)
    
    progress_text = f"Flashcard {current_index + 1} of {total_cards}"
    progress_label = tk.Label(progress_frame, 
                             text=progress_text,
                             font=('Segoe UI', 20, 'bold'),
                             bg='#1e293b',
                             fg='#f8fafc')
    progress_label.pack(pady=(25, 10))
    
    # Stunning progress bar
    progress_container = tk.Frame(progress_frame, bg='#334155', height=12, relief=tk.FLAT)
    progress_container.pack(fill=tk.X, padx=60, pady=(0, 25))
    progress_container.pack_propagate(False)
    
    progress_width = (current_index + 1) / total_cards
    progress_fill = tk.Frame(progress_container, bg='#5b21b6', height=12)
    progress_fill.place(relwidth=progress_width, relheight=1)
    
    # Content area
    content_area = tk.Frame(container, bg='#0f172a')
    content_area.pack(fill=tk.BOTH, expand=True, padx=50, pady=30)
    
    # Spectacular card frame
    card_frame = tk.Frame(content_area, bg='#1e293b', relief=tk.FLAT, bd=0)
    card_frame.pack(fill=tk.BOTH, expand=True)
    
    # Add beautiful shadow
    card_shadow = tk.Frame(content_area, bg='#0c1525')
    card_shadow.place(in_=card_frame, x=8, y=8, relwidth=1, relheight=1)
    card_frame.lift()
    
    # Mode display with enhanced styling
    mode_text = current_mode.replace('-', ' → ').replace('+', ' + ').title()
    mode_label = tk.Label(card_frame, 
                         text=f"Mode: {mode_text}",
                         font=('Segoe UI', 16),
                         bg='#1e293b',
                         fg='#94a3b8')
    mode_label.pack(pady=(30, 20))
    
    # MASSIVE hanzi/question display - the star of the show!
    question_frame = tk.Frame(card_frame, bg='#334155', relief=tk.FLAT)
    question_frame.pack(pady=40, padx=40, fill=tk.BOTH, expand=True)
    
    # Determine if this is hanzi (Chinese characters) for extra large font
    is_hanzi = any('\u4e00' <= char <= '\u9fff' for char in question)
    font_size = 72 if is_hanzi else 48
    
    question_label = tk.Label(question_frame, 
                             text=question,
                             font=('Segoe UI', font_size, 'bold'),
                             bg='#334155', 
                             fg='#f8fafc',
                             wraplength=700)
    question_label.pack(expand=True)
    
    # Beautiful answer section (initially hidden)
    answer_frame = tk.Frame(card_frame, bg='#1e293b')
    answer_frame.pack(pady=(0, 40))
    
    separator = tk.Frame(answer_frame, bg='#5b21b6', height=4)
    separator.pack(fill=tk.X, pady=(0, 30), padx=60)
    
    # Check if answer contains hanzi for font sizing
    is_answer_hanzi = any('\u4e00' <= char <= '\u9fff' for char in answer)
    answer_font_size = 48 if is_answer_hanzi else 32
    
    answer_label = tk.Label(answer_frame, 
                           text=answer,
                           font=('Segoe UI', answer_font_size, 'bold'),
                           bg='#1e293b', 
                           fg='#0d9488',
                           wraplength=600)
    
    # Store references for show_answer callback
    answer_frame.answer_label = answer_label
    answer_frame.answer_shown = False
    
    # Gorgeous action buttons
    button_frame = tk.Frame(container, bg='#0f172a')
    button_frame.pack(pady=40)
    
    show_btn = tk.Button(button_frame, 
                        text="👁️ Show Answer",
                        command=lambda: show_answer_callback(answer_frame),
                        font=('Segoe UI', 16, 'bold'),
                        bg='#1d4ed8',
                        fg='white',
                        activebackground='#1e40af',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=35,
                        pady=18,
                        cursor='hand2')
    show_btn.pack(side=tk.LEFT, padx=20)
    
    next_btn = tk.Button(button_frame, 
                        text="➡️ Next Word",
                        command=next_card_callback,
                        font=('Segoe UI', 16, 'bold'),
                        bg='#0d9488',
                        fg='white',
                        activebackground='#0f766e',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=35,
                        pady=18,
                        cursor='hand2')
    next_btn.pack(side=tk.LEFT, padx=20)
    
    # Beautiful back button
    back_btn = tk.Button(container, 
                        text="← Back to Menu",
                        command=back_callback,
                        font=('Segoe UI', 14),
                        bg='#64748b',
                        fg='white',
                        activebackground='#475569',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=25,
                        pady=12,
                        cursor='hand2')
    back_btn.pack(pady=(0, 20))

def show_flashcard_answer(answer_frame):
    """Show the answer on the flashcard with beautiful animation"""
    if not answer_frame.answer_shown:
        answer_frame.answer_label.pack()
        answer_frame.answer_shown = True

def create_flashcard_results(main_frame, total_cards, retry_callback, menu_callback):
    """Show spectacular flashcard session completion"""
    clear_frame(main_frame)
    
    container = tk.Frame(main_frame, bg='#0f172a')
    container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
    
    # Spectacular results frame
    results_frame = tk.Frame(container, bg='#1e293b', relief=tk.FLAT, bd=0)
    results_frame.pack(pady=80, padx=80, fill=tk.BOTH, expand=True)
    
    # Add gorgeous shadow
    results_shadow = tk.Frame(container, bg='#0c1525')
    results_shadow.place(in_=results_frame, x=10, y=10, relwidth=1, relheight=1)
    results_frame.lift()
    
    # Stunning title
    title_label = tk.Label(results_frame, 
                          text="📚 Flashcards Complete!",
                          font=('Segoe UI', 36, 'bold'),
                          bg='#1e293b',
                          fg='#f8fafc')
    title_label.pack(pady=(50, 30))
    
    # Massive celebration emoji
    emoji_label = tk.Label(results_frame, 
                          text="🎉",
                          font=('Segoe UI', 80),
                          bg='#1e293b')
    emoji_label.pack(pady=40)
    
    # Beautiful completion message
    completion_text = f"You reviewed {total_cards} words!"
    completion_label = tk.Label(results_frame, 
                               text=completion_text,
                               font=('Segoe UI', 24),
                               bg='#1e293b',
                               fg='#e2e8f0')
    completion_label.pack(pady=20)
    
    # Gorgeous encouragement
    encouragement_label = tk.Label(results_frame, 
                                  text="Fantastic work! Keep up the amazing progress! 🌟",
                                  font=('Segoe UI', 18),
                                  bg='#1e293b',
                                  fg='#0d9488')
    encouragement_label.pack(pady=(30, 60))
    
    # Beautiful action buttons
    button_frame = tk.Frame(container, bg='#0f172a')
    button_frame.pack(pady=50)
    
    retry_btn = tk.Button(button_frame, 
                         text="🔄 Study Again",
                         command=retry_callback,
                         font=('Segoe UI', 18, 'bold'),
                         bg='#5b21b6',
                         fg='white',
                         activebackground='#4c1d95',
                         activeforeground='white',
                         relief=tk.FLAT,
                         bd=0,
                         padx=40,
                         pady=20,
                         cursor='hand2')
    retry_btn.pack(side=tk.LEFT, padx=25)
    
    menu_btn = tk.Button(button_frame, 
                        text="🏠 Main Menu",
                        command=menu_callback,
                        font=('Segoe UI', 18, 'bold'),
                        bg='#0d9488',
                        fg='white',
                        activebackground='#0f766e',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=40,
                        pady=20,
                        cursor='hand2')
    menu_btn.pack(side=tk.LEFT, padx=25)

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
    """Display the spectacular matching game"""
    clear_frame(main_frame)
    
    container = tk.Frame(main_frame, bg='#0f172a')
    container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
    
    # Stunning header
    header_frame = tk.Frame(container, bg='#1e293b', height=140)
    header_frame.pack(fill=tk.X, pady=0)
    header_frame.pack_propagate(False)
    
    title_label = tk.Label(header_frame, 
                          text="🎮 Matching Game",
                          font=('Segoe UI', 32, 'bold'),
                          bg='#1e293b',
                          fg='#f8fafc')
    title_label.pack(pady=(25, 15))
    
    # Beautiful score display
    score_text = f"Score: {score} | Pairs Found: {len(matched_pairs)}/{len(selected_words)}"
    score_label = tk.Label(header_frame, 
                          text=score_text,
                          font=('Segoe UI', 18, 'bold'),
                          bg='#1e293b',
                          fg='#0d9488')
    score_label.pack(pady=5)
    
    mode_text = current_mode.replace('-', ' with ').replace('+', ' + ').title()
    mode_label = tk.Label(header_frame, 
                         text=f"Click two cards to match {mode_text}",
                         font=('Segoe UI', 16),
                         bg='#1e293b',
                         fg='#94a3b8')
    mode_label.pack(pady=(5, 25))
    
    # Spectacular game grid area
    game_area = tk.Frame(container, bg='#0f172a')
    game_area.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
    
    game_frame = tk.Frame(game_area, bg='#0f172a')
    game_frame.pack(expand=True)
    
    # Calculate grid dimensions
    total_cards = len(game_pairs)
    cols = 4 if total_cards <= 12 else 5
    rows = (total_cards + cols - 1) // cols
    
    game_buttons = []
    for i, pair in enumerate(game_pairs):
        row = i // cols
        col = i % cols
        
        # Determine if this is hanzi for larger font
        is_hanzi = any('\u4e00' <= char <= '\u9fff' for char in pair["text"])
        font_size = 24 if is_hanzi else 16
        
        # Spectacular button styling
        btn = tk.Button(game_frame, 
                       text=pair["text"],
                       font=('Segoe UI', font_size, 'bold'),
                       bg='#5b21b6',
                       fg='white',
                       activebackground='#4c1d95',
                       activeforeground='white',
                       relief=tk.RAISED,
                       bd=3,
                       width=12 if is_hanzi else 16, 
                       height=4,
                       wraplength=140,
                       cursor='hand2',
                       command=lambda idx=i: card_click_callback(idx))
        btn.grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
        
        # Store pair info
        btn.pair_info = pair
        btn.index = i
        btn.matched = False
        btn.is_hanzi = is_hanzi
        game_buttons.append(btn)
    
    # Configure grid weights for responsive layout
    for i in range(cols):
        game_frame.grid_columnconfigure(i, weight=1)
    for i in range(rows):
        game_frame.grid_rowconfigure(i, weight=1)
    
    # Beautiful back button
    back_btn = tk.Button(container, 
                        text="← Back to Menu",
                        command=back_callback,
                        font=('Segoe UI', 14),
                        bg='#64748b',
                        fg='white',
                        activebackground='#475569',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=25,
                        pady=12,
                        cursor='hand2')
    back_btn.pack(pady=(0, 30))
    
    return game_buttons

def show_immediate_feedback(card, is_correct):
    """Show immediate green/red feedback on card click"""
    if is_correct:
        card.configure(bg='#10b981', activebackground='#059669')  # Green for correct
    else:
        card.configure(bg='#ef4444', activebackground='#dc2626')  # Red for incorrect

def animate_matched_cards_disappear(card1, card2, callback):
    """Animate matched cards to disappear with beautiful effect"""
    # Keep cards green for a moment
    card1.after(600, lambda: fade_out_cards_beautifully(card1, card2, callback))

def fade_out_cards_beautifully(card1, card2, callback):
    """Beautiful fade out animation for matched cards"""
    fade_colors = ['#10b981', '#34d399', '#6ee7b7', '#9ca3af', '#d1d5db', '#f3f4f6']
    
    def fade_step(step=0):
        if step < len(fade_colors):
            try:
                card1.configure(bg=fade_colors[step], fg=fade_colors[step], 
                               activebackground=fade_colors[step])
                card2.configure(bg=fade_colors[step], fg=fade_colors[step],
                               activebackground=fade_colors[step])
                card1.after(150, lambda: fade_step(step + 1))
            except tk.TclError:
                pass
        else:
            # Finally hide the cards completely
            try:
                card1.grid_remove()
                card2.grid_remove()
                card1.matched = True
                card2.matched = True
                callback()
            except tk.TclError:
                pass
    
    fade_step()

def create_game_results(main_frame, score, selected_words, play_again_callback, menu_callback):
    """Show spectacular matching game results"""
    clear_frame(main_frame)
    
    container = tk.Frame(main_frame, bg='#0f172a')
    container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
    
    # Spectacular results frame
    results_frame = tk.Frame(container, bg='#1e293b', relief=tk.FLAT, bd=0)
    results_frame.pack(pady=80, padx=80, fill=tk.BOTH, expand=True)
    
    # Add gorgeous shadow
    results_shadow = tk.Frame(container, bg='#0c1525')
    results_shadow.place(in_=results_frame, x=10, y=10, relwidth=1, relheight=1)
    results_frame.lift()
    
    # Stunning title
    title_label = tk.Label(results_frame, 
                          text="🎉 Game Complete!",
                          font=('Segoe UI', 36, 'bold'),
                          bg='#1e293b',
                          fg='#f8fafc')
    title_label.pack(pady=(50, 30))
    
    # Massive trophy
    trophy_label = tk.Label(results_frame, 
                           text="🏆",
                           font=('Segoe UI', 80),
                           bg='#1e293b')
    trophy_label.pack(pady=40)
    
    # Beautiful score display
    score_label = tk.Label(results_frame, 
                          text=f"Final Score: {score}",
                          font=('Segoe UI', 28, 'bold'),
                          bg='#1e293b',
                          fg='#fbbf24')
    score_label.pack(pady=20)
    
    # Achievement text
    achievement_text = f"All {len(selected_words)} pairs matched!"
    achievement_label = tk.Label(results_frame, 
                                text=achievement_text,
                                font=('Segoe UI', 20),
                                bg='#1e293b',
                                fg='#e2e8f0')
    achievement_label.pack(pady=15)
    
    # Gorgeous congratulations
    congrats_label = tk.Label(results_frame, 
                             text="Incredible work! You're a matching champion! 🌟✨",
                             font=('Segoe UI', 18),
                             bg='#1e293b',
                             fg='#0d9488')
    congrats_label.pack(pady=(30, 60))
    
    # Beautiful action buttons
    button_frame = tk.Frame(container, bg='#0f172a')
    button_frame.pack(pady=50)
    
    play_again_btn = tk.Button(button_frame, 
                              text="🎮 Play Again",
                              command=play_again_callback,
                              font=('Segoe UI', 18, 'bold'),
                              bg='#5b21b6',
                              fg='white',
                              activebackground='#4c1d95',
                              activeforeground='white',
                              relief=tk.FLAT,
                              bd=0,
                              padx=40,
                              pady=20,
                              cursor='hand2')
    play_again_btn.pack(side=tk.LEFT, padx=25)
    
    menu_btn = tk.Button(button_frame, 
                        text="🏠 Main Menu",
                        command=menu_callback,
                        font=('Segoe UI', 18, 'bold'),
                        bg='#0d9488',
                        fg='white',
                        activebackground='#0f766e',
                        activeforeground='white',
                        relief=tk.FLAT,
                        bd=0,
                        padx=40,
                        pady=20,
                        cursor='hand2')
    menu_btn.pack(side=tk.LEFT, padx=25)