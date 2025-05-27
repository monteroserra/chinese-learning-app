#!/usr/bin/env python3
"""
Chinese Learning App - Main Application
A simplified main file that coordinates the Chinese learning app.

Requirements:
- Python 3.6+
- tkinter (usually comes with Python)
- utils.py (contains all helper functions)

Usage:
    python main.py
"""

import tkinter as tk
from tkinter import ttk
from utils import *

class ChineseLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🇨🇳 Chinese Learning App")
        self.root.geometry("900x700")
        self.root.configure(bg='#f8f9fa')
        
        # Load vocabulary and setup
        self.vocabulary = load_vocabulary()
        setup_styles()
        
        # App state
        self.current_mode = ""
        self.selected_words = []
        self.current_card_index = 0
        self.score = 0
        self.game_pairs = []
        self.selected_cards = []
        self.matched_pairs = []
        self.game_buttons = []
        
        # UI variables
        self.mode_var = tk.StringVar(value="pinyin-hanzi")
        self.words_var = tk.IntVar(value=5)
        
        # Initialize UI
        self.create_main_frame()
        self.show_start_screen()
        center_window(self.root)
    
    def create_main_frame(self):
        """Create the main container frame"""
        self.main_frame = tk.Frame(self.root, bg='#f8f9fa', padx=40, pady=30)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_start_screen(self):
        """Display the start screen"""
        create_start_screen(
            self.main_frame, 
            self.vocabulary,
            self.mode_var,
            self.words_var,
            self.start_flashcards,
            self.start_matching_game
        )
    
    def start_flashcards(self):
        """Initialize and start flashcard mode"""
        self.current_mode, self.selected_words = prepare_words(
            self.vocabulary, self.mode_var, self.words_var
        )
        self.current_card_index = 0
        self.show_flashcard()
    
    def show_flashcard(self):
        """Display current flashcard or results if finished"""
        if self.current_card_index >= len(self.selected_words):
            self.show_flashcard_results()
            return
        
        word = self.selected_words[self.current_card_index]
        create_flashcard_screen(
            self.main_frame,
            word,
            self.current_mode,
            self.current_card_index,
            len(self.selected_words),
            show_flashcard_answer,
            self.next_flashcard,
            self.show_start_screen
        )
    
    def next_flashcard(self):
        """Move to next flashcard"""
        self.current_card_index += 1
        self.show_flashcard()
    
    def show_flashcard_results(self):
        """Show flashcard completion screen"""
        create_flashcard_results(
            self.main_frame,
            len(self.selected_words),
            self.start_flashcards,
            self.show_start_screen
        )
    
    def start_matching_game(self):
        """Initialize and start matching game"""
        self.current_mode, self.selected_words = prepare_words(
            self.vocabulary, self.mode_var, self.words_var
        )
        self.game_pairs = setup_matching_game(self.selected_words, self.current_mode)
        self.matched_pairs = []
        self.selected_cards = []
        self.score = 0
        self.show_matching_game()
    
    def show_matching_game(self):
        """Display the matching game"""
        self.game_buttons = create_matching_game_screen(
            self.main_frame,
            self.game_pairs,
            self.current_mode,
            self.score,
            self.matched_pairs,
            self.selected_words,
            self.card_clicked,
            self.show_start_screen
        )
    
    def card_clicked(self, index):
        """Handle card click in matching game"""
        btn = self.game_buttons[index]
        
        # Ignore if card already matched or already selected
        if index in self.matched_pairs or btn in self.selected_cards:
            return
        
        # Add to selected cards
        self.selected_cards.append(btn)
        btn.configure(bg='#4facfe', activebackground='#3d8bfe')
        
        # Check if we have 2 selected cards
        if len(self.selected_cards) == 2:
            self.root.after(500, self.check_match)
    
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
                # Update display
                self.show_matching_game()
        else:
            # No match - reset buttons
            card1.configure(bg='#667eea', activebackground='#5a6fd8')
            card2.configure(bg='#667eea', activebackground='#5a6fd8')
        
        self.selected_cards = []
    
    def show_game_results(self):
        """Show game completion results"""
        create_game_results(
            self.main_frame,
            self.score,
            self.selected_words,
            self.start_matching_game,
            self.show_start_screen
        )

def main():
    """Main function to run the application"""
    print("🚀 Starting Chinese Learning App...")
    
    # Create and configure the main window
    root = tk.Tk()
    
    # Initialize the app
    app = ChineseLearningApp(root)
    
    vocabulary_count = len(app.vocabulary)
    print(f"📚 Loaded {vocabulary_count} words")
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