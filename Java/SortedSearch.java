/*
Implement function countNumbers that accepts a sorted array of integers and counts the number of array elements that are less than the parameter lessThan.

For example, SortedSearch.countNumbers(new int[] { 1, 3, 5, 7 }, 4) should return 2 because there are two array elements less than 4.
 */

import java.util.Arrays;

public class SortedSearch {
    public static int countNumbers(int[] sortedArray, int lessThan) {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        int idx;

        idx= Arrays.binarySearch(sortedArray, lessThan);

        if(idx<0){
            idx=(-1*idx)-1;
        }

        return idx;

    }

    public static void main(String[] args) {
        System.out.println(SortedSearch.countNumbers(new int[] { 1, 3, 5, 7 }, 4));
    }
}