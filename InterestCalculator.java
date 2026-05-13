import java.util.Scanner;

public class InterestCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Principal Amount: ");
        Float principalAmount = sc.nextFloat();
        System.out.print("Annual Interest: ");
        Float annualInterest = sc.nextFloat();
        System.out.print("Period (Years): ");
        int period = sc.nextInt();

        float baseAmount = principalAmount;

        float finalInterest = 0;

        for (int i = 1; i <= period; i++) {
            Float interest = (annualInterest/100) * baseAmount;
            finalInterest += interest;
            baseAmount += interest;
        }

        System.out.println("Total Interest over the time: " + finalInterest);
        System.out.println("Total Amount to pay: " + (finalInterest + principalAmount));
    }
}