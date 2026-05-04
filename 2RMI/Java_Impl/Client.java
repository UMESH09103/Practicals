import java.rmi.Naming;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            StringConcat obj = (StringConcat) Naming.lookup("rmi://localhost/StringService");

            Scanner sc = new Scanner(System.in);

            System.out.print("Enter first string: ");
            String str1 = sc.nextLine();

            System.out.print("Enter second string: ");
            String str2 = sc.nextLine();

            String result = obj.concatenate(str1, str2);

            System.out.println("Concatenated String: " + result);

        } catch (Exception e) {
            System.out.println("Client error: " + e);
        }
    }
}