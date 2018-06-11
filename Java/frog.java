/*
If a frog can take 1 jump or 2 jumps then how many possible sequences of jumps can be made for a given distance
*/

public class frog
{
    
    public static int possibleJumps(int steps)
    {
        
        if(steps<=0)
        {
            return 0;
        }
        else if(steps==1)
        {
            return 1;
        }
        else if (steps==2)
        {
            return 2;
        }
        else
        {
             return(possibleJumps(steps-1) + possibleJumps(steps-2));
            
        }
    }
    
    
    public static void main(String args[])
    {
        int input;
        input = Integer.parseInt(args[0]);
   
        
        System.out.println(possibleJumps(input));
        
    }
}