/*
Write a function that, when passed a list and a target sum, returns two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return null.

For example, findTwoSum(new int[] { 3, 1, 5, 7, 5, 9 }, 10) should return a single dimensional array with two elements and contain any of the following pairs of indices:

0 and 3 (or 3 and 0) as 3 + 7 = 10
1 and 5 (or 5 and 1) as 1 + 9 = 10
2 and 4 (or 4 and 2) as 5 + 5 = 10
*/

import java.util.*;

//IMPLEMENTATION 1 - using in-built ArrayList functions
public class TwoSum {
    public static int[] findTwoSum(int[] list, int sum) {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        ArrayList<Integer> l = new ArrayList<>(); //Arrays.<Integer>asList(list);
        for(int element:list){
            l.add(element);
        }

        int[] ans={-1,-1};

        for(int i=list.length-1;i>=0;i--){
            if(list[i]<=sum){
                int diff=sum-list[i];
                int s2 = l.indexOf(diff);
                if(s2>=0 && s2!=i){
                    ans[0]=i;
                    ans[1]=s2;
                    break;
                }
            }
        }

        if(ans[0]==-1)
            ans=null;

        return ans;
    }

    //IMPLEMENTATION 2: using HashMap
    public static int[] findSum(int[] list, int sum) {
        Map<Integer, Integer> myMap = new HashMap<Integer, Integer>();

        for(int i = 0; i < list.length; i++)
        {
            myMap.put(list[i], i);
        }

        for(int i = 0; i < list.length; i++)
        {
            int num=myMap.getOrDefault(sum - list[i],-1);
            if (num>=0 && num!=i)
            {
                int[] answer = new int[] {num, i};
                return answer;
            }

        }

        return null;
    }

    public static void main(String[] args) {
        int[] indices = findTwoSum(new int[] { 3, 1, 5, 7, 5,0}, 10);
        if(indices != null) {
            System.out.println(indices[0] + " " + indices[1]);
        }
    }
}