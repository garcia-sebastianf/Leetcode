//Created by: Sebastián Felipe García Rojas


public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        
        bool LetterIsConsisted = false;
        bool WordIsConsisted = true;
        int consistedWords = 0;
            
        foreach (string word in words){
            WordIsConsisted = true; 
            
            foreach (char letterWord in word){
                LetterIsConsisted = false;
                
                foreach (char letterAllowed in allowed){
                    
                    // Find one match between the letters of the string 'allowed' and the current letter in the word
                    if (letterAllowed == letterWord){
                        LetterIsConsisted = true;
                        break;
                    }
                }
                
                // If there is no match for the word's letter, then the word is inconsistent
                if (LetterIsConsisted == false){       
                    WordIsConsisted = false;
                    break;
                }
            }
            
            // Increment the count if the word is consistent
            if (WordIsConsisted == true){
                consistedWords++;
                LetterIsConsisted = false;
            }
        }
        return consistedWords;      
    }
}