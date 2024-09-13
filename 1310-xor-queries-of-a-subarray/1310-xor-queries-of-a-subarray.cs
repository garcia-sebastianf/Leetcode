//Created by: Sebastián Felipe García Rojas

public class Solution {
    public int[] XorQueries(int[] arr, int[][] queries) {
        
        //int finish, init = 0;
        int[] output  = new int[queries.Length];
        int xoroperation = 0;
        int i = 0;
        bool once = false;
        
        foreach (int[] querie in queries){
            
            //init = querie[0];
            //finish = querie[1];
            once = false;
            
            if (querie[0] == querie[1]) {
                    output[i] = arr[querie[0]];
                    i++;
                    continue;       
            }
                
            for (int k = querie[0]; k <= querie[1]; k++){
                
                
                if (k < querie[1]){
                    if (once == false){
                        xoroperation = arr[k] ^ arr[k+1];
                        once = true;
                        continue;
                    }
                    
                    xoroperation = xoroperation ^ arr[k+1];
                    
                } 
            }
            
            output[i] = xoroperation;
            i++;
            
        }
        
        
        return output;
    }
}