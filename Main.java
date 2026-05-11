import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static String getName() {
        System.out.print("Name: ");
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();

        return name;
    }

    public static Integer getAge() {
        System.out.print("Age: ");
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();

        return age;
    }

    public static void main(String[] args) {
        ArrayList<Object> list = new ArrayList<>();
        list.add(getName());
        list.add(getAge());

        System.out.println(list.get(0) + ", " + list.get(1));

    }
}