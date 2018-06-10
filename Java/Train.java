/*
A TrainComposition is built by attaching and detaching wagons from the left and the right sides.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
//with arraylist

public class Train {

    ArrayList<Integer> train = new ArrayList<Integer>();
    //Wagon tail=null;
    //Wagon head=null;

    public void attachWagonFromLeft(int wagonId) {
        train.add(0,wagonId);
        //traverse();
    }

    public void attachWagonFromRight(int wagonId) {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        train.add(wagonId);
    }

    public int detachWagonFromLeft() {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        return (int) train.remove(0);

    }

    public int detachWagonFromRight() {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        return (int) train.remove(train.size()-1);
    }

    public void traverse(){
        System.out.println("Traverse train " + train);
    }

    void sort()
    {
        train.sort(Integer::compareTo);
    }

    int search(int key){
        return Collections.binarySearch(train,key);
    }

    public static void main(String[] args) {
        Train tree = new Train();
        tree.attachWagonFromLeft(50);
        tree.attachWagonFromLeft(40);
        tree.attachWagonFromRight(60);
        tree.attachWagonFromRight(10);
        tree.attachWagonFromLeft(30);
        tree.attachWagonFromRight(80);
        tree.traverse();
        System.out.println(tree.detachWagonFromRight()); // 7
        System.out.println(tree.detachWagonFromLeft()); // 13
        tree.sort();
        tree.traverse();
        System.out.println(tree.search(40));
        System.out.println(tree.search(20));
    }


}