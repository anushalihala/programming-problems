import java.util.*;
class 1395 {
    public int numTeams(int[] rating) {
        TreeSet<Integer> tree = new TreeSet<Integer>();
        HashMap<Integer,HashMap<String,Integer>> map = new HashMap<Integer,HashMap<String,Integer>>();
        for(int i=0; i<rating.length; i++){
            map.put(i, new HashMap<String, Integer>());
        }
        for(int i=0; i<rating.length; i++){
            int leftGreater = tree.headSet(rating[i]).size();
            int leftSmaller = tree.tailSet(rating[i]).size();
            map.get(i).put("lg", leftGreater);
            map.get(i).put("ls", leftSmaller);
            tree.add(rating[i]);
        }
        tree = new TreeSet<Integer>();
        for(int i=rating.length-1; i>=0; i--){
            int rightGreater = tree.headSet(rating[i]).size();
            int rightSmaller = tree.tailSet(rating[i]).size();
            map.get(i).put("rg", rightGreater);
            map.get(i).put("rs", rightSmaller);
            tree.add(rating[i]);
        }
        int count = 0;
        for(int i=0; i<rating.length; i++){
            count += map.get(i).get("ls") * map.get(i).get("rg");
            count += map.get(i).get("lg") * map.get(i).get("rs");
        }
        return count;
    }
}