import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Integer: ");
        int x = sc.nextInt();

        ArrayList<Integer> list = new ArrayList<>();
        
        while (true) {
            if (x == 1) {
                list.add(1);
                break;
            } else {
                list.add(x % 2);
                x /= 2;
            }

        }

        Collections.reverse(list);

        String answer = "";

        for (int i : list) {
            answer += Integer.toString(i);
        }
        System.out.println(answer);
    }
}