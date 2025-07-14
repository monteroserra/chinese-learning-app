#!/usr/bin/env python3
"""
Chinese Learning App - Ultra-Enhanced Main Application
A stunning main file with beautiful UI and enhanced matching game mechanics.

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
        self.root.geometry("1000x700")  # More reasonable size
        self.root.configure(bg='#0f172a')
        
        # Load vocabulary and setup ultra-enhanced styling
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
        self.checking_match = False  # Prevent multiple clicks during checking
        
        # UI variables
        self.mode_var = tk.StringVar(value="pinyin-hanzi")
        self.words_var = tk.IntVar(value=5)
        
        # Initialize stunning UI
        self.create_main_frame()
        self.show_start_screen()
        center_window(self.root)
        
        # Enhanced window properties
        self.root.resizable(True, True)
        self.root.minsize(900, 600)  # Reduced minimum size
        
        # Set beautiful window styling
        try:
            self.root.attributes('-alpha', 0.98)  # Slight transparency for modern look
        except:
            pass  # Some systems don't support transparency
    
    def create_main_frame(self):
        """Create the main container frame with stunning styling"""
        self.main_frame = tk.Frame(self.root, bg='#0f172a', padx=0, pady=0)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_start_screen(self):
        """Display the ultra-beautiful start screen"""
        create_start_screen(
            self.main_frame, 
            self.vocabulary,
            self.mode_var,
            self.words_var,
            self.start_flashcards,
            self.start_matching_game
        )
    
    def start_flashcards(self):
        """Initialize and start ultra-enhanced flashcard mode"""
        self.current_mode, self.selected_words = prepare_words(
            self.vocabulary, self.mode_var, self.words_var
        )
        self.current_card_index = 0
        self.show_flashcard()
    
    def show_flashcard(self):
        """Display current flashcard with massive hanzi or results if finished"""
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
        """Move to next flashcard with smooth transition"""
        self.current_card_index += 1
        self.show_flashcard()
    
    def show_flashcard_results(self):
        """Show spectacular flashcard completion screen"""
        create_flashcard_results(
            self.main_frame,
            len(self.selected_words),
            self.start_flashcards,
            self.show_start_screen
        )
    
    def start_matching_game(self):
        """Initialize and start spectacular matching game"""
        self.current_mode, self.selected_words = prepare_words(
            self.vocabulary, self.mode_var, self.words_var
        )
        self.game_pairs = setup_matching_game(self.selected_words, self.current_mode)
        self.matched_pairs = []
        self.selected_cards = []
        self.score = 0
        self.checking_match = False
        self.show_matching_game()
    
    def show_matching_game(self):
        """Display the spectacular matching game with large hanzi"""
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
        """Handle card click with immediate beautiful feedback"""
        # Prevent actions during match checking or if card already processed
        if self.checking_match:
            return
            
        btn = self.game_buttons[index]
        
        # Ignore if card already matched or already selected
        if (hasattr(btn, 'matched') and btn.matched) or btn in self.selected_cards:
            return
        
        # Ignore if card is in matched_pairs list
        if index in self.matched_pairs:
            return
        
        # Add to selected cards
        self.selected_cards.append(btn)
        
        # Show selection visual feedback
        btn.configure(
            bg='#3b82f6',  # Blue for selection
            activebackground='#2563eb',
            relief=tk.RAISED,
            bd=4
        )
        
        # Check if we have 2 selected cards
        if len(self.selected_cards) == 2:
            self.checking_match = True
            self.root.after(300, self.check_match_with_immediate_feedback)
    
    def check_match_with_immediate_feedback(self):
        """Check match and show immediate green/red feedback"""
        if len(self.selected_cards) != 2:
            self.checking_match = False
            return
            
        card1, card2 = self.selected_cards
        is_match = card1.pair_info["pair_id"] == card2.pair_info["pair_id"]
        
        # Show immediate feedback
        show_immediate_feedback(card1, is_match)
        show_immediate_feedback(card2, is_match)
        
        if is_match:
            # Handle successful match
            self.handle_successful_match(card1, card2)
        else:
            # Handle failed match
            self.handle_failed_match(card1, card2)
        
        # Clear selected cards
        self.selected_cards = []
    
    def handle_successful_match(self, card1, card2):
        """Handle successful match with beautiful animations"""
        # Add to matched pairs and update score
        self.matched_pairs.extend([card1.index, card2.index])
        self.score += 10
        
        # Start the disappearing animation
        animate_matched_cards_disappear(card1, card2, self.on_cards_disappeared)
    
    def handle_failed_match(self, card1, card2):
        """Handle failed match with visual feedback"""
        # Cards stay red for a moment, then reset
        self.root.after(800, lambda: self.reset_cards_after_mismatch(card1, card2))
    
    def reset_cards_after_mismatch(self, card1, card2):
        """Reset cards to original appearance after showing mismatch"""
        try:
            # Determine original colors based on hanzi content
            original_bg = '#5b21b6'  # Purple for normal cards
            
            card1.configure(
                bg=original_bg,
                activebackground='#4c1d95',
                relief=tk.RAISED,
                bd=3,
                fg='white'
            )
            card2.configure(
                bg=original_bg,
                activebackground='#4c1d95',
                relief=tk.RAISED,
                bd=3,
                fg='white'
            )
        except tk.TclError:
            pass  # Widget might be destroyed
        
        # Re-enable matching
        self.checking_match = False
    
    def on_cards_disappeared(self):
        """Callback when cards have finished disappearing"""
        # Re-enable matching
        self.checking_match = False
        
        # Check if game complete
        if len(self.matched_pairs) == len(self.game_pairs):
            self.root.after(1000, self.show_game_results)
        else:
            # Update the display to show new score
            self.update_score_display()
    
    def update_score_display(self):
        """Update the score display after a match"""
        # Filter out matched cards when refreshing
        remaining_pairs = []
        for i, pair in enumerate(self.game_pairs):
            if i not in self.matched_pairs:
                remaining_pairs.append(pair)
        
        # Only refresh if there are still unmatched cards
        if remaining_pairs:
            self.show_matching_game()
    
    def show_game_results(self):
        """Show spectacular game completion results"""
        create_game_results(
            self.main_frame,
            self.score,
            self.selected_words,
            self.start_matching_game,
            self.show_start_screen
        )

def main():
    """Main function to run the ultra-enhanced application"""
    print("🚀 Starting Ultra-Enhanced Chinese Learning App...")
    print("✨ Loading stunning UI components...")
    
    # Create and configure the main window with beautiful styling
    root = tk.Tk()
    
    # Set window properties for maximum beauty
    try:
        # Try to set window icon if available
        # root.iconbitmap('assets/app_icon.ico')  # Uncomment if you have an icon
        pass
    except:
        pass
    
    # Initialize the ultra-enhanced app
    app = ChineseLearningApp(root)
    
    vocabulary_count = len(app.vocabulary)
    print(f"📚 Loaded {vocabulary_count} words")
    print("🎨 Ultra-enhanced UI ready!")
    print("🌟 Massive hanzi symbols enabled!")
    print("💫 Beautiful animations activated!")
    print("🎮 Enhanced matching game with immediate feedback!")
    print("🎉 App started! Enjoy learning Chinese in style!")
    
    # Start the GUI event loop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n👋 Thanks for using the Ultra-Enhanced Chinese Learning App!")
        root.quit()

if __name__ == "__main__":
    main()