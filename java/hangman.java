import java.util.ArrayList;
import java.util.Scanner;

// HANGMAN GAME 

public class hangman {
    public static void main(String[] args) {

    String word = "watermelon";

    Scanner scanner = new Scanner(System.in);
    ArrayList<Character> wordState = new ArrayList<>();
    int wrongGuesses = 0;

    for (int i = 0; i < word.length(); i++) {
        wordState.add('_');
    }

    // WELCOME MESSAGE 
    System.out.println("*******************");
    System.out.println("Welcome to Hangman!");
    System.out.println("*******************");

    System.out.println(wordState);

    scanner.close();    
    }
    // Method in Charge of returning ASCII ART based on wrong guesses
    static String getHangmanArt(int wrongGuesses) {

        return switch(wrongGuesses) {
            /*  -> is a lambda operator meaning that 
            the code after the arrow is executed */
            case 0 -> """
            +---+
                |
                |
                |
                |
                |
            =========""";
            case 1 -> """
            +---+
            0   |
                |
                |
                |
                |
            =========""";
            case 2 -> """
            +---+
            0   |
            |   |
                |
                |
                |
            =========""";
            case 3 -> """
            +---+
            0   |
           /|   |
                |
                |
                |
            =========""";
            case 4 -> """
            +---+
            0   |
           /|\\ |
                |
                |
                |
            =========""";
            case 5 -> """
            +---+
            O   |
           /|\\ |
           /    |
                | 
                |     
            =========""";
            case 6 -> """
            +---+
            O   |
           /|\\ |
           / \\ |
            |   |
            |   |
            =========""";
            default -> "";
        };

    }
}