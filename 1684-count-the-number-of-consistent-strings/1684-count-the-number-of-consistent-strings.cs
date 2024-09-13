//Created by: Sebastián Felipe García Rojas

/*Explica

asdffffffffffffffffffffffffffffffffffffffffffffffffffff*/

public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        
        bool LetterIsConsisted = false;
        bool WordIsConsisted = true;
        int consistedWords = 0;
            
        foreach (string word in words){
            foreach (char letterWord in word){
                foreach (char letterStringAllowed in allowed){
                    if (letterStringAllowed == letterWord){
                        LetterIsConsisted = true;
                        break;
                    }
                }
                if (LetterIsConsisted == false){       
                    WordIsConsisted = false;
                    break;
                }
                LetterIsConsisted = false;
            }
            if (WordIsConsisted == true){
                consistedWords++;
                LetterIsConsisted = false;
            }
            WordIsConsisted = true; 
        }
        return consistedWords;      
    }
}