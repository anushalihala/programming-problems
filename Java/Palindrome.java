/*
A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, isPalindrome("Deleveled") should return true as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.
*/

public class Palindrome {
    public static boolean isPalindrome(String word) {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        word=word.toLowerCase();
        boolean ans = true;
        int l = word.length()-1;
        int mid = (word.length()+1)/2;
        for(int i=0;i<mid;i++){
            if(word.charAt(i)!=word.charAt(l-i)){
                return false;

            }
        }
        return  true;
    }

    public static void main(String[] args) {
        System.out.println(Palindrome.isPalindrome("Deleveled"));
    }
}