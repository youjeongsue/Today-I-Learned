//세 수

package bank_1946;

import java.util.Scanner;

public class p_10817 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int big, small, middle;
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();
        big = (num1 > num2) && (num1 > num3) ? num1 : (num3 > num2 ? num3 : num2);
        small = (num2 > num1) && (num3 > num1) ? num1 : (num2 > num3 ? num3 : num2);
        middle = (num1 + num2 + num3) - big - small;
        System.out.print(middle);
        sc.close();
    }
}