/*
A TrainComposition is built by attaching and detaching wagons from the left and the right sides.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.
 */

public class TrainComposition {
    class Wagon{
        public int value;
        //public int id;
        public Wagon right;
        public Wagon left;

        Wagon(){
            value=-1;
            right = null;
            left = null;
        }

        Wagon(int val, Wagon l, Wagon r){
            value=val;
            left = l;
            right = r;
        }
    }

    Wagon head=null; //right
    Wagon tail=null; //left

    public void attachWagonFromLeft(int wagonId) {
        Wagon w = new Wagon();
        w.value=wagonId;

        if(tail==null) {
            tail = w;
            head = w;
        }
        else{
            w.right=tail;
            tail.left=w;

            tail=w;
        }

        //traverse();
    }

    public void attachWagonFromRight(int wagonId) {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        Wagon w = new Wagon();
        w.value=wagonId;

        if(tail==null){
            tail=w;
            head=w;
        }
        else {
            w.left=head;
            head.right=w;

            head=w;
        }

        //traverse();
    }

    public int detachWagonFromLeft() {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        if(tail==null)
            return -1;

        int val = tail.value;
        tail=tail.right;

        if(tail==null)
            head=null;

        return val;

    }

    public int detachWagonFromRight() {
        //throw new UnsupportedOperationException("Waiting to be implemented.");
        if(tail==null)
            return -1;

        int val = head.value;
        head=head.left;
        if (head==null)
            tail=null;

        return val;
    }

    public void traverse(){
        if(tail==null){
            System.out.print("Empty");

        }
        else{
            Wagon ptr=tail;
            System.out.print("traverse ");
            while(ptr!=null)
            {
                System.out.print(ptr.value+" ");
                ptr=ptr.right;
            }
            System.out.print("\n");

        }
    }

    public static void main(String[] args) {
        TrainComposition tree = new TrainComposition();
        tree.attachWagonFromLeft(50);
        tree.attachWagonFromLeft(40);
        tree.attachWagonFromRight(60);
        tree.attachWagonFromRight(70);
        tree.attachWagonFromLeft(30);
        tree.attachWagonFromRight(90);
        tree.traverse();
        System.out.println(tree.detachWagonFromRight()); // 7
        System.out.println(tree.detachWagonFromLeft()); // 13
    }


}