//2007년

package bank_1946;

import java.util.Scanner;

public class p_1924 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int[] day = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        String[] result_array = { "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" };
        for (int i = 1; i < x; i++) {
            y += day[x - i - 1];
        }
        System.out.print(result_array[(y - 1) % 7]);
        sc.close();
    }
}