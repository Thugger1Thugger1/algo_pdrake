import java.util.ArrayList;
public class Example {


    ArrayList<String> merge(String[] words, String[] more) {
        ArrayList<String> sentence = new ArrayList<String>();
        for (String w : words) sentence.add(w);
        for (String w : more) sentence.add(w);
        return sentence;
    }

    public static void main(String[] args) {
        String[] words1 = {"Hello", "World"};
        String[] words2 = {"This", "is", "Java"};
        
        ArrayList<String> result = merge(words1, words2);
        System.out.println(result);
    }
}